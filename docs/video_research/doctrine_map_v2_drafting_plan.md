# Doctrine Map v2 Drafting Plan

Task: `doctrine_map_v2_drafting_plan`

Plan date: 2026-07-01

## 1. Objective and Scope

This is a docs-only plan for how to draft a future Doctrine Map v2.

This plan:

- Defines drafting principles, structure, gates, and candidate-backlog handling for a future Doctrine Map v2 draft proposal.
- Uses only existing committed documentation.
- Preserves traceability to Doctrine Map v1 and the Doctrine Map v2 candidate review.
- Keeps the next work as docs-only planning or drafting.

This plan does not:

- Update Channel Doctrine Map v1.
- Create Channel Doctrine Map v2.
- Write final Doctrine Map v2 doctrine text.
- Modify Strategy A/B code, parameters, configs, or tests.
- Create Strategy B2 or Strategy C.
- Include Batch 08.
- Access DownSub, YouTube, captions, audio, video, or ASR.
- Run backtests or optimization.
- Make profitability claims.
- Add broker, live trading, or execution logic.
- Commit raw TXT, SRT, VTT, subtitle full text, caption URLs, CSV, JSON, database, `data/`, or `results/` artifacts.

## 2. Evidence Base

Primary evidence for this drafting plan:

- `docs/video_research/doctrine_map_v2_candidate_review.md`
- `docs/video_research/doctrine_map_v2_candidate_review_review.md`
- `docs/video_research/doctrine_map_v2_candidate_update_plan.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/downsub_access_policy_v2.md`
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`

Corpus v2 Batch 01-07 audit synthesis coverage:

| metric | value |
| --- | ---: |
| completed-summary audit batches synthesized | 7 |
| total videos audited | 56 |
| total mechanical-rule candidates audited | 233 |

Secondary context, if needed for a future draft proposal:

- Batch 01 through Batch 07 completed-summary audit reports.
- Batch 01 through Batch 07 aggregate reports and quality reviews.

This plan does not add new evidence, new summaries, new caption access, or new candidate extraction.

## 3. Drafting Principles

A future Doctrine Map v2 draft proposal should follow these principles:

- Preserve traceability to Doctrine Map v1 and the Doctrine Map v2 candidate review.
- Distinguish accepted doctrine from candidate evidence.
- Keep weak or limited evidence out of doctrine text unless it is clearly labeled as an evidence note.
- Keep unresolved discretionary terms out of doctrine text unless carefully labeled as unresolved blockers.
- Avoid mechanical specificity unless the committed evidence explicitly supports that specificity.
- Do not convert doctrine into Strategy A/B rules.
- Do not infer profitability.
- Do not invent exact frequencies or counts beyond those already present in committed docs.
- Do not use Batch 08 evidence unless Batch 08 is separately approved, audited, and merged.
- Do not imply that candidate backlog items are already accepted doctrine.

The future draft should be conservative: it may propose candidate wording, but it should keep confidence, limitations, and evidence boundaries visible.

## 4. Proposed Doctrine Map v2 Structure

This is a proposed future document structure only. It is not final Doctrine Map v2 doctrine text.

| proposed section | purpose | drafting note |
| --- | --- | --- |
| Purpose and scope | Define what Doctrine Map v2 is and is not. | State that it is corpus doctrine, not Strategy A/B implementation guidance. |
| Evidence base | List the committed evidence sources used. | Include Corpus v2 Batch 01-07 synthesis and candidate review; exclude Batch 08. |
| Doctrine confidence labels | Define high, medium, low, evidence-note, and unresolved labels. | Preserve v1 confidence logic unless the draft proposal explicitly justifies changes. |
| Strengthened existing doctrine areas | Propose updates for v1 areas strengthened by candidate review. | Use candidate labels such as DM2-C01 through DM2-C07 for traceability. |
| Limited evidence / unresolved areas | Preserve weak, setup-specific, or discretionary evidence outside doctrine text. | Use evidence-note or unresolved-blocker labels, not accepted doctrine. |
| Strategy A/B boundary | Explain that doctrine is not implementation. | State that any mismatch re-check requires separate authorization after draft acceptance. |
| Batch 08 exclusion | Record that Batch 08 is excluded from v2 drafting unless separately approved and audited. | Avoid using Batch 08 selection or blocked-access material as evidence. |
| Versioning and change log | Record source version, prior documents, and draft status. | Make clear whether the document is draft proposal, review, or accepted doctrine. |
| Readiness decision | State readiness for human review only. | Do not state that Strategy A/B should change or that final doctrine is accepted. |

The future draft proposal should avoid writing implementation-ready rules, parameters, thresholds, or trading instructions.

## 5. Handling of Candidate Backlog Items

The merged candidate review backlog should be handled as follows in a future Doctrine Map v2 draft proposal.

| backlog item | topic | future draft handling | rationale |
| --- | --- | --- | --- |
| DM2-C01 | higher-timeframe context | candidate for strengthened doctrine | Candidate review marked this high confidence and strengthened relative to v1, but drafting must separate premise timeframe, monitored timeframe, and execution timeframe. |
| DM2-C02 | entries and confirmation | candidate for strengthened doctrine | Candidate review marked this high confidence, but drafting must preserve multiple confirmation families rather than one universal trigger. |
| DM2-C03 | stop placement and invalidation | candidate for strengthened doctrine | Evidence supports premise-based stops, but anchors, buffers, and stop width remain partly visual or absent. |
| DM2-C04 | TP, exit, and RR | candidate for strengthened doctrine | Future wording should separate target selection, protective exit, management, RR threshold, and trader tolerance. |
| DM2-C05 | breakout, damashi, sweep, and false-break handling | candidate for strengthened doctrine | Drafting should keep this as context/filter doctrine, not a complete breakout or reversal system. |
| DM2-C06 | range handling | candidate for strengthened doctrine | Drafting should preserve structural range language and avoid reducing it to ADX or another indicator. |
| DM2-C07 | wave context | candidate for strengthened doctrine | Wave context can be preserved as context, while wave count and wave cleanliness remain discretionary. |
| DM2-C08 | EMA and reference-candle context | evidence note only | Candidate review kept this weak/limited; use as setup-specific evidence, not broad indicator doctrine. |
| DM2-C09 | discretionary management and psychology | evidence note only | Mostly cautionary or conditional; separate warnings from positive procedures before any doctrine text. |
| DM2-C10 | discretionary chart-reading terms | unresolved blocker | Terms such as clean wave, valid line, target realism, strong reason, market fuel, and scenario coherence are not mechanically specified. |

Backlog handling rule:

- DM2-C01 through DM2-C07 may be candidates for strengthened doctrine in a future draft proposal.
- DM2-C08 and DM2-C09 should stay as evidence notes unless a future review upgrades their support and specificity.
- DM2-C10 should remain an unresolved blocker unless a future manual-review protocol defines the terms carefully.

## 6. Drafting Gates

Mandatory gates before any actual Doctrine Map v2 document is created:

| gate | requirement |
| --- | --- |
| human review of this drafting plan | This plan must be reviewed before a Doctrine Map v2 draft proposal is created. |
| explicit approval for draft proposal | A future PR must be explicitly authorized to create a Doctrine Map v2 draft proposal. |
| no Batch 08 inclusion | Batch 08 must remain excluded unless separately audited, approved, and merged. |
| no Strategy A/B implication | Strategy A/B mismatch work must be separately authorized after a draft or candidate doctrine set is accepted. |
| no final doctrine text without approval | Final Doctrine Map v2 doctrine text must not be written without explicit approval. |
| no implementation work | No code, config, test, backtest, optimization, broker, live trading, or execution work. |
| no raw/source artifacts | No raw subtitle, caption URL, media, CSV, JSON, database, `data/`, or `results/` artifacts. |
| confidence and limitation preservation | Future drafting must preserve confidence labels and limitations from candidate review. |

If any gate is not satisfied, the next work should remain planning or review only.

## 7. Strategy A/B Boundary

Strategy A/B mismatch re-check should happen only after a Doctrine Map v2 draft proposal or accepted candidate doctrine set is explicitly accepted by the project owner.

This plan does not modify Strategy A/B. It does not recommend Strategy A/B parameter changes, config changes, test changes, Strategy B2, Strategy C, backtests, optimization, or live execution changes.

Potential mismatch re-check topics identified in the candidate review should remain planning references only:

- higher-timeframe context;
- entries and confirmation;
- stop placement and invalidation;
- TP, exit, and RR;
- breakout, damashi, sweep, and false-break handling;
- range handling;
- wave context;
- EMA and reference-candle context;
- discretionary management and psychology.

No Strategy A/B action should be taken from this drafting plan.

## 8. Non-Goals

This plan does not authorize:

- Strategy A/B implementation.
- Strategy A/B parameter tuning.
- Strategy A/B config or test changes.
- Strategy B2 or Strategy C.
- Backtests.
- Optimization.
- Profitability conclusions.
- Live trading.
- Broker or execution logic.
- Market-data access.
- Batch 08 inclusion.
- Channel Doctrine Map v1 edits.
- Channel Doctrine Map v2 creation.
- Final Doctrine Map v2 doctrine text.
- Raw subtitle, caption URL, audio, video, CSV, JSON, database, `data/`, or `results/` artifacts.

## 9. Recommended Next PR After This Plan

Recommended next docs-only PR:

`Doctrine Map v2 draft proposal`

Reason: the candidate update plan and candidate review already established the review method, candidate family dispositions, and backlog handling. A Strategy A/B mismatch re-check plan should wait until a Doctrine Map v2 draft proposal or accepted candidate doctrine set exists; otherwise Strategy comparison would be measuring against planning artifacts rather than a reviewed doctrine draft.

The next PR should still avoid final doctrine acceptance. It should be a draft proposal with traceability, confidence labels, limitations, and review gates. It should not modify Strategy A/B, include Batch 08, run backtests, optimize parameters, or make profitability claims.

## 10. Readiness Decision

`doctrine_map_v2_drafting_plan_ready_for_human_review`

Reason: this docs-only drafting plan uses the merged Doctrine Map v2 candidate review, Corpus v2 Batch 01-07 audit synthesis, current Doctrine Map v1, DownSub access policy v2, and existing Strategy A/B doctrine mismatch analysis to define how a future Doctrine Map v2 draft proposal should be structured and gated. It is ready for human review as a drafting plan only. It does not state that Doctrine Map v2 is ready, does not create Doctrine Map v2, does not write final Doctrine Map v2 doctrine text, does not include Batch 08, and does not state that Strategy A/B should change.
