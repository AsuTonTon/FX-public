from __future__ import annotations

import csv
import json
from collections.abc import Sequence
from datetime import datetime, timedelta
from pathlib import Path

from src.backtest.strategy_b_runner import (
    StrategyBReadOnlyRunConfig,
    run_strategy_b_readonly,
)
from src.backtest.trade import OHLCBar
from src.strategies.ema_wave3_strategy_b import EmaWave3StrategyB, StrategyBConfig


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


def force_touch(
    bars: list[OHLCBar], strategy_obj: EmaWave3StrategyB, index: int
) -> None:
    indicator = strategy_obj.with_indicators(bars)[index]
    bars[index].low = min(bars[index].low, indicator.ema_fast - 0.1)
    bars[index].high = max(bars[index].high, indicator.ema_fast + 0.1)


def strategy_b_fixture_bars() -> list[OHLCBar]:
    bars = make_bars([100, 120, 90, 90, 90, 90, 90, 110, 108, 112, 113, 130, 140])
    bars[1].high = 125
    bars[1].low = 119
    bars[2].high = 91
    bars[2].low = 80
    bars[3].high = 130
    bars[3].low = 85
    bars[4].high = 91
    bars[4].low = 89
    bars[5].high = 140
    bars[5].low = 88
    bars[6].high = 91
    bars[6].low = 89
    strategy_obj = EmaWave3StrategyB(
        StrategyBConfig(
            fast_period=2,
            slow_period=3,
            min_warmup_bars=4,
            atr_period=2,
            adx_period=2,
            adx_minimum=0.0,
            swing_width=1,
            swing_lookback_bars=20,
            tp1_min_rr=0.1,
            tp2_min_rr=0.2,
            tp1_only_min_rr=0.2,
            min_stop_atr_multiple=0.0,
            max_stop_atr_multiple=100.0,
        )
    )
    force_touch(bars, strategy_obj, 8)
    bars[10].open = 113
    bars[10].high = 126
    bars[11].high = 131
    return bars


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


def test_strategy_b_runner_writes_readonly_outputs(tmp_path: Path) -> None:
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    write_ohlc_csv(input_dir / "TEST_4h.csv", strategy_b_fixture_bars())
    pair_settings_path = tmp_path / "pairs.json"
    write_pair_settings(pair_settings_path)

    result = run_strategy_b_readonly(
        StrategyBReadOnlyRunConfig(
            input_dir=input_dir,
            output_dir=output_dir,
            pair_settings_path=pair_settings_path,
            pairs=("TEST",),
            fast_period=2,
            slow_period=3,
            min_warmup_bars=4,
            atr_period=2,
            adx_period=2,
            adx_minimum=0.0,
            swing_width=1,
            swing_lookback_bars=20,
            tp1_min_rr=0.1,
            tp2_min_rr=0.2,
            tp1_only_min_rr=0.2,
            min_stop_atr_multiple=0.0,
            max_stop_atr_multiple=100.0,
        )
    )

    assert len(result["runs"]) == 1
    assert (output_dir / "summary.md").exists()
    assert (output_dir / "trades" / "TEST_strategy_b_trades.csv").exists()
    assert (output_dir / "events" / "TEST_strategy_b_events.csv").exists()
    assert (output_dir / "candidates" / "TEST_strategy_b_candidates.csv").exists()
    assert (output_dir / "tp_candidates" / "TEST_strategy_b_tp_candidates.csv").exists()
    assert (output_dir / "metrics" / "TEST_strategy_b_metrics.json").exists()
    assert (output_dir / "metrics" / "metrics_comparison.csv").exists()

    summary = (output_dir / "summary.md").read_text(encoding="utf-8")
    assert "Strategy B" in summary
    assert "not profitability claims" in summary

    payload = json.loads(
        (output_dir / "metrics" / "TEST_strategy_b_metrics.json").read_text(
            encoding="utf-8"
        )
    )
    assert payload["strategy_settings"]["atr_period"] == 2
    assert payload["strategy_settings"]["adx_minimum"] == 0.0
    assert payload["metrics"]["trade_count"] == 1
    assert payload["candidate_count"] == 1

    with (output_dir / "candidates" / "TEST_strategy_b_candidates.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        candidate_rows = list(csv.DictReader(handle))

    assert len(candidate_rows) == 1
    candidate = candidate_rows[0]
    assert candidate["pair"] == "TEST"
    assert candidate["accepted"] == "True"
    assert candidate["first_fail_reason"] == ""
    assert candidate["all_failed_reasons"] == "[]"
    assert candidate["tp1_min_rr_pass"] == "True"

    with (output_dir / "tp_candidates" / "TEST_strategy_b_tp_candidates.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        target_rows = list(csv.DictReader(handle))

    assert len(target_rows) == 3
    assert target_rows[0]["target_rank"] == "1"
    assert float(target_rows[0]["target_price"]) == 125.0
    assert target_rows[0]["selected_tp1"] == "True"
    assert target_rows[0]["selected_tp2"] == "False"
    assert target_rows[1]["target_rank"] == "2"
    assert float(target_rows[1]["target_price"]) == 130.0
    assert target_rows[1]["selected_tp1"] == "False"
    assert target_rows[1]["selected_tp2"] == "True"
    assert target_rows[2]["target_rank"] == "3"
    assert float(target_rows[2]["target_price"]) == 140.0
    assert target_rows[2]["accepted"] == "True"
    assert target_rows[2]["first_fail_reason"] == ""
