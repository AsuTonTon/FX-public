from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Sequence

from src.backtest.csv_loader import load_ohlc_csv
from src.backtest.metrics import calculate_metrics
from src.backtest.pair_config import PairConfigError, PairSettings, load_pair_settings
from src.backtest.strategy_a_runner import find_pair_csv
from src.backtest.trade import BacktestEvent, BacktestResult, EntryOrder, OHLCBar, Trade
from src.strategies.ema_wave3_strategy_a import normalize_bars
from src.strategies.ema_wave3_strategy_b import (
    EmaWave3StrategyB,
    StrategyBCandidate,
    StrategyBConfig,
    StrategyBTargetCandidateDiagnostic,
)


STRATEGY_B_TRADE_FIELDS = (
    "pair",
    "direction",
    "setup_time",
    "touch_time",
    "confirmation_time",
    "entry_time",
    "entry_price",
    "stop_price",
    "take_profit_price",
    "tp1_price",
    "tp2_price",
    "tp1_r",
    "tp2_r",
    "partial_exit_ratio",
    "exit_time",
    "exit_price",
    "exit_reason",
    "r_multiple",
    "bars_held",
)
EVENT_FIELDS = ("event_type", "pair", "time", "direction", "reason", "details")
CANDIDATE_FIELDS = (
    "pair",
    "direction",
    "setup_time",
    "touch_time",
    "confirmation_time",
    "entry_time",
    "entry_price",
    "atr",
    "adx",
    "adx_pass",
    "stop_anchor",
    "stop_price",
    "buffer",
    "risk",
    "stop_distance_atr",
    "stop_too_narrow_pass",
    "stop_too_wide_pass",
    "tp1_price",
    "tp2_price",
    "tp1_r",
    "tp2_r",
    "left_side_tp1_available",
    "tp1_min_rr_pass",
    "tp1_only_min_rr_pass",
    "tp2_min_rr_pass",
    "accepted",
    "first_fail_reason",
    "all_failed_reasons",
)
TP_CANDIDATE_FIELDS = (
    "pair",
    "direction",
    "setup_time",
    "touch_time",
    "confirmation_time",
    "entry_time",
    "entry_price",
    "stop_price",
    "risk",
    "atr",
    "target_rank",
    "target_price",
    "target_r",
    "swing_index",
    "swing_kind",
    "swing_time",
    "swing_bar_distance_from_confirmation",
    "swing_price_distance_from_entry",
    "swing_price_distance_atr",
    "simple_prominence",
    "simple_prominence_atr",
    "selected_tp1",
    "selected_tp2",
    "accepted",
    "first_fail_reason",
)


@dataclass(frozen=True)
class StrategyBReadOnlyRunConfig:
    input_dir: Path
    output_dir: Path
    pair_settings_path: Path
    pairs: tuple[str, ...] | None = None
    timeframe_hours: int = 4
    fast_period: int = 20
    slow_period: int = 200
    min_warmup_bars: int | None = None
    touch_expiry_bars: int = 30
    confirmation_expiry_bars: int = 10
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


