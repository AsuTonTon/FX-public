# Strategy B TP1 Selection Issue 45 Review

## 1. Objective and scope

This report reviews Strategy B TP1 selection using committed Strategy B
specification, implementation, validation, candidate-export, and TP-candidate
diagnostic documents.

Scope:

- summarize current TP1 selection and TP1 minimum RR behavior;
- summarize committed candidate-export and TP-candidate diagnostic evidence;
- classify the likely TP1 failure mode without changing Strategy B;
- identify files and rules that should remain the next review surface;
- recommend one bounded docs-only next task.

Out of scope:

- no Strategy A/B/B2/C rule, code, parameter, config, test, or backtest change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no new data acquisition or diagnostics generation;
- no raw market data, normalized CSV, candidate/result CSV, transcript text,
  subtitle text, caption URL, downloaded media, `data/`, or `results/` content;
- no profitability claim or trading recommendation.

## 2. Source files and docs used

Committed Strategy B docs:

- `docs/video_research/vkaA9MCRlx4/strategy_b_spec_design.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_implementation_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_filter_funnel_diagnostics.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_candidate_export_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_instrumentation.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_memo.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
- `docs/video_research/strategy_b_tp1_selection_review_current.md`

Committed code inspected read-only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`
- `tests/test_ema_wave3_strategy_b.py`
- `tests/test_strategy_b_runner.py`

No uncommitted local files, raw CSV rows, generated result artifacts, market
data, broker/live systems, YouTube, DownSub, captions, transcripts, comments,
or external sources were used.

## 3. Current Strategy B TP1 selection summary

Strategy B keeps the Strategy A setup sequence, then applies fixed Strategy B
gates and management rules after a body-close confirmation candidate exists.

Current TP1 selection is mechanical:

| item | current behavior |
| --- | --- |
| Swing model | Fractal-style left-side swings with default width `2` candles left and `2` candles right. |
| Lookback | `100` closed 4H candles before the confirmation candle. |
| Validity | Swing confirmation candles must already be closed before the Strategy B confirmation candle. |
| Long TP candidates | Valid left-side swing highs above entry. |
| Short TP candidates | Valid left-side swing lows below entry. |
| Ordering | Price-nearest target beyond entry first. |
| TP1 | First ordered target candidate. |
| TP2 | Second ordered target candidate, when present. |
| Missing TP1 | Candidate fails as `no_left_side_tp1`; later TP/RR gates cannot be evaluated. |

The code path in `src/strategies/ema_wave3_strategy_b.py` matches the
committed design: target candidates are ordered by eligible price distance,
`_target_prices()` selects the first candidate as TP1 and the second as TP2,
and target diagnostics mark rank 1 as `selected_tp1`.

Current TP1 is therefore not selected by target prominence, wave count,
horizontal-zone quality, channel boundary, range boundary, or discretionary
target realism. It is a deterministic nearest eligible left-side swing proxy.

## 4. Current minimum RR rule summary

After TP1 and stop are available, Strategy B computes risk and target R:

- long risk = `entry_price - stop_price`;
- short risk = `stop_price - entry_price`;
- long TP1 R = `(TP1 - entry_price) / risk`;
- short TP1 R = `(entry_price - TP1) / risk`.

The fixed RR gates are:

| gate | threshold |
| --- | ---: |
| TP1 minimum RR | `1.0R` |
| TP2 minimum RR, when TP2 exists | `1.5R` |
| TP1-only full-exit minimum RR, when TP2 is absent | `1.5R` |

Stop distance also affects TP1 R because risk is the denominator. Current stop
logic uses the committed stop-side swing or reference-candle fallback, applies
`max(pair_buffer, 0.10 * ATR(14), tick_size)`, and rejects stops outside
`0.25 * ATR(14)` to `3.0 * ATR(14)`.

This report does not change any threshold or stop rule.

## 5. Committed diagnostics evidence summary

Committed diagnostics show a severe post-confirmation acceptance collapse:

| measure | value |
| --- | ---: |
| confirmation candidates | 373 |
| accepted candidates | 2 |
| rejected candidates | 371 |
| `tp1_below_min_rr` first-fail count | 218 |
| `tp1_below_min_rr` all-failed-reason count | 335 of 371 rejected candidates |
| `stop_too_wide` all-failed-reason count | 101 |
| `stop_too_wide` candidates also failing `tp1_below_min_rr` | 101 of 101 |
| `adx_below_threshold` all-failed-reason count | 25 |
| ADX failures also failing TP1 minimum RR | 20 of 25 |
| rank-1 TP1 evaluable candidates | 340 |
| rank-1 TP1 median R | `0.1714R` |
| rank-1 TP1 values at or above `1.0R` | 5 of 340 |
| low-rank-1 cases where any rank 2-5 reaches at least `1.0R` | 76 of 335 |
| low-rank-1 cases still below `1.0R` across ranks 2-5 | 259 of 335 |
| `stop_too_wide` cases where any rank 1-5 reaches at least `1.0R` | 8 of 101 |

Evidence read:

- TP1 minimum RR is the broadest documented rejection footprint.
- Stop width and TP1 RR are tightly coupled in the documented diagnostics.
- ADX is not the primary driver for the current Strategy B candidate collapse.
- Later target ranks expose some possible diagnostic rescue potential, but they
  do not supply an automatic replacement rule.
