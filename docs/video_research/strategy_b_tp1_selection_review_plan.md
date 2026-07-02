# Strategy B TP1 Selection Review Plan

Task: `strategy_b_tp1_selection_review_plan`

Plan date: 2026-07-01

## 1. Objective and scope

This is a docs-only plan to review Strategy B TP1 selection.

This plan:

- Defines the scope, questions, classifications, outputs, and guardrails for a future Strategy B TP1 selection review.
- Uses only existing committed docs and repository context.
- Uses the Doctrine Map v2 draft proposal and Strategy A/B mismatch findings only as context, not as final or accepted doctrine.
- Preserves the prior Strategy B TP1 decision cycle as non-change evidence unless a later separately approved review finds otherwise.

This plan does not:

- Change Strategy B.
- Modify Strategy B TP1 selection logic.
- Modify Strategy B RR rules.
- Modify Strategy B stop logic.
- Modify Strategy B filters.
- Modify Strategy A/B code, parameters, configs, or tests.
- Run backtests or optimization.
- Access market data or fetch market data.
- Use broker APIs.
- Add broker, live trading, or execution logic.
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
- Commit raw TXT, SRT, VTT, subtitle full text, caption URLs, CSV, JSON, database, `data/`, or `results/` artifacts.

## 2. Evidence base

The future review should use only committed evidence and read-only repository context.

Primary planning context:

- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_human_review.md`
- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck.md`
- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_plan.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal_human_review.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal.md`
- `docs/video_research/doctrine_map_v2_candidate_review.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`

Strategy B context to inspect read-only:

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
- Existing Strategy B implementation and tests read-only only.

Known committed research findings to carry forward without inventing new numbers:

| finding | committed source context |
| --- | --- |
| Strategy B validation reduced USDJPY from 195 Strategy A RR1.5 reference trades to 1 Strategy B accepted trade, and EURUSD from 178 to 1. | Strategy B read-only validation report. |
| Strategy B candidate export analysis records 373 confirmation candidates, 2 accepted candidates, and 371 rejected candidates. | Strategy B candidate export analysis and prior TP1 selection review. |
| `tp1_below_min_rr` is the broadest recorded failure: 335 of 371 rejected candidates in all-failed-reason analysis. | Strategy B candidate export analysis. |
| `tp1_below_min_rr` is also the largest first-fail reason: 218 of 373 candidates, or 58.4% of all candidates. | Strategy B candidate export analysis. |
| `stop_too_wide` overlaps with `tp1_below_min_rr`: all 101 `stop_too_wide` candidates also fail `tp1_below_min_rr`. | Strategy B candidate export analysis. |
| ADX is not the primary rejection driver: 25 rejected candidates fail ADX, and 20 of those also fail TP1 minimum RR. | Strategy B candidate export analysis. |
| Among 340 evaluable rank-1 TP1 values, only 5 reach at least 1.0R and the median rank-1 TP1 distance is 0.1714R. | Strategy B candidate export analysis and TP candidate diagnostics analysis. |
| Later ranks provide diagnostic information but not an automatic fix: any rank 2-5 reaches at least 1.0R in 76 of 335 low-rank-1 cases, while 259 remain below 1.0R. | Strategy B TP candidate diagnostics analysis. |
| A prior TP1 decision cycle closed with no Strategy B TP1, RR, stop, filter, management, or Strategy B2 change approved. | Strategy B TP1 decision closure note. |

These findings are diagnostic context only. They are not profitability evidence and do not authorize Strategy B changes.

## 3. Current problem statement

Strategy B appears over-constrained around TP1 selection and/or TP1 minimum RR. The future review should determine whether current TP1 selection behavior is aligned with the intended Strategy B specification and the committed video-derived context.

The future review should not assume that TP1 logic is wrong.

The future review should not assume that the solution is changing RR, stop width, TP selection, ADX, filters, or parameters.

The review should separate at least four concepts:

| concept | why it must stay separate |
| --- | --- |
| TP1 selection | Which structural target Strategy B selects as TP1. |
| TP1 minimum RR | Whether the selected TP1 clears the fixed RR gate. |
| Stop placement and stop width | Whether the risk denominator makes the selected TP1 fail RR, and whether the stop is structurally valid. |
| Management rules | Whether partial exit and break-even after TP1 are being confused with entry acceptance. |

The prior TP1 decision closure note froze current Strategy B behavior. This plan does not reopen implementation. It only defines a docs-only review path for assessing whether the mismatch findings and existing TP diagnostics warrant future specification discussion.

## 4. Read-only map of current Strategy B TP1 logic

The future review should document the current TP1 mechanism without changing it.

| map item | planned review question | expected source |
| --- | --- | --- |
| TP1 candidate selection | How is the current TP1 candidate selected after confirmation? | Strategy B spec, implementation notes, implementation code, tests, prior TP1 review. |
| Structural target definition | What left-side swing or structural target definition is used, and what is explicitly specified versus inferred from code? | Strategy B spec and implementation. |
| Directionality | For long and short candidates, how are eligible swing highs or lows chosen and ordered? | Strategy B implementation notes and tests. |
| TP1 versus TP2 | How does Strategy B distinguish nearest TP1 from second target TP2, and what happens when TP2 is absent? | Strategy B spec, implementation notes, candidate export notes. |
| TP1 minimum RR | How is TP1 R computed, what fixed threshold is applied, and when does `tp1_below_min_rr` arise? | Strategy B spec, validation, filter funnel, candidate export notes. |
| Stop interaction | How does stop placement affect TP1 R and how do `stop_too_wide` and `tp1_below_min_rr` overlap? | Candidate export analysis and TP candidate diagnostics analysis. |
| Partial exit and break-even | How do partial exit and break-even depend on TP1, and are they entry-acceptance requirements or management after acceptance? | Strategy B spec, implementation notes, mismatch re-check. |
| Rejection pathways | Which TP1-related rejection reasons can arise, and which are first-fail versus all-failed diagnostics? | Filter funnel diagnostics and candidate export notes. |
| Prior closure state | Which TP1, RR, stop, ADX, and Strategy B2 items were frozen by the prior decision cycle? | TP1 decision closure note. |

This section is a future review plan only. It does not change TP1, TP2, RR, stops, filters, or management.

## 5. Review questions

The future Strategy B TP1 selection review should answer:

- Is current TP1 selection selecting the intended structural target?
- Is TP1 too close because the selected swing is mechanically nearest rather than meaningfully structural?
- Is TP1 minimum RR rejecting candidates because TP1 is too close, stop is too wide, or both?
- Are `tp1_below_min_rr` and `stop_too_wide` independent issues or mostly overlapping symptoms?
- Does TP1 selection collapse separate concepts from the mismatch review, such as structural TP, RR threshold, staged management, and trader tolerance?
- Does the current TP1 rule accidentally encode a stricter rule than the original Strategy B spec intended?
- Does TP1 selection differ between long and short candidates in any systematic way?
- Are there candidates that look structurally plausible but fail only due to TP1 minimum RR?
- Are there candidates with valid TP1 structure but invalid stop-to-target geometry?
- Is the current TP1 selection reviewable from committed diagnostics only, or would a later diagnostic export be needed?
- Which conclusions can be made from existing docs, and which must remain unknown without new diagnostics?
- Does the prior TP1 closure note remain sufficient after the PR #81 and PR #82 mismatch findings, or does it only need a docs-only reaffirmation?

## 6. Classification framework

The future review should use conservative review classifications. No classification should be phrased as requiring a code change.

| classification | use |
| --- | --- |
| no TP1 selection issue found | Existing committed evidence does not show a TP1 selection concern beyond known Strategy B simplification. |
| documentation ambiguity | The docs do not clearly explain TP1 selection, but the issue is documentation only. |
| specification ambiguity | The intended Strategy B spec is not precise enough to decide whether the implementation is aligned. |
| implementation/spec mismatch candidate | Committed evidence suggests a possible difference between spec wording and implemented behavior, but it remains a candidate only. |
| TP1 selection proxy limitation | Current nearest-left-side-fractal behavior is a known proxy for broader structural target judgment. |
| TP1 minimum RR gate issue candidate | Evidence suggests the fixed TP1 RR gate may deserve later spec discussion, without changing it now. |
| stop-to-TP geometry issue candidate | Evidence suggests stop placement and target distance interact, without approving stop or RR changes. |
| prior closure still controls | The prior TP1 decision closure remains the controlling non-change decision. |
| insufficient committed evidence | Existing docs do not support a conclusion. |
| out of scope until separately approved diagnostics | A conclusion would require new diagnostics, generated artifacts, market data access, backtests, or implementation work. |

The future review should not classify any item as "change Strategy B", "tune parameter", "implement Strategy B2", or "run backtest".

## 7. Planned review outputs

A later actual Strategy B TP1 selection review should output:

- Current TP1 logic summary.
- TP1-related rejection pathway map.
- Table of TP1 selection assumptions.
- Table separating TP1 selection from TP1 minimum RR.
- Table separating TP1-related issues from stop-related issues.
- Table separating TP1-related issues from ADX or broader range-filter issues.
- Known evidence from committed diagnostics.
- How PR #81 and PR #82 mismatch findings affect TP1 review context.
- Unknowns that require future diagnostics.
- Conservative no-change, defer, documentation-only, or specification-review-only recommendations.
- Explicit statement that no Strategy B modification is authorized.

The future review must not output raw candidate rows, raw CSV, generated CSV, database files, data files, result files, market data, chart images, subtitle text, caption URLs, or backtest output.

## 8. Data and artifact guardrails

This plan and any future TP1 selection review under this plan must keep artifacts Git-safe.

Disallowed artifacts:

- Raw candidate CSV.
- Generated candidate CSV.
- Raw market CSV.
- Normalized market CSV.
- Database files.
- `data/` directory artifacts.
- `results/` directory artifacts.
- Backtest output.
- Transcript or subtitle full text.
- Caption URLs.
- Video or audio files.
- ASR output.

Disallowed actions:

- Market data access or market data fetch.
- Broker API use.
- Live trading, order execution, or execution logic.
- Backtests.
- Optimization.
- Parameter tuning.
- Strategy A/B code, config, parameter, or test changes.
- Strategy B TP1, RR, stop, filter, or management changes.
- Strategy B2 or Strategy C creation.
- Batch 08 inclusion.

The plan may reference aggregate values already committed in docs. It must not generate or commit new data artifacts.

## 9. Relationship to mismatch findings

PR #81 and PR #82 findings should be used as context only.

| mismatch area | use in future TP1 review |
| --- | --- |
| TP, exit, and RR | Use as context that Strategy B combines structural TP, RR gates, partial exit, and break-even. Do not treat this as approval to change TP or RR. |
| Stop placement and invalidation | Use as context that stop-anchor validity and stop-width tolerance should stay separate. Do not change stop anchors, buffers, or sanity gates. |
| EMA/reference-candle | Preserve no-change handling. The TP1 review should not reopen Strategy A/B entry identity. |
| ADX range proxy | Keep ADX as a known proxy limitation. Do not change ADX in this task. |
| Breakout, damashi, sweep, false-break | Keep unresolved. Do not import these discretionary concepts into TP1 review unless a later manual-review protocol is separately approved. |
| Wave context | Keep unresolved and broader than current Strategy B. Do not add wave-count logic. |
| Discretionary management | Use only to keep partial exit, break-even, protective exit, and trader tolerance distinct. Do not change management rules. |

The future Strategy B TP1 selection review should not automatically inherit all Doctrine Map v2 draft candidates. The Doctrine Map v2 draft proposal is non-final and does not authorize Strategy changes.

## 10. Guardrails for future work after the plan

Any future Strategy B TP1 selection review must not:

- Modify Strategy B.
- Modify Strategy A/B code, parameters, configs, or tests.
- Modify TP1 or TP2 selection.
- Modify TP1, TP2, or TP1-only RR thresholds.
- Modify stop anchors, stop buffers, or stop sanity gates.
- Modify ADX, range filters, or other filters.
- Modify partial exit, break-even, or management rules.
- Tune parameters.
- Run backtests.
- Run optimization.
- Create Strategy B2 or Strategy C.
- Claim profitability.
- Access market data.
- Use broker APIs, live trading, order execution, or execution logic.
- Add raw subtitle, raw market, raw candidate, data, or result artifacts.
- Include Batch 08.
- Treat Doctrine Map v2 draft proposal as final doctrine.

If a future review needs new diagnostics, that must be separately approved and must define exactly what artifacts are generated, whether they remain ignored, and what aggregate docs-only output may be committed.

## 11. Decision gates after the future review

After the future review, no Strategy B change should proceed unless all required gates are passed.

| gate | required before |
| --- | --- |
| Human review of TP1 selection findings | Treating the future TP1 review as decision context. |
| Separate approval for any Strategy B spec change | Editing Strategy B specification, TP1 assumptions, RR assumptions, stop assumptions, or management assumptions. |
| Separate approval for any code, config, parameter, or test change | Modifying implementation or test behavior. |
| Separate approval for any new diagnostic export | Generating or analyzing new candidate or TP diagnostic artifacts. |
| Separate approval for any backtest | Running Strategy A/B or any variant against market data. |
| Separate approval for Strategy B2 or Strategy C | Creating any new strategy variant. |
| Separate approval for Doctrine Map v2 finalization | Treating draft doctrine as final or accepted. |

No parameter optimization should be performed under this plan.

## 12. Recommended next PR after this plan

Recommended next docs-only PR:

`Strategy B TP1 selection review`

Reason:

- This plan defines review scope, questions, conservative classifications, expected outputs, and guardrails.
- The Strategy A/B mismatch re-check human review recommends TP1 selection work as a future docs-only planning step.
- Existing committed Strategy B diagnostics identify TP1 selection, TP1 minimum RR, and stop-to-TP geometry as the main research area.
- The next PR should perform the docs-only TP1 selection review without modifying Strategy B rules, parameters, code, configs, or tests.
- The next PR should still not run backtests or optimization.

The next PR should explicitly state that Strategy B remains unchanged and that any later implementation, diagnostics, or backtest work requires separate approval.

## 13. Readiness decision

Decision:

`strategy_b_tp1_selection_review_plan_ready_for_human_review`

Reason: this docs-only plan defines a conservative review path for Strategy B TP1 selection using only committed evidence and read-only repository context. It records known Strategy B TP1, stop, RR, and ADX diagnostic findings without inventing new numbers, treats PR #81 and PR #82 mismatch findings as context only, preserves the non-final status of the Doctrine Map v2 draft proposal, excludes Batch 08, and does not authorize Strategy B changes, Strategy B2, Strategy C, backtests, optimization, market-data access, broker logic, or profitability claims.

This plan does not state that Strategy B should change. It does not state that TP1 selection is wrong. It does not state that Doctrine Map v2 is final.
