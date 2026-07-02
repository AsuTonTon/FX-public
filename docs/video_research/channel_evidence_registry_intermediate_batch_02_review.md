# Channel Evidence Registry Intermediate Batch 02 Review

Task: `channel_evidence_registry_intermediate_batch_02_review`

Status: docs-only review. This document reviews the committed Intermediate Batch 02 evidence-registry slice and decides whether its compact overview plus per-row detail layout should be reused for future narrow registry slices. It does not add registry rows, create a full channel-wide registry, update doctrine maps, or modify Strategy A/B/B2/C behavior.

## 1. Objective and scope

The objective is to review whether the committed 10-row Intermediate Batch 02 evidence-registry slice preserves traceability, source granularity, title/source separation, and Strategy/corpus boundaries.

This review:

- uses committed repository docs only;
- reviews `docs/video_research/channel_evidence_registry_intermediate_batch_02.md`;
- compares its compact overview plus per-row detail layout against the earlier Intermediate Batch 03 pilot wide-table layout;
- decides whether future narrow registry slices should use the Batch 02 layout by default;
- identifies any schema or layout issues to resolve before another population slice;
- recommends one next docs-only task.

This review does not:

- access YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, downloaded media, ASR, market data, broker/live systems, or non-approved external sources;
- inspect or reconstruct raw caption, subtitle, or transcript text;
- add raw transcript text, subtitle full text, raw TXT/SRT/VTT files, caption URLs, raw DownSub output, raw extractor output, CSV, JSON database dumps, generated candidate rows, `data/`, `results`, credentials, tokens, or secrets;
- add, backfill, or revise evidence-registry rows;
- create a full channel-wide registry;
- update Doctrine Map v1 or create/finalize Doctrine Map v2;
- modify Strategy A/B/B2/C rules, code, tests, parameters, configs, backtests, or conclusions;
- create Strategy C;
- perform parameter optimization;
- make profitability claims or guarantees;
- mix corpus findings into Strategy A/B conclusions;
- change guardrail policy.

## 2. Source docs used

Registry and planning context:

- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_next_population_slice_plan.md`

Reviewed Batch 02 slice:

- `docs/video_research/channel_evidence_registry_intermediate_batch_02.md`

Comparison docs:

- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03.md`
- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03_review.md`

No non-repository source was used. Compact titles in committed docs remain metadata only and are not treated as content evidence, performance evidence, or profitability evidence.

## 3. Traceability review

Traceability decision:

`batch_02_registry_traceability_preserved`

The Batch 02 slice preserves source traceability because each row has:

- a stable `evidence_id`;
- a compact paraphrased `claim_text`;
- one repo-relative `source_doc`;
- a `source_doc_section`;
- `video_id` or `not_applicable`;
- `playlist_or_batch`;
- row-level notes explaining the review boundary.

The compact overview table is sufficient for routing review attention, while the per-row detail sections carry the source path, source section, blocker, unresolved definition, title warning, raw-artifact status, and corpus boundary. That split makes source evidence easier to inspect than the earlier Batch 03 pilot's single wide table.

No row lacks a source path. No row points to raw subtitle/caption/transcript text, caption URLs, generated CSV/JSON, `data/`, or `results`.

## 4. Source-granularity review

Source-granularity decision:

`batch_02_source_granularity_preserved`

The Batch 02 slice applies exactly one controlled `source_granularity` value per row:

| source_granularity | Batch 02 row count | Review result |
| --- | ---: | --- |
| `per_video_summary` | 5 | passed |
| `batch_synthesis` | 3 | passed |
| `completed_summary_audit` | 2 | passed |

The row set does not mix granularities within a row. It also avoids using unsupported values such as `doctrine_map` or `strategy_boundary_doc`, because those source docs are outside the Batch 02 population slice.

The absence of `aggregate_inventory` rows is acceptable for this slice. The committed source bundle included aggregate context, but the selected 10 rows were grounded at per-video summary, synthesis, or completed-summary-audit levels.

## 5. Title-only and source-evidence separation review

Title/source separation decision:

`title_metadata_separation_preserved`

The Batch 02 slice preserves the title/source boundary:

- content rows cite committed summary, synthesis, or audit sections rather than title wording;
- rows with compact-title context use `mixed_title_and_summary_context` where needed;
- the title-boundary row `CER-I02-010` is explicitly metadata-only and supports review hygiene rather than doctrine or trading claims;
- performance-style title language is not converted into a project conclusion;
- no row quotes or reconstructs raw caption, subtitle, or transcript text.

This is stronger than treating titles as candidate evidence. The slice keeps title metadata visible enough for review while preventing it from supporting content claims.

## 6. Strategy/corpus separation review

Strategy/corpus separation decision:

`corpus_only_no_strategy_integration`

The Batch 02 slice remains inside the YouTube channel-wide corpus line:

- `possible_strategy_ab_review_input` is used only as a routing label;
- rows that look mechanical still list blockers or unresolved definitions;
- no Strategy A/B/B2/C behavior, tests, parameters, configs, backtests, or conclusions are changed;
- no row creates Strategy C or recommends Strategy C work;
- no row recommends parameter optimization;
- no row treats corpus doctrine as accepted implementation guidance.

Any later Strategy-line use still requires a separate issue and design decision.

## 7. Layout comparison against Batch 03 pilot

Layout comparison decision:

`compact_overview_plus_detail_better_default_for_future_slices`

The Batch 03 pilot wide table was acceptable for a first 10-row schema test because it exposed every field in one place. Its weakness is review ergonomics: the row width makes blocker notes, source paths, title warnings, and guardrail fields hard to compare without horizontal scanning.

The Batch 02 compact overview plus per-row detail layout improves reviewability:

| review need | Batch 03 wide table | Batch 02 compact overview plus details |
| --- | --- | --- |
| fast row routing | adequate but wide | stronger, because stable routing fields are visible first |
| source traceability | present but crowded | stronger, because source paths and sections are isolated per row |
| blocker inspection | present but compressed | stronger, because blocker and unresolved-definition fields have room |
| title/source boundary | present | stronger, because title warning and notes can be reviewed per row |
| Strategy/corpus boundary | present | stronger, because boundary wording is not hidden in a wide table |
| Git review ergonomics | acceptable for a small pilot | better default for repeat narrow slices |

The compact overview plus details layout should be the default for future narrow evidence-registry slices, even at 8 to 12 rows. A wide table should be reserved for very small schema experiments or rows with unusually short fields.

## 8. Schema and layout issues before another slice

Blocking issues:

- none identified.

Nonblocking guidance for the next slice:

- keep the compact overview table limited to routing fields, not all schema fields;
- keep exactly one `source_granularity` value per row;
- keep `blocker_reason` separate from `unresolved_definition`;
- keep title metadata and summary-derived claims visibly separated;
- keep `raw_artifact_status` wording consistent within each registry document;
- include a row-count and source-granularity confirmation section;
- include a final guardrail section and changed-file validation in the PR body.

No schema change is required before the next narrow population slice. The current schema and Batch 02 layout are sufficient for another conservative docs-only slice.

## 9. Default layout decision

Default layout decision:

`future_narrow_registry_slices_should_default_to_compact_overview_plus_per_row_details`

Reason:

The Batch 02 layout better matches the current registry design. It keeps the review table narrow, preserves row-level traceability, avoids CSV/JSON/database artifacts, gives blockers and source sections enough space, and makes guardrail review easier without changing the underlying evidence schema.

Future narrow slices should use:

1. a compact overview table with `evidence_id`, `claim_text`, `source_granularity`, `evidence_type`, `claim_type`, `mechanical_readiness`, `strategy_relevance`, and `review_status`;
2. per-row details for source paths, source sections, video/batch identifiers, doctrine/setup labels, blockers, unresolved definitions, title warning, raw-artifact status, corpus boundary, and notes;
3. row-count, source-granularity, title/source, Strategy/corpus, and guardrail confirmation sections.

## 10. Guardrail review

Guardrail decision:

`batch_02_review_guardrails_preserved`

This docs-only review preserves these guardrails:

- committed repository docs only;
- no YouTube, DownSub, caption, subtitle, transcript-body, caption-URL, comment, live-chat, community-post, downloaded-media, ASR, market-data, broker/live, or external-source access;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw DownSub output, downloaded media, CSV, JSON database dump, generated candidate rows, `data/`, or `results` artifact;
- no credentials, tokens, or secrets;
- no Doctrine Map v1 update and no Doctrine Map v2 creation/finalization;
- no Strategy A/B/B2/C behavior, tests, parameters, configs, backtests, or conclusions changed;
- no Strategy C creation;
- no parameter optimization;
- no market-data access;
- no broker/live behavior;
- no profitability claims or guarantees;
- no corpus findings mixed into executable Strategy A/B conclusions.

## 11. Recommended next docs-only task

Recommended next task:

`[codex] Plan the next narrow evidence-registry population slice using the Batch 02 layout decision`

Recommended scope:

- use committed repository docs only;
- choose one bounded source bundle for the next narrow registry slice;
- reuse the compact overview plus per-row detail layout by default;
- keep the target row count small enough for line-by-line review;
- do not add rows in the planning PR;
- do not update doctrine maps, modify Strategy A/B/B2/C, access source material, run backtests, access market data, or change guardrail policy.
