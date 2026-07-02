from __future__ import annotations

import json
from collections.abc import Sequence
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from src.backtest.csv_loader import CsvOHLCFormatError
from src.backtest.strategy_a_runner import (
    StrategyAReadOnlyRunConfig,
    run_strategy_a_rr_comparison,
)
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


def force_touch(
    bars: list[OHLCBar], strategy_obj: EmaWave3StrategyA, index: int
) -> None:
    indicator = strategy_obj.with_indicators(bars)[index]
    bars[index].low = min(bars[index].low, indicator.ema_fast - 0.1)
    bars[index].high = max(bars[index].high, indicator.ema_fast + 0.1)


def write_ohlc_csv(path: Path, bars: list[OHLCBar]) -> None:
    lines = ["timestamp,open,high,low,close"]
    for bar in bars:
        lines.append(
            ",".join(
                [
                    bar.time.isoformat(),
                    str(bar.open),
                    str(bar.high),
                    str(bar.low),
                    str(bar.close),
                ]
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_pair_settings(path: Path) -> None:
    path.write_text(
        """
        {
          "pairs": {
            "TEST": {
              "tick_size": 0.01,
              "assumed_spread": 0.00,
              "buffer": 0.00
            }
          }
        }
        """,
        encoding="utf-8",
    )


def test_strategy_a_runner_writes_default_rr_outputs_from_local_csv(
    tmp_path: Path,
) -> None:
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    bars = make_bars([100, 100, 100, 110, 108, 112, 113, 114])
    strategy_obj = EmaWave3StrategyA(
        StrategyAConfig(fast_period=2, slow_period=3, rr_multiple=1.5)
    )
    force_touch(bars, strategy_obj, 4)
    bars[6].open = 113.0
    signal = strategy_obj.generate_entries("TEST", bars)
    bars[6].high = signal.entries[0].trade.take_profit_price + 0.1
    write_ohlc_csv(input_dir / "TEST_4h.csv", bars)

    pair_settings_path = tmp_path / "pairs.json"
    write_pair_settings(pair_settings_path)

    result = run_strategy_a_rr_comparison(
        StrategyAReadOnlyRunConfig(
            input_dir=input_dir,
            output_dir=output_dir,
            pair_settings_path=pair_settings_path,
            pairs=("TEST",),
            fast_period=2,
            slow_period=3,
        )
    )

    assert len(result["runs"]) == 4
    assert {run["rr"] for run in result["runs"]} == {1.0, 1.5, 2.0, 3.0}
    assert (output_dir / "trades" / "TEST_rr_1_0_trades.csv").exists()
    assert (output_dir / "events" / "TEST_rr_1_5_events.csv").exists()
    assert (output_dir / "metrics" / "metrics_comparison.csv").exists()
    assert len(list((output_dir / "metrics").glob("TEST_rr_*_metrics.json"))) == 4
    assert len(list((output_dir / "trades").glob("TEST_rr_*_trades.csv"))) == 4
    assert len(list((output_dir / "events").glob("TEST_rr_*_events.csv"))) == 4

    summary = (output_dir / "summary.md").read_text(encoding="utf-8")
    assert "data_start" in summary.lower() or "Data Start" in summary
    assert "data_end" in summary.lower() or "Data End" in summary
    assert "bar_count" in summary.lower() or "Bar Count" in summary
    assert "EMA warmup bars: 3" in summary
    assert "2026-01-01T00:00:00" in summary
    assert "2026-01-02T04:00:00" in summary
    assert "8 |" in summary

    metrics_payload = json.loads(
        (output_dir / "metrics" / "TEST_rr_1_5_metrics.json").read_text(
            encoding="utf-8"
        )
    )
    assert metrics_payload["metrics"]["trade_count"] == 1
    assert metrics_payload["metrics"]["total_r"] == pytest.approx(1.5)
    assert metrics_payload["strategy_settings"]["min_warmup_bars"] == 3


def test_strategy_a_runner_rejects_non_4h_csv(tmp_path: Path) -> None:
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    bars = make_bars([100, 100, 100, 110, 108, 112, 113, 114])
    bars[1].time = bars[0].time + timedelta(hours=1)
    write_ohlc_csv(input_dir / "TEST_4h.csv", bars)

    pair_settings_path = tmp_path / "pairs.json"
    write_pair_settings(pair_settings_path)

    with pytest.raises(CsvOHLCFormatError, match="gap of at least 8 hours"):
        run_strategy_a_rr_comparison(
            StrategyAReadOnlyRunConfig(
                input_dir=input_dir,
                output_dir=output_dir,
                pair_settings_path=pair_settings_path,
                pairs=("TEST",),
                fast_period=2,
                slow_period=3,
            )
        )


def test_strategy_a_runner_rejects_daily_csv(tmp_path: Path) -> None:
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    bars = make_bars([100, 101, 102])
    for index, bar in enumerate(bars):
        bar.time = bars[0].time + timedelta(days=index)
    write_ohlc_csv(input_dir / "TEST_4h.csv", bars)

    pair_settings_path = tmp_path / "pairs.json"
    write_pair_settings(pair_settings_path)

    with pytest.raises(CsvOHLCFormatError, match="at least one 4-hour interval"):
        run_strategy_a_rr_comparison(
            StrategyAReadOnlyRunConfig(
                input_dir=input_dir,
                output_dir=output_dir,
                pair_settings_path=pair_settings_path,
                pairs=("TEST",),
                fast_period=2,
                slow_period=3,
            )
        )
