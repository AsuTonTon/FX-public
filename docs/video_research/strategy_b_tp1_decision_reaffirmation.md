# Strategy B TP1 Decision Reaffirmation

Task: `strategy_b_tp1_decision_reaffirmation`

Review date: 2026-07-01

## 1. Objective and scope

This is a docs-only decision reaffirmation for the Strategy B TP1 selection review cycle merged through PR #85.

This reaffirmation:

- Reaffirms the PR #85 human-review decision: `strategy_b_tp1_selection_human_review_keep_prior_closure`.
- Keeps the prior Strategy B TP1 decision closure controlling.
- Freezes current Strategy B TP1, TP2, RR, stop, filter, management, implementation, and Strategy B2 status.
- Defines what would be required to reopen any TP1 diagnostic, specification, implementation, Strategy B2, backtest, or market-data path later.
- Uses committed repository docs only.

This reaffirmation does not:

- Modify Strategy A/B code, parameters, configs, or tests.
- Modify Strategy B TP1 selection logic.
- Modify Strategy B TP2 selection logic.
- Modify Strategy B TP1, TP2, or TP1-only RR thresholds.
- Modify Strategy B stop anchors, stop buffers, or stop sanity gates.
- Modify Strategy B ADX or other filters.
- Modify Strategy B partial-exit, break-even, or management logic.
- Create Strategy B2 or Strategy C.
- Run backtests or optimization.
- Generate diagnostics.
- Access market data or fetch market data.
- Use broker APIs or live execution logic.
- Make profitability claims.
- Update `docs/video_research/channel_doctrine_map_v1.md`.
- Create or finalize `docs/video_research/channel_doctrine_map_v2.md`.
- Treat the Doctrine Map v2 draft proposal as final doctrine.
- Include Batch 08.
- Access DownSub or YouTube.
- Fetch captions.
- Download video or audio.
- Run ASR.
- Use proxies, VPN rotation, IP rotation, or platform-rate-limit bypass.
- Commit raw TXT, SRT, VTT, subtitle full text, caption URLs, CSV, JSON, database, raw candidate rows, generated candidate CSV, raw market CSV, normalized market CSV, `data/`, `results/`, or backtest-output artifacts.

## 2. Evidence base

This reaffirmation uses only committed docs and read-only repository context. It introduces no new diagnostics, raw rows, market data, or generated artifacts.

Primary decision documents:

- `docs/video_research/strategy_b_tp1_selection_human_review.md`
- `docs/video_research/strategy_b_tp1_selection_human_review_review.md`
- `docs/video_research/strategy_b_tp1_selection_review_current.md`
- `docs/video_research/strategy_b_tp1_selection_review_current_review.md`
- `docs/video_research/strategy_b_tp1_selection_review_plan.md`
- `docs/video_research/strategy_b_tp1_selection_review_plan_review.md`

Strategy B supporting documents:

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

Doctrine and mismatch context used as non-final context only:

- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_human_review.md`
- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal_human_review.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal.md`
- `docs/video_research/doctrine_map_v2_candidate_review.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`

