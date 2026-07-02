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
from src.strategies.ema_wave3_strategy_a import calculate_ema, normalize_bars


TARGET_CANDIDATE_DIAGNOSTIC_LIMIT = 5


@dataclass(frozen=True)
class SwingPoint:
    index: int
    price: float
    kind: str


@dataclass
class StrategyBConfig:
    fast_period: int = 20
    slow_period: int = 200
    pair_buffer: float = 0.0
    tick_size: float = 0.0
    touch_expiry_bars: int = 30
    confirmation_expiry_bars: int = 10
    min_warmup_bars: int | None = None
    atr_period: int = 14
    atr_buffer_multiplier: float = 0.10
    swing_width: int = 2
    swing_lookback_bars: int = 100
    tp1_min_rr: float = 1.0
    tp2_min_rr: float = 1.5
    tp1_only_min_rr: float = 1.5
    partial_exit_ratio: float = 0.5
    adx_period: int = 14
    adx_minimum: float = 18.0
    min_stop_atr_multiple: float = 0.25
    max_stop_atr_multiple: float = 3.0

    def __post_init__(self) -> None:
        if self.min_warmup_bars is not None and self.min_warmup_bars < 0:
            raise ValueError("min_warmup_bars must be zero or positive")
        if self.atr_period <= 0:
            raise ValueError("atr_period must be positive")
        if self.adx_period <= 0:
            raise ValueError("adx_period must be positive")
        if self.swing_width <= 0:
            raise ValueError("swing_width must be positive")
        if self.swing_lookback_bars <= 0:
            raise ValueError("swing_lookback_bars must be positive")
        if self.tick_size < 0:
            raise ValueError("tick_size must be zero or positive")
        if self.pair_buffer < 0:
            raise ValueError("pair_buffer must be zero or positive")
        if self.atr_buffer_multiplier < 0:
            raise ValueError("atr_buffer_multiplier must be zero or positive")
        if not 0 < self.partial_exit_ratio < 1:
            raise ValueError("partial_exit_ratio must be between zero and one")

    @property
    def effective_min_warmup_bars(self) -> int:
        if self.min_warmup_bars is None:
            return self.slow_period
        return self.min_warmup_bars


@dataclass
class StrategyBIndicatorBar:
    bar: OHLCBar
    ema_fast: float
    ema_slow: float
    atr: float | None
    adx: float | None
    cross_up: bool
    cross_down: bool


@dataclass(frozen=True)
class StrategyBCandidate:
    pair: str
    direction: str
    setup_time: Any
    touch_time: Any
    confirmation_time: Any
    entry_time: Any | None
    entry_price: float | None
    atr: float | None
    adx: float | None
    adx_pass: bool | None
    stop_anchor: float | None
    stop_price: float | None
    buffer: float | None
    risk: float | None
    stop_distance_atr: float | None
    stop_too_narrow_pass: bool | None
    stop_too_wide_pass: bool | None
    tp1_price: float | None
    tp2_price: float | None
    tp1_r: float | None
    tp2_r: float | None
    left_side_tp1_available: bool
    tp1_min_rr_pass: bool | None
    tp1_only_min_rr_pass: bool | None
    tp2_min_rr_pass: bool | None
    accepted: bool
    first_fail_reason: str | None
    all_failed_reasons: tuple[str, ...]


@dataclass(frozen=True)
class StrategyBTargetCandidateDiagnostic:
    pair: str
    direction: str
    setup_time: Any
    touch_time: Any
    confirmation_time: Any
    entry_time: Any
    entry_price: float
    stop_price: float | None
    risk: float | None
    atr: float | None
    target_rank: int
    target_price: float
    target_r: float | None
    swing_index: int
    swing_kind: str
    swing_time: Any
    swing_bar_distance_from_confirmation: int
    swing_price_distance_from_entry: float
    swing_price_distance_atr: float | None
    simple_prominence: float | None
    simple_prominence_atr: float | None
    selected_tp1: bool
    selected_tp2: bool
    accepted: bool
    first_fail_reason: str | None


def calculate_true_ranges(bars: list[OHLCBar]) -> list[float]:
    ranges: list[float] = []
    for index, bar in enumerate(bars):
        if index == 0:
            ranges.append(bar.high - bar.low)
            continue
        previous_close = bars[index - 1].close
        ranges.append(
            max(
                bar.high - bar.low,
                abs(bar.high - previous_close),
                abs(bar.low - previous_close),
            )
        )
    return ranges


