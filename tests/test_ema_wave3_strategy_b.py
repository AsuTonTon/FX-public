from __future__ import annotations

from typing import Any
from collections.abc import Sequence
from datetime import datetime, timedelta

import pytest

from src.backtest.strategy_b_runner import StrategyBBacktestEngine
from src.backtest.trade import EntryOrder, OHLCBar, StrategySignalResult, Trade
from src.strategies.ema_wave3_strategy_a import EmaWave3StrategyA, StrategyAConfig
from src.strategies.ema_wave3_strategy_b import (
    EmaWave3StrategyB,
    StrategyBConfig,
    calculate_atr,
    detect_swings,
)


def make_bars(closes: Sequence[float]) -> list[OHLCBar]:
    start = datetime(2026, 1, 1)
    return [
        OHLCBar(
            time=start + timedelta(hours=4 * index),
            open=close,
            high=close + 0.5,
            low=close - 0.5,
            close=close,
        )
        for index, close in enumerate(closes)
    ]


def base_config(**overrides: Any) -> StrategyBConfig:
    values: dict[str, Any] = {
        "fast_period": 2,
        "slow_period": 3,
        "min_warmup_bars": 4,
        "atr_period": 2,
        "adx_period": 2,
        "adx_minimum": 0.0,
        "swing_width": 1,
        "swing_lookback_bars": 20,
        "tp1_min_rr": 0.1,
        "tp2_min_rr": 0.2,
        "tp1_only_min_rr": 0.2,
        "min_stop_atr_multiple": 0.0,
        "max_stop_atr_multiple": 100.0,
        "pair_buffer": 0.0,
        "tick_size": 0.01,
    }
    values.update(overrides)
    return StrategyBConfig(**values)


def force_touch(
    bars: list[OHLCBar], strategy_obj: EmaWave3StrategyB, index: int
) -> None:
    indicator = strategy_obj.with_indicators(bars)[index]
    bars[index].low = min(bars[index].low, indicator.ema_fast - 0.1)
    bars[index].high = max(bars[index].high, indicator.ema_fast + 0.1)


def long_fixture(
    config: StrategyBConfig | None = None,
    *,
    include_left_targets: bool = True,
) -> tuple[list[OHLCBar], EmaWave3StrategyB]:
    bars = make_bars([100, 120, 90, 90, 90, 90, 90, 110, 108, 112, 113, 130, 140])
    if include_left_targets:
        bars[1].high = 125
        bars[3].high = 130
        bars[5].high = 140
    else:
        bars[1].high = 105
        bars[3].high = 106
        bars[5].high = 107
        bars[11].high = 150
    bars[1].low = 119
    bars[2].high = 91
    bars[2].low = 80
    bars[3].low = 85
    bars[4].high = 91
    bars[4].low = 89
    bars[5].low = 88
    bars[6].high = 91
    bars[6].low = 89
    strategy_obj = EmaWave3StrategyB(config or base_config())
    force_touch(bars, strategy_obj, 8)
    bars[10].open = 113
    return bars, strategy_obj


def short_fixture() -> tuple[list[OHLCBar], EmaWave3StrategyB]:
    bars = make_bars([100, 80, 110, 110, 110, 110, 110, 90, 92, 88, 87, 70, 60])
    bars[1].low = 75
    bars[1].high = 81
    bars[2].low = 109
    bars[2].high = 120
    bars[3].low = 70
    bars[3].high = 115
    bars[4].low = 109
    bars[4].high = 111
    bars[5].low = 60
    bars[5].high = 112
    bars[6].low = 109
    bars[6].high = 111
    strategy_obj = EmaWave3StrategyB(base_config())
    force_touch(bars, strategy_obj, 8)
    bars[10].open = 87
    return bars, strategy_obj


