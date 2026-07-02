from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from math import inf
from statistics import median
from typing import Any

from src.backtest.trade import Trade


def calculate_metrics(trades: list[Trade]) -> dict[str, Any]:
    r_values = [
        float(trade.r_multiple) for trade in trades if trade.r_multiple is not None
    ]
    trade_count = len(r_values)
    wins = [value for value in r_values if value > 0]
    losses = [value for value in r_values if value < 0]
    gross_win = sum(wins)
    gross_loss = abs(sum(losses))

    if gross_loss == 0:
        profit_factor = inf if gross_win > 0 else 0.0
    else:
        profit_factor = gross_win / gross_loss

    return {
        "trade_count": trade_count,
        "win_rate": len(wins) / trade_count if trade_count else 0.0,
        "average_r": sum(r_values) / trade_count if trade_count else 0.0,
        "median_r": median(r_values) if r_values else 0.0,
        "profit_factor": profit_factor,
        "max_consecutive_losses": max_consecutive_losses(r_values),
        "max_drawdown_r": max_drawdown_r(r_values),
        "total_r": sum(r_values),
        "yearly_r": yearly_r(trades),
    }


def max_consecutive_losses(r_values: list[float]) -> int:
    longest = 0
    current = 0
    for value in r_values:
        if value < 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


def max_drawdown_r(r_values: list[float]) -> float:
    equity = 0.0
    peak = 0.0
    max_drawdown = 0.0
    for value in r_values:
        equity += value
        peak = max(peak, equity)
        max_drawdown = min(max_drawdown, equity - peak)
    return max_drawdown


def yearly_r(trades: list[Trade]) -> dict[int, float]:
    totals: dict[int, float] = defaultdict(float)
    for trade in trades:
        if trade.r_multiple is None:
            continue
        year = _extract_year(trade.exit_time)
        if year is not None:
            totals[year] += float(trade.r_multiple)
    return dict(sorted(totals.items()))


def _extract_year(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.year
    if hasattr(value, "year"):
        try:
            return int(value.year)
        except (TypeError, ValueError):
            return None
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value).year
        except ValueError:
            return None
    return None