class StrategyBBacktestEngine:
    def __init__(self, conservative_same_bar: bool = True) -> None:
        self.conservative_same_bar = conservative_same_bar

    def run(
        self,
        pair: str,
        bars: Iterable[OHLCBar | dict[str, Any]],
        strategy: Any,
    ) -> BacktestResult:
        normalized_bars = normalize_bars(bars)
        signal_result = strategy.generate_entries(pair, normalized_bars)
        events = list(signal_result.events)
        trades: list[Trade] = []
        active_until_index = -1

        for order in signal_result.entries:
            if order.entry_index <= active_until_index:
                events.append(
                    BacktestEvent(
                        event_type="no_trade",
                        pair=pair,
                        time=order.trade.entry_time,
                        direction=order.trade.direction,
                        reason="overlap_open_position",
                    )
                )
                continue

            events.append(
                BacktestEvent(
                    event_type="entry",
                    pair=pair,
                    time=order.trade.entry_time,
                    direction=order.trade.direction,
                    details={
                        "entry_price": order.trade.entry_price,
                        "stop_price": order.trade.stop_price,
                        "tp1_price": order.trade.tp1_price,
                        "tp2_price": order.trade.tp2_price,
                        "tp1_r": order.trade.tp1_r,
                        "tp2_r": order.trade.tp2_r,
                    },
                )
            )
            trade, exit_index, order_events = self._simulate_order(
                normalized_bars, order
            )
            active_until_index = exit_index
            trades.append(trade)
            events.extend(order_events)

        return BacktestResult(
            trades=trades,
            events=events,
            candidates=list(signal_result.candidates),
            target_candidates=list(signal_result.target_candidates),
        )

    def _simulate_order(
        self,
        bars: list[OHLCBar],
        order: EntryOrder,
    ) -> tuple[Trade, int, list[BacktestEvent]]:
        trade = order.trade
        entry_index = order.entry_index
        risk = self._risk_per_unit(trade)
        tp1_price = trade.tp1_price
        if tp1_price is None or trade.tp1_r is None:
            raise ValueError("Strategy B trades require TP1 price and TP1 R")

        tp1_hit = False
        events: list[BacktestEvent] = []
        partial_ratio = trade.partial_exit_ratio or 1.0

        for index in range(entry_index, len(bars)):
            bar = bars[index]
            if not tp1_hit:
                stop_hit = self._stop_hit(trade, bar, trade.stop_price)
                tp1_reached = self._target_hit(trade.direction, bar, tp1_price)
                tp2_reached = trade.tp2_price is not None and self._target_hit(
                    trade.direction, bar, trade.tp2_price
                )

                if stop_hit and tp1_reached and self.conservative_same_bar:
                    return self._close_trade(
                        trade,
                        bar,
                        index,
                        entry_index,
                        trade.stop_price,
                        "stop_loss",
                        -1.0,
                    )
                if stop_hit:
                    return self._close_trade(
                        trade,
                        bar,
                        index,
                        entry_index,
                        trade.stop_price,
                        "stop_loss",
                        -1.0,
                    )
                if not tp1_reached:
                    continue

                events.append(
                    BacktestEvent(
                        event_type="tp1_hit",
                        pair=trade.pair,
                        time=bar.time,
                        direction=trade.direction,
                        details={
                            "tp1_price": tp1_price,
                            "tp1_r": trade.tp1_r,
                            "partial_exit_ratio": partial_ratio,
                        },
                    )
                )
                if trade.tp2_price is None or partial_ratio >= 1.0:
                    return self._close_trade(
                        trade,
                        bar,
                        index,
                        entry_index,
                        tp1_price,
                        "take_profit",
                        trade.tp1_r,
                        events,
                    )

                tp1_hit = True
                if tp2_reached and trade.tp2_r is not None:
                    total_r = self._weighted_r(trade.tp1_r, trade.tp2_r, partial_ratio)
                    return self._close_trade(
                        trade,
                        bar,
                        index,
                        entry_index,
                        trade.tp2_price,
                        "take_profit",
                        total_r,
                        events,
                    )
                continue

            breakeven_hit = self._stop_hit(trade, bar, trade.entry_price)
            tp2_hit = trade.tp2_price is not None and self._target_hit(
                trade.direction, bar, trade.tp2_price
            )
            if breakeven_hit and tp2_hit and self.conservative_same_bar:
                total_r = self._weighted_r(trade.tp1_r or 0.0, 0.0, partial_ratio)
                return self._close_trade(
                    trade,
                    bar,
                    index,
                    entry_index,
                    trade.entry_price,
                    "breakeven_after_tp1",
                    total_r,
                    events,
                )
            if tp2_hit and trade.tp2_r is not None and trade.tp2_price is not None:
                total_r = self._weighted_r(
                    trade.tp1_r or 0.0, trade.tp2_r, partial_ratio
                )
                return self._close_trade(
                    trade,
                    bar,
                    index,
                    entry_index,
                    trade.tp2_price,
                    "take_profit",
                    total_r,
                    events,
                )
            if breakeven_hit:
                total_r = self._weighted_r(trade.tp1_r or 0.0, 0.0, partial_ratio)
                return self._close_trade(
                    trade,
                    bar,
                    index,
                    entry_index,
                    trade.entry_price,
                    "breakeven_after_tp1",
                    total_r,
                    events,
                )

        last_index = len(bars) - 1
        last_bar = bars[last_index]
        if tp1_hit:
            final_leg_r = self._mark_to_market_r(trade, last_bar.close, risk)
            r_multiple = self._weighted_r(
                trade.tp1_r or 0.0, final_leg_r, partial_ratio
            )
        else:
            r_multiple = self._mark_to_market_r(trade, last_bar.close, risk)
        return self._close_trade(
            trade,
            last_bar,
            last_index,
            entry_index,
            last_bar.close,
            "end_of_data",
            r_multiple,
            events,
        )

    @staticmethod
    def _weighted_r(
        first_leg_r: float, second_leg_r: float, first_ratio: float
    ) -> float:
        return first_leg_r * first_ratio + second_leg_r * (1.0 - first_ratio)

    @staticmethod
    def _risk_per_unit(trade: Trade) -> float:
        if trade.direction == "long":
            return trade.entry_price - trade.stop_price
        return trade.stop_price - trade.entry_price

    @staticmethod
    def _mark_to_market_r(trade: Trade, exit_price: float, risk: float) -> float:
        if trade.direction == "long":
            return (exit_price - trade.entry_price) / risk
        return (trade.entry_price - exit_price) / risk

    @staticmethod
    def _target_hit(direction: str, bar: OHLCBar, target_price: float) -> bool:
        if direction == "long":
            return bar.high >= target_price
        return bar.low <= target_price

    @staticmethod
    def _stop_hit(trade: Trade, bar: OHLCBar, stop_price: float) -> bool:
        if trade.direction == "long":
            return bar.low <= stop_price
        return bar.high >= stop_price

    @staticmethod
    def _close_trade(
        trade: Trade,
        bar: OHLCBar,
        exit_index: int,
        entry_index: int,
        exit_price: float,
        exit_reason: str,
        r_multiple: float,
        prior_events: list[BacktestEvent] | None = None,
    ) -> tuple[Trade, int, list[BacktestEvent]]:
        trade.exit_time = bar.time
        trade.exit_price = exit_price
        trade.exit_reason = exit_reason
        trade.r_multiple = r_multiple
        trade.bars_held = exit_index - entry_index + 1
        events = list(prior_events or [])
        events.append(
            BacktestEvent(
                event_type=exit_reason,
                pair=trade.pair,
                time=bar.time,
                direction=trade.direction,
                details={
                    "exit_price": exit_price,
                    "r_multiple": r_multiple,
                    "bars_held": trade.bars_held,
                },
            )
        )
        return trade, exit_index, events


