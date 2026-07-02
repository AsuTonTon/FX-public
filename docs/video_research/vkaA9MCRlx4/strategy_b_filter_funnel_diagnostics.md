# Strategy B Filter Funnel Diagnostics

## 0. Scope and Guardrails

- Generated at: 2026-06-25T03:26:32
- Inputs: `results/strategy_b_readonly/events/*.csv`, `trades/*.csv`, `metrics/metrics_comparison.csv`, `docs/video_research/vkaA9MCRlx4/strategy_b_readonly_validation_report.md`, and `src/strategies/ema_wave3_strategy_b.py`.
- This report diagnoses why fixed Strategy B produced only one accepted trade per pair.
- No parameter changes, parameter optimization, Strategy C, market-data API, broker API, auto-trading, order placement, or real-money handling are included.
- Results are mechanical diagnostics on local CSV outputs only. They do not prove profitability or live-trading viability.

Important logging interpretation:

- `confirmation_candidates` means: first-touch setup reached body-close confirmation and had a next bar available, before Strategy B entry filters either accepted or rejected it.
- `no_trade.reason` is the first failed gate in `_build_entry`, not an independent attribution of all rules that could have failed.
- The gate order is ATR availability, ADX threshold, left-side TP1 availability, ATR/buffer stop construction, stop-distance sanity, TP1 minimum RR, TP1-only minimum RR, and TP2 minimum RR.

## 1. Funnel Counts

| pair | setup_started | reference_touch | confirmation_candidates | no_trade | accepted_entry | acceptance_rate_from_confirmation |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 424 | 399 | 195 | 194 | 1 | 0.5% |
| EURUSD | 390 | 365 | 178 | 177 | 1 | 0.6% |

Funnel read: Strategy B did not fail to find setups or first touches. The collapse happens after body-close confirmation, at the Strategy B filter gates.

## 2. No-trade Reason Counts

| pair | reason | count | share_of_no_trade |
| --- | --- | ---: | ---: |
| USDJPY | tp1_below_min_rr | 121 | 62.4% |
| USDJPY | stop_too_wide | 49 | 25.3% |
| USDJPY | adx_below_threshold | 15 | 7.7% |
| USDJPY | no_left_side_tp1 | 7 | 3.6% |
| USDJPY | tp1_only_below_min_rr | 2 | 1.0% |
| EURUSD | tp1_below_min_rr | 97 | 54.8% |
| EURUSD | stop_too_wide | 48 | 27.1% |
| EURUSD | no_left_side_tp1 | 21 | 11.9% |
| EURUSD | adx_below_threshold | 10 | 5.6% |
| EURUSD | tp2_below_min_rr | 1 | 0.6% |

Combined no-trade reasons:

| reason | count | share_of_all_no_trade |
| --- | ---: | ---: |
| tp1_below_min_rr | 218 | 58.8% |
| stop_too_wide | 97 | 26.1% |
| no_left_side_tp1 | 28 | 7.5% |
| adx_below_threshold | 25 | 6.7% |
| tp1_only_below_min_rr | 2 | 0.5% |
| tp2_below_min_rr | 1 | 0.3% |

## 3. `tp1_below_min_rr` Details

Strategy B requires TP1 to be at least 1.0R. These rows reached target selection and stop construction, but their first left-side target was too close relative to risk.

| pair | count | min_tp1_r | median_tp1_r | avg_tp1_r | max_tp1_r | <0.5R | 0.5R-1.0R | >=1.0R |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 121 | 0.0078 | 0.1818 | 0.2319 | 0.9756 | 107 | 14 | 0 |
| EURUSD | 97 | 0.0062 | 0.2073 | 0.2818 | 0.9807 | 78 | 19 | 0 |

Interpretation: TP1 minimum RR is the largest first-fail reason on both pairs. Most failed TP1 values are below 0.5R, so the issue is not just candidates narrowly missing 1.0R.

## 4. `stop_too_wide` Details

Strategy B rejects entries when stop distance is greater than 3.0 ATR. This check runs before TP1 minimum RR, so these candidates may also have had weak RR, but the first failing gate is wide stop distance.

| pair | count | min_stop_distance_atr | median_stop_distance_atr | avg_stop_distance_atr | max_stop_distance_atr | 3.0-4.0ATR | 4.0-5.0ATR | >=5.0ATR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 49 | 3.0132 | 3.6745 | 3.9984 | 7.5272 | 29 | 13 | 7 |
| EURUSD | 48 | 3.0094 | 3.6955 | 3.8324 | 7.0428 | 34 | 11 | 3 |

Interpretation: every `stop_too_wide` row is above the fixed 3.0ATR ceiling by definition. The median is well above 3.0ATR on both pairs, suggesting the stop-anchor logic plus ATR regime is a real bottleneck, not just rounding near the threshold.

