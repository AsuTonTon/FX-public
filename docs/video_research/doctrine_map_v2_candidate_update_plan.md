# Doctrine Map v2 Candidate Update Plan

Task: `doctrine_map_v2_candidate_update_plan`

Plan date: 2026-07-01

## 1. Objective and Scope

This is a docs-only plan for a future Channel Doctrine Map v2 candidate update.

Scope:

- Define a conservative review method for deciding which Corpus v2 Batch 01-07 audit findings may later become Doctrine Map v2 candidate updates.
- Use only existing committed documentation.
- Keep Doctrine Map v1 unchanged.
- Avoid creating Doctrine Map v2 in this PR.
- Avoid modifying Strategy A/B.
- Keep Batch 08 outside this plan's evidence base.

Out of scope:

- Updating `docs/video_research/channel_doctrine_map_v1.md`.
- Creating a Channel Doctrine Map v2 document.
- Adding, removing, or rewriting doctrine statements.
- Modifying Strategy A/B code, parameters, configs, or tests.
- Creating Strategy B2 or Strategy C.
- Running backtests, optimization, live trading, broker, or execution logic.
- Making profitability conclusions.
- Accessing DownSub or YouTube.
- Fetching captions, downloading audio/video, or running ASR.
- Committing raw TXT, SRT, VTT, subtitle full text, caption URLs, CSV, JSON, database, `data/`, or `results/` artifacts.

## 2. Evidence Base

Primary evidence for this plan:

- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis_review.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/downsub_access_policy_v2.md`
- Batch 01 through Batch 07 completed-summary audit reports.

Secondary context, if needed for a future candidate review:

- Batch 01 through Batch 07 aggregate reports.
- Batch 01 through Batch 07 quality reviews.
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`

Corpus v2 Batch 01-07 audit synthesis coverage:

| metric | value |
| --- | ---: |
| completed-summary audit batches synthesized | 7 |
| total videos audited | 56 |
| total mechanical-rule candidates audited | 233 |

This plan does not add new evidence, new summaries, new caption access, or new candidate extraction.

## 3. Why a Plan Is Needed

Batch 01 through Batch 07 completed-summary audits confirm that existing candidate claims were caption-supported where available, candidate IDs matched the corresponding aggregate reports, and no candidate required removal, demotion, or wording correction in those audits.

That audit result is useful, but it is not the same as doctrine approval.

Important distinctions:

- Caption-supported candidate claims are not automatically channel doctrine.
- Caption-supported candidate claims are not automatically mechanical strategy rules.
- A recurring candidate family can still be too visual, discretionary, or setup-specific to express as doctrine.
- A one-off example can be valuable research evidence without becoming a doctrine statement.
- A future Doctrine Map v2 update must separate recurring principles from one-off examples, weak evidence, and discretionary chart-reading terms.

Doctrine Map v2 candidate review therefore needs a conservative, reviewable process before any doctrine text is drafted.

## 4. Proposed Doctrine Map v2 Candidate Review Method

The future review should proceed in this order:

1. Collect candidate families from `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`.
2. For each family, inspect the relevant Batch 01-07 aggregate reports, completed-summary audits, and quality reviews.
3. Compare each family against `docs/video_research/channel_doctrine_map_v1.md`.
4. Classify each finding using one of the review dispositions below.
5. Record whether the evidence is multi-video, multi-batch, one-off, contradictory, weak, or too discretionary.
6. Preserve uncertainty and confidence labels from v1 and the source reports.
7. Keep chart-only or visual-discretion concepts unresolved unless they can be mechanically specified without overclaiming.
8. Produce a candidate-review document before drafting any Doctrine Map v2 text.

Review dispositions:

| disposition | meaning | allowed output |
| --- | --- | --- |
| keep v1 unchanged | Corpus v2 does not materially alter the v1 principle. | Note the evidence and preserve current doctrine wording. |
| strengthen existing doctrine | Corpus v2 adds clearer or broader support for a v1 principle. | Propose a candidate strengthening for later Doctrine Map v2 review. |
| add candidate doctrine | Corpus v2 supports a recurring principle not clearly expressed in v1. | Propose as candidate doctrine only, with confidence and limitations. |
| keep as weak/limited evidence | Evidence is useful but one-off, low-confidence, setup-specific, or incomplete. | Preserve in a backlog or evidence note, not doctrine text. |
| reject as too discretionary | Evidence relies on chart-only visual judgment or undefined terms that cannot be responsibly stated as doctrine. | Record as unresolved, not doctrine. |

Minimum standards:

- Require multi-video support before treating a claim as doctrine.
- Prefer multi-batch support for high-confidence or broadly worded doctrine.
- Do not turn absence findings into universal channel claims unless the source reports explicitly support that scope.
- Do not turn Strategy A/B proxies into doctrine.
- Do not turn doctrine candidates into Strategy A/B changes.
- Keep visual terms such as clean wave, valid line, target realism, strong reason, market fuel, or scenario coherence unresolved unless a future review defines them precisely.

## 5. Candidate Families to Review

The future candidate review should use high-level families only. It should not invent exact frequencies unless they are explicitly present in committed docs.

