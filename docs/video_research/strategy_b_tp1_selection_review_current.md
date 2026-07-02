# Strategy B TP1 Selection Review Current

Task: `strategy_b_tp1_selection_review_current`

Review date: 2026-07-01

## 1. Objective and scope

This is a docs-only review of current Strategy B TP1 selection.

This review:

- Documents current Strategy B TP1 behavior using committed docs and read-only repository context.
- Separates TP1 selection, TP1 minimum RR, stop-to-TP geometry, and management dependency issues.
- Uses the Doctrine Map v2 draft proposal and Strategy A/B mismatch findings only as non-final context.
- Reviews whether committed evidence is sufficient for a future human decision context.

This review does not:

- Change Strategy B.
- Modify Strategy B TP1 selection logic.
- Modify Strategy B TP2 selection logic.
- Modify Strategy B RR rules.
- Modify Strategy B stop logic.
- Modify Strategy B filters.
- Modify Strategy B management rules.
- Modify Strategy A/B code, parameters, configs, or tests.
- Run backtests or optimization.
- Access market data or fetch market data.
- Use broker APIs.
- Add broker, live trading, order execution, or execution logic.
- Make profitability claims.
- Create Strategy B2 or Strategy C.
- Update `docs/video_research/channel_doctrine_map_v1.md`.
- Create or update `docs/video_research/channel_doctrine_map_v2.md`.
- Treat the Doctrine Map v2 draft proposal as final or accepted doctrine.
- Include Batch 08.
- Access DownSub or YouTube.
- Fetch captions.
- Download video or audio.
- Run ASR.
- Commit raw TXT, SRT, VTT, subtitle full text, caption URLs, CSV, JSON, database, raw candidate rows, generated candidate CSV, raw market CSV, normalized market CSV, `data/`, `results/`, or backtest-output artifacts.

## 2. Evidence base

This review uses only committed evidence and read-only repository context.

Primary review plan:

- `docs/video_research/strategy_b_tp1_selection_review_plan.md`
- `docs/video_research/strategy_b_tp1_selection_review_plan_review.md`

Strategy B documents inspected:

- `docs/video_research/vkaA9MCRlx4/strategy_b_spec_design.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_implementation_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_readonly_validation_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_filter_funnel_diagnostics.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_candidate_export_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_candidate_export_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_instrumentation.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_memo.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`

Doctrine and mismatch context inspected as non-final context:

- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_human_review.md`
- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck.md`
- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_plan.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal_human_review.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal.md`
- `docs/video_research/doctrine_map_v2_candidate_review.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`

Implementation and tests inspected read-only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`
- `tests/test_ema_wave3_strategy_b.py`
- `tests/test_strategy_b_runner.py`

No new diagnostics were created. No candidate rows, CSVs, market data, backtest outputs, or result artifacts were generated or committed.

## 3. Current Strategy B TP1 logic summary

Current Strategy B keeps the Strategy A setup sequence: EMA20/EMA200 trend-cross context, first 20EMA touch, body-close confirmation, and next-bar-open entry.

After a confirmation candidate exists, current TP1 behavior is:

