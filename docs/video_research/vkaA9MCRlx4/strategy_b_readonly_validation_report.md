# Strategy B Read-only Validation Report

## 0. Scope and Guardrails

- Generated at: 2026-06-24T21:02:04
- Source outputs: `results/strategy_b_readonly/summary.md`, `metrics/metrics_comparison.csv`, `trades/*.csv`, and `events/*.csv`.
- Input data: local normalized CSV files only.
- No market-data API, broker API, auto-trading, order placement, real-money handling, Strategy C, or parameter optimization was used.
- Strategy B parameters were kept at the fixed implementation defaults.
- These are mechanical read-only validation outputs on the supplied CSVs. They are not profitability claims, investment advice, or evidence of live-trading viability.
- `2026` is partial data ending at `2026-06-24T04:00:00` in the supplied CSVs.

## 1. Execution Conditions

```powershell
python -m src.backtest.strategy_b_runner `
  --input-dir data/strategy_a_ohlc `
  --pair-settings config/strategy_a_pairs.example.json `
  --output-dir results/strategy_b_readonly `
  --pairs USDJPY EURUSD
```

- Timeframe validation: strict 4H validation in the CSV loader.
- Price type: XM MT4/MT5 export broker OHLC inherited from the normalized CSV workflow.
- Timezone: XM server time as stored in the normalized CSVs.
- Output files remain local under `results/` and are intentionally not committed to Git.

## 2. Used CSVs

| pair | input_file | data_start | data_end | bar_count |
| --- | --- | --- | --- | ---: |
| USDJPY | `data\strategy_a_ohlc\USDJPY_4h.csv` | 1999-01-04T04:00:00 | 2026-06-24T04:00:00 | 42769 |
| EURUSD | `data\strategy_a_ohlc\EURUSD_4h.csv` | 1999-01-04T08:00:00 | 2026-06-24T04:00:00 | 42780 |

## 3. Fixed Strategy B Parameters

| parameter | value |
| --- | ---: |
| fast_period | 20 |
| slow_period | 200 |
| min_warmup_bars | 200 |
| touch_expiry_bars | 30 |
| confirmation_expiry_bars | 10 |
| atr_period | 14 |
| atr_buffer_multiplier | 0.1 |
| swing_width | 2 |
| swing_lookback_bars | 100 |
| tp1_min_rr | 1.0 |
| tp2_min_rr | 1.5 |
| tp1_only_min_rr | 1.5 |
| partial_exit_ratio | 0.5 |
| adx_period | 14 |
| adx_minimum | 18.0 |
| min_stop_atr_multiple | 0.25 |
| max_stop_atr_multiple | 3.0 |

Pair-level cost/buffer assumptions:

| pair | tick_size | assumed_spread | buffer |
| --- | ---: | ---: | ---: |
| USDJPY | 0.001 | 0.015 | 0.016 |
| EURUSD | 1e-05 | 0.0001 | 0.00011 |

## 4. USDJPY / EURUSD Results

| pair | trade_count | win_rate | average_r | median_r | total_r | profit_factor | max_drawdown_r | max_consecutive_losses |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 1 | 100.00% | 1.5062 | 1.5062 | 1.5062 | inf | 0.0000 | 0 |
| EURUSD | 1 | 100.00% | 2.1897 | 2.1897 | 2.1897 | inf | 0.0000 | 0 |

Important interpretation: both pairs produced only one completed trade. The high win rate and infinite profit factor are arithmetic artifacts of a one-trade sample, not robust performance evidence.

## 5. Strategy A Comparison

Strategy A comparison uses the prior Strategy A RR1.5 default baseline from `strategy_a_result_diagnostics.md`. This is a mechanical reference point only; Strategy B uses left-side swing targets instead of fixed RR exits.

| pair | strategy | trade_count | win_rate | average_r | median_r | total_r | profit_factor | max_drawdown_r | max_consecutive_losses |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | Strategy A RR1.5 | 195 | 42.05% | 0.0513 | -1.0000 | 10.0000 | 1.0885 | -14.0000 | 7 |
| USDJPY | Strategy B fixed | 1 | 100.00% | 1.5062 | 1.5062 | 1.5062 | inf | 0.0000 | 0 |
| EURUSD | Strategy A RR1.5 | 178 | 42.70% | 0.0674 | -1.0000 | 12.0000 | 1.1176 | -9.5000 | 6 |
| EURUSD | Strategy B fixed | 1 | 100.00% | 2.1897 | 2.1897 | 2.1897 | inf | 0.0000 | 0 |

