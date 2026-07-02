from __future__ import annotations

import math
from datetime import datetime

import pytest

from src.backtest.metrics import calculate_metrics
from src.backtest.trade import Trade


def closed_trade(r_multiple: float, exit_time: datetime) -> Trade:
    return Trade(
        pair="TEST",
        direction="long",
        setup_time=exit_time,
        touch_time=exit_time,
        confirmation_time=exit_time,
        entry_time=exit_time,
        entry_price=100.0,
        stop_price=99.0,
        take_profit_price=101.5,
        exit_time=exit_time,
        exit_price=100.0 + r_multiple,
        exit_reason="test",
        r_multiple=r_multiple,
        bars_held=1,
    )


def test_metrics_are_calculated_from_r_multiples() -> None:
    trades = [
        closed_trade(1.5, datetime(2026, 1, 1)),
        closed_trade(-1.0, datetime(2026, 1, 2)),
        closed_trade(-1.0, datetime(2026, 1, 3)),
        closed_trade(2.0, datetime(2027, 1, 1)),
    ]

    metrics = calculate_metrics(trades)

    assert metrics["trade_count"] == 4
    assert metrics["win_rate"] == pytest.approx(0.5)
    assert metrics["average_r"] == pytest.approx(0.375)
    assert metrics["median_r"] == pytest.approx(0.25)
    assert metrics["profit_factor"] == pytest.approx(1.75)
    assert metrics["max_consecutive_losses"] == 2
    assert metrics["max_drawdown_r"] == pytest.approx(-2.0)
    assert metrics["total_r"] == pytest.approx(1.5)
    assert metrics["yearly_r"] == {2026: -0.5, 2027: 2.0}


def test_profit_factor_is_infinite_when_there_are_no_losses() -> None:
    trades = [
        closed_trade(1.0, datetime(2026, 1, 1)),
        closed_trade(2.0, datetime(2026, 1, 2)),
    ]

    metrics = calculate_metrics(trades)

    assert math.isinf(metrics["profit_factor"])


def test_empty_metrics_are_zero_like() -> None:
    metrics = calculate_metrics([])

    assert metrics["trade_count"] == 0
    assert metrics["win_rate"] == 0.0
    assert metrics["average_r"] == 0.0
    assert metrics["median_r"] == 0.0
    assert metrics["profit_factor"] == 0.0
    assert metrics["max_consecutive_losses"] == 0
    assert metrics["max_drawdown_r"] == 0.0
    assert metrics["total_r"] == 0
    assert metrics["yearly_r"] == {}
