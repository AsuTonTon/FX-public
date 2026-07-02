# Strategy B TP Candidate Diagnostics Analysis

## 1. Scope and Guardrails

This is an analysis-only document for Strategy B TP candidate diagnostics.

No Strategy B code, rules, parameters, TP1/TP2 selection, stop placement, trade
acceptance, or backtest simulation behavior were changed. Strategy B2 and
Strategy C are not implemented here. This document makes no profitability
claim and is not a trading recommendation.

Strictly excluded:

- Market-data API, broker API, auto-trading, order placement, live trading, and
  real-money handling.
- TP1 minimum RR changes, TP2 minimum RR changes, stop-width limit changes,
  swing parameter changes, and parameter optimization.
- Committing raw CSV, normalized CSV, generated trade/event/candidate/
  TP-candidate/results CSV, transcript text, subtitles, videos, secrets, or
  credentials.

## 2. Data Sources

Local ignored CSVs under `results/` were read for aggregate analysis only.
Generated CSV rows are not pasted into this document and remain uncommitted.

| pair | source type | local path | file observation timestamp |
| --- | --- | --- | --- |
| USDJPY | candidate gates | `results/strategy_b_readonly/candidates/USDJPY_strategy_b_candidates.csv` | 2026-06-25T09:42:19 |
| USDJPY | TP candidate diagnostics | `results/strategy_b_readonly/tp_candidates/USDJPY_strategy_b_tp_candidates.csv` | 2026-06-25T09:42:19 |
| EURUSD | candidate gates | `results/strategy_b_readonly/candidates/EURUSD_strategy_b_candidates.csv` | 2026-06-25T09:42:39 |
| EURUSD | TP candidate diagnostics | `results/strategy_b_readonly/tp_candidates/EURUSD_strategy_b_tp_candidates.csv` | 2026-06-25T09:42:39 |

Reference documents:

- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_instrumentation.md`

## 3. Coverage Summary

| pair | confirmation candidates | TP diagnostic rows | rank 1 available | rank 2 available | rank 3 available | rank 4 available | rank 5 available | accepted candidates | accepted with TP rows | rejected candidates | rejected with TP rows |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 195 | 595 | 185 | 153 | 106 | 83 | 68 | 1 | 1 | 194 | 184 |
| EURUSD | 178 | 475 | 155 | 120 | 87 | 63 | 50 | 1 | 1 | 177 | 154 |
| Combined | 373 | 1070 | 340 | 273 | 193 | 146 | 118 | 2 | 2 | 371 | 338 |

Coverage read:

- All accepted candidates have TP diagnostics.
- Rejected candidates without TP rows are mostly cases where no valid left-side
  target candidate existed for the current Strategy B target model.
- The analysis is strongest for the 340 candidates with rank 1 TP diagnostics.

## 4. Rank-wise Target R Distribution

`target_r` is the candidate target distance divided by the existing Strategy B
risk. It does not change Strategy B exits; it only describes alternative
targets already exported by diagnostics instrumentation.

### USDJPY

| rank | count | min | median | average | p75 | max | >=0.5R | >=0.8R | >=1.0R | >=1.5R |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 185 | 0.0078 | 0.1607 | 0.2276 | 0.2959 | 1.5062 | 19 | 6 | 3 | 1 |
| 2 | 153 | 0.0302 | 0.3350 | 0.3965 | 0.5450 | 1.5052 | 44 | 13 | 7 | 1 |
| 3 | 106 | 0.0761 | 0.5101 | 0.5850 | 0.7972 | 1.6430 | 54 | 26 | 16 | 2 |
| 4 | 83 | 0.1507 | 0.6896 | 0.8662 | 1.0216 | 3.8880 | 58 | 33 | 23 | 9 |
| 5 | 68 | 0.1892 | 0.9444 | 1.1046 | 1.2895 | 3.7933 | 54 | 38 | 31 | 15 |

### EURUSD

| rank | count | min | median | average | p75 | max | >=0.5R | >=0.8R | >=1.0R | >=1.5R |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 155 | 0.0057 | 0.1781 | 0.2451 | 0.3160 | 1.3920 | 22 | 5 | 2 | 0 |
| 2 | 120 | 0.0250 | 0.3321 | 0.4368 | 0.5507 | 2.9874 | 34 | 16 | 13 | 2 |
| 3 | 87 | 0.0999 | 0.5143 | 0.6402 | 0.8515 | 3.2385 | 47 | 24 | 17 | 4 |
| 4 | 63 | 0.1124 | 0.7170 | 0.7963 | 1.0632 | 2.3032 | 44 | 25 | 19 | 4 |
| 5 | 50 | 0.1995 | 0.9053 | 0.9830 | 1.2558 | 2.7564 | 42 | 29 | 19 | 9 |

### Combined

| rank | count | min | median | average | p75 | max | >=0.5R | >=0.8R | >=1.0R | >=1.5R |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 340 | 0.0057 | 0.1714 | 0.2356 | 0.3094 | 1.5062 | 41 | 11 | 5 | 1 |
| 2 | 273 | 0.0250 | 0.3338 | 0.4142 | 0.5450 | 2.9874 | 78 | 29 | 20 | 3 |
| 3 | 193 | 0.0761 | 0.5109 | 0.6098 | 0.8155 | 3.2385 | 101 | 50 | 33 | 6 |
| 4 | 146 | 0.1124 | 0.6993 | 0.8360 | 1.0259 | 3.8880 | 102 | 58 | 42 | 13 |
| 5 | 118 | 0.1892 | 0.9169 | 1.0531 | 1.2836 | 3.7933 | 96 | 67 | 50 | 24 |

Rank-wise read:

- Rank 1 is very close in R terms. Combined median rank 1 is only 0.1714R.
- Later ranks are materially farther on average. Combined median rank 5 is
  0.9169R, and 50 of 118 rank 5 rows reach at least 1.0R.
- Later ranks are not universally sufficient. Even rank 5 has a median below
  1.0R and is unavailable for many candidates.

## 5. Rank 1 vs Later-rank Comparison

The table below looks only at candidates with rank 1 available and rank 1
`target_r < 1.0R`.

| pair | rank 1 available | rank 1 < 1.0R | rank 2 >= 1.0R | any rank 2-5 >= 1.0R | any rank 2-5 >= 1.5R | ranks 2-5 still < 1.0R | median best later R | median best-later minus rank-1 R |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 185 | 182 | 7 | 45 | 18 | 137 | 0.6520 | 0.4680 |
| EURUSD | 155 | 153 | 11 | 31 | 10 | 122 | 0.6248 | 0.4122 |
| Combined | 340 | 335 | 18 | 76 | 28 | 259 | 0.6289 | 0.4500 |

Diagnostic answers:

- When rank 1 is below 1.0R, rank 2 reaches 1.0R in 18 of 335 combined cases
  (5.4%).
- Any of ranks 2-5 reaches 1.0R in 76 of 335 combined cases (22.7%).
- Any of ranks 2-5 reaches 1.5R in 28 of 335 combined cases (8.4%).
- Later ranks are materially better for a minority of candidates, but most
  candidates are still structurally too close relative to existing Strategy B
  risk.
- USDJPY has slightly more rank 2-5 diagnostic rescue potential than EURUSD:
  45 of 182 cases (24.7%) versus 31 of 153 cases (20.3%).

## 6. Rejected-candidate Diagnostic Rescue Potential

This section uses "diagnostic rescue potential" only to describe whether later
target ranks would have crossed an R threshold. It is not an improvement claim,
profitability claim, or instruction to change Strategy B.

### All rejected candidates

| pair | rejected candidates | evaluable with rank 1 | rank 1 < 1.0R | rank 2 >= 1.0R | any rank 2-5 >= 1.0R | any rank 2-5 >= 1.5R | later ranks still < 1.0R |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 194 | 184 | 182 | 7 | 45 | 18 | 137 |
| EURUSD | 177 | 154 | 153 | 11 | 31 | 10 | 122 |
| Combined | 371 | 338 | 335 | 18 | 76 | 28 | 259 |

### Rejected candidates with `tp1_below_min_rr`

| pair | `tp1_below_min_rr` candidates | evaluable with rank 1 | rank 1 < 1.0R | rank 2 >= 1.0R | any rank 2-5 >= 1.0R | any rank 2-5 >= 1.5R | later ranks still < 1.0R |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 182 | 182 | 182 | 7 | 45 | 18 | 137 |
| EURUSD | 153 | 153 | 153 | 11 | 31 | 10 | 122 |
| Combined | 335 | 335 | 335 | 18 | 76 | 28 | 259 |

Rescue-potential read:

- The current rank 1 TP1 selection is a major bottleneck, but simply switching
  to rank 2 would affect only a small subset.
- Looking across ranks 2-5 finds more diagnostic potential, but still leaves
  259 of 335 TP1-below-min-RR cases below 1.0R.
- This argues against a quick rule change such as "use rank 2 instead of rank
  1" without chart review or a more principled target definition.

## 7. Prominence Analysis

`simple_prominence_atr` is only a local fractal proxy. It is not proof of
video-like market structure, liquidity, or discretionary significance.

### Prominence by rank

| pair | rank | count | median prominence ATR | average prominence ATR | p75 prominence ATR | max prominence ATR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 1 | 185 | 0.1815 | 0.2326 | 0.3199 | 1.3386 |
| USDJPY | 2 | 153 | 0.1876 | 0.2665 | 0.4063 | 1.0418 |
| USDJPY | 3 | 106 | 0.1829 | 0.2681 | 0.3667 | 1.3724 |
| USDJPY | 4 | 83 | 0.2290 | 0.3241 | 0.4201 | 1.8639 |
| USDJPY | 5 | 68 | 0.2035 | 0.2877 | 0.3537 | 1.3884 |
| EURUSD | 1 | 155 | 0.2008 | 0.2694 | 0.3466 | 1.5177 |
| EURUSD | 2 | 120 | 0.1714 | 0.2277 | 0.2882 | 2.6161 |
| EURUSD | 3 | 87 | 0.1777 | 0.2278 | 0.3377 | 0.7488 |
| EURUSD | 4 | 63 | 0.1425 | 0.2272 | 0.2839 | 1.3413 |
| EURUSD | 5 | 50 | 0.2052 | 0.3148 | 0.4151 | 1.5219 |
| Combined | 1 | 340 | 0.1911 | 0.2494 | 0.3267 | 1.5177 |
| Combined | 2 | 273 | 0.1795 | 0.2494 | 0.3347 | 2.6161 |
| Combined | 3 | 193 | 0.1792 | 0.2499 | 0.3647 | 1.3724 |
| Combined | 4 | 146 | 0.1851 | 0.2823 | 0.3547 | 1.8639 |
| Combined | 5 | 118 | 0.2035 | 0.2992 | 0.3865 | 1.5219 |

### Candidate-level prominence comparisons

| pair | rank 1 median | rank 2 median | best later-rank median | best later prominence > rank 1 | comparable candidates | accepted rank 1 median | rejected rank 1 median | `tp1_below_min_rr` rank 1 median |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| USDJPY | 0.1815 | 0.1876 | 0.4086 | 118 | 153 | 0.0635 | 0.1816 | 0.1795 |
| EURUSD | 0.2008 | 0.1714 | 0.2996 | 86 | 120 | 0.0802 | 0.2033 | 0.2057 |
| Combined | 0.1911 | 0.1795 | 0.3521 | 204 | 273 | 0.0718 | 0.1931 | 0.1931 |

Prominence read:

- Rank 2 is not consistently more prominent than rank 1. Combined medians are
  very close: rank 1 at 0.1911 ATR and rank 2 at 0.1795 ATR.
- The best later rank among ranks 2-5 is often more prominent than rank 1:
  204 of 273 comparable candidates. This supports further review, but it does
  not identify a deterministic replacement rule by itself.
- Accepted candidates have lower rank 1 prominence in this tiny accepted sample
  of two trades, so prominence alone does not explain acceptance.
- TP1-below-min-RR candidates have rank 1 prominence similar to all rejected
  candidates. Their main issue remains target distance in R, not conclusively
  local fractal prominence.

## 8. Stop-distance Interaction

| pair | `stop_too_wide` candidates | evaluable | any rank 1-5 >= 1.0R | all ranks 1-5 < 1.0R |
| --- | ---: | ---: | ---: | ---: |
| USDJPY | 52 | 52 | 4 | 48 |
| EURUSD | 49 | 49 | 4 | 45 |
| Combined | 101 | 101 | 8 | 93 |

Stop-distance read:

- For stop-too-wide candidates, later TP ranks rarely overcome the large risk
  denominator. Only 8 of 101 stop-too-wide candidates have any rank 1-5 target
  at or above 1.0R.
- This supports the prior finding that stop width and target distance interact.
  It does not justify widening the stop-distance ceiling.

## 9. Failure-mode Classification Update

| classification | assessment |
| --- | --- |
| Rank 1 is too close but later ranks often have viable R | Partly true, but only for a minority. Any rank 2-5 reaches 1.0R in 76 of 335 rank-1-below-1.0R cases. |
| Rank 1 is too close and later ranks are also mostly too close | Strong. 259 of 335 rank-1-below-1.0R cases still have no rank 2-5 target reaching 1.0R. |
| Rank 1 has low prominence compared with later ranks | Mixed. Best later prominence is often higher, but rank 2 is not consistently higher and accepted examples do not support prominence as a standalone gate. |
| Prominence measure is inconclusive | Strong. `simple_prominence_atr` is a local fractal proxy and does not prove video-like structure. |
| Stop distance remains too large relative to all nearby targets | Strong for the `stop_too_wide` subset. 93 of 101 stop-too-wide candidates still have all ranks 1-5 below 1.0R. |
| Pair-specific difference exists | Mild. USDJPY has slightly more later-rank rescue potential than EURUSD, but both pairs show the same broad pattern. |
| Insufficient evidence for rule change | Strong. The diagnostics show a problem, but not a safe replacement rule. |

## 10. Non-action Decision

This evidence is not enough to change Strategy B rules.

Do not change TP1 minimum RR yet. Do not switch to rank 2 target yet. Do not
modify `swing_width` or `swing_lookback_bars` yet. Do not widen the stop-width
limit yet. Do not create a Strategy B2 implementation yet.

Reasoning:

- Rank 1 is clearly too close in many cases.
- Later ranks provide useful diagnostic evidence, but only a minority of
  rejected candidates become threshold-evaluable at 1.0R by looking at ranks
  2-5.
- A naive rank 2 switch would miss most of the potential and would still be an
  unvalidated rule change.
- Prominence evidence is suggestive but not decisive.
- Stop-distance interaction remains important for wide-stop candidates.

## 11. Recommended Next Step

The safest next research step is a docs-only manual chart review protocol that
compares rank 1 versus later ranks without changing Strategy B.

Suggested protocol:

1. Sample candidates by fixed buckets, not outcome:
   `rank1 < 0.25R`, `0.25R <= rank1 < 0.5R`, `0.5R <= rank1 < 1.0R`, and
   accepted candidates.
2. For each sampled candidate, inspect rank 1 through rank 5 target locations
   on the chart.
3. Mark whether a human video-like interpretation would likely choose rank 1,
   a later rank, no target, or no trade.
4. Record reasons using a fixed vocabulary: minor swing, clear swing,
   liquidity-like level, too close, too far, stop too wide, no clean structure.
5. Only after that review, write a docs-only Strategy B2 design note. Do not
   implement a new rule in this PR.

## 12. Validation

This change is docs-only. No Strategy B code, tests, parameters, runner logic,
or generated CSV outputs were changed or committed. Full test execution was not
required for this analysis-only document.
