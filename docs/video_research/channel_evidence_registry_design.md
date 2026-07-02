# Channel Evidence Registry Design

Task: `channel_evidence_registry_design`

Status: design only. This document defines a future claim-level evidence registry for the YouTube channel-wide corpus line. It does not create the registry data table, extract all rows, update doctrine maps, or authorize Strategy A/B implementation changes.

## 1. Objective and scope

The objective is to design a Git-safe evidence registry that can connect committed video summaries, audits, syntheses, and doctrine-map observations to small, reviewable research claims.

The registry should make later review easier by answering:

- which committed document supports a claim;
- whether the claim came from metadata, a paraphrased summary, an audit, a synthesis, or doctrine mapping;
- whether the claim is mechanical-looking, discretionary, doctrine-only, or not automation-ready;
- whether title metadata is being kept separate from transcript-derived evidence;
- what blocks a claim from Strategy A/B review or mechanical testing.

This design stays inside the YouTube channel-wide corpus line. It does not mix corpus findings into Strategy A/B conclusions and does not define executable strategy rules.

## 2. Source docs considered

This design uses committed repository docs only.

Primary context:

- `AGENTS.md`
- `docs/video_research/channel_full_corpus_research_plan.md`
- `docs/video_research/channel_video_inventory_design.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/channel_doctrine_evidence_index_v1.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal.md`
- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03.md`
- `docs/video_research/channel_evidence_registry_pilot_intermediate_batch_03_review.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_synthesis.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`

The design does not inspect YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, downloaded media, ASR output, market data, broker systems, or any non-approved external source.

## 3. Registry purpose

The registry should be a claim-level ledger, not a raw-source archive.

Each future row should represent one compact research claim, candidate, blocker, or doctrine observation that can be traced back to committed Git-safe docs. A row may point to one source video, a batch report, a completed-summary audit, a synthesis, or a doctrine-map document.

The registry should support these review tasks:

- trace a doctrine claim back to supporting committed summaries and reports;
- compare similar claims across batches without re-reading every summary;
- separate metadata-only rows from summary-derived evidence;
- identify mechanical candidates that still depend on visual discretion;
- preserve blockers such as undefined thresholds, unresolved anchors, or personal risk tolerance;
- mark whether a claim may be useful for a future Strategy A/B review without changing Strategy A/B.

It should not become:

- a transcript store;
- a subtitle or caption URL index;
- a raw metadata dump;
- a generated candidate CSV;
- a backtest input table;
- a Strategy B or Strategy B2 specification.

## 4. Proposed schema

The future registry should be row-oriented. One row should describe one claim or candidate at the smallest useful review level.

| field | required | purpose |
| --- | --- | --- |
| `evidence_id` | yes | Stable ID for the registry row. Suggested format: `CER-YYYY-NNN` or a scoped prefix such as `CER-I03-001`. |
| `claim_text` | yes | Compact paraphrase of the claim. Must not copy raw transcript or subtitle text. |
| `video_id` | optional | Source video ID when a claim traces to a specific committed summary. Use `not_applicable` for synthesis-only or doctrine-map rows. |
| `playlist_or_batch` | yes | Source grouping, such as `lightweight_batch_07`, `intermediate_batch_03`, or `doctrine_map_v1`. |
| `source_doc` | yes | Repo-relative path to the committed Git-safe document supporting the row. |
| `source_doc_section` | optional | Short section label or table name if useful for review. Do not use raw transcript offsets. |
| `evidence_type` | yes | Classifies how the evidence reached Git. See taxonomy below. |
| `source_granularity` | yes | Classifies the level of committed document structure supporting the row, such as one summary, an aggregate inventory, a synthesis, an audit, a doctrine map, or a boundary document. See taxonomy below. |
| `claim_type` | yes | Research claim category: entry, stop, TP, RR, management, risk, study process, behavior, capital progression, no-trade filter, metadata status, or blocker. |
| `doctrine_category` | optional | Higher-level doctrine bucket when applicable, such as timeframe hierarchy, entry confirmation, stop/invalidation, TP/exit, horizontal-line doctrine, or discretionary blockers. |
| `setup_family` | optional | Pattern, wave, Dow, trend, range, support/resistance, process, behavior, capital, or other scoped family. |
| `mechanical_readiness` | yes | Conservative readiness label. See readiness taxonomy below. |
| `blocker_reason` | optional | Reason the row cannot be translated mechanically yet. |
| `unresolved_definition` | optional | Specific term or anchor requiring later definition. |
| `strategy_relevance` | yes | Routing label for later review. This is not implementation approval. |
| `title_only_warning` | yes | Explicitly records whether the row is title-only, summary-derived, or mixed with title metadata. |
| `raw_artifact_status` | yes | Confirms raw text, subtitle files, caption URLs, CSV/JSON dumps, data files, and result files are not stored in the row. |
| `corpus_strategy_boundary` | yes | Confirms the row remains corpus evidence unless a later Strategy-line review authorizes integration. |
| `review_status` | yes | Current review state for the row. |
| `notes` | optional | Compact review note, blocker note, or contradiction note. |

The registry should prefer explicit empty values such as `not_applicable`, `unknown`, or `unresolved` over silent omission when the distinction matters for review.

## 5. Evidence-type taxonomy

Recommended `evidence_type` values:

| value | use |
| --- | --- |
| `metadata_only` | Video ID, playlist order, title, availability, or status evidence only. This must not support transcript-derived claims. |
| `summary_derived` | Claim derived from a committed paraphrased per-video summary. |
| `audit_derived` | Claim or blocker derived from a committed completed-summary audit or quality review. |
| `synthesis_derived` | Claim derived from a committed batch, playlist, or cross-batch synthesis. |
| `doctrine_derived` | Claim derived from a committed doctrine map, doctrine evidence index, doctrine review, or doctrine proposal. |
| `strategy_boundary_derived` | Boundary or mismatch note derived from committed Strategy A/B separation docs. |
| `blocked_status` | Status row documenting inaccessible, ambiguous, blocked, or unresolved source access without creating content claims. |

Rules:

- `metadata_only` rows may identify candidate topics, source ordering, or access status, but they must not become content evidence.
- `blocked_status` rows may record why evidence does not exist yet.
- `summary_derived`, `audit_derived`, `synthesis_derived`, and `doctrine_derived` rows must point to committed Git-safe docs only.
- No row may point to raw local transcript files, raw subtitle files, caption URLs, downloaded media, generated CSV/JSON, `data/`, or `results/`.

## 6. Source-granularity taxonomy

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

`source_granularity` is separate from `evidence_type` because the two fields answer different review questions.

- `evidence_type` records how the evidence reached the repository, such as metadata-only, summary-derived, audit-derived, synthesis-derived, doctrine-derived, strategy-boundary-derived, or blocked-status evidence.
- `source_granularity` records the level of committed document structure that supports the row, such as a single per-video summary, a batch synthesis, an audit boundary, or a doctrine map.

This separation prevents reviewers from treating one-video evidence, batch-level synthesis, audit status, and doctrine-map observations as if they had the same review scope. It also keeps blocked-status rows and Strategy-boundary rows visibly separate from content claims.

Rules:

- Use exactly one `source_granularity` value per row unless a later review explicitly approves multiple values.
- If a claim combines materially different granularities, split it into separate rows.
- If splitting would make the claim misleading, keep the row narrow and explain the dependency in `notes`.
- `blocked_status` granularity must not support content or doctrine claims.
- `aggregate_inventory` should not be treated as stronger evidence than the summary, synthesis, or audit context that explains the claim.
- `doctrine_map` and `strategy_boundary_doc` values do not authorize Strategy A/B/B2/C changes.

## 7. Claim-type taxonomy

Recommended `claim_type` values:

| value | examples |
| --- | --- |
| `entry` | confirmation, reaction, reference candle, pullback, false-break recovery |
| `stop` | invalidation anchor, stop placement, stop width, stop movement boundary |
| `tp` | initial target, structural target, partial target, final target |
| `rr` | risk/reward threshold, tolerance, contextual RR caveat |
| `management` | break-even, partial exit, protective exit, advanced management warning |
| `risk` | sizing, reserve buffer, growth gate, survival constraint |
| `study_process` | pre-study objective, post-study extraction, review workflow |
| `behavior` | outsourced judgment warning, shortcut filter, negative success filter |
| `capital_progression` | staged account growth, stabilization, reserve-aware behavior |
| `no_trade_filter` | range quality, trendless state, dirty structure, insufficient room |
| `metadata_status` | source ordering, caption availability, blocked row, summary status |
| `blocker` | visual discretion, undefined term, insufficient repetition, ambiguity |

The registry may allow multiple values only if the row remains readable. If a row becomes too broad, split it into separate claim rows.

## 8. Readiness and blocker taxonomy

Recommended `mechanical_readiness` values:

| value | meaning |
| --- | --- |
| `mechanical_candidate` | The claim has checklist or specification shape, but still needs later definition and review before code or tests. |
| `needs_visual_discretion` | The claim depends on chart-reading judgment such as clean wave, valid line, touch quality, target realism, or scenario coherence. |
| `doctrine_only` | Useful channel doctrine or behavior guidance, but not a trading-system rule candidate. |
| `not_automation_ready` | Personal, ambiguous, insufficiently repeated, psychology-bound, or otherwise unsafe for mechanical translation. |
| `metadata_only` | Navigation/status evidence only; not content evidence. |
| `blocked` | Evidence is unavailable or source access is blocked under current guardrails. |

Recommended `blocker_reason` values:

- `visual_discretion`
- `undefined_threshold`
- `undefined_anchor`
- `missing_timeframe_hierarchy`
- `insufficient_repetition`
- `one_off_or_case_bound`
- `personal_risk_tolerance`
- `psychology_or_behavior_only`
- `title_only_metadata`
- `caption_access_blocked`
- `ambiguous_source_access`
- `strategy_line_review_required`

Rules:

- `mechanical_candidate` does not mean ready for implementation.
- `needs_visual_discretion` must name the unresolved visual term when possible.
- `doctrine_only` rows may later inform review questions, but they should not become code requirements by default.
- `blocked` rows should recommend wait, no-op, or human decision rather than source-access widening.

## 9. Title-only vs summary-derived evidence rules

The registry must prevent title language from becoming a project conclusion.

Use `title_only_warning` values:

| value | meaning |
| --- | --- |
| `title_metadata_only` | The row uses title or playlist metadata only. It cannot support doctrine or content claims. |
| `summary_derived_not_title_only` | The row is supported by a committed paraphrased summary, audit, synthesis, or doctrine doc. |
| `mixed_title_and_summary_context` | Title metadata exists in the source doc, but the claim itself must cite only the paraphrased summary or review finding. |
| `blocked_no_content_evidence` | Caption/body access or other source access is blocked; no content claim should be created. |

Registry rules:

- Hype words or outcome claims in titles must remain metadata only.
- A row cannot claim a method works, wins, makes money, or is profitable because a title says so.
- If a committed summary includes a compact title, the registry must distinguish that title from the summary-derived claim.
- Blocked rows cannot be converted into summary-derived evidence from title metadata alone.

## 10. Strategy/corpus separation rules

The registry is a corpus-line artifact. It may support later Strategy A/B review only by creating traceable questions or mismatch candidates.

Use `strategy_relevance` values:

| value | meaning |
| --- | --- |
| `none` | Not relevant to Strategy A/B review. |
| `possible_strategy_ab_review_input` | May be useful for later review, but not implementation-ready. |
| `mismatch_review_input` | May inform a future mismatch-analysis PR if separately authorized. |
| `not_strategy_relevant` | Explicitly outside Strategy A/B, such as pure study-process or behavior context. |
| `strategy_line_review_required` | Cannot move further without a separate Strategy-line issue or design decision. |

Rules:

- A registry row must not modify Strategy A/B/B2/C behavior, tests, parameters, configs, or conclusions.
- A row must not recommend parameter optimization.
- A row must not create Strategy C.
- A row must not treat corpus doctrine as accepted implementation guidance.
- Future Strategy review must cite evidence rows and source docs, but must still make a separate design decision before changing code or backtests.

## 11. Larger-registry Markdown layout

A small pilot can use one wide Markdown table to test every field in one place. Larger registry docs should avoid a single very wide table because review becomes error-prone and field boundaries become hard to inspect.

Recommended larger-registry layout:

1. Start with a compact overview table containing stable routing fields:
   - `evidence_id`
   - `claim_text`
   - `source_granularity`
   - `evidence_type`
   - `claim_type`
   - `mechanical_readiness`
   - `strategy_relevance`
   - `review_status`
2. Add per-row detail sections for:
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
3. End with a short validation and guardrail section.

This structure keeps the registry Git-reviewable while avoiding CSV, JSON, database dumps, raw artifacts, or generated result files unless a future issue explicitly and narrowly authorizes a different format.

## 12. Review workflow

Recommended future workflow:

1. Select a narrow committed-doc source set, such as one batch synthesis and its audit.
2. Extract only compact claim rows from those docs.
3. Mark every row with `evidence_type`, `source_granularity`, `mechanical_readiness`, `title_only_warning`, and `strategy_relevance`.
4. Run a forbidden-artifact scan before commit.
5. Review rows for overclaiming, title-only leakage, raw-text leakage, and Strategy/corpus mixing.
6. Only after review, use the rows to support doctrine-map review or a separately authorized Strategy-line mismatch plan.

The first larger registry population PR should still be narrow, not a full backfill. A reasonable next population step would update the existing Intermediate Batch 03 pilot rows to use `source_granularity` and the larger-registry Markdown layout before any broader corpus backfill.

## 13. Validation and guardrails

Future registry PRs should validate:

- changed files are limited to the intended registry design or registry pilot docs;
- no `data/` or `results/` files are added;
- no raw market data, normalized market CSV, generated candidate CSV, generated result CSV, or backtest output is added;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw DownSub output, downloaded video, downloaded audio, or ASR output is added;
- no credentials, tokens, or secrets are added;
- no market-data API, broker API, order-placement, auto-trading, or live-trading behavior is added;
- no Strategy A/B/B2/C behavior, tests, parameters, configs, or conclusions are changed;
- no parameter optimization or profitability claim is made;
- title metadata is not treated as transcript-derived evidence;
- blocked source access is recorded as blocked rather than worked around.

Recommended validation commands for docs-only registry work:

```powershell
git diff --check
git status --short
```

When registry rows are added later, also run a changed-file sanity check and a forbidden-artifact path/content scan over the changed files.

## 14. Design decision

Readiness decision:

`channel_evidence_registry_design_ready_with_source_granularity`

Reason: the future channel evidence registry should be claim-level, source-doc-traceable, and conservative. It should preserve the separation among metadata, paraphrased summary evidence, audits, syntheses, doctrine observations, mechanical candidates, discretionary blockers, source granularity, and Strategy relevance. It should not store raw artifacts, generated data, or executable strategy decisions.

## 15. Recommended next docs-only task

Recommended next issue:

`[codex] Update Intermediate Batch 03 pilot evidence registry rows with source_granularity`

Recommended scope:

- use committed repository docs only;
- update the existing Intermediate Batch 03 pilot registry rows to include `source_granularity`;
- keep the row set unchanged unless a separate issue authorizes a new pilot or backfill;
- use the controlled value set from this design;
- consider shifting the pilot toward compact overview plus per-row details if the wide table remains hard to review;
- do not update Doctrine Map v1, create or finalize Doctrine Map v2, modify Strategy A/B/B2/C, run backtests, access source material, or create generated artifacts.

This should be a docs-only schema-application task before any larger registry backfill.
