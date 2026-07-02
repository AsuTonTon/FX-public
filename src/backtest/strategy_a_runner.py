from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Sequence

from src.backtest.csv_loader import load_ohlc_csv
from src.backtest.engine import BacktestEngine
from src.backtest.metrics import calculate_metrics
from src.backtest.pair_config import PairConfigError, PairSettings, load_pair_settings
from src.backtest.trade import BacktestEvent, Trade
from src.strategies.ema_wave3_strategy_a import EmaWave3StrategyA, StrategyAConfig


DEFAULT_RR_VALUES = (1.0, 1.5, 2.0, 3.0)
TRADE_FIELDS = (
    "pair",
    "direction",
    "setup_time",
    "touch_time",
    "confirmation_time",
    "entry_time",
    "entry_price",
    "stop_price",
    "take_profit_price",
    "exit_time",
    "exit_price",
    "exit_reason",
    "r_multiple",
    "bars_held",
)
EVENT_FIELDS = ("event_type", "pair", "time", "direction", "reason", "details")


@dataclass(frozen=True)
class StrategyAReadOnlyRunConfig:
    input_dir: Path
    output_dir: Path
    pair_settings_path: Path
    pairs: tuple[str, ...] | None = None
    rr_values: tuple[float, ...] = DEFAULT_RR_VALUES
    timeframe_hours: int = 4
    fast_period: int = 20
    slow_period: int = 200
    min_warmup_bars: int | None = None
    touch_expiry_bars: int = 30
    confirmation_expiry_bars: int = 10
    conservative_same_bar: bool = True


def run_strategy_a_rr_comparison(
    config: StrategyAReadOnlyRunConfig,
) -> dict[str, Any]:
    pair_settings = load_pair_settings(config.pair_settings_path)
    pairs = _selected_pairs(config.pairs, pair_settings)
    _prepare_output_dirs(config.output_dir)
    effective_min_warmup_bars = (
        config.slow_period if config.min_warmup_bars is None else config.min_warmup_bars
    )

    run_rows: list[dict[str, Any]] = []
    for pair in pairs:
        settings = pair_settings[pair]
        csv_path = find_pair_csv(config.input_dir, pair)
        bars = load_ohlc_csv(csv_path, strict_timeframe_hours=config.timeframe_hours)
        data_start = bars[0].time
        data_end = bars[-1].time
        bar_count = len(bars)

        for rr_value in config.rr_values:
            strategy = EmaWave3StrategyA(
                StrategyAConfig(
                    fast_period=config.fast_period,
                    slow_period=config.slow_period,
                    rr_multiple=rr_value,
                    buffer=settings.buffer,
                    touch_expiry_bars=config.touch_expiry_bars,
                    confirmation_expiry_bars=config.confirmation_expiry_bars,
                    min_warmup_bars=config.min_warmup_bars,
                )
            )
            result = BacktestEngine(
                conservative_same_bar=config.conservative_same_bar
            ).run(pair, bars, strategy)
            metrics = calculate_metrics(result.trades)
            run_row = {
                "pair": pair,
                "rr": rr_value,
                "input_file": str(csv_path),
                "data_start": data_start,
                "data_end": data_end,
                "bar_count": bar_count,
                "fast_period": config.fast_period,
                "slow_period": config.slow_period,
                "min_warmup_bars": effective_min_warmup_bars,
                "touch_expiry_bars": config.touch_expiry_bars,
                "confirmation_expiry_bars": config.confirmation_expiry_bars,
                "settings": settings,
                "metrics": metrics,
                "trade_count": len(result.trades),
                "event_count": len(result.events),
            }
            _write_run_outputs(config.output_dir, run_row, result.trades, result.events)
            run_rows.append(run_row)

    _write_metrics_comparison(config.output_dir, run_rows)
    _write_summary(config.output_dir, config, run_rows)
    return {"runs": run_rows, "output_dir": str(config.output_dir)}