def calculate_atr(bars: list[OHLCBar], period: int = 14) -> list[float | None]:
    if period <= 0:
        raise ValueError("period must be positive")
    true_ranges = calculate_true_ranges(bars)
    atr: list[float | None] = []
    for index in range(len(true_ranges)):
        if index + 1 < period:
            atr.append(None)
            continue
        window = true_ranges[index + 1 - period : index + 1]
        atr.append(sum(window) / period)
    return atr


def calculate_adx(bars: list[OHLCBar], period: int = 14) -> list[float | None]:
    if period <= 0:
        raise ValueError("period must be positive")
    if not bars:
        return []

    true_ranges = calculate_true_ranges(bars)
    plus_dm = [0.0]
    minus_dm = [0.0]

    for index in range(1, len(bars)):
        up_move = bars[index].high - bars[index - 1].high
        down_move = bars[index - 1].low - bars[index].low
        plus_dm.append(up_move if up_move > down_move and up_move > 0 else 0.0)
        minus_dm.append(down_move if down_move > up_move and down_move > 0 else 0.0)

    dx_values: list[float | None] = []
    for index in range(len(bars)):
        if index + 1 < period:
            dx_values.append(None)
            continue
        tr_sum = sum(true_ranges[index + 1 - period : index + 1])
        if tr_sum <= 0:
            dx_values.append(0.0)
            continue
        plus_di = 100.0 * sum(plus_dm[index + 1 - period : index + 1]) / tr_sum
        minus_di = 100.0 * sum(minus_dm[index + 1 - period : index + 1]) / tr_sum
        denominator = plus_di + minus_di
        dx_values.append(
            0.0 if denominator <= 0 else 100.0 * abs(plus_di - minus_di) / denominator
        )

    adx: list[float | None] = []
    for index in range(len(dx_values)):
        valid_dx = [value for value in dx_values[: index + 1] if value is not None]
        if len(valid_dx) < period:
            adx.append(None)
            continue
        adx.append(sum(valid_dx[-period:]) / period)
    return adx


def detect_swings(bars: list[OHLCBar], width: int = 2) -> list[SwingPoint]:
    if width <= 0:
        raise ValueError("width must be positive")
    swings: list[SwingPoint] = []
    for index in range(width, len(bars) - width):
        left = bars[index - width : index]
        right = bars[index + 1 : index + 1 + width]
        high = bars[index].high
        low = bars[index].low

        if all(high > bar.high for bar in left + right):
            swings.append(SwingPoint(index=index, price=high, kind="high"))
        if all(low < bar.low for bar in left + right):
            swings.append(SwingPoint(index=index, price=low, kind="low"))
    return swings


def add_strategy_b_indicators(
    rows: Iterable[OHLCBar | dict[str, Any]],
    fast_period: int = 20,
    slow_period: int = 200,
    atr_period: int = 14,
    adx_period: int = 14,
) -> list[StrategyBIndicatorBar]:
    bars = normalize_bars(rows)
    closes = [bar.close for bar in bars]
    ema_fast = calculate_ema(closes, fast_period)
    ema_slow = calculate_ema(closes, slow_period)
    atr_values = calculate_atr(bars, atr_period)
    adx_values = calculate_adx(bars, adx_period)
    indicator_bars: list[StrategyBIndicatorBar] = []

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
            StrategyBIndicatorBar(
                bar=bar,
                ema_fast=ema_fast[index],
                ema_slow=ema_slow[index],
                atr=atr_values[index],
                adx=adx_values[index],
                cross_up=cross_up,
                cross_down=cross_down,
            )
        )
    return indicator_bars


