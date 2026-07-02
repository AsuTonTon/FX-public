from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime, timedelta

import pytest

from src.backtest.engine import BacktestEngine
from src.backtest.trade import OHLCBar
from src.strategies.ema_wave3_strategy_a import EmaWave3StrategyA, StrategyAConfig


def make_bars(closes: Sequence[float]) -> list[OHLCBar]:
    start = datetime(2026, 1, 1)
    return [
        OHLCBar(
            time=start + timedelta(hours=4 * index),
            open=close,
            high=close + 0.2,
            low=close - 0.2,
            close=close,
        )
        for index, close in enumerate(closes)
    ]


def strategy(rr: float = 1.5, min_warmup_bars: int | None = None) -> EmaWave3StrategyA:
    return EmaWave3StrategyA(
        StrategyAConfig(
            fast_period=2,
            slow_period=3,
            rr_multiple=rr,
            buffer=0.0,
            touch_expiry_bars=30,
            confirmation_expiry_bars=10,
            min_warmup_bars=min_warmup_bars,
        )
    )


def force_touch(
    bars: list[OHLCBar], strategy_obj: EmaWave3StrategyA, index: int
) -> None:
    indicator = strategy_obj.with_indicators(bars)[index]
    bars[index].low = min(bars[index].low, indicator.ema_fast - 0.1)
    bars[index].high = max(bars[index].high, indicator.ema_fast + 0.1)


def test_golden_cross_detection() -> None:
    bars = make_bars([100, 100, 100, 110])
    indicators = strategy().with_indicators(bars)

    assert indicators[3].cross_up is True
    assert indicators[3].cross_down is False


def test_warmup_blocks_setup_start_before_minimum_bars() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 112, 113])
    strategy_obj = strategy(min_warmup_bars=4)
    force_touch(bars, strategy_obj, 4)

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries == []
    assert not any(event.event_type == "setup_started" for event in result.events)


def test_setup_can_start_after_warmup() -> None:
    bars = make_bars([100, 100, 100, 100, 110, 108, 112, 113])
    strategy_obj = strategy(min_warmup_bars=4)
    force_touch(bars, strategy_obj, 5)

    result = strategy_obj.generate_entries("TEST", bars)

    assert len(result.entries) == 1
    assert any(event.event_type == "setup_started" for event in result.events)


def test_dead_cross_detection() -> None:
    bars = make_bars([100, 100, 100, 90])
    indicators = strategy().with_indicators(bars)

    assert indicators[3].cross_down is True
    assert indicators[3].cross_up is False


def test_long_confirmation_uses_reference_high_close_break() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 112, 113])
    strategy_obj = strategy()
    force_touch(bars, strategy_obj, 4)
    bars[6].open = 113.45

    result = strategy_obj.generate_entries("TEST", bars)

    assert len(result.entries) == 1
    order = result.entries[0]
    assert order.trade.direction == "long"
    assert order.touch_index == 4
    assert order.confirmation_index == 5


def test_short_confirmation_uses_reference_low_close_break() -> None:
    bars = make_bars([100, 100, 100, 90, 92, 88, 87])
    strategy_obj = strategy()
    force_touch(bars, strategy_obj, 4)

    result = strategy_obj.generate_entries("TEST", bars)

    assert len(result.entries) == 1
    order = result.entries[0]
    assert order.trade.direction == "short"
    assert order.touch_index == 4
    assert order.confirmation_index == 5


def test_entry_uses_next_bar_open() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 112, 113])
    strategy_obj = strategy()
    force_touch(bars, strategy_obj, 4)
    bars[6].open = 113.45

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries[0].entry_index == 6
    assert result.entries[0].trade.entry_price == pytest.approx(113.45)


def test_first_ema_touch_only_is_adopted() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 109, 110, 111, 112, 113])
    bars.extend(make_bars([114, 115, 116, 117, 118]))
    strategy_obj = strategy()
    force_touch(bars, strategy_obj, 4)
    bars[4].high = 999.0
    force_touch(bars, strategy_obj, 5)
    bars[6].close = bars[5].high + 1.0

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries == []
    assert any(event.event_type == "ignored_touch" for event in result.events)


