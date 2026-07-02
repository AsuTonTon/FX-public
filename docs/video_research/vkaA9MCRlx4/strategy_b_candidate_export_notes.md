# Strategy B Candidate Export Notes

## 1. Purpose

This change adds a diagnostics-only confirmation candidate export for Strategy B.
It records each body-close confirmation candidate and the pass/fail state of the
Strategy B entry gates. It does not change Strategy B parameters, entries,
exits, trade simulation, metrics, or live-trading behavior.

## 2. Output

Runner output now includes:

`results/strategy_b_readonly/candidates/*_strategy_b_candidates.csv`

The output remains under `results/`, which is ignored by Git. Raw CSVs,
normalized CSVs, candidate CSVs, trades, events, and metrics outputs are not
intended to be committed.

## 3. Candidate Columns

| column | meaning |
| --- | --- |
| pair | Pair name. |
| direction | Candidate direction, `long` or `short`. |
| setup_time | EMA cross setup time. |
| touch_time | First 20EMA touch time. |
| confirmation_time | Body-close confirmation time. |
| entry_time | Next bar open time used for hypothetical entry. |
| entry_price | Next bar open price. |
| atr | ATR value at confirmation. |
| adx | ADX value at confirmation. |
| adx_pass | Whether the fixed ADX gate passes. |
| stop_anchor | Selected left-side stop anchor or reference candle anchor. |
| stop_price | Stop price after ATR/pair/tick buffer. |
| buffer | `max(pair_buffer, 0.10 * ATR, tick_size)`. |
| risk | Entry-to-stop distance. |
| stop_distance_atr | Risk divided by ATR. |
| stop_too_narrow_pass | Whether risk is at least the fixed minimum ATR multiple. |
| stop_too_wide_pass | Whether risk is no more than the fixed maximum ATR multiple. |
| tp1_price | Selected first left-side swing target. |
| tp2_price | Selected second left-side swing target, if available. |
| tp1_r | TP1 distance in R. |
| tp2_r | TP2 distance in R, if available. |
| left_side_tp1_available | Whether TP1 was found in the fixed left-side swing window. |
| tp1_min_rr_pass | Whether TP1 meets the fixed minimum RR. |
| tp1_only_min_rr_pass | Whether TP1-only final exit meets the fixed minimum RR, when TP2 is unavailable. |
| tp2_min_rr_pass | Whether TP2 meets the fixed minimum RR, when TP2 is available. |
| accepted | Whether the candidate became an entry order. |
| first_fail_reason | First failed gate in Strategy B's existing gate order. |
| all_failed_reasons | JSON array of all failed gates that can be evaluated for that candidate. |

## 4. Gate Order

`first_fail_reason` preserves the existing Strategy B order:

1. `atr_unavailable`
2. `adx_unavailable`
3. `adx_below_threshold`
4. `no_left_side_tp1`
5. `invalid_risk`
6. `stop_too_narrow`
7. `stop_too_wide`
8. `tp1_below_min_rr`
9. `tp1_only_below_min_rr`
10. `tp2_below_min_rr`

`all_failed_reasons` can include later gates when their inputs are available.
For example, a candidate can have `first_fail_reason = stop_too_wide` while
also failing `tp1_below_min_rr`.

## 5. Validation

Read-only runner was rerun on the local USDJPY/EURUSD CSVs. The
`metrics_comparison.csv` content was unchanged after adding candidate export:

- USDJPY remains 1 trade, total R 1.5061872484326255.
- EURUSD remains 1 trade, total R 2.189734625774731.

Generated candidate files:

- `results/strategy_b_readonly/candidates/USDJPY_strategy_b_candidates.csv`
- `results/strategy_b_readonly/candidates/EURUSD_strategy_b_candidates.csv`

This confirms the export is diagnostics-only for the current run. It is not a
profitability claim and does not indicate live-trading viability.

## 6. Explicit Non-goals

- No Strategy B parameter changes.
- No parameter optimization.
- No Strategy C.
- No market-data API.
- No broker API.
- No auto-trading.
- No order placement.
- No real-money handling.
- No profitability conclusion.