Implementation and tests remain read-only context only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`
- `tests/test_ema_wave3_strategy_b.py`
- `tests/test_strategy_b_runner.py`

Committed aggregate values carried forward:

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

No new numbers are introduced by this reaffirmation.

## 3. Reaffirmed decision

Reaffirmed decision:

`strategy_b_tp1_selection_human_review_keep_prior_closure`

The following remain unchanged:

- Current Strategy B TP1 selection.
- Current Strategy B TP2 selection.
- Current Strategy B TP1 minimum RR.
- Current Strategy B TP2 minimum RR.
- Current Strategy B TP1-only minimum RR.
- Current Strategy B stop anchors.
- Current Strategy B stop buffers.
- Current Strategy B stop sanity gates.
- Current Strategy B ADX filter.
- Current Strategy B partial exit.
- Current Strategy B break-even handling.
- Current Strategy B implementation.

This reaffirmation does not create Strategy B2 or Strategy C.

This reaffirmation does not authorize implementation changes.

## 4. Rationale

PR #84 documented current Strategy B TP1 behavior, candidate diagnostics, review classifications, and safe recommendations as a conservative docs-only current-state review.

PR #85 accepted that review and selected `strategy_b_tp1_selection_human_review_keep_prior_closure`.

The current TP1 selection proxy limitation is a documented limitation, not a confirmed implementation defect. Current committed evidence does not support replacing rank-1 TP1 selection by default.

The TP1 RR gate candidate is a review area, not a threshold-change request. The committed diagnostics show a large TP1 minimum RR rejection footprint, but they do not authorize lowering, raising, removing, optimizing, or contextualizing the threshold.

The stop-to-TP geometry candidate is a review area, not a stop-change request. The committed diagnostics show strong overlap between `stop_too_wide` and `tp1_below_min_rr`, but they do not authorize stop-anchor, buffer, or sanity-gate changes.

ADX remains secondary in the committed diagnostics. No ADX or filter change is authorized.

The prior closure controls because committed evidence remains insufficient for:

- Strategy B code, parameter, config, or test changes;
- TP1, TP2, RR, stop, filter, or management changes;
- new diagnostics generation;
- default Strategy B2 or Strategy C creation;
- backtests or optimization;
- market-data or broker work.

## 5. Frozen items

| item | current status | changed by this PR | future reopening requirement |
| --- | --- | --- | --- |
| TP1 selection | Current rank-1 nearest eligible left-side target remains frozen. | no | Separate project-owner approval and a bounded TP1 diagnostic or specification-review plan. |
| TP2 selection | Current rank-2 eligible target behavior remains frozen. | no | Separate project-owner approval and a TP1/TP2 specification-review plan. |
| TP1 minimum RR | Fixed `1.0R` gate remains frozen. | no | Separate project-owner approval and a TP1 RR specification-review plan; no threshold work by implication. |
| TP2 minimum RR | Fixed `1.5R` gate remains frozen. | no | Separate project-owner approval and an RR specification-review plan. |
| TP1-only RR | Fixed `1.5R` fallback gate remains frozen. | no | Separate project-owner approval and an RR fallback review plan. |
| Stop anchor | Current stop-side left-swing/reference-candle fallback remains frozen. | no | Separate project-owner approval and a stop-anchor review plan. |
| Stop buffer | Current `max(pair_buffer, 0.10 * ATR(14), tick_size)` buffer remains frozen. | no | Separate project-owner approval and a stop-buffer review plan. |
| Stop sanity gates | Current `0.25 * ATR(14)` minimum and `3.0 * ATR(14)` maximum gates remain frozen. | no | Separate project-owner approval and a stop-sanity review plan. |
| ADX filter | Current ADX(14) no-trade threshold remains frozen. | no | Separate project-owner approval and an ADX/filter review plan. |
| Partial exit | Current fixed 50% TP1 partial exit remains frozen. | no | Separate project-owner approval and a management review plan. |
| Break-even management | Current remaining 50% move-to-entry after TP1 remains frozen. | no | Separate project-owner approval and a management review plan. |
| Strategy B code | Implementation remains unchanged. | no | Separate implementation-review approval after docs-level decision work. |
| Strategy B tests | Tests remain unchanged. | no | Separate implementation-review approval after docs-level decision work. |
| Strategy B2 | Not created. | no | Separate Strategy B2 decision plan and explicit project-owner approval. |
| Strategy C | Not created. | no | Separate Strategy C decision plan and explicit project-owner approval. |
| Backtests | Not run. | no | Separate backtest planning PR and explicit project-owner approval. |
| Optimization | Not run. | no | Separate optimization planning PR and explicit project-owner approval. |
| Market data access | Not accessed or fetched. | no | Separate market-data planning PR and explicit project-owner approval. |
| Broker/live execution logic | Not added. | no | Separate live/broker authorization outside this docs-only workflow. |

## 6. Requirements to reopen

This PR approves none of the reopening paths below. It only records what would be required before any future reopening.

| possible future path | minimum reopening gate | status in this PR |
| --- | --- | --- |
| TP1 diagnostic planning | Project-owner approval, bounded scope, artifact plan, aggregate-only committed output, and explicit no-backtest/no-optimization/no-profitability guardrails. | not approved |
| TP1 specification review plan | Project-owner approval, documented questions, no parameter changes, and no implementation edits. | not approved |
| Strategy B implementation review plan | Project-owner approval after a completed docs-level decision that identifies an implementation question. | not approved |
| Strategy B2 decision plan | Project-owner approval and a docs-only decision plan that separates Strategy B2 from current Strategy B. | not approved |
| Backtest planning | Project-owner approval, separate plan, data-artifact guardrails, no profitability framing, and no code changes by implication. | not approved |
| Optimization planning | Project-owner approval, separate plan, guardrails against tuning-by-result, and no profitability framing. | not approved |
| Market-data planning | Project-owner approval, separate access plan, no broker/live logic, and explicit artifact controls. | not approved |

No path is reopened by this reaffirmation.

## 7. Relationship to Doctrine Map and mismatch findings

The Doctrine Map v2 draft proposal remains non-final. This reaffirmation does not update Doctrine Map v1 and does not create a final Doctrine Map v2.

PR #81 and PR #82 mismatch context remains context only:

| area | reaffirmed handling |
| --- | --- |
| TP/RR and stop mismatch | Provides context for TP1, RR, and stop review areas; does not authorize Strategy B changes. |
| EMA/reference-candle mismatch | Remains no-change for current Strategy A/B entry identity. |
| ADX proxy limitation | Remains no-change; ADX is secondary in the committed TP1 diagnostics. |
| Breakout, damashi, sweep, false-break | Remain unresolved and discretionary; not imported into Strategy B TP1 logic. |
| Wave context | Remains broader than current Strategy B; no wave-count logic is authorized. |
| Discretionary management | Remains a separate doctrine and management topic; no management logic change is authorized. |
| Batch 08 | Excluded from this decision reaffirmation. |

The TP/RR and stop mismatch context does not authorize current Strategy B TP1, TP2, RR, stop, filter, management, implementation, or Strategy B2 changes.

## 8. Research status after reaffirmation

Research status after this reaffirmation:

- Strategy B initial version remains restrictive in the committed candidate diagnostics.
- The accepted sample remains very small in the committed aggregate evidence.
- TP1 minimum RR and stop-to-TP geometry remain the main documented bottleneck families.
- Current TP1 selection remains documented as a mechanical proxy limitation.
- Later TP ranks remain diagnostic context only and are not an automatic replacement rule.
- ADX remains a secondary diagnostic area for this TP1 decision cycle.
- The current decision is not to change Strategy B.
- The current decision is not to create Strategy B2 or Strategy C.
- This is not a profitability conclusion.
- This is not a broker, live-trading, execution, or market-readiness conclusion.

This reaffirmation does not state that Strategy B should change. It does not state that TP1 selection is wrong. It does not state that TP1 selection is correct.

## 9. Recommended next PR

Recommended next docs-only PR:

`Channel full-corpus remaining-input status review`

Reason:

- The Strategy B TP1 review line is now closed with prior closure reaffirmed.
- The project should not continue Strategy B summary/review PRs by default.
- The next priority is returning to the YouTube full-channel corpus research line.
- Full-channel metadata inventory and transcript availability accounting already exist in committed docs.
- The next task should use existing committed inventory, availability, priority, and completed-summary docs as the source of truth.
- The next task should identify remaining unsummarized, caption-available, caption-unknown, blocked, unavailable, and Shorts segments.
- It should not regenerate the full inventory unless a specific gap is found.
- It should not commit raw transcripts, subtitle text, caption URLs, CSV, JSON, `data/`, `results/`, videos, audio, or raw candidate rows.
- It should not modify Strategy A/B, create Strategy B2/C, run backtests, optimize, access market data, or make profitability claims.

The recommended next PR should remain docs-only and should not reopen Strategy B diagnostics, specification work, implementation, Strategy B2, Strategy C, backtests, optimization, or market data.

## 10. Readiness decision

Decision:

`strategy_b_tp1_decision_reaffirmation_ready_for_human_review`

Reason: this docs-only reaffirmation records that PR #85 keeps prior Strategy B TP1 closure controlling, freezes current Strategy B TP1, TP2, RR, stop, filter, management, implementation, and Strategy B2 status, defines future reopening gates without approving them, and preserves all artifact, market-data, Doctrine, Strategy, Batch 08, backtest, optimization, and profitability guardrails.

This document does not authorize implementation changes, diagnostics generation, market-data access, Strategy B2/C creation, Doctrine Map updates, backtests, optimization, or profitability claims.