def manual_long_order(
    bars: list[OHLCBar],
    *,
    tp2_price: float | None = 120.0,
) -> EntryOrder:
    trade = Trade(
        pair="TEST",
        direction="long",
        setup_time=bars[0].time,
        touch_time=bars[0].time,
        confirmation_time=bars[0].time,
        entry_time=bars[0].time,
        entry_price=100.0,
        stop_price=90.0,
        take_profit_price=tp2_price or 110.0,
        tp1_price=110.0,
        tp2_price=tp2_price,
        tp1_r=1.0,
        tp2_r=2.0 if tp2_price is not None else None,
        partial_exit_ratio=0.5 if tp2_price is not None else 1.0,
    )
    return EntryOrder(
        trade=trade,
        entry_index=0,
        confirmation_index=0,
        setup_index=0,
        touch_index=0,
    )


def test_swing_high_low_detection() -> None:
    bars = [
        OHLCBar(0, 10, 11, 9, 10),
        OHLCBar(1, 10, 15, 8, 10),
        OHLCBar(2, 10, 11, 9, 10),
    ]

    swings = detect_swings(bars, width=1)

    assert any(swing.kind == "high" and swing.index == 1 for swing in swings)
    assert any(swing.kind == "low" and swing.index == 1 for swing in swings)


def test_future_swing_is_not_used_for_target() -> None:
    bars, strategy_obj = long_fixture(include_left_targets=False)

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries == []
    assert any(event.reason == "no_left_side_tp1" for event in result.events)


def test_tp1_tp2_selection_for_long() -> None:
    bars, strategy_obj = long_fixture()

    result = strategy_obj.generate_entries("TEST", bars)

    assert len(result.entries) == 1
    trade = result.entries[0].trade
    assert trade.direction == "long"
    assert trade.tp1_price == pytest.approx(125)
    assert trade.tp2_price == pytest.approx(130)


def test_tp_candidate_diagnostics_include_selected_tp1_and_tp2() -> None:
    bars, strategy_obj = long_fixture()

    result = strategy_obj.generate_entries("TEST", bars)

    trade = result.entries[0].trade
    first_target = result.target_candidates[0]
    second_target = result.target_candidates[1]
    assert first_target.target_rank == 1
    assert first_target.target_price == pytest.approx(trade.tp1_price)
    assert first_target.target_r == pytest.approx(trade.tp1_r)
    assert first_target.selected_tp1 is True
    assert first_target.selected_tp2 is False
    assert second_target.target_rank == 2
    assert second_target.target_price == pytest.approx(trade.tp2_price)
    assert second_target.target_r == pytest.approx(trade.tp2_r)
    assert second_target.selected_tp1 is False
    assert second_target.selected_tp2 is True


def test_tp1_tp2_selection_for_short() -> None:
    bars, strategy_obj = short_fixture()

    result = strategy_obj.generate_entries("TEST", bars)

    assert len(result.entries) == 1
    trade = result.entries[0].trade
    assert trade.direction == "short"
    assert trade.tp1_price == pytest.approx(75)
    assert trade.tp2_price == pytest.approx(70)


def test_minimum_rr_gate_passes_and_fails() -> None:
    bars, passing_strategy = long_fixture()
    passing_result = passing_strategy.generate_entries("TEST", bars)

    failing_bars, failing_strategy = long_fixture(base_config(tp1_min_rr=0.6))
    failing_result = failing_strategy.generate_entries("TEST", failing_bars)

    assert len(passing_result.entries) == 1
    assert failing_result.entries == []
    assert any(event.reason == "tp1_below_min_rr" for event in failing_result.events)


def test_accepted_candidate_has_pass_flags() -> None:
    bars, strategy_obj = long_fixture()

    result = strategy_obj.generate_entries("TEST", bars)

    candidate = result.candidates[0]
    assert candidate.accepted is True
    assert candidate.first_fail_reason is None
    assert candidate.all_failed_reasons == ()
    assert candidate.adx_pass is True
    assert candidate.left_side_tp1_available is True
    assert candidate.stop_too_narrow_pass is True
    assert candidate.stop_too_wide_pass is True
    assert candidate.tp1_min_rr_pass is True
    assert candidate.tp2_min_rr_pass is True