def find_pair_csv(input_dir: Path, pair: str) -> Path:
    candidates = (
        input_dir / f"{pair}_4h.csv",
        input_dir / f"{pair}.csv",
        input_dir / f"{pair.lower()}_4h.csv",
        input_dir / f"{pair.lower()}.csv",
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    expected = ", ".join(candidate.name for candidate in candidates)
    raise FileNotFoundError(f"No CSV found for {pair}. Expected one of: {expected}")


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
    for child in ("trades", "events", "metrics"):
        (output_dir / child).mkdir(parents=True, exist_ok=True)


def _write_run_outputs(
    output_dir: Path,
    run_row: dict[str, Any],
    trades: list[Trade],
    events: list[BacktestEvent],
) -> None:
    pair = str(run_row["pair"])
    rr_label = format_rr(float(run_row["rr"]))
    stem = f"{pair}_rr_{rr_label}"
    _write_trades_csv(output_dir / "trades" / f"{stem}_trades.csv", trades)
    _write_events_csv(output_dir / "events" / f"{stem}_events.csv", events)
    _write_metrics_json(
        output_dir / "metrics" / f"{stem}_metrics.json",
        run_row,
    )


def _write_trades_csv(path: Path, trades: list[Trade]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRADE_FIELDS)
        writer.writeheader()
        for trade in trades:
            writer.writerow(
                {field: _csv_cell(getattr(trade, field)) for field in TRADE_FIELDS}
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


def _write_metrics_json(path: Path, run_row: dict[str, Any]) -> None:
    settings = run_row["settings"]
    payload = {
        "pair": run_row["pair"],
        "rr": run_row["rr"],
        "input_file": run_row["input_file"],
        "data_start": run_row["data_start"],
        "data_end": run_row["data_end"],
        "bar_count": run_row["bar_count"],
        "strategy_settings": {
            "fast_period": run_row["fast_period"],
            "slow_period": run_row["slow_period"],
            "min_warmup_bars": run_row["min_warmup_bars"],
            "touch_expiry_bars": run_row["touch_expiry_bars"],
            "confirmation_expiry_bars": run_row["confirmation_expiry_bars"],
        },
        "pair_settings": {
            "tick_size": settings.tick_size,
            "assumed_spread": settings.assumed_spread,
            "buffer": settings.buffer,
        },
        "metrics": run_row["metrics"],
        "trade_count": run_row["trade_count"],
        "event_count": run_row["event_count"],
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
        "min_warmup_bars",
        "rr",
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
                    "min_warmup_bars": run_row["min_warmup_bars"],
                    "rr": run_row["rr"],
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
    config: StrategyAReadOnlyRunConfig,
    run_rows: list[dict[str, Any]],
) -> None:
    generated_at = datetime.now().replace(microsecond=0).isoformat()
    lines = [
        "# Strategy A Read-only RR Comparison Summary",
        "",
        f"- Generated at: {generated_at}",
        f"- Input directory: `{config.input_dir}`",
        f"- Output directory: `{config.output_dir}`",
        f"- Pair settings: `{config.pair_settings_path}`",
        f"- Timeframe validation: positive multiples of {config.timeframe_hours} hours.",
        f"- EMA warmup bars: {config.slow_period if config.min_warmup_bars is None else config.min_warmup_bars}",
        f"- RR values: {', '.join(str(value) for value in config.rr_values)}",
        "- Data access: local CSV files only; no market-data API, broker API, "
        "order placement, auto trading, or real-money operation.",
        "- Scope: Strategy A only. Strategy B/C logic is intentionally excluded.",
        "- 注意書き: この結果は指定CSVに対するStrategy Aの機械的検証であり、"
        "収益性や実運用可能性を示すものではない。",
        "- Interpretation: these are mechanical validation outputs, not profitability "
        "claims or trading recommendations.",
        "",
        "| pair | input_file | data_start | data_end | bar_count | min_warmup_bars | RR | Trades | "
        "Win Rate | Average R | Median R | Total R | Profit Factor | Max DD R | "
        "Max Consecutive Losses |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
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
            f"{run_row['min_warmup_bars']} | "
            f"{run_row['rr']} | "
            f"{metrics['trade_count']} | "
            f"{_pct(metrics['win_rate'])} | "
            f"{_fmt(metrics['average_r'])} | "
            f"{_fmt(metrics['median_r'])} | "
            f"{_fmt(metrics['total_r'])} | "
            f"{_fmt(metrics['profit_factor'])} | "
            f"{_fmt(metrics['max_drawdown_r'])} | "
            f"{metrics['max_consecutive_losses']} |"
        )

    lines.extend(
        [
            "",
            "## Output Files",
            "",
            "- `trades/*_trades.csv`: closed trade records.",
            "- `events/*_events.csv`: setup, expiry, entry, TP/SL, and no-trade events.",
            "- `metrics/*_metrics.json`: per-pair and per-RR metrics.",
            "- `metrics/metrics_comparison.csv`: RR comparison table.",
        ]
    )

    (output_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_rr(rr_value: float) -> str:
    return str(rr_value).replace(".", "_")


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


def parse_rr_values(values: Sequence[str] | None) -> tuple[float, ...]:
    if not values:
        return DEFAULT_RR_VALUES
    rr_values = tuple(float(value) for value in values)
    if any(value <= 0 for value in rr_values):
        raise argparse.ArgumentTypeError("RR values must be positive")
    return rr_values


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Strategy A read-only RR comparison from local OHLC CSV files."
    )
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--pair-settings", required=True, type=Path)
    parser.add_argument("--pairs", nargs="*")
    parser.add_argument("--rr-values", nargs="*")
    parser.add_argument("--timeframe-hours", type=int, default=4)
    parser.add_argument("--fast-period", type=int, default=20)
    parser.add_argument("--slow-period", type=int, default=200)
    parser.add_argument("--min-warmup-bars", type=int)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    config = StrategyAReadOnlyRunConfig(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        pair_settings_path=args.pair_settings,
        pairs=tuple(args.pairs) if args.pairs else None,
        rr_values=parse_rr_values(args.rr_values),
        timeframe_hours=args.timeframe_hours,
        fast_period=args.fast_period,
        slow_period=args.slow_period,
        min_warmup_bars=args.min_warmup_bars,
    )
    run_strategy_a_rr_comparison(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
