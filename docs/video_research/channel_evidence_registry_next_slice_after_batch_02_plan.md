# Channel Evidence Registry Next Slice After Batch 02 Plan

Task: `channel_evidence_registry_next_slice_after_batch_02_plan`

Status: docs-only planning. This document chooses the next narrow committed-doc source bundle for a future evidence-registry population PR after the Batch 02 layout review. It does not add registry rows, create a full channel-wide registry, update doctrine maps, or modify Strategy A/B/B2/C behavior.

## 1. Objective and scope

The objective is to plan the next narrow channel evidence-registry population slice using the committed Batch 02 layout decision.

This plan:

- uses committed repository docs only;
- reviews the Batch 02 compact overview plus per-row detail decision;
- chooses one bounded committed-doc source bundle for a future registry slice;
- defines selection criteria, target row-count guidance, schema requirements, layout requirements, and guardrails;
- keeps title-only metadata, source evidence, blocked status, and Strategy/corpus boundaries separate.

This plan does not:

- access YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, downloaded media, ASR, market data, broker/live systems, or non-approved external sources;
- inspect or reconstruct raw caption, subtitle, or transcript text;
- add raw transcript text, subtitle full text, raw TXT/SRT/VTT files, caption URLs, raw DownSub output, raw extractor output, CSV, JSON database dumps, generated candidate rows, `data/`, `results`, credentials, tokens, or secrets;
- add or backfill evidence-registry rows;
- populate the next evidence-registry slice;
- update Doctrine Map v1 or create/finalize Doctrine Map v2;
- modify Strategy A/B/B2/C rules, code, tests, parameters, configs, backtests, or conclusions;
- create Strategy C;
- perform parameter optimization;
- make profitability claims or guarantees;
- mix corpus findings into Strategy A/B conclusions;
- change guardrail policy.

## 2. Source docs used

Registry design and prior slice context:

- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_next_population_slice_plan.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_02.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_02_review.md`
- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03.md`
- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03_review.md`

Proposed next-slice source bundle:

- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_target_table.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_aggregate_report.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_review.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`

No non-repository source was used. Compact titles in committed docs remain metadata only and must not be treated as content evidence, strategy evidence, or profitability evidence.

## 3. Batch 02 layout lessons used

The Batch 02 review adopted this default layout for future narrow registry slices:

`future_narrow_registry_slices_should_default_to_compact_overview_plus_per_row_details`

Practical lessons for the next slice:

- keep the compact overview table limited to routing fields;
- carry source paths, source sections, blocker notes, title warnings, raw-artifact status, and corpus boundaries in per-row details;
- use exactly one controlled `source_granularity` value per row;
- keep `blocker_reason` separate from `unresolved_definition`;
- include row-count and source-granularity confirmation sections;
- include final title/source, Strategy/corpus, and guardrail confirmation sections;
- avoid CSV, JSON, database dumps, `data/`, `results`, or generated artifacts.

The Batch 02 layout is especially suitable for blocked-status rows because the overview can stay short while the per-row details record why content evidence is unavailable.

## 4. Next-slice selection criteria

The next population slice should satisfy all of these criteria:

| criterion | requirement |
| --- | --- |
| committed evidence only | Use only Git-safe committed docs already in this repository. |
| bounded source bundle | Use one clearly scoped bundle, not a full channel-wide registry. |
| new review value | Cover a source state not already tested by the Batch 02 content slice or Batch 03 pilot. |
| title-risk visibility | Keep promotional or outcome-style title language as metadata only. |
| blocked-status handling | Record unavailable source evidence conservatively without creating content claims. |
| Strategy boundary | Keep all rows in the corpus line unless a future Strategy-line issue separately authorizes review. |
| reviewability | Keep the future row count small enough for line-by-line review. |
| artifact safety | Avoid raw text, caption URLs, CSV, JSON, database, `data/`, or `results` artifacts. |

## 5. Proposed next committed-doc source bundle

Planning decision:

`next_population_slice_intermediate_batch_03_continuation_blocked_status_bundle`

The next evidence-registry population PR should use the committed Intermediate Batch 03 continuation blocked-status bundle for playlist rows `21..27`.

Recommended source bundle:

- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_target_table.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_aggregate_report.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_review.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`

Reason:

- the bundle is already committed and bounded to seven exact playlist rows;
- the target table and aggregate report identify all seven selected IDs as target-resolved but caption-blocked;
- the review confirms the source-access boundary, raw-artifact guardrails, and Strategy/corpus separation;
- the recovery plan is the correct committed context for blocked-status handling before any later probe;
- this slice would test registry support for `blocked_status` rows, which Batch 02 did not exercise;
- it avoids creating content, doctrine, strategy, or profitability claims from title metadata.

The future population PR should treat the seven rows as blocked-status evidence only. It must not create per-video content claims, doctrine claims, mechanical-rule candidates, or Strategy A/B review inputs from compact titles.

## 6. Future target row-count guidance

The future population PR should target `7` evidence rows, one row for each committed Batch 03 continuation target:

- row 21: `bG3-_KfpskE`
- row 22: `-VNpaMQWGUE`
- row 23: `69XsLQQwo_M`
- row 24: `8ityiaa4j8c`
- row 25: `8tzBkeMR92g`
- row 26: `piuUBEWYeug`
- row 27: `ex-3Ywii0Qs`

Seven rows is safer than forcing the generic `8` to `12` target because the committed continuation bundle contains exactly seven blocked targets. Adding an eighth row would widen beyond the approved rows `21..27` or mix a different source bundle into the same population slice.

All future rows should use:

- `evidence_type`: `blocked_status`
- `source_granularity`: `blocked_status`
- `claim_type`: `metadata_status` or `blocker`
- `mechanical_readiness`: `blocked`
- `strategy_relevance`: `none`
- `title_only_warning`: `blocked_no_content_evidence` or `title_metadata_only`, depending on row wording
- `raw_artifact_status`: `no_raw_text_no_caption_url_no_generated_artifact`
- `corpus_strategy_boundary`: `corpus_line_only_no_strategy_change`

## 7. Required schema and layout requirements

The future population PR should use the Batch 02 compact overview plus per-row detail layout.

The compact overview table should include:

- `evidence_id`
- `claim_text`
- `source_granularity`
- `evidence_type`
- `claim_type`
- `mechanical_readiness`
- `strategy_relevance`
- `review_status`

Per-row details should include:

- `source_doc`
- `source_doc_section`
- `video_id`
- `playlist_or_batch`
- `doctrine_category`
- `setup_family`
- `blocker_reason`
- `unresolved_definition`
- `title_only_warning`
- `raw_artifact_status`
- `corpus_strategy_boundary`
- `notes`

The document should end with:

- row-count confirmation;
- source-granularity confirmation;
- title-only and source-evidence separation check;
- Strategy/corpus separation check;
- guardrail review;
- recommended next docs-only task.

## 8. Title-only and source-evidence separation rules

The future population PR must preserve these rules:

- compact titles may identify source rows but must not support content claims;
- promotional or outcome-style title language must remain metadata only;
- blocked caption access cannot be converted into summary-derived evidence;
- no row may infer a trading rule, doctrine conclusion, win-rate improvement, growth result, or profitability claim from a title;
- no row may quote or reconstruct raw subtitle, caption, transcript, or source-body text;
- no row may cite caption URLs, raw response bodies, downloaded media, ASR, CSV, JSON, `data/`, or `results` artifacts.

The future slice should explicitly state that no caption-body evidence was available for rows `21..27` in the committed continuation docs.

## 9. Strategy/corpus separation rules

The future population PR must stay inside the YouTube channel-wide corpus line.

Rules:

- rows should be blocked-status and metadata-status rows only;
- rows must not use `possible_strategy_ab_review_input` merely because a title sounds mechanical;
- rows must not change Strategy A/B/B2/C behavior, tests, parameters, configs, backtests, or conclusions;
- rows must not create Strategy C or authorize Strategy C work;
- rows must not recommend parameter optimization;
- rows must not treat corpus metadata as accepted implementation guidance;
- any later source-access recovery or Strategy-line use requires a separate issue and design decision.

## 10. Guardrail requirements

The future population PR should preserve these guardrails:

- committed repository docs only;
- no YouTube, DownSub, caption, subtitle, transcript-body, caption-URL, comment, live-chat, community-post, downloaded-media, ASR, market-data, broker/live, or external-source access;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw DownSub output, downloaded media, CSV, JSON database dump, generated candidate row, `data/`, or `results` artifact;
- no credentials, tokens, or secrets;
- no Doctrine Map v1 update and no Doctrine Map v2 creation/finalization;
- no Strategy A/B/B2/C behavior, tests, parameters, configs, backtests, or conclusions changed;
- no Strategy C creation;
- no parameter optimization;
- no market-data access;
- no broker/live behavior;
- no profitability claims or guarantees;
- no corpus findings mixed into executable Strategy A/B conclusions.

Recommended validation for the future population PR:

- `git diff --check`
- `git status --short`
- changed-file scope limited to the intended registry population document;
- row-count sanity check confirming exactly seven rows;
- controlled-value sanity check confirming every row uses `blocked_status` source granularity;
- mojibake/encoding sanity check over the changed Markdown file;
- forbidden-artifact path scan;
- local guardrail-equivalent public-readiness scan;
- repository guardrail workflow through the PR.

## 11. Recommended next docs-only task

Recommended next issue:

`[codex] Populate a narrow Batch 03 continuation blocked-status evidence registry slice`

Recommended scope:

- use committed repository docs only;
- add one evidence-registry population document for the Batch 03 continuation rows `21..27`;
- create exactly seven blocked-status rows;
- use the compact overview plus per-row detail layout;
- keep compact titles as metadata only;
- do not create content claims, doctrine claims, mechanical-rule candidates, Strategy A/B review inputs, or profitability conclusions from title metadata;
- do not create a full channel-wide registry, update doctrine maps, modify Strategy A/B/B2/C, access source material, run backtests, access market data, or change guardrail policy.

## 12. Planning decision

Planning decision:

`batch_03_continuation_blocked_status_slice_ready_for_future_population`

Reason: after the Batch 02 layout review, the next useful narrow registry slice is a blocked-status slice over the committed Batch 03 continuation rows `21..27`. This tests the registry's ability to preserve source-access blockers, title-only boundaries, and corpus/Strategy separation without inventing content evidence or widening source access.