Observations:

- Strategy B reduced the sample from 195 to 1 trade on USDJPY and from 178 to 1 trade on EURUSD versus Strategy A RR1.5.
- The reduction is mainly caused by minimum RR checks, wide stop checks, ADX checks, and left-side target availability.
- Because the Strategy B sample is too small, it cannot be fairly ranked against Strategy A on performance metrics.

## 6. No-trade Reason Aggregation

| pair | reason | count |
| --- | --- | ---: |
| USDJPY | tp1_below_min_rr | 121 |
| USDJPY | stop_too_wide | 49 |
| USDJPY | adx_below_threshold | 15 |
| USDJPY | no_left_side_tp1 | 7 |
| USDJPY | tp1_only_below_min_rr | 2 |
| EURUSD | tp1_below_min_rr | 97 |
| EURUSD | stop_too_wide | 48 |
| EURUSD | no_left_side_tp1 | 21 |
| EURUSD | adx_below_threshold | 10 |
| EURUSD | tp2_below_min_rr | 1 |

## 7. TP1 / TP2 / Breakeven Analysis

| pair | tp1_hit events | tp2 final exits | tp1-only final exits | breakeven_after_tp1 exits | stop_loss exits | end_of_data exits |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 1 | 0 | 1 | 0 | 0 | 0 |
| EURUSD | 1 | 1 | 0 | 0 | 0 | 0 |

## 8. Event Log Check

| pair | events_total | setup_started | reference_touch | expired_setup | no_trade | ignored_touch | entry | take_profit events | stop_loss events |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 2462 | 424 | 399 | 229 | 194 | 1213 | 1 | 1 | 0 |
| EURUSD | 2251 | 390 | 365 | 212 | 177 | 1104 | 1 | 1 | 0 |

Event-log interpretation:

- Setup discovery is still active: hundreds of setup and reference-touch events were detected on each pair.
- Valid entries collapsed to one per pair after Strategy B filters and left-side swing target gates.
- `ignored_touch` remains high for the same reason as Strategy A: only the first post-cross 20EMA touch is valid, and later touches are logged as ignored.

## 9. Yearly Performance

| pair | year | total_r |
| --- | ---: | ---: |
| USDJPY | 2022 | 1.5062 |
| EURUSD | 2023 | 2.1897 |

| pair | winning years | losing years | flat years | max winning year | max losing year | recent 5 years 2022-2026 |
| --- | ---: | ---: | ---: | --- | --- | ---: |
| USDJPY | 1 | 0 | 0 | 2022 / 1.5062R | 2022 / 1.5062R | 1.5062 |
| EURUSD | 1 | 0 | 0 | 2023 / 2.1897R | 2023 / 2.1897R | 2.1897 |

Yearly interpretation: with only one trade per pair, yearly tables mainly identify when the lone accepted trade occurred. They are not enough for regime-level conclusions.

## 10. Three-period Comparison

| pair | 1999-2008 | 2009-2018 | 2019-2026 |
| --- | ---: | ---: | ---: |
| USDJPY | 0.0000R | 0.0000R | 1.5062R |
| EURUSD | 0.0000R | 0.0000R | 2.1897R |

The period comparison is dominated by a single 2019-2026 trade per pair. It should be treated as sample-coverage information, not performance evidence.

## 11. Verification Commands

| command | result |
| --- | --- |
| `pytest` | 60 passed |
| `ruff check src tests` | All checks passed |
| `ruff format --check src tests` | 19 files already formatted |
| `mypy src tests` | Success: no issues found in 19 source files |

## 12. Provisional Judgment

- Strategy B implementation can be executed read-only against the provided CSVs, and the output files were generated as expected.
- As currently fixed, Strategy B appears too restrictive for meaningful EURUSD/USDJPY performance comparison: only one trade per pair survived all gates over the supplied 1999-2026 H4 files.
- Strategy B should not be discarded solely from this run, because the logic may still be useful as a video-like filter model, but the current validation result is mainly a coverage diagnostic rather than a performance diagnostic.
- The next useful step is to review the filtering funnel, especially `tp1_below_min_rr`, `stop_too_wide`, `adx_below_threshold`, and `no_left_side_tp1`, without doing parameter optimization.
- Do not use this report as evidence that Strategy B is profitable or live-tradable.