def run_strategy_b_readonly(config: StrategyBReadOnlyRunConfig) -> dict[str, Any]:
    pair_settings = load_pair_settings(config.pair_settings_path)
    pairs = _selected_pairs(config.pairs, pair_settings)
    _prepare_output_dirs(config.output_dir)

    run_rows: list[dict[str, Any]] = []
    for pair in pairs:
        settings = pair_settings[pair]
        csv_path = find_pair_csv(config.input_dir, pair)
        bars = load_ohlc_csv(csv_path, strict_timeframe_hours=config.timeframe_hours)
        strategy = EmaWave3StrategyB(_strategy_config(config, settings))
        result = StrategyBBacktestEngine().run(pair, bars, strategy)
        metrics = calculate_metrics(result.trades)
        run_row = {
            "pair": pair,
            "input_file": str(csv_path),
            "data_start": bars[0].time,
            "data_end": bars[-1].time,
            "bar_count": len(bars),
            "settings": settings,
            "strategy_settings": _strategy_settings_payload(strategy.config),
            "metrics": metrics,
            "trade_count": len(result.trades),
            "event_count": len(result.events),
            "candidate_count": len(result.candidates),
        }
        _write_run_outputs(
            config.output_dir,
            run_row,
            result.trades,
            result.events,
            result.candidates,
            result.target_candidates,
        )
        run_rows.append(run_row)

    _write_metrics_comparison(config.output_dir, run_rows)
    _write_summary(config.output_dir, config, run_rows)
    return {"runs": run_rows, "output_dir": str(config.output_dir)}