def test_second_touch_is_ignored_even_when_it_would_confirm() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 109, 110])
    strategy_obj = strategy()
    force_touch(bars, strategy_obj, 4)
    first_high = bars[4].high
    bars[4].high = first_high + 20.0
    force_touch(bars, strategy_obj, 5)
    bars[6].close = bars[5].high + 0.5

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries == []
    assert any(event.reason == "only_first_touch_is_valid" for event in result.events)


def test_opposite_cross_expires_setup_before_confirmation() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 90, 89])
    strategy_obj = strategy()
    force_touch(bars, strategy_obj, 4)

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries == []
    assert any(event.reason == "opposite_cross" for event in result.events)


def test_touch_timeout_after_30_bars() -> None:
    bars = make_bars([100, 100, 100, 110] + [115 + index for index in range(32)])
    strategy_obj = strategy()

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries == []
    assert any(event.reason == "touch_timeout" for event in result.events)


def test_confirmation_timeout_after_10_bars() -> None:
    bars = make_bars([100, 100, 100, 110] + [108] * 13)
    strategy_obj = strategy()
    force_touch(bars, strategy_obj, 4)
    bars[4].high = 999.0

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries == []
    assert any(event.reason == "confirmation_timeout" for event in result.events)


def test_take_profit_exit_records_positive_rr() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 112, 113, 114])
    strategy_obj = strategy(rr=1.5)
    force_touch(bars, strategy_obj, 4)
    bars[6].open = 113.0

    signal = strategy_obj.generate_entries("TEST", bars)
    take_profit = signal.entries[0].trade.take_profit_price
    bars[6].high = take_profit + 0.1

    result = BacktestEngine().run("TEST", bars, strategy_obj)

    assert len(result.trades) == 1
    trade = result.trades[0]
    assert trade.exit_reason == "take_profit"
    assert trade.r_multiple == pytest.approx(1.5)


def test_stop_loss_exit_records_minus_one_r() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 112, 113, 114])
    strategy_obj = strategy(rr=1.5)
    force_touch(bars, strategy_obj, 4)
    bars[6].open = 113.0

    signal = strategy_obj.generate_entries("TEST", bars)
    stop = signal.entries[0].trade.stop_price
    bars[6].low = stop - 0.1

    result = BacktestEngine().run("TEST", bars, strategy_obj)

    assert len(result.trades) == 1
    trade = result.trades[0]
    assert trade.exit_reason == "stop_loss"
    assert trade.r_multiple == pytest.approx(-1.0)


def test_same_bar_take_profit_and_stop_loss_prefers_stop_loss() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 112, 113, 114])
    strategy_obj = strategy(rr=1.5)
    force_touch(bars, strategy_obj, 4)
    bars[6].open = 113.0

    signal = strategy_obj.generate_entries("TEST", bars)
    stop = signal.entries[0].trade.stop_price
    take_profit = signal.entries[0].trade.take_profit_price
    bars[6].low = stop - 0.1
    bars[6].high = take_profit + 0.1

    result = BacktestEngine(conservative_same_bar=True).run("TEST", bars, strategy_obj)

    trade = result.trades[0]
    assert trade.exit_reason == "stop_loss"
    assert trade.r_multiple == pytest.approx(-1.0)


def test_end_of_data_exit_records_mark_to_market_r() -> None:
    bars = make_bars([100, 100, 100, 110, 108, 112, 113])
    strategy_obj = strategy(rr=1.5)
    force_touch(bars, strategy_obj, 4)
    bars[6].open = 113.0
    bars[6].high = 113.2
    bars[6].low = 112.8
    bars[6].close = 114.0

    result = BacktestEngine().run("TEST", bars, strategy_obj)

    trade = result.trades[0]
    risk = trade.entry_price - trade.stop_price
    assert trade.exit_reason == "end_of_data"
    assert trade.exit_price == pytest.approx(114.0)
    assert trade.r_multiple == pytest.approx((114.0 - trade.entry_price) / risk)
