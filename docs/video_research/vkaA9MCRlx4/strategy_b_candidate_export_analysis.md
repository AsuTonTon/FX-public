# Strategy B Candidate Export Analysis

## 0. Scope and Guardrails

- Generated at: 2026-06-25T08:12:56
- Inputs: `results/strategy_b_readonly/candidates/USDJPY_strategy_b_candidates.csv`, `results/strategy_b_readonly/candidates/EURUSD_strategy_b_candidates.csv`, `strategy_b_candidate_export_notes.md`, and `strategy_b_filter_funnel_diagnostics.md`.
- This report analyzes candidate-level gate failures only. It does not change Strategy B rules or parameters.
- No parameter optimization, Strategy C, market-data API, broker API, auto-trading, order placement, or real-money handling is included.
- Candidate CSVs remain under ignored `results/` and must not be committed to Git.
- The figures below are diagnostics, not profitability claims or trading recommendations.

## 1. Candidate and Accepted Counts

| pair | candidates | accepted | rejected | accepted_rate |
| --- | ---: | ---: | ---: | ---: |
| USDJPY | 195 | 1 | 194 | 0.5% |
| EURUSD | 178 | 1 | 177 | 0.6% |
| ALL | 373 | 2 | 371 | 0.5% |

Both pairs still have only one accepted candidate. This confirms the previous funnel finding: the collapse happens after confirmation candidate creation.

## 2. First-fail Reason Counts

`first_fail_reason` preserves the Strategy B gate order. Accepted candidates are shown as `accepted`.

| pair | first_fail_reason | count | share_of_candidates |
| --- | --- | ---: | ---: |
| USDJPY | tp1_below_min_rr | 121 | 62.1% |
| USDJPY | stop_too_wide | 49 | 25.1% |
| USDJPY | adx_below_threshold | 15 | 7.7% |
| USDJPY | no_left_side_tp1 | 7 | 3.6% |
| USDJPY | tp1_only_below_min_rr | 2 | 1.0% |
| USDJPY | accepted | 1 | 0.5% |
| EURUSD | tp1_below_min_rr | 97 | 54.5% |
| EURUSD | stop_too_wide | 48 | 27.0% |
| EURUSD | no_left_side_tp1 | 21 | 11.8% |
| EURUSD | adx_below_threshold | 10 | 5.6% |
| EURUSD | tp2_below_min_rr | 1 | 0.6% |
| EURUSD | accepted | 1 | 0.6% |
| ALL | tp1_below_min_rr | 218 | 58.4% |
| ALL | stop_too_wide | 97 | 26.0% |
| ALL | no_left_side_tp1 | 28 | 7.5% |
| ALL | adx_below_threshold | 25 | 6.7% |
| ALL | tp1_only_below_min_rr | 2 | 0.5% |
| ALL | accepted | 2 | 0.5% |
| ALL | tp2_below_min_rr | 1 | 0.3% |

## 3. All-failed Reason Counts

`all_failed_reasons` counts every gate that could be evaluated and failed. One candidate can appear in multiple rows here.

| pair | failed_reason | count | share_of_rejected_candidates |
| --- | --- | ---: | ---: |
| USDJPY | tp1_below_min_rr | 182 | 93.8% |
| USDJPY | tp2_below_min_rr | 152 | 78.4% |
| USDJPY | stop_too_wide | 52 | 26.8% |
| USDJPY | tp1_only_below_min_rr | 31 | 16.0% |
| USDJPY | adx_below_threshold | 15 | 7.7% |
| USDJPY | no_left_side_tp1 | 10 | 5.2% |
| EURUSD | tp1_below_min_rr | 153 | 86.4% |
| EURUSD | tp2_below_min_rr | 118 | 66.7% |
| EURUSD | stop_too_wide | 49 | 27.7% |
| EURUSD | tp1_only_below_min_rr | 35 | 19.8% |
| EURUSD | no_left_side_tp1 | 23 | 13.0% |
| EURUSD | adx_below_threshold | 10 | 5.6% |
| ALL | tp1_below_min_rr | 335 | 90.3% |
| ALL | tp2_below_min_rr | 270 | 72.8% |
| ALL | stop_too_wide | 101 | 27.2% |
| ALL | tp1_only_below_min_rr | 66 | 17.8% |
| ALL | no_left_side_tp1 | 33 | 8.9% |
| ALL | adx_below_threshold | 25 | 6.7% |

Key read: `tp1_below_min_rr` appears in 335 of 371 rejected candidates, or 90.3% of all rejected candidates. That is the broadest failure across evaluable gates.

## 4. Overlap: `stop_too_wide` and `tp1_below_min_rr`

| pair | stop_too_wide | also_tp1_below_min_rr | overlap_share | stop_too_wide_without_tp1_failure |
| --- | ---: | ---: | ---: | ---: |
| USDJPY | 52 | 52 | 100.0% | 0 |
| EURUSD | 49 | 49 | 100.0% | 0 |
| ALL | 101 | 101 | 100.0% | 0 |

All `stop_too_wide` candidates also fail `tp1_below_min_rr`. This means wide stops are not an independent primary blocker in this candidate set; they worsen a target-distance problem that is already present.

## 5. Overlap: `adx_below_threshold` With Other Fails