## 5. `adx_below_threshold` Details

Strategy B rejects entries when ADX(14) is below 18.0. ADX is checked before left-side target and stop/RR gates.

| pair | count | min_adx | median_adx | avg_adx | max_adx | <10 | 10-14 | 14-18 | >=18 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 15 | 13.3257 | 15.4955 | 15.3350 | 17.9118 | 0 | 4 | 11 | 0 |
| EURUSD | 10 | 11.1645 | 16.2428 | 15.3402 | 17.6185 | 0 | 4 | 6 | 0 |

Interpretation: ADX is not the main bottleneck in this run. It explains 25 of 371 no-trade events across both pairs, far less than TP1 RR and stop-distance gates.

## 6. `no_left_side_tp1` Details

The fixed implementation searches confirmed, left-side swings within `swing_lookback_bars = 100`. A `no_left_side_tp1` event means no valid left-side target was found in that window.

| pair | no_left_side_tp1 | share_of_no_trade | swing_lookback_bars |
| --- | ---: | ---: | ---: |
| USDJPY | 7 | 3.6% | 100 |
| EURUSD | 21 | 11.9% | 100 |

Interpretation: this is a secondary bottleneck. It is more visible on EURUSD than USDJPY, but still much smaller than TP1 RR and stop-distance rejections.

## 7. Accepted Trades and Exits

| pair | accepted_entry | exit_reason | r_multiple | tp1_r | tp2_r | bars_held |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| USDJPY | 1 | take_profit | 1.5062 | 1.5062 | n/a | 15 |
| EURUSD | 1 | take_profit | 2.1897 | 1.3920 | 2.9874 | 22 |

Accepted-trade interpretation: the two accepted trades are not enough to evaluate performance. They only confirm that the execution path can pass TP1/TP2 handling on real CSV inputs.

## 8. Hypotheses: Why Strategy B Is Too Strict Here

1. The first left-side swing TP1 is often too close relative to the ATR-buffered stop distance. This is the dominant first-fail pattern.
2. The stop anchor can land far away from the entry in ATR terms, especially after the selected reference/touch structure. This creates `stop_too_wide` before RR is even evaluated.
3. ADX filtering removes some candidates, but it is not the primary reason the sample collapsed.
4. The swing lookback window occasionally cannot find a valid left-side TP1, especially on EURUSD, but this is secondary to RR and stop-distance failures.
5. The combination of strict TP1 minimum RR, stop-distance ceiling, and left-side target selection leaves almost no accepted entries even though Strategy A-style confirmations exist.

## 9. Candidate Rules To Review Later

These are review candidates, not implemented changes and not optimization results.

| priority | rule area | why review it | caution |
| ---: | --- | --- | --- |
| 1 | TP1 selection / TP1 minimum RR gate | Largest first-fail reason on both pairs. Most failures are below 0.5R, so target proximity is structurally important. | Do not simply lower the threshold to force more trades; first inspect whether left-side target selection is matching the video intent. |
| 2 | Stop anchor and 3.0ATR stop-distance ceiling | Second-largest first-fail reason. Median stop/ATR is above the ceiling, suggesting stop construction may be too conservative for many confirmed candidates. | Raising the ceiling can increase tail risk; review anchor definition before changing the limit. |
| 3 | Left-side swing lookback / swing validity | `no_left_side_tp1` is smaller but meaningful, especially on EURUSD. | Expanding lookback can introduce distant, less relevant targets and hindsight-like behavior if not specified carefully. |
| 4 | ADX threshold | ADX rejects relatively few candidates. | Lower priority because it is not the main bottleneck in current outputs. |
| 5 | Additional instrumentation | Current `no_trade.reason` records only the first failed gate. | Add diagnostics-only logging before changing rules, so future comparisons avoid guessing. |

## 10. Recommended Next Diagnostic Step

Before changing Strategy B, add or run a diagnostics-only candidate export that records every confirmed candidate with ATR, ADX, selected TP1/TP2, risk, stop_distance/ATR, and all pass/fail flags. That would show whether TP1 RR and stop-distance are jointly failing on the same candidates. This is instrumentation, not a trading-rule change or parameter optimization.

Provisional judgment: Strategy B should continue only as a diagnostics project for now. The current fixed rule set is too restrictive for meaningful performance comparison on USDJPY/EURUSD because it accepts only one trade per pair. No profitability conclusion should be drawn.

## 11. Verification Commands

| command | result |
| --- | --- |
| `pytest` | 60 passed |
| `ruff check src tests` | All checks passed |
| `ruff format --check src tests` | 19 files already formatted |
| `mypy src tests` | Success: no issues found in 19 source files |