| item | current behavior | source basis |
| --- | --- | --- |
| Swing definition | Uses a fractal-style swing with default width `2` candles left and `2` candles right. | Strategy B spec, implementation notes, implementation. |
| Left-side validity | A swing is valid only if it is inside the fixed lookback and its right-side confirmation candles are closed before the Strategy B confirmation candle. | Strategy B spec, implementation notes, implementation. |
| Lookback | Uses `100` closed 4H candles before confirmation. | Strategy B spec and validation report. |
| Long TP candidates | Valid left-side swing highs above entry. | Strategy B spec and implementation. |
| Short TP candidates | Valid left-side swing lows below entry. | Strategy B spec and implementation. |
| Ordering | Long candidates are sorted by nearest higher price first; short candidates are sorted by nearest lower price first. | Implementation and prior TP1 selection review. |
| TP1 | First ordered target candidate, or absent when no valid target exists. | Strategy B spec, implementation, tests. |
| TP2 | Second ordered target candidate when present. | Strategy B spec, implementation, tests. |
| Missing TP1 | Candidate can fail as `no_left_side_tp1`; later TP/RR gates cannot be evaluated. | Candidate export notes and analysis. |
| Missing TP2 | TP1-only fallback requires TP1 to clear the TP1-only minimum RR. | Strategy B spec and implementation. |
| TP1 R | For long candidates, target distance is `(TP1 - entry) / risk`; for shorts, `(entry - TP1) / risk`. | Implementation and candidate export notes. |
| Risk | Long risk is entry minus stop; short risk is stop minus entry. | Strategy B spec and implementation. |
| TP1 minimum RR | Fixed at `1.0R`. | Strategy B spec, implementation notes, validation report. |
| TP2 minimum RR | Fixed at `1.5R` when TP2 exists. | Strategy B spec, implementation notes, validation report. |
| TP1-only minimum RR | Fixed at `1.5R` when TP2 is absent. | Strategy B spec and validation report. |
| Stop anchor | Uses a valid stop-side left swing beyond the reference candle when available, otherwise the reference candle level. | Strategy B spec, implementation notes, implementation. |
| Stop buffer | Uses `max(pair_buffer, 0.10 * ATR(14), tick_size)`. | Strategy B spec and implementation notes. |
| Stop sanity | Rejects if risk is below `0.25 * ATR(14)` or above `3.0 * ATR(14)`. | Strategy B spec, implementation notes, validation report. |
| Partial exit | TP1 is required before the fixed 50% partial exit path can occur. | Strategy B spec, implementation notes. |
| Break-even | After TP1, remaining 50% moves to break-even at original entry. | Strategy B spec, implementation notes. |

Assumptions explicitly specified in docs:

- Fractal width, lookback, TP1/TP2 ordering, RR thresholds, ATR buffer, stop sanity, partial exit ratio, and break-even behavior are specified in Strategy B docs.
- Long/short target selection is specified as left-side swing highs above entry for longs and left-side swing lows below entry for shorts.
- No future swing usage is specified and tested.

Assumptions inferred from implementation or diagnostics:

- Current TP1 is price-rank based rather than prominence-based, wave-count-based, channel-boundary-based, or discretionary-structure-based.
- The same ordered target list powers TP1/TP2 selection and TP candidate diagnostics.
- Rejection pathways can record both a first failing reason and all failed reasons; `stop_too_wide` can be first-fail while `tp1_below_min_rr` is also present.

This review does not change any of the above behavior.

## 4. Known diagnostic findings

Committed diagnostics show that Strategy B currently has a very small accepted sample and a large TP1/RR-related rejection footprint.

| diagnostic finding | committed value |
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
| rank-1 TP1 median R | 0.1714R |
| rank-1 TP1 values at or above 1.0R | 5 of 340 |
| low-rank-1 cases where any rank 2-5 reaches at least 1.0R | 76 of 335 |
| low-rank-1 cases still below 1.0R across ranks 2-5 | 259 of 335 |
| `stop_too_wide` cases where any rank 1-5 reaches at least 1.0R | 8 of 101 |
| manual-review base candidates selecting `current_rank1` | 22 of 30 |
| manual-review base candidates selecting `later_rank` | 2 of 30 |
| second-review `revise_to_later_rank_candidate` | 0 |

Interpretation:

- TP1 distance and TP1 minimum RR are the broadest documented rejection area.
- Stop width and TP1 RR strongly overlap in the committed diagnostics.
- ADX is visible but secondary in the current documented diagnostic set.
- Later ranks provide useful diagnostic context for a minority of candidates, but they do not provide an automatic replacement rule.
- The prior decision cycle froze current Strategy B behavior and did not approve any TP1, RR, stop, filter, management, Strategy B2, or implementation change.

These are aggregate committed findings only. This review does not create new diagnostics, generate candidate rows, or include raw candidate data.

## 5. TP1 selection versus TP1 minimum RR

The committed evidence supports separating four related but distinct issues.