def _strategy_config(
    config: StrategyBReadOnlyRunConfig, settings: PairSettings
) -> StrategyBConfig:
    return StrategyBConfig(
        fast_period=config.fast_period,
        slow_period=config.slow_period,
        pair_buffer=settings.buffer,
        tick_size=settings.tick_size,
        touch_expiry_bars=config.touch_expiry_bars,
        confirmation_expiry_bars=config.confirmation_expiry_bars,
        min_warmup_bars=config.min_warmup_bars,
        atr_period=config.atr_period,
        atr_buffer_multiplier=config.atr_buffer_multiplier,
        swing_width=config.swing_width,
        swing_lookback_bars=config.swing_lookback_bars,
        tp1_min_rr=config.tp1_min_rr,
        tp2_min_rr=config.tp2_min_rr,
        tp1_only_min_rr=config.tp1_only_min_rr,
        partial_exit_ratio=config.partial_exit_ratio,
        adx_period=config.adx_period,
        adx_minimum=config.adx_minimum,
        min_stop_atr_multiple=config.min_stop_atr_multiple,
        max_stop_atr_multiple=config.max_stop_atr_multiple,
    )


def _strategy_settings_payload(config: StrategyBConfig) -> dict[str, Any]:
    return {
        "fast_period": config.fast_period,
        "slow_period": config.slow_period,
        "min_warmup_bars": config.effective_min_warmup_bars,
        "touch_expiry_bars": config.touch_expiry_bars,
        "confirmation_expiry_bars": config.confirmation_expiry_bars,
        "atr_period": config.atr_period,
        "atr_buffer_multiplier": config.atr_buffer_multiplier,
        "swing_width": config.swing_width,
        "swing_lookback_bars": config.swing_lookback_bars,
        "tp1_min_rr": config.tp1_min_rr,
        "tp2_min_rr": config.tp2_min_rr,
        "tp1_only_min_rr": config.tp1_only_min_rr,
        "partial_exit_ratio": config.partial_exit_ratio,
        "adx_period": config.adx_period,
        "adx_minimum": config.adx_minimum,
        "min_stop_atr_multiple": config.min_stop_atr_multiple,
        "max_stop_atr_multiple": config.max_stop_atr_multiple,
    }


def _selected_pairs(
    requested_pairs: tuple[str, ...] | None,
    pair_settings: dict[str, PairSettings],
) -> tuple[str, ...]:
    if requested_pairs is None:
        return tuple(sorted(pair_settings))

    pairs = tuple(pair.upper() for pair in requested_pairs)
    missing = [pair for pair in pairs if pair not in pair_settings]
    if missing:
        raise PairConfigError(
            "Pair settings missing for: " + ", ".join(sorted(missing))
        )
    return pairs


def _prepare_output_dirs(output_dir: Path) -> None:
    for child in ("trades", "events", "metrics", "candidates", "tp_candidates"):
        (output_dir / child).mkdir(parents=True, exist_ok=True)


