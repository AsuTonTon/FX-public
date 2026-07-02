from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

from src.backtest.trade import (
    BacktestEvent,
    EntryOrder,
    OHLCBar,
    StrategySignalResult,
    Trade,
)


@dataclass
class StrategyAConfig:
    fast_period: int = 20
    slow_period: int = 200
    rr_multiple: float = 1.5
    buffer: float = 0.0
    touch_expiry_bars: int = 30
    confirmation_expiry_bars: int = 10
    min_warmup_bars: int | None = None

    def __post_init__(self) -> None:
        if self.min_warmup_bars is not None and self.min_warmup_bars < 0:
            raise ValueError("min_warmup_bars must be zero or positive")

    @property
    def effective_min_warmup_bars(self) -> int:
        if self.min_warmup_bars is None:
            return self.slow_period
        return self.min_warmup_bars


@dataclass
class IndicatorBar:
    bar: OHLCBar
    ema_fast: float
    ema_slow: float
    cross_up: bool
    cross_down: bool


def calculate_ema(values: Iterable[float], period: int) -> list[float]:
    if period <= 0:
        raise ValueError("period must be positive")
    values_list = [float(value) for value in values]
    if not values_list:
        return []

    alpha = 2.0 / (period + 1.0)
    ema_values = [values_list[0]]
    for value in values_list[1:]:
        ema_values.append(value * alpha + ema_values[-1] * (1.0 - alpha))
    return ema_values


def normalize_bars(rows: Iterable[OHLCBar | dict[str, Any]]) -> list[OHLCBar]:
    bars: list[OHLCBar] = []
    for row in rows:
        if isinstance(row, OHLCBar):
            bars.append(row)
        else:
            bars.append(OHLCBar.from_mapping(row))
    return bars


def add_ema_indicators(
    rows: Iterable[OHLCBar | dict[str, Any]],
    fast_period: int = 20,
    slow_period: int = 200,
) -> list[IndicatorBar]:
    bars = normalize_bars(rows)
    closes = [bar.close for bar in bars]
    ema_fast = calculate_ema(closes, fast_period)
    ema_slow = calculate_ema(closes, slow_period)
    indicator_bars: list[IndicatorBar] = []

    for index, bar in enumerate(bars):
        cross_up = False
        cross_down = False
        if index > 0:
            cross_up = (
                ema_fast[index - 1] <= ema_slow[index - 1]
                and ema_fast[index] > ema_slow[index]
            )
            cross_down = (
                ema_fast[index - 1] >= ema_slow[index - 1]
                and ema_fast[index] < ema_slow[index]
            )
        indicator_bars.append(
            IndicatorBar(
                bar=bar,
                ema_fast=ema_fast[index],
                ema_slow=ema_slow[index],
                cross_up=cross_up,
                cross_down=cross_down,
            )
        )
    return indicator_bars