| candidate family | review focus | likely v1 comparison area |
| --- | --- | --- |
| entries and confirmation | Delayed entry, line close, pullback confirmation, reference candle behavior, breakout confirmation, false-break recovery, and second confirmation. | Entry doctrine; timeframe hierarchy doctrine; false-break doctrine. |
| stop placement and invalidation | Premise failure, wave/pattern invalidation, structural backing, pivots, stop-width boundaries, and rejection of unclear stops. | Stop / invalidation doctrine. |
| TP, exit, and RR | Structural TP, realistic target, left-side levels, partial or staged exit, protective exit, RR contextuality, and trader tolerance. | TP / exit doctrine; risk/reward doctrine; trade-management doctrine. |
| breakout, damashi, sweep, and false-break handling | Breakout validity, line quality, triangle false-break caution, sweep/reclaim behavior, dirty structure, and delayed confirmation. | False-break / damashi / sweep doctrine; horizontal-line doctrine. |
| range handling | Range boundary maturity, touch count, short-term range-entry caution, dirty range rejection, and higher-timeframe veto. | Trend / range / pattern-quality doctrine. |
| wave context | Wave stage, wave overlap, third-wave examples, pullback waiting, wave-aligned stops and targets, and wave-quality blockers. | Timeframe hierarchy doctrine; stop / invalidation doctrine; TP / exit doctrine. |
| EMA and reference-candle context | Moving-average context, 20EMA touch, body-close confirmation, 200EMA environment, and reference-candle logic. | Indicator doctrine; entry doctrine. |
| higher-timeframe context | Higher-timeframe veto, monitored-timeframe confirmation, context-before-trigger logic, and timeframe ownership of premise, stop, and target. | Timeframe hierarchy doctrine; entry doctrine. |
| discretionary management and psychology | Mid-profit exit, protective exit, break-even or stop-change caution, trader tolerance, and warnings against copying advanced management. | Trade-management doctrine; risk/reward doctrine; discretionary blockers. |

The review should treat these as candidate families, not final doctrine sections.

## 6. Doctrine Map v1 Comparison Checklist

For each candidate family or proposed doctrine candidate, the future review should answer:

| checklist item | review question |
| --- | --- |
| v1 statement | What does Doctrine Map v1 already say about this topic? |
| Corpus v2 support | Does Corpus v2 Batch 01-07 strengthen the v1 statement? |
| contradiction check | Does Corpus v2 contradict, narrow, or qualify the v1 statement? |
| one-off separation | Is the evidence recurring, or is it only a one-off example? |
| discretion boundary | Does the claim remain visual, chart-only, or discretionary? |
| doctrine safety | Is it safe to express as doctrine without overclaiming mechanical precision? |
| confidence | Should the candidate be high, medium, low, or unresolved? |
| Strategy A/B boundary | Would this topic require a later Strategy A/B mismatch re-check if Doctrine Map v2 accepts it? |
| non-goal confirmation | Does the candidate avoid code, parameter, backtest, optimization, live trading, and profitability implications? |

Any accepted candidate should include the exact disposition, confidence, limitation, and source-doc references in the future candidate-review document.

## 7. Explicit Non-Goals

This plan does not authorize:

- Strategy A/B implementation.
- Strategy A/B parameter changes.
- Strategy A/B config or test changes.
- Strategy B2 or Strategy C.
- Backtests.
- Optimization.
- Profitability conclusions.
- Live trading.
- Broker or execution logic.
- Market-data fetches.
- Batch 08 inclusion.
- Channel Doctrine Map v1 edits.
- Channel Doctrine Map v2 creation.
- Raw subtitle, caption URL, audio, video, CSV, JSON, database, `data/`, or `results/` artifacts.

## 8. Proposed Next Document After This Plan

Recommended next docs-only PR:

`Doctrine Map v2 candidate review`

Reason: a Strategy A/B mismatch re-check should compare Strategy A/B against an accepted doctrine candidate set. The project should first review whether Corpus v2 Batch 01-07 evidence strengthens, narrows, adds, or rejects candidate doctrine relative to v1. Only after that review is accepted should a `Strategy A/B mismatch re-check plan` decide what changed enough to compare against Strategy A/B.

The next document should remain a review document, not Doctrine Map v2 itself. It should classify candidate families using the disposition table above and preserve the same guardrails: no Doctrine Map v1 update, no Doctrine Map v2 creation, no Strategy A/B change, no Batch 08 inclusion, no caption access, no backtest, and no profitability claim.

## 9. Readiness Decision

`doctrine_map_v2_candidate_update_plan_ready_for_review`

Reason: this plan defines a conservative docs-only process for reviewing Corpus v2 Batch 01-07 audit findings against Doctrine Map v1 before any Doctrine Map v2 candidate update is drafted. It uses the merged synthesis covering 56 audited videos and 233 audited mechanical-rule candidates, preserves the distinction between caption-supported candidates, doctrine, and mechanical strategy rules, keeps Batch 08 separate, and does not update Doctrine Map v1, create Doctrine Map v2, modify Strategy A/B, run backtests, optimize, or make profitability claims.
