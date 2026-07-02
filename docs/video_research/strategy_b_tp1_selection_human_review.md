# Strategy B TP1 Selection Human Review

Task: `strategy_b_tp1_selection_human_review`

Review date: 2026-07-01

## 1. Objective and scope

This is a docs-only human-review-style assessment of the current Strategy B TP1 selection review in `docs/video_research/strategy_b_tp1_selection_review_current.md`.

This human review:

- Reviews whether the current TP1 selection review is conservative, traceable, and bounded.
- Reviews whether the current review correctly documents Strategy B TP1/TP2 behavior.
- Reviews whether the current review preserves prior Strategy B TP1 closure.
- Selects a next docs-only decision path.

This human review does not:

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
- Authorize implementation changes.

## 2. Evidence base reviewed

This review uses only committed evidence and read-only repository context.

Primary reviewed docs:

- `docs/video_research/strategy_b_tp1_selection_review_current.md`
- `docs/video_research/strategy_b_tp1_selection_review_current_review.md`
- `docs/video_research/strategy_b_tp1_selection_review_plan.md`
- `docs/video_research/strategy_b_tp1_selection_review_plan_review.md`

Strategy B evidence reviewed:

- `docs/video_research/vkaA9MCRlx4/strategy_b_spec_design.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_implementation_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_readonly_validation_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_filter_funnel_diagnostics.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_candidate_export_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_candidate_export_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_memo.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`

Doctrine and mismatch context reviewed as non-final context:

- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_human_review.md`
- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal_human_review.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal.md`
- `docs/video_research/doctrine_map_v2_candidate_review.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`