| issue | current evidence | review assessment |
| --- | --- | --- |
| TP1 selection issue | Rank-1 TP1 is selected mechanically as the nearest eligible left-side swing target. Rank-1 TP1 median R is 0.1714R across 340 evaluable values. | Current selection is a mechanical proxy for structural target selection. Evidence supports reviewing whether the proxy is too local, but does not prove the rule is wrong. |
| TP1 minimum RR gate issue | `tp1_below_min_rr` appears in 335 of 371 rejected candidates and is the largest first-fail reason. | TP1 minimum RR is the direct rejection gate in many cases, but changing the threshold would be parameter work not authorized by this review. |
| Stop-to-TP geometry issue | All 101 `stop_too_wide` candidates also fail `tp1_below_min_rr`; only 8 of those have any rank 1-5 target at or above 1.0R. | Stop width and TP proximity appear to be a shared geometry symptom, not fully independent issues. This does not authorize stop changes. |
| Management dependency issue | Partial exit and break-even depend on TP1 being accepted and hit, but Strategy B requires TP1 RR before staged management can occur. | Management is downstream of TP1 acceptance. The mismatch context supports keeping management distinct from structural TP and RR thresholds. |

Committed evidence indicates that TP1 is often mechanically close relative to the current fixed RR gate. It does not establish that TP1 selection is categorically wrong, nor does it establish that TP1 minimum RR should be lowered, removed, or optimized.

Later TP ranks may help some cases. However, any rank 2-5 reaches 1.0R in 76 of 335 low-rank-1 cases, while 259 remain below 1.0R across ranks 2-5. This supports review and possible future human interpretation, not an automatic later-rank rule.

## 6. Stop interaction review

Current stop logic affects TP1 R because risk is the denominator in the TP1 R calculation.

Current stop mechanics:

- Long stop anchor uses a valid left-side swing low below the reference candle low when available, otherwise the reference candle low.
- Short stop anchor uses a valid left-side swing high above the reference candle high when available, otherwise the reference candle high.
- The ATR buffer is applied outside the stop anchor.
- The stop sanity gate rejects candidates below `0.25 * ATR(14)` or above `3.0 * ATR(14)`.

Why the overlap matters:

- `stop_too_wide` is recorded when risk exceeds the fixed maximum ATR multiple.
- `tp1_below_min_rr` is recorded when the selected TP1 is too close relative to that risk.
- The documented 101 of 101 overlap means wide-stop candidates also have insufficient TP1 RR in the all-failed-reason analysis.
- This suggests that stop width and TP1 target proximity are often a shared stop-to-TP geometry symptom.

What remains unknown from committed diagnostics only:

- Whether each wide stop is structurally valid, questionable, or not visually interpretable.
- Whether a given low-R TP1 is a meaningful structural target or a minor local swing.
- Whether some candidates should remain no-trade because valid stop and valid TP geometry cannot coexist.
- Whether the same pattern holds beyond the committed two-pair diagnostic set.

This review does not recommend stop-anchor, stop-buffer, stop-sanity, or RR-threshold changes.

## 7. TP1 structural target review

Current TP1 selection is clearly specified as nearest eligible left-side target selection in the Strategy B spec and implementation notes.

Review assessment:

- The rule is clear mechanically: long TP1 uses the nearest valid left-side swing high above entry; short TP1 uses the nearest valid left-side swing low below entry.
- Directionality handling appears symmetrical from committed docs and implementation: longs search above entry, shorts search below entry, and both use nearest-price ordering.
- The current rule is a proxy for structural target selection. It does not score target prominence, wave context, horizontal-line importance, channel/range boundary, liquidity-like level, or discretionary target realism.
- Diagnostics show that rank-1 TP1 is often close in R terms, but current docs do not prove the selected target is structurally invalid.
- Manual review evidence from the prior decision cycle weakens the case for replacing rank 1 wholesale because `current_rank1` was selected for 22 of 30 base candidates and second review produced no `revise_to_later_rank_candidate` result.

Conclusion: current TP1 selection should be classified as a `TP1 selection proxy limitation`, not as a confirmed implementation defect.

## 8. Relationship to Strategy A/B mismatch findings

PR #81 and PR #82 findings are context only.