class EmaWave3StrategyB:
    def __init__(self, config: StrategyBConfig | None = None) -> None:
        self.config = config or StrategyBConfig()

    def with_indicators(
        self, rows: Iterable[OHLCBar | dict[str, Any]]
    ) -> list[StrategyBIndicatorBar]:
        return add_strategy_b_indicators(
            rows,
            fast_period=self.config.fast_period,
            slow_period=self.config.slow_period,
            atr_period=self.config.atr_period,
            adx_period=self.config.adx_period,
        )

    def generate_entries(
        self, pair: str, rows: Iterable[OHLCBar | dict[str, Any]]
    ) -> StrategySignalResult:
        bars = self.with_indicators(rows)
        raw_bars = [bar.bar for bar in bars]
        swings = detect_swings(raw_bars, self.config.swing_width)
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

            if bars_since_touch <= 0 or not self._is_confirmed(setup, current):
                continue

            entry_index = index + 1
            if entry_index >= len(bars):
                result.candidates.append(
                    self._no_next_bar_candidate(pair, setup, current)
                )
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

            order, candidate, target_candidates, reason, details = self._build_entry(
                pair,
                bars,
                swings,
                setup,
                confirmation_index=index,
                entry_index=entry_index,
            )
            result.candidates.append(candidate)
            result.target_candidates.extend(target_candidates)
            if order is None:
                result.events.append(
                    self._event(
                        "no_trade",
                        pair,
                        current,
                        setup["direction"],
                        reason,
                        setup,
                        details,
                    )
                )
            else:
                result.entries.append(order)
            setup = None

        return result

    @staticmethod
    def _cross_direction(bar: StrategyBIndicatorBar) -> str | None:
        if bar.cross_up:
            return "long"
        if bar.cross_down:
            return "short"
        return None

    @staticmethod
    def _touches_fast_ema(bar: StrategyBIndicatorBar) -> bool:
        return bar.bar.low <= bar.ema_fast <= bar.bar.high

    @staticmethod
    def _is_confirmed(setup: dict[str, Any], bar: StrategyBIndicatorBar) -> bool:
        if setup["direction"] == "long":
            return bar.bar.close > float(setup["reference_high"])
        return bar.bar.close < float(setup["reference_low"])

    def _build_entry(
        self,
        pair: str,
        bars: list[StrategyBIndicatorBar],
        swings: list[SwingPoint],
        setup: dict[str, Any],
        confirmation_index: int,
        entry_index: int,
    ) -> tuple[
        EntryOrder | None,
        StrategyBCandidate,
        list[StrategyBTargetCandidateDiagnostic],
        str | None,
        dict[str, Any],
    ]:
        confirmation = bars[confirmation_index]
        atr = confirmation.atr
        adx = confirmation.adx
        direction = str(setup["direction"])
        entry_bar = bars[entry_index].bar
        entry_price = entry_bar.open
        failed_reasons: list[str] = []

        if atr is None or atr <= 0:
            failed_reasons.append("atr_unavailable")

        adx_pass: bool | None
        if self.config.adx_minimum <= 0:
            adx_pass = True
        elif adx is None:
            adx_pass = False
            failed_reasons.append("adx_unavailable")
        elif adx < self.config.adx_minimum:
            adx_pass = False
            failed_reasons.append("adx_below_threshold")
        else:
            adx_pass = True

        target_swings = self._ordered_target_swings(
            swings=swings,
            direction=direction,
            entry_price=entry_price,
            confirmation_index=confirmation_index,
        )
        targets = self._target_prices(target_swings)
        left_side_tp1_available = targets[0] is not None
        if not left_side_tp1_available:
            failed_reasons.append("no_left_side_tp1")

        buffer: float | None = None
        stop_anchor: float | None = None
        stop_price: float | None = None
        risk: float | None = None
        stop_distance_atr: float | None = None
        stop_too_narrow_pass: bool | None = None
        stop_too_wide_pass: bool | None = None
        tp1_r: float | None = None
        tp2_r: float | None = None
        tp1_min_rr_pass: bool | None = None
        tp1_only_min_rr_pass: bool | None = None
        tp2_min_rr_pass: bool | None = None

        if atr is not None and atr > 0 and targets[0] is not None:
            buffer = max(
                self.config.pair_buffer,
                self.config.atr_buffer_multiplier * atr,
                self.config.tick_size,
            )
            stop_anchor = self._select_stop_anchor(
                swings=swings,
                setup=setup,
                direction=direction,
                confirmation_index=confirmation_index,
            )

            if direction == "long":
                stop_price = stop_anchor - buffer
                risk = entry_price - stop_price
                tp1_r = (targets[0] - entry_price) / risk if risk > 0 else 0.0
                tp2_r = (
                    (targets[1] - entry_price) / risk
                    if targets[1] is not None and risk > 0
                    else None
                )
            else:
                stop_price = stop_anchor + buffer
                risk = stop_price - entry_price
                tp1_r = (entry_price - targets[0]) / risk if risk > 0 else 0.0
                tp2_r = (
                    (entry_price - targets[1]) / risk
                    if targets[1] is not None and risk > 0
                    else None
                )

            if risk <= 0:
                failed_reasons.append("invalid_risk")
            else:
                stop_distance_atr = risk / atr
                stop_too_narrow_pass = risk >= self.config.min_stop_atr_multiple * atr
                stop_too_wide_pass = risk <= self.config.max_stop_atr_multiple * atr
                tp1_min_rr_pass = tp1_r >= self.config.tp1_min_rr
                if not stop_too_narrow_pass:
                    failed_reasons.append("stop_too_narrow")
                if not stop_too_wide_pass:
                    failed_reasons.append("stop_too_wide")
                if not tp1_min_rr_pass:
                    failed_reasons.append("tp1_below_min_rr")
                if targets[1] is None:
                    tp1_only_min_rr_pass = tp1_r >= self.config.tp1_only_min_rr
                    if not tp1_only_min_rr_pass:
                        failed_reasons.append("tp1_only_below_min_rr")
                else:
                    tp2_min_rr_pass = (
                        tp2_r is not None and tp2_r >= self.config.tp2_min_rr
                    )
                    if not tp2_min_rr_pass:
                        failed_reasons.append("tp2_below_min_rr")

        first_fail_reason = self._first_fail_reason(failed_reasons)
        accepted = first_fail_reason is None

        details = {
            "atr": atr,
            "adx": adx,
            "buffer": buffer,
            "risk": risk,
            "stop_anchor": stop_anchor,
            "tp1_price": targets[0],
            "tp2_price": targets[1],
            "tp1_r": tp1_r,
            "tp2_r": tp2_r,
        }
        candidate = StrategyBCandidate(
            pair=pair,
            direction=direction,
            setup_time=setup["setup_time"],
            touch_time=setup["touch_time"],
            confirmation_time=confirmation.bar.time,
            entry_time=entry_bar.time,
            entry_price=entry_price,
            atr=atr,
            adx=adx,
            adx_pass=adx_pass,
            stop_anchor=stop_anchor,
            stop_price=stop_price,
            buffer=buffer,
            risk=risk,
            stop_distance_atr=stop_distance_atr,
            stop_too_narrow_pass=stop_too_narrow_pass,
            stop_too_wide_pass=stop_too_wide_pass,
            tp1_price=targets[0],
            tp2_price=targets[1],
            tp1_r=tp1_r,
            tp2_r=tp2_r,
            left_side_tp1_available=left_side_tp1_available,
            tp1_min_rr_pass=tp1_min_rr_pass,
            tp1_only_min_rr_pass=tp1_only_min_rr_pass,
            tp2_min_rr_pass=tp2_min_rr_pass,
            accepted=accepted,
            first_fail_reason=first_fail_reason,
            all_failed_reasons=tuple(failed_reasons),
        )
        target_candidates = self._target_candidate_diagnostics(
            pair=pair,
            bars=bars,
            setup=setup,
            direction=direction,
            confirmation_index=confirmation_index,
            entry_bar=entry_bar,
            entry_price=entry_price,
            atr=atr,
            stop_price=stop_price,
            risk=risk,
            target_swings=target_swings,
            accepted=accepted,
            first_fail_reason=first_fail_reason,
        )
        if not accepted:
            return (
                None,
                candidate,
                target_candidates,
                first_fail_reason,
                self._event_details(first_fail_reason, details, atr, adx),
            )

        if stop_price is None or targets[0] is None:
            raise ValueError("accepted Strategy B candidate requires stop and TP1")

        full_exit_at_tp1 = False
        if targets[1] is None:
            full_exit_at_tp1 = True
            take_profit_price = targets[0]
        else:
            take_profit_price = targets[1]

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
            tp1_price=targets[0],
            tp2_price=targets[1],
            tp1_r=tp1_r,
            tp2_r=tp2_r,
            partial_exit_ratio=(
                1.0 if full_exit_at_tp1 else self.config.partial_exit_ratio
            ),
        )
        details["full_exit_at_tp1"] = full_exit_at_tp1
        return (
            EntryOrder(
                trade=trade,
                entry_index=entry_index,
                confirmation_index=confirmation_index,
                setup_index=int(setup["cross_index"]),
                touch_index=int(setup["touch_index"]),
                details=details,
            ),
            candidate,
            target_candidates,
            None,
            details,
        )

    def _no_next_bar_candidate(
        self,
        pair: str,
        setup: dict[str, Any],
        confirmation: StrategyBIndicatorBar,
    ) -> StrategyBCandidate:
        return StrategyBCandidate(
            pair=pair,
            direction=str(setup["direction"]),
            setup_time=setup["setup_time"],
            touch_time=setup["touch_time"],
            confirmation_time=confirmation.bar.time,
            entry_time=None,
            entry_price=None,
            atr=confirmation.atr,
            adx=confirmation.adx,
            adx_pass=None,
            stop_anchor=None,
            stop_price=None,
            buffer=None,
            risk=None,
            stop_distance_atr=None,
            stop_too_narrow_pass=None,
            stop_too_wide_pass=None,
            tp1_price=None,
            tp2_price=None,
            tp1_r=None,
            tp2_r=None,
            left_side_tp1_available=False,
            tp1_min_rr_pass=None,
            tp1_only_min_rr_pass=None,
            tp2_min_rr_pass=None,
            accepted=False,
            first_fail_reason="no_next_bar_for_entry",
            all_failed_reasons=("no_next_bar_for_entry",),
        )

    @staticmethod
    def _first_fail_reason(failed_reasons: list[str]) -> str | None:
        gate_order = (
            "atr_unavailable",
            "adx_unavailable",
            "adx_below_threshold",
            "no_left_side_tp1",
            "invalid_risk",
            "stop_too_narrow",
            "stop_too_wide",
            "tp1_below_min_rr",
            "tp1_only_below_min_rr",
            "tp2_below_min_rr",
        )
        for reason in gate_order:
            if reason in failed_reasons:
                return reason
        return None

    @staticmethod
    def _event_details(
        reason: str | None,
        details: dict[str, Any],
        atr: float | None,
        adx: float | None,
    ) -> dict[str, Any]:
        if reason == "atr_unavailable":
            return {"atr": atr}
        if reason in {"adx_unavailable", "adx_below_threshold", "no_left_side_tp1"}:
            return {"atr": atr, "adx": adx}
        return details

    def _select_targets(
        self,
        swings: list[SwingPoint],
        direction: str,
        entry_price: float,
        confirmation_index: int,
    ) -> tuple[float | None, float | None]:
        return self._target_prices(
            self._ordered_target_swings(
                swings=swings,
                direction=direction,
                entry_price=entry_price,
                confirmation_index=confirmation_index,
            )
        )

    def _ordered_target_swings(
        self,
        swings: list[SwingPoint],
        direction: str,
        entry_price: float,
        confirmation_index: int,
    ) -> list[SwingPoint]:
        valid_swings = self._valid_left_swings(swings, confirmation_index)
        if direction == "long":
            return sorted(
                (
                    swing
                    for swing in valid_swings
                    if swing.kind == "high" and swing.price > entry_price
                ),
                key=lambda swing: (swing.price, swing.index),
            )
        return sorted(
            (
                swing
                for swing in valid_swings
                if swing.kind == "low" and swing.price < entry_price
            ),
            key=lambda swing: (-swing.price, swing.index),
        )

    @staticmethod
    def _target_prices(
        target_swings: list[SwingPoint],
    ) -> tuple[float | None, float | None]:
        targets = [swing.price for swing in target_swings]
        if not targets:
            return None, None
        tp1 = targets[0]
        tp2 = targets[1] if len(targets) > 1 else None
        return tp1, tp2

    def _target_candidate_diagnostics(
        self,
        *,
        pair: str,
        bars: list[StrategyBIndicatorBar],
        setup: dict[str, Any],
        direction: str,
        confirmation_index: int,
        entry_bar: OHLCBar,
        entry_price: float,
        atr: float | None,
        stop_price: float | None,
        risk: float | None,
        target_swings: list[SwingPoint],
        accepted: bool,
        first_fail_reason: str | None,
    ) -> list[StrategyBTargetCandidateDiagnostic]:
        diagnostics: list[StrategyBTargetCandidateDiagnostic] = []
        for rank, swing in enumerate(
            target_swings[:TARGET_CANDIDATE_DIAGNOSTIC_LIMIT], start=1
        ):
            price_distance = self._target_price_distance(
                direction=direction,
                entry_price=entry_price,
                target_price=swing.price,
            )
            target_r = price_distance / risk if risk is not None and risk > 0 else None
            price_distance_atr = (
                price_distance / atr if atr is not None and atr > 0 else None
            )
            simple_prominence = self._simple_swing_prominence(
                bars=bars,
                swing=swing,
                confirmation_index=confirmation_index,
            )
            simple_prominence_atr = (
                simple_prominence / atr
                if simple_prominence is not None and atr is not None and atr > 0
                else None
            )
            diagnostics.append(
                StrategyBTargetCandidateDiagnostic(
                    pair=pair,
                    direction=direction,
                    setup_time=setup["setup_time"],
                    touch_time=setup["touch_time"],
                    confirmation_time=bars[confirmation_index].bar.time,
                    entry_time=entry_bar.time,
                    entry_price=entry_price,
                    stop_price=stop_price,
                    risk=risk,
                    atr=atr,
                    target_rank=rank,
                    target_price=swing.price,
                    target_r=target_r,
                    swing_index=swing.index,
                    swing_kind=swing.kind,
                    swing_time=bars[swing.index].bar.time,
                    swing_bar_distance_from_confirmation=confirmation_index
                    - swing.index,
                    swing_price_distance_from_entry=price_distance,
                    swing_price_distance_atr=price_distance_atr,
                    simple_prominence=simple_prominence,
                    simple_prominence_atr=simple_prominence_atr,
                    selected_tp1=rank == 1,
                    selected_tp2=rank == 2,
                    accepted=accepted,
                    first_fail_reason=first_fail_reason,
                )
            )
        return diagnostics

    @staticmethod
    def _target_price_distance(
        *,
        direction: str,
        entry_price: float,
        target_price: float,
    ) -> float:
        if direction == "long":
            return target_price - entry_price
        return entry_price - target_price

    def _simple_swing_prominence(
        self,
        *,
        bars: list[StrategyBIndicatorBar],
        swing: SwingPoint,
        confirmation_index: int,
    ) -> float | None:
        width = self.config.swing_width
        if swing.index - width < 0 or swing.index + width >= confirmation_index:
            return None

        neighbors = [
            indicator.bar
            for indicator in (
                bars[swing.index - width : swing.index]
                + bars[swing.index + 1 : swing.index + 1 + width]
            )
        ]
        if len(neighbors) != width * 2:
            return None

        if swing.kind == "high":
            return max(0.0, swing.price - max(bar.high for bar in neighbors))
        return max(0.0, min(bar.low for bar in neighbors) - swing.price)

    def _select_stop_anchor(
        self,
        swings: list[SwingPoint],
        setup: dict[str, Any],
        direction: str,
        confirmation_index: int,
    ) -> float:
        valid_swings = self._valid_left_swings(swings, confirmation_index)
        if direction == "long":
            reference_low = float(setup["reference_low"])
            candidates = sorted(
                (
                    swing.price
                    for swing in valid_swings
                    if swing.kind == "low" and swing.price < reference_low
                ),
                reverse=True,
            )
            return candidates[0] if candidates else reference_low

        reference_high = float(setup["reference_high"])
        candidates = sorted(
            swing.price
            for swing in valid_swings
            if swing.kind == "high" and swing.price > reference_high
        )
        return candidates[0] if candidates else reference_high

    def _valid_left_swings(
        self, swings: list[SwingPoint], confirmation_index: int
    ) -> list[SwingPoint]:
        start_index = max(0, confirmation_index - self.config.swing_lookback_bars)
        return [
            swing
            for swing in swings
            if start_index <= swing.index < confirmation_index
            and swing.index + self.config.swing_width < confirmation_index
        ]

    @staticmethod
    def _event(
        event_type: str,
        pair: str,
        bar: StrategyBIndicatorBar,
        direction: str | None,
        reason: str | None,
        setup: dict[str, Any],
        extra_details: dict[str, Any] | None = None,
    ) -> BacktestEvent:
        details = {
            "setup_time": setup.get("setup_time"),
            "touch_time": setup.get("touch_time"),
            "cross_index": setup.get("cross_index"),
            "touch_index": setup.get("touch_index"),
        }
        if extra_details:
            details.update(extra_details)
        return BacktestEvent(
            event_type=event_type,
            pair=pair,
            time=bar.bar.time,
            direction=direction,
            reason=reason,
            details=details,
        )