| pair | adx_below_threshold | also_tp1_below_min_rr | also_tp2_below_min_rr | also_stop_too_wide | also_no_left_side_tp1 | also_tp1_only_below_min_rr |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 15 | 12 | 11 | 3 | 3 | 1 |
| EURUSD | 10 | 8 | 6 | 1 | 2 | 2 |
| ALL | 25 | 20 | 17 | 4 | 5 | 3 |

ADX is a secondary gate here. It affects 25 rejected candidates, but 20 of those also fail TP1 minimum RR. It is not the first rule to revisit.

## 6. Overlap: `no_left_side_tp1` With Other Fails

| pair | no_left_side_tp1 | also_adx_below_threshold | other_evaluable_failures |
| --- | ---: | ---: | ---: |
| USDJPY | 10 | 3 | 0 |
| EURUSD | 23 | 2 | 0 |
| ALL | 33 | 5 | 0 |

When TP1 is unavailable, later TP/RR gates cannot be evaluated. The only observed overlap is with ADX. This is a separate target-availability issue, but smaller than the TP1 RR problem.

## 7. TP1 R Distribution

| pair | evaluable_count | min | median | avg | max | <0.25R | 0.25-0.5R | 0.5-1.0R | >=1.0R |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 185 | 0.0078 | 0.1607 | 0.2276 | 1.5062 | 129 | 37 | 16 | 3 |
| EURUSD | 155 | 0.0057 | 0.1781 | 0.2451 | 1.3920 | 104 | 29 | 20 | 2 |
| ALL | 340 | 0.0057 | 0.1714 | 0.2356 | 1.5062 | 233 | 66 | 36 | 5 |

Only 5 of 340 evaluable TP1 values reach 1.0R or more. The median TP1 R is 0.1714R across both pairs, which strongly supports TP1 target distance as the main bottleneck.

## 8. Stop-distance / ATR Distribution

| pair | evaluable_count | min | median | avg | max | <1ATR | 1-2ATR | 2-3ATR | 3-4ATR | 4-5ATR | >=5ATR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 185 | 0.6249 | 2.2772 | 2.5522 | 7.5272 | 4 | 65 | 64 | 32 | 13 | 7 |
| EURUSD | 155 | 0.7802 | 2.4680 | 2.6563 | 7.0428 | 3 | 38 | 65 | 35 | 11 | 3 |
| ALL | 340 | 0.6249 | 2.3893 | 2.5997 | 7.5272 | 7 | 103 | 129 | 67 | 24 | 10 |

The median stop distance is 2.3893ATR across both pairs. The 3.0ATR ceiling rejects 101 candidates, but every one of those also fails TP1 minimum RR.

## 9. Accepted vs Rejected Candidates

| pair | group | count | median_tp1_r | median_stop_distance_atr | median_adx | left_side_tp1_available |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| USDJPY | accepted | 1 | 1.5062 | 1.6830 | 23.5604 | 1/1 |
| USDJPY | rejected | 194 | 0.1597 | 2.2941 | 38.7386 | 184/194 |
| EURUSD | accepted | 1 | 1.3920 | 0.9351 | 59.7258 | 1/1 |
| EURUSD | rejected | 177 | 0.1780 | 2.4781 | 37.9810 | 154/177 |
| ALL | accepted | 2 | 1.4491 | 1.3090 | 41.6431 | 2/2 |
| ALL | rejected | 371 | 0.1710 | 2.3936 | 38.7163 | 338/371 |

Accepted candidates have much larger TP1 R than rejected candidates. Rejected candidates have only slightly lower or comparable ADX, so ADX does not explain the sample collapse.

## 10. Which Rule Is the Real Culprit?

The strongest culprit is the TP1 selection / TP1 minimum RR relationship.

Evidence:

- `tp1_below_min_rr` appears in 335 of 371 rejected candidates, or 90.3%.
- Every `stop_too_wide` candidate also fails `tp1_below_min_rr`.
- ADX failures are few, and most ADX failures also fail TP1 minimum RR.
- Only 5 of 340 candidates with evaluable TP1 R reach 1.0R or more.
- Accepted candidates have median TP1 R of 1.4491R, while rejected candidates have median TP1 R of 0.1710R.

`stop_too_wide` is still important, but the overlap shows it is usually paired with an already-insufficient TP1. The first rule to inspect should therefore be how TP1 is selected and interpreted, not simply the 3.0ATR ceiling.

## 11. If Only One Rule Is Reviewed Next

Review TP1 selection / TP1 minimum RR first. Do not change the parameter yet.

Recommended next diagnostic question:

- Is Strategy B selecting the video-intended left-side target, or is it mechanically choosing a nearest minor swing that is too close to entry to be useful?

A safe next step is a docs-only or diagnostics-only review of candidate examples where TP1 R is below 0.25R, comparing the selected TP1 with the surrounding swing structure. That is still not a trading-rule change and not optimization.

## 12. Non-action Decision

No Strategy B rule should be changed from this report alone. The candidate export improves visibility, but the result is still a two-pair historical diagnostic on local CSVs. No profitability conclusion should be drawn.

## 13. Verification Commands

| command | result |
| --- | --- |
| `pytest` | 66 passed |
| `ruff check src tests` | All checks passed |
| `ruff format --check src tests` | 19 files already formatted |
| `mypy src tests` | Success: no issues found in 19 source files |