def test_tp1_below_min_rr_candidate_records_failure() -> None:
    bars, strategy_obj = long_fixture(base_config(tp1_min_rr=0.6))

    result = strategy_obj.generate_entries("TEST", bars)

    candidate = result.candidates[0]
    assert result.entries == []
    assert candidate.accepted is False
    assert candidate.first_fail_reason == "tp1_below_min_rr"
    assert "tp1_below_min_rr" in candidate.all_failed_reasons
    assert candidate.tp1_min_rr_pass is False
    assert candidate.tp1_r is not None
    assert result.target_candidates[0].accepted is False
    assert result.target_candidates[0].first_fail_reason == "tp1_below_min_rr"


def test_atr_calculation_uses_true_range_average() -> None:
    bars = [
        OHLCBar(0, 10, 12, 9, 11),
        OHLCBar(1, 11, 13, 10, 12),
    ]

    atr = calculate_atr(bars, period=2)

    assert atr == [None, pytest.approx(3.0)]


def test_atr_buffer_uses_largest_component() -> None:
    bars, strategy_obj = long_fixture(base_config(pair_buffer=0.1, tick_size=0.01))

    result = strategy_obj.generate_entries("TEST", bars)

    details = result.entries[0].details
    assert details["buffer"] == pytest.approx(details["atr"] * 0.10)


def test_stop_distance_sanity_checks_too_narrow_and_too_wide() -> None:
    narrow_bars, narrow_strategy = long_fixture(base_config(min_stop_atr_multiple=10.0))
    wide_bars, wide_strategy = long_fixture(
        base_config(min_stop_atr_multiple=0.0, max_stop_atr_multiple=1.0)
    )

    narrow_result = narrow_strategy.generate_entries("TEST", narrow_bars)
    wide_result = wide_strategy.generate_entries("TEST", wide_bars)

    assert any(event.reason == "stop_too_narrow" for event in narrow_result.events)
    assert any(event.reason == "stop_too_wide" for event in wide_result.events)


def test_stop_too_wide_candidate_records_failure() -> None:
    bars, strategy_obj = long_fixture(base_config(max_stop_atr_multiple=1.0))

    result = strategy_obj.generate_entries("TEST", bars)

    candidate = result.candidates[0]
    assert result.entries == []
    assert candidate.first_fail_reason == "stop_too_wide"
    assert "stop_too_wide" in candidate.all_failed_reasons
    assert candidate.stop_too_wide_pass is False
    assert candidate.stop_distance_atr is not None
    assert candidate.stop_distance_atr > 1.0


def test_adx_below_threshold_creates_no_trade() -> None:
    bars, strategy_obj = long_fixture(base_config(adx_minimum=99.0))

    result = strategy_obj.generate_entries("TEST", bars)

    assert result.entries == []
    assert any(event.reason == "adx_below_threshold" for event in result.events)


def test_adx_below_threshold_candidate_records_failure() -> None:
    bars, strategy_obj = long_fixture(base_config(adx_minimum=99.0))

    result = strategy_obj.generate_entries("TEST", bars)

    candidate = result.candidates[0]
    assert candidate.first_fail_reason == "adx_below_threshold"
    assert "adx_below_threshold" in candidate.all_failed_reasons
    assert candidate.adx_pass is False
    assert candidate.accepted is False


def test_no_left_side_tp1_candidate_records_failure() -> None:
    bars, strategy_obj = long_fixture(include_left_targets=False)

    result = strategy_obj.generate_entries("TEST", bars)

    candidate = result.candidates[0]
    assert candidate.first_fail_reason == "no_left_side_tp1"
    assert candidate.left_side_tp1_available is False
    assert candidate.tp1_price is None
    assert "no_left_side_tp1" in candidate.all_failed_reasons
    assert result.target_candidates == []


