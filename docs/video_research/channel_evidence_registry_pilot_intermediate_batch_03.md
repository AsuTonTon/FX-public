# Channel Evidence Registry Pilot: Intermediate Batch 03

Task: `channel_evidence_registry_pilot_intermediate_batch_03`

Status: docs-only pilot. This file tests the channel evidence registry design on a small set of committed Intermediate Batch 03 evidence rows. It is not a full registry, not final channel doctrine, and not an implementation specification.

## 1. Objective and scope

The objective is to validate whether the claim-level registry schema from `docs/video_research/channel_evidence_registry_design.md` can capture a compact, reviewable set of evidence rows from the committed Intermediate Batch 03 synthesis and related audit context.

This pilot:

- uses committed repository docs only;
- creates a small Markdown evidence table with `10` rows;
- applies the adopted `source_granularity` field to every pilot row;
- keeps title metadata separate from summary-derived and synthesis-derived evidence;
- preserves conservative readiness, blocker, and Strategy-relevance labels;
- stays inside the YouTube channel-wide corpus line.

This pilot does not:

- create a full channel-wide registry;
- backfill every Intermediate Batch 03 candidate;
- access YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, downloaded media, ASR, market data, broker/live systems, or external sources;
- add raw transcript text, subtitle text, raw TXT/SRT/VTT files, caption URLs, CSV, JSON, `data/`, `results/`, credentials, tokens, or secrets;
- update Doctrine Map v1 or create/finalize Doctrine Map v2;
- modify Strategy A/B/B2/C behavior, tests, parameters, configs, or conclusions;
- run backtests, perform optimization, or make profitability claims.

## 2. Source docs used

Primary source docs:

- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_completed_summary_audit.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_aggregate_report.md`

The pilot did not use raw caption bodies or non-repository sources. The compact titles in the committed docs are treated as metadata only and do not support content or outcome claims.

## 3. Pilot selection rules

Rows were selected to test whether the schema can represent mixed evidence without overclaiming:

- include several claim types rather than one setup family;
- prefer source rows already summarized in the Batch 03 synthesis or aggregate candidate inventory;
- include both mechanical-looking candidates and discretionary blockers;
- include process, behavior, capital progression, and metadata/status rows;
- stop at a small pilot set instead of exhausting all 27 audited candidates.

## 4. Pilot evidence registry table

| evidence_id | claim_text | video_id | playlist_or_batch | source_doc | source_doc_section | evidence_type | source_granularity | claim_type | doctrine_category | setup_family | mechanical_readiness | blocker_reason | unresolved_definition | strategy_relevance | title_only_warning | raw_artifact_status | corpus_strategy_boundary | review_status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `CER-I03-001` | Batch 03 frames stronger entry quality as a gating problem: timing, higher-timeframe support, structural plausibility, and pattern context must be checked before action. | `not_applicable` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md` | `Compact synthesis` | `synthesis_derived` | `batch_synthesis` | `entry` | `entry_confirmation` | `process` | `needs_visual_discretion` | `visual_discretion` | `timing condition; structural plausibility; higher-timeframe support` | `possible_strategy_ab_review_input` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Useful as an umbrella row; not specific enough for code or tests. |
| `CER-I03-002` | The entry-timing gate says not to enter until the actual timing condition is present. | `eBJ9OwHXPz8` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_aggregate_report.md` | `Mechanical-rule candidate inventory` | `summary_derived` | `aggregate_inventory` | `entry` | `entry_confirmation` | `timing` | `mechanical_candidate` | `undefined_threshold` | `actual timing condition` | `possible_strategy_ab_review_input` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Checklist-shaped, but the trigger remains undefined. |
| `CER-I03-003` | Wave-shape plausibility can filter out trade paths that look structurally unnatural for the traded market. | `eBJ9OwHXPz8` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_aggregate_report.md` | `Mechanical-rule candidate inventory` | `summary_derived` | `aggregate_inventory` | `no_trade_filter` | `timeframe_hierarchy` | `wave` | `needs_visual_discretion` | `visual_discretion` | `structurally plausible wave path` | `possible_strategy_ab_review_input` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Good blocker test for visually discretionary language. |
| `CER-I03-004` | Chart-pattern use depends on context, location, line quality, stop logic, and target logic rather than pattern names alone. | `UnRs896Utnc` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md` | `Repeated doctrine and principles` | `synthesis_derived` | `batch_synthesis` | `entry` | `horizontal_line_doctrine` | `pattern` | `needs_visual_discretion` | `visual_discretion` | `context; location; line quality; target logic` | `possible_strategy_ab_review_input` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Captures a repeated context requirement without creating a pattern rule. |
| `CER-I03-005` | A double-bottom/top stop candidate anchors the stop slightly beyond the second point, but buffer sizing is unresolved. | `UnRs896Utnc` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_aggregate_report.md` | `Mechanical-rule candidate inventory` | `summary_derived` | `aggregate_inventory` | `stop` | `stop_invalidation` | `pattern` | `mechanical_candidate` | `undefined_anchor` | `second point; buffer size` | `possible_strategy_ab_review_input` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Mechanical-looking enough for future review, not ready for implementation. |
| `CER-I03-006` | Dow-style trend labeling distinguishes a broken prior trend from confirmed opposite-trend structure by preserving a trendless transition state. | `fbTWY8U4h9A` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md` | `Compact synthesis; Unresolved definitions and blockers` | `synthesis_derived` | `batch_synthesis` | `blocker` | `timeframe_hierarchy` | `dow` | `mechanical_candidate` | `undefined_threshold` | `meaningful swing; opposite trend confirmation; state transition` | `mismatch_review_input` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Candidate is promising for later review but depends on swing definitions. |
| `CER-I03-007` | Study-process rows require defining the learning objective before consuming material and checking what changed afterward. | `not_applicable` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md` | `Compact synthesis; Candidate-family synthesis` | `synthesis_derived` | `batch_synthesis` | `study_process` | `study_process` | `process` | `mechanical_candidate` | `undefined_threshold` | `objective taxonomy; extracted outcome standard` | `not_strategy_relevant` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Process-checklist candidate, not a trading signal. |
| `CER-I03-008` | Behavior-veto doctrine treats shortcut seeking, outsourced judgment, and status behavior as anti-progress filters. | `not_applicable` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md` | `Compact synthesis; Candidate-family synthesis` | `synthesis_derived` | `batch_synthesis` | `behavior` | `behavior_filter` | `behavior` | `doctrine_only` | `psychology_or_behavior_only` | `closed behavior-veto rubric` | `not_strategy_relevant` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Useful corpus doctrine; should not be routed into Strategy A/B rules. |
| `CER-I03-009` | Capital progression is staged: prove stability before growth, then shift toward reserve-aware stabilization after the growth phase. | `fexGcPTNlN0` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md` | `Compact synthesis; Unresolved definitions and blockers` | `synthesis_derived` | `batch_synthesis` | `capital_progression` | `risk_management` | `capital` | `doctrine_only` | `personal_risk_tolerance` | `seed target; proof window; reserve ratio` | `not_strategy_relevant` | `summary_derived_not_title_only` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Keeps account-policy doctrine separate from strategy logic. |
| `CER-I03-010` | The six selected Batch 03 rows have committed summaries and passed the completed-summary audit with notes, while later rows remain outside completed-summary claims. | `not_applicable` | `intermediate_batch_03` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_completed_summary_audit.md` | `Target-Row and Summary-File Completeness` | `audit_derived` | `completed_summary_audit` | `metadata_status` | `not_applicable` | `metadata` | `metadata_only` | `title_only_metadata` | `not_applicable` | `none` | `mixed_title_and_summary_context` | `no_raw_artifact_stored` | `corpus_only_until_separate_strategy_review` | `pilot_selected` | Status row tests registry handling for coverage and boundary evidence. |

## 5. Title-only vs summary-derived evidence check

This pilot uses compact title metadata only to identify source rows already represented in committed docs. It does not treat title language as evidence that a method works, wins, or produces income.

Rows `CER-I03-001` through `CER-I03-009` are summary-, synthesis-, or audit-derived content rows. Row `CER-I03-010` is a metadata/status boundary row that records coverage and audit status rather than content doctrine.

No row relies on raw transcript text, subtitle text, caption URLs, raw DownSub output, or downloaded media.

## 6. Readiness and blocker review

The pilot confirms that the registry needs both `mechanical_readiness` and `blocker_reason` fields:

- `mechanical_candidate` rows still require explicit unresolved-definition fields because they are not ready for implementation.
- `needs_visual_discretion` rows need a named visual blocker; otherwise the registry hides why the row is not testable.
- `doctrine_only` rows are necessary for behavior and capital-process content that matters to corpus review but should not enter Strategy A/B by default.
- `metadata_only` rows are useful for audit boundaries and availability status, but they must remain separate from content evidence.

## 7. Strategy/corpus separation check

This pilot stays in the YouTube channel-wide corpus line. It creates reviewable evidence rows only.

It does not:

- change Strategy A/B/B2/C code, tests, parameters, configs, or conclusions;
- convert corpus doctrine into executable Strategy A/B rules;
- authorize a Strategy-line mismatch review;
- run backtests or optimization;
- access market data or broker/live systems.

Rows marked `possible_strategy_ab_review_input` or `mismatch_review_input` are routing labels only. They require a separate Strategy-line issue or design decision before any rule, test, or backtest change.

## 8. Pilot findings and schema adjustment recommendations

Pilot decision:

`channel_evidence_registry_pilot_intermediate_batch_03_source_granularity_applied`

Findings:

- The proposed schema is usable for a small Markdown pilot.
- The adopted `source_granularity` field now has exactly one controlled value on every existing pilot row.
- The existing row set remains unchanged at `10` rows; no evidence rows were added, removed, or replaced.
- The row assignments distinguish aggregate-inventory rows from batch-synthesis rows and the completed-summary-audit boundary row.
- The `title_only_warning` field is important because Batch 03 committed docs contain compact titles with promotional language that must not become project conclusions.
- The `unresolved_definition` field should remain separate from `blocker_reason`; otherwise the row loses the exact term that blocks mechanical translation.
- `strategy_relevance` should continue using routing labels rather than approval labels.
- The wide table remains acceptable for this `10`-row pilot after adding `source_granularity`, but larger registry docs should use the design's compact overview plus per-row detail layout.

## 9. Recommended next docs-only task

Recommended next task:

`[codex] Use the source_granularity pilot to plan the next narrow channel evidence registry population slice`

Reason:

- the pilot now applies the adopted schema field to every existing row;
- the next task can choose a narrow committed-doc source set before any larger registry backfill;
- the next task should remain docs-only and should not create a full channel-wide registry yet.

## 10. Guardrails

This pilot preserved these guardrails:

- committed repository docs only;
- no YouTube, DownSub, caption, subtitle, transcript-body, caption-URL, comment, live-chat, community-post, downloaded-media, ASR, market-data, broker, live-system, or external-source access;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw DownSub output, downloaded media, CSV, JSON database dump, generated candidate rows, `data/`, or `results` artifact;
- no credentials, tokens, or secrets;
- no Doctrine Map v1 update and no Doctrine Map v2 finalization;
- no Strategy A/B/B2/C behavior, tests, parameters, configs, or conclusions changed;
- no Strategy C creation;
- no parameter optimization;
- no backtests;
- no market data;
- no broker/live behavior;
- no profitability claims or guarantees;
- no corpus findings mixed into executable Strategy A/B conclusions.