def _write_run_outputs(
    output_dir: Path,
    run_row: dict[str, Any],
    trades: list[Trade],
    events: list[BacktestEvent],
    candidates: list[Any],
    target_candidates: list[Any],
) -> None:
    pair = str(run_row["pair"])
    stem = f"{pair}_strategy_b"
    _write_trades_csv(output_dir / "trades" / f"{stem}_trades.csv", trades)
    _write_events_csv(output_dir / "events" / f"{stem}_events.csv", events)
    _write_candidates_csv(
        output_dir / "candidates" / f"{stem}_candidates.csv",
        [
            candidate
            for candidate in candidates
            if isinstance(candidate, StrategyBCandidate)
        ],
    )
    _write_tp_candidates_csv(
        output_dir / "tp_candidates" / f"{stem}_tp_candidates.csv",
        [
            candidate
            for candidate in target_candidates
            if isinstance(candidate, StrategyBTargetCandidateDiagnostic)
        ],
    )
    _write_metrics_json(output_dir / "metrics" / f"{stem}_metrics.json", run_row)


def _write_trades_csv(path: Path, trades: list[Trade]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=STRATEGY_B_TRADE_FIELDS)
        writer.writeheader()
        for trade in trades:
            writer.writerow(
                {
                    field: _csv_cell(getattr(trade, field))
                    for field in STRATEGY_B_TRADE_FIELDS
                }
            )


def _write_events_csv(path: Path, events: list[BacktestEvent]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=EVENT_FIELDS)
        writer.writeheader()
        for event in events:
            writer.writerow(
                {
                    "event_type": event.event_type,
                    "pair": event.pair,
                    "time": _csv_cell(event.time),
                    "direction": event.direction or "",
                    "reason": event.reason or "",
                    "details": _csv_cell(event.details),
                }
            )


def _write_candidates_csv(path: Path, candidates: list[StrategyBCandidate]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CANDIDATE_FIELDS)
        writer.writeheader()
        for candidate in candidates:
            writer.writerow(
                {
                    field: _csv_cell(getattr(candidate, field))
                    for field in CANDIDATE_FIELDS
                }
            )


def _write_tp_candidates_csv(
    path: Path, candidates: list[StrategyBTargetCandidateDiagnostic]
) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TP_CANDIDATE_FIELDS)
        writer.writeheader()
        for candidate in candidates:
            writer.writerow(
                {
                    field: _csv_cell(getattr(candidate, field))
                    for field in TP_CANDIDATE_FIELDS
                }
            )