- The existing decision memo and closure note keep current TP1, RR, stop,
  filter, management, and Strategy B2 status frozen.

## 6. Failure-mode analysis

| possible cause | assessment | rationale |
| --- | --- | --- |
| Genuinely too-distant stops | Partial cause. | Stop width matters, but every `stop_too_wide` candidate also fails TP1 RR, and only 8 of 101 have any rank 1-5 target at or above `1.0R`. |
| TP1 target too conservative or nearby | Strong documented symptom. | Rank-1 TP1 median is `0.1714R`, and only 5 of 340 rank-1 TP1 values reach `1.0R`. |
| TP1 selection selecting the wrong structural level | Plausible but unproven. | Current rank-1 selection is a nearest-fractal proxy. Diagnostics show low R, but committed evidence does not prove rank 1 is structurally invalid in general. |
| Mismatch between stop anchor and TP1 anchor | Plausible geometry issue. | Risk denominator and nearby TP1 interact; stop validity still needs separate structural classification. |
| Overly strict minimum RR against chosen TP1 | Plausible but not actionable here. | The gate dominates rejections, but changing the threshold would be parameter work and is not authorized by committed evidence. |
| Data or signal sparsity | Secondary. | There are 373 confirmation candidates; the collapse happens after confirmation, at Strategy B gates. |
| ADX filter | Not primary. | ADX affects far fewer candidates and mostly overlaps TP1 RR failures. |
| Implementation defect | Not supported by committed evidence. | The code appears aligned with the committed Strategy B specification and tests for TP1/TP2 behavior. |

## 7. Review classification

Current issue classification:

`structural_proxy_limitation_with_stop_to_tp_geometry_evidence_insufficient_for_rule_change`

Interpretation:

- The current TP1 method is structurally narrow because it turns a broader
  video-like target idea into nearest eligible fractal-swing selection.
- The current minimum RR gate is mechanically clear and is the direct rejection
  reason for many candidates.
- Stop-to-TP geometry is a material interaction: a valid-looking target can
  still fail if stop-side risk is large, and a wide stop can make nearby TP1
  fail RR.
- The committed evidence does not show an implementation/spec mismatch.
- The committed evidence is not sufficient to lower TP1 minimum RR, switch to
  rank 2, use any farther-rank exception, change stop anchors, change stop
  width limits, remove ADX, create Strategy B2, or alter executable Strategy B.

## 8. Files and rules to review next

The next review surface, if reopened by a separate issue, should remain:

- `src/strategies/ema_wave3_strategy_b.py`
  - `_ordered_target_swings()`
  - `_target_prices()`
  - `_select_stop_anchor()`
  - TP1/TP2 RR gate construction inside entry building
- `src/backtest/strategy_b_runner.py`
  - candidate export fields
  - TP-candidate diagnostics fields
  - summary/report wording
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
  - low-R-but-structural TP classification
  - micro-structure TP classification
  - no-valid-target separation
  - stop-anchor diagnostic path
  - contextual RR doctrine mapping

Any reopened work should remain docs-only until a separate design decision
approves a specific mechanical rule change.

## 9. Decision matrix

| option | evidence support | risk | decision |
| --- | --- | --- | --- |
| Keep Strategy B unchanged and document limitation | Strong. Current behavior is specified, implemented, tested, and covered by the closure note. | Low. | Recommended now. |
| Request a narrower diagnostic export/report | Possible later. Existing docs already define diagnostic backlog topics. | Medium, because generated artifacts must stay out of Git. | Defer to separate issue. |
| Propose a Strategy B2 design review later | Not supported now. | High overfitting and scope drift risk. | Do not do now. |
| Defer until more corpus evidence is available | Supported by closure note. | Low. | Acceptable. |
| Lower TP1 minimum RR | Not supported. | High parameter-optimization risk. | Do not do. |
| Switch TP1 to rank 2 or later rank | Not supported. | High rule-fitting risk; rank 2 helps only a small subset. | Do not do. |
| Change stop anchor or stop-width limits | Not supported. | High risk of invalidating premise-based stop logic. | Do not do. |
| Remove or retune ADX | Not supported by TP1 evidence. | Medium parameter-drift risk. | Do not do. |

## 10. Guardrail confirmation

Confirmed for this report:

- docs-only diagnostic review;
- committed repository docs and code only;
- no Strategy A/B/B2/C behavior change;
- no Strategy B rules, parameters, configs, tests, runner behavior, or backtest
  behavior changed;
- no Strategy B2 or Strategy C created;
- no parameter optimization;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, comments,
  downloaded media, ASR, or external sources accessed;
- no raw market data, normalized CSV, generated candidate/result/trade/event
  CSV, raw transcript, subtitle text, caption URL, downloaded media, `data/`,
  `results/`, credentials, tokens, or secrets committed;
- no profitability claim or trading recommendation.

## 11. Recommended next bounded task

Recommended next task:

`[codex] Strategy B TP1 stop-anchor follow-up backlog review`

Scope for that task:

- docs-only;
- inspect the existing TP1/stop-anchor follow-up backlog;
- choose exactly one future diagnostic question to preserve, defer, or close;
- do not generate new diagnostics;
- do not change Strategy B behavior;
- keep the existing TP1 decision closure controlling unless a separate human
  review explicitly reopens the design line.
