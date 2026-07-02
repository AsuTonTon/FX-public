from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


Direction = str


@dataclass
class OHLCBar:
    time: Any
    open: float
    high: float
    low: float
    close: float

    @classmethod
    def from_mapping(cls, row: dict[str, Any]) -> "OHLCBar":
        time = row.get("time", row.get("timestamp"))
        return cls(
            time=time,
            open=float(row["open"]),
            high=float(row["high"]),
            low=float(row["low"]),
            close=float(row["close"]),
        )


@dataclass
class Trade:
    pair: str
    direction: Direction
    setup_time: Any
    touch_time: Any
    confirmation_time: Any
    entry_time: Any
    entry_price: float
    stop_price: float
    take_profit_price: float
    tp1_price: float | None = None
    tp2_price: float | None = None
    tp1_r: float | None = None
    tp2_r: float | None = None
    partial_exit_ratio: float | None = None
    exit_time: Any | None = None
    exit_price: float | None = None
    exit_reason: str | None = None
    r_multiple: float | None = None
    bars_held: int | None = None


@dataclass
class EntryOrder:
    trade: Trade
    entry_index: int
    confirmation_index: int
    setup_index: int
    touch_index: int
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class BacktestEvent:
    event_type: str
    pair: str
    time: Any
    direction: Direction | None = None
    reason: str | None = None
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class StrategySignalResult:
    entries: list[EntryOrder] = field(default_factory=list)
    events: list[BacktestEvent] = field(default_factory=list)
    candidates: list[Any] = field(default_factory=list)
    target_candidates: list[Any] = field(default_factory=list)


@dataclass
class BacktestResult:
    trades: list[Trade] = field(default_factory=list)
    events: list[BacktestEvent] = field(default_factory=list)
    candidates: list[Any] = field(default_factory=list)
    target_candidates: list[Any] = field(default_factory=list)