def test_tp_candidate_prominence_is_deterministic_and_left_side_only() -> None:
    bars, strategy_obj = long_fixture()

    first_result = strategy_obj.generate_entries("TEST", bars)
    second_result = strategy_obj.generate_entries("TEST", bars)

    first_values = [
        (
            diagnostic.target_rank,
            diagnostic.simple_prominence,
            diagnostic.simple_prominence_atr,
        )
        for diagnostic in first_result.target_candidates
    ]
    second_values = [
        (
            diagnostic.target_rank,
            diagnostic.simple_prominence,
            diagnostic.simple_prominence_atr,
        )
        for diagnostic in second_result.target_candidates
    ]
    assert first_values == second_values

    confirmation_index = first_result.entries[0].confirmation_index
    assert all(
        diagnostic.swing_index + strategy_obj.config.swing_width < confirmation_index
        for diagnostic in first_result.target_candidates
    )


def test_candidate_first_fail_reason_preserves_gate_order() -> None:
    bars, strategy_obj = long_fixture(
        base_config(max_stop_atr_multiple=1.0, tp1_min_rr=10.0)
    )

    result = strategy_obj.generate_entries("TEST", bars)

    candidate = result.candidates[0]
    assert candidate.first_fail_reason == "stop_too_wide"
    assert "stop_too_wide" in candidate.all_failed_reasons
    assert "tp1_below_min_rr" in candidate.all_failed_reasons


def test_strategy_a_setup_logic_indices_are_unchanged() -> None:
    bars, strategy_b = long_fixture()
    strategy_a = EmaWave3StrategyA(
        StrategyAConfig(
            fast_period=2,
            slow_period=3,
            min_warmup_bars=4,
            touch_expiry_bars=30,
            confirmation_expiry_bars=10,
        )
    )

    result_a = strategy_a.generate_entries("TEST", bars)
    result_b = strategy_b.generate_entries("TEST", bars)

    order_a = result_a.entries[0]
    order_b = result_b.entries[0]
    assert order_b.setup_index == order_a.setup_index
    assert order_b.touch_index == order_a.touch_index
    assert order_b.confirmation_index == order_a.confirmation_index
    assert order_b.entry_index == order_a.entry_index


def test_tp1_partial_exit_and_tp2_final_exit() -> None:
    bars = make_bars([100, 100])
    bars[0].high = 111
    bars[0].low = 95
    bars[1].high = 121
    bars[1].low = 101

    result = StrategyBBacktestEngine().run(
        "TEST", bars, StaticStrategy(manual_long_order(bars))
    )

    trade = result.trades[0]
    assert any(event.event_type == "tp1_hit" for event in result.events)
    assert trade.exit_reason == "take_profit"
    assert trade.r_multiple == pytest.approx(1.5)


def test_tp1_then_breakeven_exit() -> None:
    bars = make_bars([100, 100])
    bars[0].high = 111
    bars[0].low = 95
    bars[1].high = 115
    bars[1].low = 100

    result = StrategyBBacktestEngine().run(
        "TEST", bars, StaticStrategy(manual_long_order(bars))
    )

    trade = result.trades[0]
    assert trade.exit_reason == "breakeven_after_tp1"
    assert trade.exit_price == pytest.approx(100)
    assert trade.r_multiple == pytest.approx(0.5)


def test_same_bar_stop_and_tp1_prefers_stop_loss() -> None:
    bars = make_bars([100])
    bars[0].high = 111
    bars[0].low = 89

    result = StrategyBBacktestEngine(conservative_same_bar=True).run(
        "TEST", bars, StaticStrategy(manual_long_order(bars))
    )

    trade = result.trades[0]
    assert trade.exit_reason == "stop_loss"
    assert trade.r_multiple == pytest.approx(-1.0)
    assert not any(event.event_type == "tp1_hit" for event in result.events)


class StaticStrategy:
    def __init__(self, order: EntryOrder) -> None:
        self.order = order

    def generate_entries(self, pair: str, rows: list[OHLCBar]) -> object:
        del pair, rows
        return StrategySignalResult(entries=[self.order])