| mismatch area | effect on this review |
| --- | --- |
| TP/RR and stop findings | Support reviewing Strategy B TP1 selection, TP1 minimum RR, and stop-to-TP geometry as distinct issues. They do not authorize any change. |
| EMA/reference-candle findings | Remain no-change. This review does not reopen the Strategy A/B entry identity. |
| ADX range proxy | ADX remains a known proxy limitation. The committed diagnostics also show ADX is not the primary current rejection driver. No ADX change is recommended. |
| Breakout, damashi, sweep, and false-break | Remain unresolved and discretionary. They should not be imported into TP1 selection review without a separately approved protocol. |
| Wave context | Remains broader and more discretionary than Strategy B. No wave-count logic is recommended. |
| Discretionary management and psychology | Supports keeping partial exit, break-even, protective exit, and trader tolerance distinct. No management change is recommended. |
| Doctrine Map v2 draft proposal | Remains non-final and must not be treated as Strategy requirements. |

The mismatch findings support a human-readable review of current TP1 behavior. They do not convert Doctrine Map v2 draft candidates into Strategy B requirements.

## 9. Classification of findings

| issue | classification | rationale |
| --- | --- | --- |
| Current TP1 target selection | TP1 selection proxy limitation | Nearest-left-side-fractal behavior is clear and deterministic but narrower than structural chart judgment. |
| TP1 specification clarity | no TP1 selection issue found | The basic TP1/TP2 target ordering is documented and tested. |
| Structural meaning of rank-1 target | insufficient committed evidence | Aggregate docs do not include raw candidate rows or chart-level structure needed to decide each case. |
| TP1 minimum RR rejection | TP1 minimum RR gate issue candidate | `tp1_below_min_rr` dominates first-fail and all-failed diagnostics, but no threshold change is authorized. |
| Stop and TP1 overlap | stop-to-TP geometry issue candidate | `stop_too_wide` and `tp1_below_min_rr` overlap completely in the committed all-failed analysis for stop-too-wide candidates. |
| Later-rank target evidence | insufficient committed evidence | Later ranks help a minority but do not identify a deterministic replacement rule. |
| Implementation/spec mismatch | insufficient committed evidence | Current implementation appears aligned with the documented fixed Strategy B spec; broader doctrine mismatch remains non-final context. |
| ADX role | no TP1 selection issue found | ADX is secondary in current diagnostics and should stay outside TP1 change discussion. |
| Prior TP1 decision closure | prior closure still controls | The closure note freezes TP1, RR, stop, filter, management, and Strategy B2 changes. |
| New diagnostics need | out of scope until separately approved diagnostics | Any candidate-level or chart-level review would require separate planning and artifact guardrails. |

No finding is classified as requiring code change.

## 10. Review table

| review row | evidence source | finding | classification | confidence from committed docs | safe recommendation | new diagnostics needed? | change authorized? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Current TP1 candidate selection | Strategy B spec, implementation notes, implementation, prior TP1 review | TP1 is the first ordered eligible left-side target beyond entry. | TP1 selection proxy limitation | high | document as known limitation | no for current behavior summary; yes for chart-level validity | no |
| TP1 versus TP2 distinction | Strategy B spec, implementation notes, tests | TP1 is rank 1; TP2 is rank 2 when present. | no TP1 selection issue found | high | no change | no | no |
| TP1 minimum RR calculation | Strategy B spec, validation, implementation | TP1 R is target distance divided by entry-to-stop risk; fixed TP1 minimum is `1.0R`. | TP1 minimum RR gate issue candidate | high | later specification review only | no for current summary; yes for any replacement threshold | no |
| TP1 rejection path | Filter funnel, candidate export notes, candidate export analysis | `tp1_below_min_rr` is the largest first-fail reason and appears in 335 rejected candidates as all-failed evidence. | TP1 minimum RR gate issue candidate | high | document as known limitation | no | no |
| Stop-to-TP geometry | Candidate export analysis, TP candidate diagnostics analysis | All `stop_too_wide` candidates also fail TP1 RR; most have no rank 1-5 target at or above 1.0R. | stop-to-TP geometry issue candidate | high | later specification review only | yes for stop validity classification | no |
| Rank-1 TP1 behavior | Candidate export analysis, prior TP1 review | Rank-1 median TP1 R is 0.1714R; only 5 of 340 reach at least 1.0R. | TP1 selection proxy limitation | high | document as known limitation | yes for structural plausibility | no |
| Rank 2-5 TP candidate diagnostics | TP candidate diagnostics analysis | Later ranks help a minority; 259 of 335 low-rank-1 cases remain below 1.0R across ranks 2-5. | insufficient committed evidence | high | insufficient evidence | yes for human structural labels | no |
| ADX versus TP1 rejection | Candidate export analysis, mismatch human review | ADX affects 25 rejected candidates; 20 also fail TP1 RR. ADX is not the primary TP1 issue. | no TP1 selection issue found | high | no change | no | no |
| Partial exit / break-even dependency | Strategy B spec, implementation notes, mismatch re-check | Partial exit and break-even depend on TP1 but should not be collapsed into TP selection or RR threshold. | documentation ambiguity | medium | document as known limitation | no | no |
| Prior closure state | TP1 decision memo, TP1 closure note | Current rank-1 TP1, RR, stop, ADX, management, and Strategy B2 remain frozen. | prior closure still controls | high | keep prior closure controlling | no | no |

