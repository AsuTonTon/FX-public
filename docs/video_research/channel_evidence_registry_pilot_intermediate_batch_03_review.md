# Channel Evidence Registry Pilot Review: Intermediate Batch 03

Task: `channel_evidence_registry_pilot_intermediate_batch_03_review`

Status: docs-only schema review. This document reviews the committed Intermediate Batch 03 evidence-registry pilot and recommends a small schema adjustment before any larger registry backfill. It does not update the registry design document, add registry rows, update doctrine maps, or modify Strategy A/B/B2/C behavior.

## 1. Objective and scope

The objective is to review whether the committed 10-row Intermediate Batch 03 evidence-registry pilot is usable for claim-level evidence tracking and whether the registry schema should adopt a `source_granularity` field before larger population work.

This review:

- uses committed repository docs only;
- reviews the pilot's schema usability, evidence separation, and Markdown layout;
- recommends whether to adopt `source_granularity`;
- proposes a controlled value set for that field;
- recommends one next docs-only task.

This review does not:

- access YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, downloaded media, ASR, market data, broker/live systems, or external sources;
- inspect or reconstruct raw caption, subtitle, or transcript text;
- create a full channel-wide registry;
- backfill additional evidence rows;
- update Doctrine Map v1 or create/finalize Doctrine Map v2;
- modify Strategy A/B/B2/C rules, code, tests, parameters, configs, backtests, or conclusions;
- create Strategy C;
- perform parameter optimization;
- make profitability claims or guarantees;
- change guardrail policy.

## 2. Source docs used

Primary source docs:

- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_completed_summary_audit.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_aggregate_report.md`

No non-repository source was used. Compact title metadata in committed docs remains metadata only and is not treated as proof of content claims or outcomes.

## 3. Pilot usability review

Review decision:

`pilot_schema_usable_for_small_claim_level_registry`

The 10-row pilot is usable for a small claim-level registry because it captures:

- one compact claim per row;
- the source document and source section;
- whether evidence is summary-, synthesis-, audit-, metadata-, or blocked-status derived;
- claim type, doctrine category, setup family, and conservative mechanical-readiness labels;
- blocker reasons and unresolved definitions;
- Strategy/corpus boundary routing;
- title-only warning and raw-artifact status.

The pilot also exposes two limits that matter before larger backfill:

- the same `source_doc` field can point to several different evidence levels, such as per-video summary, aggregate inventory, batch synthesis, and completed-summary audit;
- the full table is readable at 10 rows but becomes difficult to review because the schema is wide and each row carries many guardrail fields.

The pilot should therefore be treated as a successful schema test with small adjustments needed before broader use, not as a complete registry model ready for large-scale population.

## 4. Source-granularity adoption decision

Adoption decision:

`adopt_source_granularity_before_larger_backfill`

Reason:

The pilot already distinguishes `evidence_type`, but `evidence_type` answers how evidence reached the repository, not the level of document structure that supports the row. A separate `source_granularity` field would make later review clearer by recording whether a claim is grounded in a per-video summary, aggregate candidate inventory, synthesis, audit boundary, doctrine map, or blocked-status document.

This separation matters because:

- a per-video summary row and a batch-synthesis row can both be `summary_derived` or `synthesis_derived` but carry different review strength and scope;
- an audit-derived metadata row should not be confused with content doctrine;
- blocked-status rows must remain separate from content evidence;
- future Strategy-line reviewers need to know whether a candidate comes from one video, a synthesis pattern, or a boundary/audit document before deciding whether a separate Strategy review is justified.

Adopting `source_granularity` should be a schema refinement only. It should not authorize a larger backfill, new source access, Strategy integration, or Doctrine Map updates.

## 5. Proposed controlled value set

Recommended `source_granularity` values:

| value | use |
| --- | --- |
| `per_video_summary` | Claim is supported by one committed paraphrased per-video summary. |
| `aggregate_inventory` | Claim is supported by a committed aggregate report, candidate inventory, target table, or coverage table. |
| `batch_synthesis` | Claim is supported by a committed batch or playlist synthesis. |
| `completed_summary_audit` | Claim is supported by a committed completed-summary audit or quality boundary check. |
| `blocked_status` | Row records unavailable, blocked, ambiguous, or not-yet-complete source status without creating content evidence. |
| `doctrine_map` | Claim is supported by a committed doctrine map, doctrine evidence index, doctrine review, or doctrine proposal. |
| `strategy_boundary_doc` | Row is supported by committed Strategy/corpus separation, mismatch, or boundary documentation. |

Recommended rules:

- Use exactly one value per row unless a future review explicitly approves multiple values.
- If a row combines sources at different levels, split the row unless the claim would become misleading without the combined context.
- `blocked_status` must not support content or doctrine claims.
- `aggregate_inventory` should not be treated as stronger evidence than the summary or synthesis that explains the claim.
- `doctrine_map` and `strategy_boundary_doc` values do not authorize Strategy A/B/B2/C changes.

## 6. Markdown layout review

Layout decision:

`wide_table_acceptable_for_pilot_not_for_larger_registry`

The current wide-table layout is acceptable for a 10-row pilot because it keeps all fields visible in one place and makes schema testing direct.

For larger registry docs, a better Markdown structure would be:

1. a compact overview table with stable fields such as `evidence_id`, `claim_text`, `source_granularity`, `evidence_type`, `claim_type`, `mechanical_readiness`, `strategy_relevance`, and `review_status`;
2. per-row detail sections for blocker details, unresolved definitions, title warnings, source sections, notes, and guardrail boundary language;
3. a short validation and guardrail section at the end of the document.

This format would preserve Git reviewability while avoiding CSV/JSON/database dumps and avoiding a table so wide that meaningful review becomes error-prone.

## 7. Evidence-separation review

The pilot preserves separation among the required evidence classes:

| evidence class | review result | note |
| --- | --- | --- |
| metadata-only | passed | Coverage/status row `CER-I03-010` stays boundary-focused and does not create content doctrine. |
| summary-derived | passed | Rows that cite aggregate candidate inventory or summary context remain paraphrased and conservative. |
| synthesis-derived | passed | Synthesis rows are used for cross-video or batch-level claims, not implementation approval. |
| audit-derived | passed | Audit evidence is used for completeness and boundary status, not trading-rule proof. |
| doctrine-derived | not used in pilot | The value remains needed for later registry rows based on committed doctrine documents. |
| blocked-status | not used in pilot | The value remains needed for rows such as caption-access blockers or incomplete source windows. |

The proposed `source_granularity` field would strengthen this separation by distinguishing document level from evidence type.

## 8. Strategy/corpus separation check

Separation decision:

`corpus_only_no_strategy_integration`

This review stays inside the YouTube channel-wide corpus line. It does not change Strategy A/B/B2/C behavior, tests, parameters, configs, backtests, or conclusions.

Rows in the pilot marked `possible_strategy_ab_review_input` or `mismatch_review_input` should remain routing labels only. They may support a later separately authorized Strategy-line review, but they do not authorize implementation, parameter optimization, Strategy C creation, market-data access, broker/live work, or profitability conclusions.

## 9. Guardrail review

Guardrail decision:

`guardrails_preserved`

This review confirms:

- committed repository docs only were used;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw DownSub output, downloaded media, CSV, JSON database dump, generated candidate row, `data/`, or `results` artifact is added;
- no credentials, tokens, or secrets are added;
- no market-data, broker API, order-placement, auto-trading, or live-trading functionality is added;
- no Strategy A/B/B2/C behavior, tests, parameters, configs, or conclusions are changed;
- no Doctrine Map v1 update and no Doctrine Map v2 creation/finalization is made;
- no parameter optimization or profitability claim is made;
- corpus findings are not mixed into executable Strategy A/B conclusions.

## 10. Recommended next docs-only task

Recommended next task:

`[codex] Update the channel evidence registry design to add source_granularity`

Recommended scope:

- docs-only update to `docs/video_research/channel_evidence_registry_design.md`;
- add `source_granularity` to the proposed schema;
- add the controlled value set from this review;
- add layout guidance for compact overview plus per-row detail sections before any larger registry backfill;
- do not add registry rows, update doctrine maps, touch Strategy A/B/B2/C, access sources, run backtests, access market data, or change guardrail policy.

## 11. Review conclusion

Conclusion:

`source_granularity_schema_refinement_recommended_before_backfill`

The Intermediate Batch 03 pilot is strong enough to validate the core evidence-registry schema for a small Markdown pilot. Before larger use, the schema should add `source_granularity` and larger registry docs should move away from a single very wide table. Those changes would improve traceability and reviewability while preserving source-access, raw-artifact, Strategy/corpus, and guardrail boundaries.