def _write_metrics_json(path: Path, run_row: dict[str, Any]) -> None:
    settings = run_row["settings"]
    payload = {
        "pair": run_row["pair"],
        "input_file": run_row["input_file"],
        "data_start": run_row["data_start"],
        "data_end": run_row["data_end"],
        "bar_count": run_row["bar_count"],
        "strategy_settings": run_row["strategy_settings"],
        "pair_settings": {
            "tick_size": settings.tick_size,
            "assumed_spread": settings.assumed_spread,
            "buffer": settings.buffer,
        },
        "metrics": run_row["metrics"],
        "trade_count": run_row["trade_count"],
        "event_count": run_row["event_count"],
        "candidate_count": run_row["candidate_count"],
    }
    path.write_text(
        json.dumps(_json_safe(payload), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _write_metrics_comparison(output_dir: Path, run_rows: list[dict[str, Any]]) -> None:
    path = output_dir / "metrics" / "metrics_comparison.csv"
    fields = (
        "pair",
        "input_file",
        "data_start",
        "data_end",
        "bar_count",
        "trade_count",
        "win_rate",
        "average_r",
        "median_r",
        "profit_factor",
        "max_consecutive_losses",
        "max_drawdown_r",
        "total_r",
        "yearly_r",
    )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for run_row in run_rows:
            metrics = run_row["metrics"]
            writer.writerow(
                {
                    "pair": run_row["pair"],
                    "input_file": run_row["input_file"],
                    "data_start": _csv_cell(run_row["data_start"]),
                    "data_end": _csv_cell(run_row["data_end"]),
                    "bar_count": run_row["bar_count"],
                    "trade_count": metrics["trade_count"],
                    "win_rate": metrics["win_rate"],
                    "average_r": metrics["average_r"],
                    "median_r": metrics["median_r"],
                    "profit_factor": _csv_cell(metrics["profit_factor"]),
                    "max_consecutive_losses": metrics["max_consecutive_losses"],
                    "max_drawdown_r": metrics["max_drawdown_r"],
                    "total_r": metrics["total_r"],
                    "yearly_r": _csv_cell(metrics["yearly_r"]),
                }
            )


def _write_summary(
    output_dir: Path,
    config: StrategyBReadOnlyRunConfig,
    run_rows: list[dict[str, Any]],
) -> None:
    generated_at = datetime.now().replace(microsecond=0).isoformat()
    lines = [
        "# Strategy B Read-only Summary",
        "",
        f"- Generated at: {generated_at}",
        f"- Input directory: `{config.input_dir}`",
        f"- Output directory: `{config.output_dir}`",
        f"- Pair settings: `{config.pair_settings_path}`",
        f"- Timeframe validation: {config.timeframe_hours}H.",
        "- Data access: local CSV files only; no market-data API, broker API, "
        "order placement, auto trading, or real-money operation.",
        "- Scope: Strategy B initial implementation only. Strategy C is excluded.",
        "- Interpretation: these are mechanical validation outputs, not profitability "
        "claims or trading recommendations.",
        "",
        "| pair | input_file | data_start | data_end | bar_count | Trades | Win Rate | "
        "Average R | Median R | Total R | Profit Factor | Max DD R | "
        "Max Consecutive Losses |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for run_row in run_rows:
        metrics = run_row["metrics"]
        lines.append(
            "| "
            f"{run_row['pair']} | "
            f"`{run_row['input_file']}` | "
            f"{_csv_cell(run_row['data_start'])} | "
            f"{_csv_cell(run_row['data_end'])} | "
            f"{run_row['bar_count']} | "
            f"{metrics['trade_count']} | "
            f"{_pct(metrics['win_rate'])} | "
            f"{_fmt(metrics['average_r'])} | "
            f"{_fmt(metrics['median_r'])} | "
            f"{_fmt(metrics['total_r'])} | "
            f"{_fmt(metrics['profit_factor'])} | "
            f"{_fmt(metrics['max_drawdown_r'])} | "
            f"{metrics['max_consecutive_losses']} |"
        )

    (output_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _csv_cell(value: Any) -> Any:
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, float) and not math.isfinite(value):
        return "inf" if value > 0 else "-inf"
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(_json_safe(value), ensure_ascii=False, sort_keys=True)
    return value


def _json_safe(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, float) and not math.isfinite(value):
        return "inf" if value > 0 else "-inf"
    if isinstance(value, PairSettings):
        return {
            "pair": value.pair,
            "tick_size": value.tick_size,
            "assumed_spread": value.assumed_spread,
            "buffer": value.buffer,
        }
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    return value


def _pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def _fmt(value: Any) -> str:
    if isinstance(value, float):
        if math.isinf(value):
            return "inf" if value > 0 else "-inf"
        return f"{value:.4f}"
    return str(value)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Strategy B read-only validation from local OHLC CSV files."
    )
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--pair-settings", required=True, type=Path)
    parser.add_argument("--pairs", nargs="*")
    parser.add_argument("--timeframe-hours", type=int, default=4)
    parser.add_argument("--fast-period", type=int, default=20)
    parser.add_argument("--slow-period", type=int, default=200)
    parser.add_argument("--min-warmup-bars", type=int)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    config = StrategyBReadOnlyRunConfig(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        pair_settings_path=args.pair_settings,
        pairs=tuple(args.pairs) if args.pairs else None,
        timeframe_hours=args.timeframe_hours,
        fast_period=args.fast_period,
        slow_period=args.slow_period,
        min_warmup_bars=args.min_warmup_bars,
    )
    run_strategy_b_readonly(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