## 11. Safe recommendations

Safe recommendations from this review:

- no change to Strategy B TP1 selection;
- no change to Strategy B TP2 selection;
- no change to TP1, TP2, or TP1-only RR rules;
- no change to stop anchors, stop buffers, or stop sanity limits;
- no change to ADX or other filters;
- no change to partial exit, break-even, or management rules;
- document current TP1 selection as a known mechanical proxy limitation;
- document TP1 minimum RR and stop-to-TP geometry as candidate specification-review topics only;
- keep the prior TP1 decision closure controlling;
- treat later diagnostics as requiring separate planning and approval;
- keep all raw candidate, market, data, result, and backtest artifacts out of Git.

No immediate Strategy B implementation change is recommended.

## 12. Unknowns and diagnostic needs

The following cannot be resolved from committed docs alone:

- candidate-level structural plausibility without raw candidate rows or chart-level review;
- whether rejected candidates visually had meaningful later targets;
- whether TP1 target choice differs materially by direction beyond the current symmetrical rule;
- whether stop-to-TP geometry is caused mainly by stop width, TP proximity, or both in individual cases;
- whether a low-R rank-1 target is structurally valid, minor/noisy, or not a valid target;
- whether no-left-side-target and no-valid-target cases remain stable in a broader fixed sample;
- whether the two-pair diagnostic pattern holds in any separately approved future dataset or review scope.

If new diagnostics would be useful, a separate planning PR is required before generating any artifact. That planning PR must define scope, artifact location, ignored-file handling, aggregate-only committed output, and explicit no-backtest/no-optimization/no-profitability guardrails.

## 13. Decision and readiness

Decision:

`strategy_b_tp1_selection_review_completed_docs_only_no_change`

Reason: committed docs are sufficient to document current Strategy B TP1 behavior, identify TP1 selection as a mechanical proxy limitation, identify TP1 minimum RR and stop-to-TP geometry as candidate review areas, and preserve prior closure as the controlling non-change decision. The same evidence is not sufficient to approve any TP1, TP2, RR, stop, filter, management, Strategy B2, Strategy C, code, config, parameter, test, backtest, or optimization change.

This review does not state that Strategy B should change. It does not state that TP1 selection is wrong. It does not state that TP1 selection is correct. It makes no profitability claim.

## 14. Recommended next PR

Recommended next docs-only PR:

`Strategy B TP1 selection human review`

Reason:

- The current review consolidates enough committed evidence for human decision context.
- The human review should decide whether the current no-change decision and prior closure remain sufficient after the PR #81/#82 mismatch context.
- The human review should not modify Strategy B rules, parameters, code, configs, or tests.
- The human review should not run backtests, optimization, market data access, or diagnostics generation.
- The human review should decide whether to keep closure controlling, request a separate diagnostic planning PR, or request a later specification review plan.

If the human reviewer decides committed evidence is insufficient for the next decision, the next step after human review should be `Strategy B TP1 diagnostic planning`, not implementation.