Strategy B implementation and tests were inspected read-only where needed:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`
- `tests/test_ema_wave3_strategy_b.py`
- `tests/test_strategy_b_runner.py`

Aggregate values carried forward from committed docs only:

| evidence item | committed value |
| --- | ---: |
| confirmation candidates | 373 |
| accepted candidates | 2 |
| rejected candidates | 371 |
| `tp1_below_min_rr` all-failed-reason count | 335 of 371 rejected candidates |
| `tp1_below_min_rr` first-fail count | 218 |
| `stop_too_wide` all-failed-reason count | 101 |
| `stop_too_wide` candidates also failing `tp1_below_min_rr` | 101 of 101 |
| ADX all-failed-reason count | 25 |
| ADX failures also failing TP1 minimum RR | 20 of 25 |
| rank-1 TP1 evaluable candidates | 340 |
| rank-1 TP1 median R | 0.1714R |
| rank-1 TP1 values at or above 1.0R | 5 of 340 |
| any rank 2-5 reaches at least 1.0R in low-rank-1 cases | 76 of 335 |
| low-rank-1 cases still below 1.0R across ranks 2-5 | 259 of 335 |
| manual-review base candidates selecting `current_rank1` | 22 of 30 |
| manual-review base candidates selecting `later_rank` | 2 of 30 |
| second-review `revise_to_later_rank_candidate` | 0 |

No new numbers are introduced by this review.

## 3. Review questions

| review question | assessment |
| --- | --- |
| Does the current Strategy B TP1 selection review correctly remain docs-only? | Yes. It documents current behavior, diagnostics, classifications, unknowns, and recommendations only. |
| Does it correctly document current TP1 and TP2 behavior? | Yes. It describes the rank-1 TP1 and rank-2 TP2 model, directionality, left-side swing validity, RR thresholds, stop interaction, and management dependency. |
| Does it correctly separate TP1 selection, TP1 minimum RR, stop-to-TP geometry, and management dependency? | Yes. The review keeps these as separate issue families and does not collapse them into one rule-change request. |
| Does it correctly treat current TP1 selection as a mechanical proxy limitation rather than a confirmed defect? | Yes. The review notes that nearest-left-side-fractal selection is narrower than structural judgment, but does not claim it is wrong. |
| Does it correctly treat TP1 minimum RR as a gate issue candidate without authorizing threshold change? | Yes. It identifies the gate's diagnostic footprint while preserving no-change guardrails. |
| Does it correctly treat stop-to-TP geometry as a candidate review area without authorizing stop changes? | Yes. It recognizes the stop/RR overlap but does not recommend stop-anchor, buffer, or sanity-limit changes. |
| Does it correctly keep ADX secondary and outside the TP1 change discussion? | Yes. It preserves ADX as a known proxy limitation and notes that ADX is not the main documented blocker. |
| Does it correctly preserve prior TP1 decision closure as controlling? | Yes. It keeps current rank-1 TP1, RR, stop, ADX, management, and Strategy B2 frozen. |
| Does it correctly identify unknowns that require separate diagnostic planning? | Yes. It lists chart-level and candidate-level unknowns without generating artifacts. |
| Does it correctly avoid implementation, backtest, optimization, market data, and profitability claims? | Yes. It authorizes none of those actions. |

Overall assessment: the current Strategy B TP1 selection review is conservative enough to use as decision context for this human-review step.

## 4. Finding-by-finding human review

| finding from current review | classification appropriate? | confidence appropriate? | safe recommendation appropriate? | new diagnostics needed before stronger conclusion? | implementation-change risk | disposition |
| --- | --- | --- | --- | --- | --- | --- |
| current TP1 candidate selection | Yes. `TP1 selection proxy limitation` is appropriate because current TP1 is deterministic nearest-left-side-fractal selection, not full structural judgment. | Yes. High confidence is appropriate for current behavior; structural validity remains lower because raw/chart evidence is absent. | Yes. `document as known limitation` is safe. | Yes, for chart-level target validity or any replacement rule. | Medium if converted directly into a target-ranking change. | accept |
| TP1 versus TP2 distinction | Yes. `no TP1 selection issue found` is appropriate for the documented rank-1/rank-2 distinction. | Yes. High confidence is supported by spec, implementation notes, implementation, and tests. | Yes. `no change` is safe. | No for current behavior. | Low if kept as documentation; high if used to alter target ordering. | accept |
| TP1 minimum RR calculation | Yes. `TP1 minimum RR gate issue candidate` is appropriate because the fixed gate has a large diagnostic footprint. | Yes. High confidence is appropriate for the current calculation and thresholds. | Yes. `later specification review only` avoids threshold tuning. | Yes, before any threshold or contextual-RR proposal. | High because RR thresholds are easy to tune. | accept |
| TP1 rejection path | Yes. `TP1 minimum RR gate issue candidate` is appropriate. | Yes. High confidence is supported by first-fail and all-failed counts. | Yes. `document as known limitation` is safe. | No for documenting the current rejection path; yes for cause-by-candidate diagnosis. | High if used to lower or remove TP1 RR. | accept |
| stop-to-TP geometry | Yes. `stop-to-TP geometry issue candidate` is appropriate because stop width and TP1 RR overlap strongly. | Yes. High confidence is appropriate for aggregate overlap; lower confidence remains for visual stop validity. | Yes. `later specification review only` is conservative. | Yes, before any stop-anchor or stop-width change. | High because stop changes can reshape risk and invalidate premise logic. | accept |
| rank-1 TP1 behavior | Yes. `TP1 selection proxy limitation` is appropriate. | Yes. High confidence is appropriate for rank-1 R distribution. | Yes. `document as known limitation` is safe. | Yes, for deciding whether rank 1 is structurally valid or too local in individual cases. | Medium to high if converted into a farther-target rule. | accept |
| rank 2-5 TP candidate diagnostics | Yes. `insufficient committed evidence` is appropriate because later ranks help a minority but do not specify a replacement rule. | Yes. High confidence is appropriate for aggregate diagnostic values, not for structural conclusions. | Yes. `insufficient evidence` is safe. | Yes, before any rank-selection proposal. | High if used as an automatic rank 2-5 switch. | accept |
| ADX versus TP1 rejection | Yes. `no TP1 selection issue found` is appropriate for ADX staying out of TP1 change discussion. | Yes. High confidence is supported by committed counts. | Yes. `no change` is safe. | No for current human-review decision. | Medium if ADX tuning is inferred incorrectly. | accept |
| partial exit / break-even dependency | Yes. `documentation ambiguity` is acceptable because management depends on TP1 but should remain distinct from TP selection and RR threshold. | Yes. Medium confidence is appropriate because management doctrine remains less directly specified. | Yes. `document as known limitation` is safe. | No for current documentation; yes before any management redesign. | Medium if partial exit or break-even is changed without separate approval. | accept |
| prior closure state | Yes. `prior closure still controls` is appropriate. | Yes. High confidence is supported by the decision memo and closure note. | Yes. `keep prior closure controlling` is the safest recommendation. | No before continuing documentation work. | Low if respected; high if skipped to implementation. | accept |

No finding requires revision before this human-review decision.

## 5. Decision review

Reviewed current decision:

`strategy_b_tp1_selection_review_completed_docs_only_no_change`

Assessment:

- Committed docs are sufficient to document current Strategy B TP1 and TP2 behavior.
- Committed docs are sufficient to identify current TP1 selection as a mechanical proxy limitation.
- Committed docs are sufficient to identify TP1 minimum RR and stop-to-TP geometry as candidate review areas.
- Committed docs are sufficient to keep ADX secondary in the current TP1 decision.
- Committed docs are sufficient to preserve prior closure as the controlling non-change decision.
- Committed docs are not sufficient to approve Strategy B changes.
- Committed docs are not sufficient to approve TP1, TP2, RR, stop, filter, or management changes.
- Committed docs are not sufficient to create Strategy B2 or Strategy C.
- Committed docs are not sufficient to run backtests, optimization, diagnostics generation, or market-data work.

The reviewed decision is appropriate.

## 6. Decision options

Available decisions:

- `strategy_b_tp1_selection_human_review_keep_prior_closure`
- `strategy_b_tp1_selection_human_review_request_diagnostic_planning`
- `strategy_b_tp1_selection_human_review_request_spec_review_plan`
- `strategy_b_tp1_selection_human_review_requires_revision`

Decision:

`strategy_b_tp1_selection_human_review_keep_prior_closure`

Reason: current committed evidence supports no Strategy B change and supports keeping the prior TP1 decision closure controlling. PR #84 correctly documents current behavior and review areas, but it does not introduce evidence strong enough to reopen diagnostics, specification work, or implementation by default. Diagnostic planning and specification review remain possible only through separate explicit approval if the project owner decides to continue that line later.

This decision does not authorize implementation changes.

## 7. Recommended next PR

Recommended next docs-only PR:

`Strategy B TP1 decision reaffirmation`

Reason:

- PR #84 documents current behavior and preserves no-change.
- This human review accepts PR #84's classifications and safe recommendations.
- The prior TP1 decision closure remains controlling.
- A decision reaffirmation can state that current TP1, TP2, RR, stop, filter, management, ADX, and Strategy B2 status remain frozen.
- A decision reaffirmation can clearly state what would be required to reopen TP1 diagnostics or specification work.
- It should not modify Strategy B, run backtests, generate diagnostics, access market data, or create Strategy B2/C.

If a later project-owner decision requests more evidence, the appropriate separate path would be `Strategy B TP1 diagnostic planning`. That path is not authorized by this human review.

## 8. Guardrails

This human review does not:

- modify Strategy B;
- modify TP1, TP2, RR, stop, filter, or management rules;
- modify code, parameters, configs, or tests;
- create Strategy B2 or Strategy C;
- run backtests;
- run optimization;
- claim profitability;
- access market data;
- fetch market data;
- use broker APIs or live execution logic;
- add raw candidate rows, generated CSV, data, results, raw market data, normalized market data, or backtest output;
- include Batch 08;
- access DownSub or YouTube;
- fetch captions;
- download video or audio;
- run ASR;
- add raw subtitle material or caption URLs;
- update `docs/video_research/channel_doctrine_map_v1.md`;
- create or update `docs/video_research/channel_doctrine_map_v2.md`;
- treat Doctrine Map v2 draft proposal as final doctrine.

## 9. Readiness decision

Decision:

`strategy_b_tp1_selection_human_review_ready_for_human_review`

Reason: this docs-only human-review-style assessment accepts the current Strategy B TP1 selection review as conservative, traceable, Strategy-safe, Doctrine-safe, Batch 08-safe, artifact-safe, market-data-safe, and implementation-change-safe. It keeps prior TP1 closure controlling, recommends only a docs-only decision reaffirmation, and authorizes no Strategy B change.

This review does not state that Strategy B should change. It does not state that TP1 selection is wrong. It does not state that TP1 selection is correct. It does not state that Doctrine Map v2 is final. It makes no profitability claim.
