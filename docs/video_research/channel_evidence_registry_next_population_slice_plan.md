# Channel Evidence Registry Next Population Slice Plan

Task: `channel_evidence_registry_next_population_slice_plan`

Status: docs-only planning. This document chooses the next narrow committed-doc source set for a future evidence-registry population PR. It does not add registry rows, create a full channel-wide registry, update doctrine maps, or modify Strategy A/B/B2/C behavior.

## 1. Objective and scope

The objective is to use the committed source-granularity registry design and the Intermediate Batch 03 pilot to plan the next small evidence-registry population slice.

This plan:

- uses committed repository docs only;
- selects one narrow source bundle for a future population PR;
- defines selection criteria, row-count guidance, schema requirements, and layout guidance;
- preserves title-only versus summary-derived evidence separation;
- preserves the Strategy/corpus boundary.

This plan does not:

- access YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, downloaded media, ASR, market data, broker/live systems, or external sources;
- inspect or reconstruct raw caption, subtitle, or transcript text;
- create or populate the next evidence-registry slice;
- add or backfill evidence rows;
- create a full channel-wide registry;
- update Doctrine Map v1 or create/finalize Doctrine Map v2;
- modify Strategy A/B/B2/C rules, code, tests, parameters, configs, backtests, or conclusions;
- create Strategy C;
- perform parameter optimization;
- make profitability claims or guarantees;
- change guardrail policy.

## 2. Source docs used

Primary registry context:

- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03.md`
- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03_review.md`

Proposed next-slice source context:

- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_synthesis.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_completed_summary_audit.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_review.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_aggregate_report.md`

No non-repository source was used. Compact titles in the committed docs remain metadata only and must not be treated as project conclusions.

## 3. Pilot lessons used

The Intermediate Batch 03 pilot supports these planning rules:

- keep the next slice small enough for line-by-line review;
- use exactly one controlled `source_granularity` value per row;
- split rows when materially different source granularities would otherwise be mixed;
- keep `evidence_type` separate from `source_granularity`;
- keep `blocker_reason` separate from `unresolved_definition`;
- treat `mechanical_candidate` as a review label, not implementation approval;
- use `strategy_relevance` only as routing metadata;
- keep title metadata, summary-derived evidence, synthesis evidence, audit evidence, and blocked-status evidence visibly separate.

The pilot also shows that a single wide Markdown table is still acceptable around `10` rows, but larger or more detailed slices should use a compact overview plus per-row detail sections.

## 4. Next-slice selection criteria

The next population slice should satisfy all of these criteria:

| criterion | requirement |
| --- | --- |
| committed evidence only | Use only Git-safe committed docs already in this repository. |
| completed source bundle | Prefer a source set with per-video summaries, aggregate report, review, completed-summary audit, and synthesis. |
| narrow scope | Use one batch or similarly bounded source bundle, not a full channel-wide registry. |
| mixed claim coverage | Include enough variation to test process, risk, execution-boundary, visual-discretion, doctrine-only, and metadata/audit rows. |
| title-risk visibility | Include title-warning handling where compact titles contain outcome or hype language. |
| Strategy boundary | Keep all rows in the corpus line unless a future Strategy-line issue separately authorizes review. |
| reviewability | Keep the future row count small and avoid CSV, JSON, database, `data/`, or `results` artifacts. |

## 5. Proposed next committed-doc source set

Planning decision:

`next_population_slice_intermediate_batch_02_committed_bundle`

The next evidence-registry population PR should use Intermediate Batch 02 as the next narrow source set.

Recommended source bundle:

- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_synthesis.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_completed_summary_audit.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_review.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_aggregate_report.md`

Reason:

- Batch 02 is already summarized, reviewed, audited, and synthesized in committed docs.
- The synthesis consolidates process, risk, expectancy, short-term execution, line-governance, timeframe-boundary, and visual-discretion themes.
- The completed-summary audit records candidate-support and guardrail status without requiring new source access.
- The source bundle is narrower than a doctrine-map-wide or channel-wide backfill.
- It is distinct from the Batch 03 pilot, which helps test whether the schema generalizes across a second committed batch.

The future population PR may cite per-video Batch 02 summaries as row sources when needed, but it should not re-read or reconstruct raw subtitle/caption bodies.

## 6. Future population row-count guidance

The future population PR should target `8` to `12` evidence rows.

Suggested row mix:

- `2` journal or review-process rows;
- `1` expectancy or reward/risk row;
- `1` timeframe-consistency or execution-boundary row;
- `2` short-term setup or line-governance rows with visual-discretion blockers;
- `1` broad risk or growth-policy doctrine row;
- `1` metadata/audit boundary row;
- optional additional rows only if needed to represent a materially different source granularity or blocker class.

The future PR should stop before becoming a full Batch 02 registry. It should not exhaust all `32` Batch 02 candidates.

## 7. Required schema fields

The future population PR should include every field from the current registry design:

| field group | required fields |
| --- | --- |
| stable routing | `evidence_id`, `claim_text`, `video_id`, `playlist_or_batch`, `source_doc`, `source_doc_section` |
| evidence classification | `evidence_type`, `source_granularity`, `claim_type`, `doctrine_category`, `setup_family` |
| readiness and blockers | `mechanical_readiness`, `blocker_reason`, `unresolved_definition` |
| boundary and review | `strategy_relevance`, `title_only_warning`, `raw_artifact_status`, `corpus_strategy_boundary`, `review_status`, `notes` |

`source_granularity` must use the controlled value set from the design:

- `per_video_summary`
- `aggregate_inventory`
- `batch_synthesis`
- `completed_summary_audit`
- `blocked_status`
- `doctrine_map`
- `strategy_boundary_doc`

For the Batch 02 slice, likely values are `per_video_summary`, `aggregate_inventory`, `batch_synthesis`, and `completed_summary_audit`. `doctrine_map` and `strategy_boundary_doc` should not be used unless the future issue explicitly includes those source docs.

## 8. Layout guidance

The future Batch 02 population PR should use the larger-registry layout if it approaches the upper end of the target row range or if rows contain long blocker notes.

Recommended layout:

1. compact overview table with:
   - `evidence_id`
   - `claim_text`
   - `source_granularity`
   - `evidence_type`
   - `claim_type`
   - `mechanical_readiness`
   - `strategy_relevance`
   - `review_status`
2. per-row detail sections with:
   - source path and source section;
   - video ID and batch;
   - doctrine category and setup family;
   - blocker reason and unresolved definition;
   - title-only warning;
   - raw-artifact and Strategy/corpus boundary statements;
   - compact notes.
3. final validation and guardrail section.

A single wide table remains acceptable only if the future row set stays close to `8` rows and each note remains compact.

## 9. Title-only and source-evidence separation rules

The future population PR must preserve these rules:

- title metadata can identify a source row, but it cannot support content doctrine;
- compact title language such as outcome, performance, or hype wording must not become a project finding;
- summary-derived rows must cite committed paraphrased summary, aggregate, synthesis, audit, or review docs only;
- audit-derived rows can support completeness, boundary, and residual-risk status, but not trading-rule proof;
- blocked or unavailable source status cannot be converted into a content claim;
- no row may quote or reconstruct raw subtitle, caption, or transcript text.

The `title_only_warning` field should use design-controlled labels such as `title_metadata_only`, `summary_derived_not_title_only`, `mixed_title_and_summary_context`, or `blocked_no_content_evidence`.

## 10. Strategy/corpus separation rules

The future population PR must stay inside the YouTube channel-wide corpus line.

Rules:

- rows marked `possible_strategy_ab_review_input` or `mismatch_review_input` are routing labels only;
- no row may change Strategy A/B/B2/C behavior, tests, parameters, configs, backtests, or conclusions;
- no row may create Strategy C or authorize Strategy C work;
- no row may recommend parameter optimization;
- no row may treat corpus doctrine as accepted implementation guidance;
- any later Strategy-line use requires a separate issue and design decision.

Process, journal, risk, growth-policy, and behavior rows should usually remain `not_strategy_relevant`, `doctrine_only`, or `strategy_line_review_required` rather than executable-rule candidates.

## 11. Validation expectations for the future population PR

The future population PR should validate:

- `git diff --check`
- `git status --short`
- changed-file scope limited to the intended registry population doc;
- expected row count is within the planned `8` to `12` range or the PR explains why fewer rows are safer;
- every row has exactly one `source_granularity` value;
- every row has a title-warning value and raw-artifact status;
- no `data/`, `results`, CSV, JSON dump, generated artifact, raw transcript, raw subtitle, raw TXT/SRT/VTT, caption URL, downloaded media, credential, token, or secret is added;
- no market-data, broker/live, Strategy A/B/B2/C, optimization, backtest, or profitability claim is introduced.

The repository guardrail workflow should run through the PR before merge-gate review.

## 12. Recommended next docs-only task

Recommended next issue:

`[codex] Populate a narrow Batch 02 channel evidence registry slice`

Recommended scope:

- use committed repository docs only;
- add one Batch 02 evidence-registry population document;
- target `8` to `12` rows;
- use the compact overview plus per-row detail layout unless the final row set is short enough for a clean wide table;
- include `source_granularity` on every row;
- preserve title-only, raw-artifact, and Strategy/corpus guardrails;
- do not create a full channel-wide registry, update doctrine maps, modify Strategy A/B/B2/C, access source material, run backtests, access market data, or change guardrail policy.

## 13. Guardrails

This planning document preserves these guardrails:

- committed repository docs only;
- no YouTube, DownSub, caption, subtitle, transcript-body, caption-URL, comment, live-chat, community-post, downloaded-media, ASR, market-data, broker, live-system, or external-source access;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw DownSub output, downloaded media, CSV, JSON database dump, generated candidate rows, `data/`, or `results` artifact;
- no credentials, tokens, or secrets;
- no Doctrine Map v1 update and no Doctrine Map v2 finalization;
- no Strategy A/B/B2/C behavior, tests, parameters, configs, backtests, or conclusions changed;
- no Strategy C creation;
- no parameter optimization;
- no market-data access;
- no broker/live behavior;
- no profitability claims or guarantees;
- no corpus findings mixed into executable Strategy A/B conclusions.
