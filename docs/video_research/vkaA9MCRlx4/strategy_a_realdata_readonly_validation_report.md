# Strategy A Real Data Read-only Validation Report

## Implemented Files

- `src/backtest/csv_loader.py`
- `src/backtest/pair_config.py`
- `src/backtest/strategy_a_runner.py`
- `src/strategies/ema_wave3_strategy_a.py`
- `config/strategy_a_pairs.example.json`
- `tests/test_csv_loader.py`
- `tests/test_pair_config.py`
- `tests/test_strategy_a_runner.py`
- `tests/test_ema_wave3_strategy_a.py`
- `docs/video_research/vkaA9MCRlx4/strategy_a_realdata_readonly_plan.md`
- `docs/video_research/vkaA9MCRlx4/strategy_a_realdata_readonly_validation_report.md`

## CSV Input Spec

- Input source is local CSV only.
- One CSV file represents one pair.
- Recommended filenames: `PAIR_4h.csv` or `PAIR.csv`.
- Required columns: `timestamp`, `open`, `high`, `low`, `close`.
- Timestamp aliases accepted: `timestamp`, `time`, `datetime`, `date`.
- Rows must be sorted from oldest to newest.
- Duplicate timestamps are rejected.
- Missing prices are rejected.
- Invalid OHLC shapes are rejected:
  - `high < low`
  - `high < open/close`
  - `low > open/close`
- Mixed timezone-aware and timezone-naive timestamps are rejected.

## Strengthened 4H Validation

`strategy_a_runner.py` calls:

```python
load_ohlc_csv(csv_path, strict_timeframe_hours=4)
```

Strict 4H validation checks the distribution of timestamp intervals:

- 4-hour intervals are treated as normal bars.
- 8-hour-or-larger intervals are allowed as weekend or market-closure gap candidates.
- Intervals smaller than 8 hours that are not exactly 4 hours are rejected.
- CSVs with no 4-hour interval are rejected.
- If the most frequent interval is not 4 hours, the CSV is rejected.

This prevents daily CSVs from being accepted as 4H data merely because 24 hours is a multiple of 4 hours.

## Pair Setting Spec

Pair settings are JSON under a `pairs` object.

Required:

- `tick_size`
- `assumed_spread`

Optional:

- `buffer`

If `buffer` is omitted, it defaults to `assumed_spread + tick_size`.

Rejected settings:

- `tick_size <= 0`
- `assumed_spread < 0`
- `buffer < 0`
- non-numeric values

Pair names are normalized to uppercase.

`config/strategy_a_pairs.example.json` contains assumed values for:

- `USDJPY`
- `EURUSD`
- `GBPUSD`
- `AUDUSD`
- `USDCAD`
- `USDCHF`
- `EURJPY`
- `GBPJPY`

These values are examples only. They are not current spreads, broker quotes, or recommended trading assumptions.

## EMA Warmup

EMA warmup has been added.

- `StrategyAConfig.min_warmup_bars` is available.
- Default effective warmup is `slow_period`.
- In `generate_entries()`, setup start is ignored while `index < min_warmup_bars`.
- Tests can set `min_warmup_bars=0` or another small value.
- `summary.md` reports the effective EMA warmup bars.
- Metrics JSON includes `strategy_settings.min_warmup_bars`.

This avoids accepting early signals before EMA200 has enough history for real-data validation.

## RR Comparison Runner Spec

Scope: Strategy A: Core Mechanical only.

Default RR values:

- `1.0`
- `1.5`
- `2.0`
- `3.0`

Process:

1. Read pair settings JSON.
2. Find local CSV files for the selected pairs.
3. Validate the CSV as 4H data.
4. Run Strategy A for each RR value.
5. Write trades, events, metrics, and summary outputs.

No market-data API, broker API, order placement, auto-trading, real-money handling, or Strategy B/C logic is implemented.

## Output File Spec

```text
output_dir/
  summary.md
  trades/
    PAIR_rr_1_0_trades.csv
    PAIR_rr_1_5_trades.csv
    PAIR_rr_2_0_trades.csv
    PAIR_rr_3_0_trades.csv
  events/
    PAIR_rr_1_0_events.csv
    PAIR_rr_1_5_events.csv
    PAIR_rr_2_0_events.csv
    PAIR_rr_3_0_events.csv
  metrics/
    PAIR_rr_1_0_metrics.json
    PAIR_rr_1_5_metrics.json
    PAIR_rr_2_0_metrics.json
    PAIR_rr_3_0_metrics.json
    metrics_comparison.csv
```

`summary.md` includes:

- `pair`
- `input_file`
- `data_start`
- `data_end`
- `bar_count`
- effective EMA warmup bars
- RR-specific metrics
- a warning that the results are mechanical Strategy A validation on the specified CSV only, not evidence of profitability or live-trading viability.

Metrics JSON includes:

- input metadata
- pair settings
- strategy settings, including `min_warmup_bars`
- metrics
- trade and event counts

## Validation Results

Commands were run from the local repository working tree with the project Python interpreter. Local machine paths are intentionally omitted from this public-safe report.

| Check | Command | Result |
| --- | --- | --- |
| pytest | `python -B -m pytest` | `46 passed in 0.31s` |
| ruff check | `python -m ruff check src tests` | `All checks passed!` |
| ruff format | `python -m ruff format --check src tests` | `15 files already formatted` |
| mypy | `python -m mypy src tests` | `Success: no issues found in 15 source files` |

## Git Diff Stat

This report is documentation-only and records the read-only validation design and command results. It does not include raw CSVs, generated result files, market data, broker integrations, live execution, or profitability claims.