class EmaWave3StrategyA:
    def __init__(self, config: StrategyAConfig | None = None) -> None:
        self.config = config or StrategyAConfig()

    def with_indicators(
        self, rows: Iterable[OHLCBar | dict[str, Any]]
    ) -> list[IndicatorBar]:
        return add_ema_indicators(
            rows,
            fast_period=self.config.fast_period,
            slow_period=self.config.slow_period,
        )

    def generate_entries(
        self, pair: str, rows: Iterable[OHLCBar | dict[str, Any]]
    ) -> StrategySignalResult:
        bars = self.with_indicators(rows)
        result = StrategySignalResult()
        setup: dict[str, Any] | None = None
        min_warmup_bars = self.config.effective_min_warmup_bars

        for index in range(1, len(bars)):
            current = bars[index]
            direction_from_cross = self._cross_direction(current)

            if index < min_warmup_bars:
                continue

            if direction_from_cross is not None:
                if setup is not None and direction_from_cross != setup["direction"]:
                    result.events.append(
                        self._event(
                            "expired_setup",
                            pair,
                            current,
                            setup["direction"],
                            "opposite_cross",
                            setup,
                        )
                    )
                setup = {
                    "direction": direction_from_cross,
                    "cross_index": index,
                    "setup_time": current.bar.time,
                    "touch_index": None,
                    "touch_time": None,
                    "reference_high": None,
                    "reference_low": None,
                }
                result.events.append(
                    self._event(
                        "setup_started",
                        pair,
                        current,
                        direction_from_cross,
                        None,
                        setup,
                    )
                )
                continue

            if setup is None:
                continue

            if setup["touch_index"] is None:
                if index - setup["cross_index"] > self.config.touch_expiry_bars:
                    result.events.append(
                        self._event(
                            "expired_setup",
                            pair,
                            current,
                            setup["direction"],
                            "touch_timeout",
                            setup,
                        )
                    )
                    setup = None
                    continue

                if index > setup["cross_index"] and self._touches_fast_ema(current):
                    setup["touch_index"] = index
                    setup["touch_time"] = current.bar.time
                    setup["reference_high"] = current.bar.high
                    setup["reference_low"] = current.bar.low
                    result.events.append(
                        self._event(
                            "reference_touch",
                            pair,
                            current,
                            setup["direction"],
                            None,
                            setup,
                        )
                    )
                continue

            if self._touches_fast_ema(current):
                result.events.append(
                    self._event(
                        "ignored_touch",
                        pair,
                        current,
                        setup["direction"],
                        "only_first_touch_is_valid",
                        setup,
                    )
                )

            bars_since_touch = index - int(setup["touch_index"])
            if bars_since_touch > self.config.confirmation_expiry_bars:
                result.events.append(
                    self._event(
                        "expired_setup",
                        pair,
                        current,
                        setup["direction"],
                        "confirmation_timeout",
                        setup,
                    )
                )
                setup = None
                continue

            if bars_since_touch <= 0:
                continue

            if not self._is_confirmed(setup, current):
                continue

            entry_index = index + 1
            if entry_index >= len(bars):
                result.events.append(
                    self._event(
                        "no_trade",
                        pair,
                        current,
                        setup["direction"],
                        "no_next_bar_for_entry",
                        setup,
                    )
                )
                setup = None
                continue

            order = self._build_entry(
                pair, bars, setup, confirmation_index=index, entry_index=entry_index
            )
            if order is None:
                result.events.append(
                    self._event(
                        "no_trade",
                        pair,
                        current,
                        setup["direction"],
                        "invalid_risk",
                        setup,
                    )
                )
            else:
                result.entries.append(order)
            setup = None

        return result

    @staticmethod
    def _cross_direction(bar: IndicatorBar) -> str | None:
        if bar.cross_up:
            return "long"
        if bar.cross_down:
            return "short"
        return None

    @staticmethod
    def _touches_fast_ema(bar: IndicatorBar) -> bool:
        return bar.bar.low <= bar.ema_fast <= bar.bar.high

    @staticmethod
    def _is_confirmed(setup: dict[str, Any], bar: IndicatorBar) -> bool:
        if setup["direction"] == "long":
            return bar.bar.close > float(setup["reference_high"])
        return bar.bar.close < float(setup["reference_low"])

    def _build_entry(
        self,
        pair: str,
        bars: list[IndicatorBar],
        setup: dict[str, Any],
        confirmation_index: int,
        entry_index: int,
    ) -> EntryOrder | None:
        direction = setup["direction"]
        entry_bar = bars[entry_index].bar
        entry_price = entry_bar.open

        if direction == "long":
            stop_price = float(setup["reference_low"]) - self.config.buffer
            risk = entry_price - stop_price
            take_profit_price = entry_price + risk * self.config.rr_multiple
        else:
            stop_price = float(setup["reference_high"]) + self.config.buffer
            risk = stop_price - entry_price
            take_profit_price = entry_price - risk * self.config.rr_multiple

        if risk <= 0:
            return None

        trade = Trade(
            pair=pair,
            direction=direction,
            setup_time=setup["setup_time"],
            touch_time=setup["touch_time"],
            confirmation_time=bars[confirmation_index].bar.time,
            entry_time=entry_bar.time,
            entry_price=entry_price,
            stop_price=stop_price,
            take_profit_price=take_profit_price,
        )
        return EntryOrder(
            trade=trade,
            entry_index=entry_index,
            confirmation_index=confirmation_index,
            setup_index=int(setup["cross_index"]),
            touch_index=int(setup["touch_index"]),
        )

    @staticmethod
    def _event(
        event_type: str,
        pair: str,
        bar: IndicatorBar,
        direction: str | None,
        reason: str | None,
        setup: dict[str, Any],
    ) -> BacktestEvent:
        return BacktestEvent(
            event_type=event_type,
            pair=pair,
            time=bar.bar.time,
            direction=direction,
            reason=reason,
            details={
                "setup_time": setup.get("setup_time"),
                "touch_time": setup.get("touch_time"),
                "cross_index": setup.get("cross_index"),
                "touch_index": setup.get("touch_index"),
            },
        )
