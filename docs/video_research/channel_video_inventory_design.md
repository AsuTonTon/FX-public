# Channel Video Inventory Design

Task: `channel_video_inventory_design`

Status: design only. This document defines the inventory layer for the full-channel YouTube corpus research track. It does not collect, fetch, scrape, download, or commit any actual YouTube inventory data.

## 1. Objective

The objective is to design a safe and reproducible video inventory layer for the full-channel corpus research track.

The future inventory should support later work:

- Transcript availability survey.
- Lightweight per-video summaries.
- Theme classification.
- Doctrine extraction.
- Strategy A/B gap analysis.

This document only defines the inventory structure, safety rules, validation expectations, and review workflow. It does not generate the inventory itself and does not inspect the channel.

## 2. Relationship to PR #10 Plan

PR #10 added `docs/video_research/channel_full_corpus_research_plan.md`, which created the overall full-channel corpus research plan.

This document expands only the inventory-design portion of that plan:

- PR #10 created the overall research plan.
- This PR designs the video inventory structure and process.
- Later PRs may generate inventory artifacts, but this PR does not.

The inventory design should be treated as a bridge between the high-level corpus plan and any future metadata or transcript-availability work. It should not be treated as evidence for Strategy A/B changes.

## 3. In Scope

This design includes:

- Proposed inventory schema.
- Field definitions.
- Allowed values and enums.
- Validation rules.
- Local-only raw artifact policy.
- Git-safe derived artifact policy.
- Review workflow.
- Inventory update workflow.
- Quality controls.
- Acceptance criteria for a future inventory-generation PR.

## 4. Out of Scope

This design explicitly excludes:

- Fetching actual YouTube data.
- Scraping YouTube.
- Calling YouTube APIs.
- Downloading videos.
- Downloading transcripts or subtitles.
- Committing raw transcripts.
- Committing subtitle full text.
- Committing raw metadata dumps.
- Committing generated CSVs.
- Market data.
- Broker APIs.
- Strategy A/B code changes.
- Strategy A/B parameter changes.
- Backtests.
- Strategy C.
- Profitability claims.

## 5. Inventory Schema

The canonical inventory should be row-oriented. Each row represents one video candidate in the channel corpus. A future generator may store the inventory locally as CSV or JSON, but Git commits should use only approved derived artifacts.

| Field | Type | Required | Allowed values | Git-safe | Notes |
| --- | --- | --- | --- | --- | --- |
| `video_id` | string | required | YouTube video ID format | yes | Primary key. Must be unique. |
| `canonical_url` | string | required | `https://www.youtube.com/watch?v={video_id}` | yes | Must match `video_id`. |
| `title` | string | required | compact title text | yes | Title is allowed when used as compact metadata. |
| `published_at` | string | optional | ISO 8601 date/time or date | yes | Use `unknown` only if the source cannot provide it. |
| `duration_seconds` | integer | optional | non-negative integer | yes | Normalized duration. |
| `duration_raw` | string | optional | source-native duration | yes | Example: ISO 8601 duration or page text. |
| `channel_id` | string | optional | channel ID or `unknown` | yes | Should be stable when known. |
| `channel_name` | string | optional | channel display name | yes | Compact metadata only. |
| `description_available` | string | required | `yes`, `no`, `unknown`, `blocked` | yes | Do not include full descriptions in the inventory. |
| `transcript_available` | string | required | see enum | yes | Status only. No transcript text. |
| `transcript_type` | string | required | see enum | yes | Source classification only. |
| `transcript_language` | string | optional | BCP 47 code, language name, `unknown`, `unavailable` | yes | Example: `ja`, `en`, `unknown`. |
| `transcript_quality` | string | required | see enum | yes | Quality estimate, not text. |
| `metadata_source` | string | required | see enum | yes | The source category used to create the row. |
| `collection_method` | string | required | see enum | yes | The collection mechanism category. |
| `collection_date` | string | required | ISO 8601 date | yes | Date the row metadata was collected or refreshed. |
| `title_detected_themes` | list[string] | optional | taxonomy labels | yes | Weak labels inferred from title only. |
| `transcript_confirmed_themes` | list[string] | optional | taxonomy labels | yes | Strong labels from derived transcript review only. No transcript text. |
| `priority` | string | required | see enum | yes | Research priority, not trading priority. |
| `strategy_relevance` | list[string] | required | see enum | yes | Use multiple labels when needed. |
| `summary_status` | string | required | see enum | yes | Tracks summary progress. |
| `review_status` | string | required | see enum | yes | Tracks human/Codex review state. |
| `notes_path` | string | optional | repo-relative derived notes path or empty | yes | Must point only to Git-safe derived notes. |
| `raw_local_path` | string | optional | ignored local path or empty | conditional | Only local references under ignored paths. Do not commit raw files. |
| `do_not_commit_raw` | boolean | required | `true`, `false` | yes | Must be `true` for rows tied to raw local material. |
| `reviewer` | string | optional | GitHub handle, local reviewer name, `unassigned` | yes | Use `unassigned` when not reviewed. |
| `last_reviewed_at` | string | optional | ISO 8601 date/time or empty | yes | Updated only after review. |
| `blocked_reason` | string | optional | compact reason or empty | yes | No raw transcript, subtitle, or copied description text. |

Schema notes:

- The inventory should not contain transcript text fields.
- The inventory should not contain subtitle text fields.
- The inventory should not contain downloaded media paths except local-only references under ignored paths.
- `title_detected_themes` and `transcript_confirmed_themes` must stay separate.
- `strategy_relevance` is for research routing only and must not imply a Strategy A/B change.

## 6. Recommended Enums

`description_available`:

- `yes`
- `no`
- `unknown`
- `blocked`

`transcript_available`:

- `yes`
- `no`
- `unknown`
- `blocked`

`transcript_type`:

- `manual_caption`
- `auto_caption`
- `external_manual`
- `unavailable`
- `unknown`

`transcript_quality`:

- `high`
- `medium`
- `low`
- `unusable`
- `unknown`

`metadata_source`:

- `manual`
- `youtube_page`
- `yt_dlp_flat_playlist`
- `youtube_data_api`
- `other`

`collection_method`:

- `manual_entry`
- `local_script`
- `external_tool`
- `api`
- `unknown`

`priority`:

- `high`
- `medium`
- `low`
- `exclude`

`strategy_relevance`:

- `tp_selection`
- `stop_invalidation`
- `entry_logic`
- `trend_filter`
- `range_filter`
- `risk_reward`
- `trade_management`
- `psychology_only`
- `not_relevant`
- `unknown`

`summary_status`:

- `not_started`
- `metadata_only`
- `summary_draft`
- `summary_reviewed`
- `blocked`

`review_status`:

- `unreviewed`
- `needs_review`
- `reviewed`
- `excluded`
- `blocked`

## 7. Git-Safe vs Local-Only Artifacts

Git-safe artifacts:

- Schema document.
- Inventory design document.
- Small manually curated sample rows using fake/example IDs only.
- Derived summary templates.
- Taxonomy references.
- Review process documents.

Local-only artifacts:

- Raw YouTube metadata dumps.
- Full generated inventory CSV/JSON if produced by scraping or API.
- Raw transcript files.
- Raw subtitle files.
- Downloaded video or audio.
- Large generated outputs.
- Processing logs containing transcript text.

Recommended ignored local paths:

- `data/video_research/channel_inventory_raw/`
- `data/video_research/transcripts_raw/`
- `results/video_research/channel_corpus/`

Future PRs must verify these paths are ignored before generating local artifacts. If ignored-path protection is uncertain, stop before collection and commit only the design or report.

## 8. Derived Inventory Policy

A derived inventory artifact may be committed only when it is compact, reviewable, and free of raw copied source content.

A committed derived inventory must:

- Avoid raw transcript text.
- Avoid full descriptions if they are large or copied verbatim.
- Avoid raw scraped JSON.
- Include only compact metadata required for research navigation.
- Be small enough for review.
- Be reproducible from local-only raw sources.
- Include a generation note if produced by a script.
- Not include credentials, tokens, cookies, or private data.

If uncertain, keep the artifact local-only and commit only a report. The report may include counts, validation status, known blockers, and schema conformance notes.

## 9. Priority Rules

High priority:

- TP selection.
- Target / 利確.
- Half profit / 半利.
- Break-even / 建値.
- Stop / invalidation / 損切り.
- Left-side highs/lows / 左側高値安値.
- 3-wave / wave completion.
- Range avoidance.
- Losing patterns.

Medium priority:

- Trend context.
- EMA / moving averages.
- Multiple timeframes.
- Pullbacks.
- Support/resistance.
- Risk/reward.
- Trade management.

Low priority:

- Mindset-only.
- Platform usage.
- Generic commentary.
- News or market commentary without rule content.

Exclude:

- Unrelated videos.
- Shorts or clips with no strategic content, unless later evidence says they matter.
- Duplicate reposts, unless they contain unique strategy explanation.

Priority rules should remain conservative. A high-priority label means the video should be reviewed earlier for research, not that its content is correct or mechanically actionable.

## 10. Inventory Review Workflow

Stage 1: metadata-only inventory

- Collect video ID, URL, title, date, and duration.
- Do not include transcript text.
- Do not include full descriptions.

Stage 2: transcript availability survey

- Record status only.
- Keep raw transcript files local-only.
- Do not add raw transcript text to Git.

Stage 3: title-based theme detection

- Assign weak theme labels.
- Keep these labels in `title_detected_themes`.
- Do not treat title-only labels as doctrine evidence.

Stage 4: transcript-confirmed theme detection

- Assign strong theme labels only after derived transcript review.
- Keep these labels in `transcript_confirmed_themes`.
- Store only derived summaries or compact notes in Git.

Stage 5: priority review

- Assign `high`, `medium`, `low`, or `exclude`.
- Record `blocked_reason` when a video cannot be assessed.
- Keep contradictory or inconvenient videos in scope unless they are truly unrelated.

Stage 6: readiness for per-video summaries

- Mark videos that enter summary batches.
- Ensure summary batches do not contain raw transcript or subtitle text.
- Keep summary status separate from doctrine extraction.

## 11. Validation Rules

A future inventory artifact must satisfy these rules:

- `video_id` must be unique.
- `canonical_url` must match `video_id`.
- No duplicate canonical URLs.
- `priority` must use the allowed enum.
- `summary_status` must use the allowed enum.
- `review_status` must use the allowed enum.
- `title_detected_themes` and `transcript_confirmed_themes` must remain separate.
- `raw_local_path` must point only to ignored/local-only paths if used.
- `do_not_commit_raw` must be `true` for any row tied to raw local material.
- No transcript text fields are allowed.
- No subtitle text fields are allowed.
- No downloaded media paths are allowed in Git artifacts except local-only references.
- `collection_date` must be present for generated or refreshed rows.
- `strategy_relevance` must use allowed labels and must not imply implementation approval.
- `blocked_reason` must be compact and must not copy raw source text.

## 12. Quality Controls

The inventory process must include controls against:

- Cherry-picking only videos that support Strategy B.
- Over-prioritizing TP1 while ignoring contradictory channel doctrine.
- Treating title-only themes as confirmed doctrine.
- Treating discretionary or mindset content as mechanical evidence.
- Committing raw or copyrighted text.
- Confusing inventory metadata with doctrine evidence.
- Prematurely designing Strategy B2 before the doctrine map exists.

Quality-control practices:

- Keep low and contradictory items visible in the inventory until explicitly excluded.
- Track unknowns and blocked rows instead of silently dropping them.
- Preserve a distinction between availability, summary, theme, and doctrine stages.
- Review high-priority videos first, but sample medium/low priority videos to detect missed doctrine.
- Do not convert a repeated claim into a strategy candidate until the doctrine map and gap analysis exist.

## 13. Future PR Acceptance Criteria

A future inventory-generation PR should:

- Keep raw collection output local-only.
- Add no raw transcript, subtitle, video, or audio files.
- Add no market data.
- Add no backtest result.
- Add no Strategy A/B code changes.
- Use the schema from this design or explicitly justify any schema difference.
- Include a small validation summary.
- Avoid full raw scraped data commits.
- Confirm ignored-path protection before any local raw artifact generation.

The validation summary should report counts only, such as:

- Total videos found.
- Transcript availability count.
- High, medium, low, and exclude priority counts.
- Blocked or unavailable count.
- Rows with schema-validation issues.

The PR should avoid committing full raw scraped data, generated CSVs, transcript bodies, subtitle bodies, or logs that contain copied transcript text.

## 14. Deliverables for This PR

This PR should deliver only:

- `docs/video_research/channel_video_inventory_design.md`
- No generated inventory.
- No scripts unless absolutely necessary.
- No raw data.
- No strategy code changes.

## 15. Assumptions

- The previous full-channel research plan from PR #10 is the controlling plan for the corpus track.
- This design is intentionally conservative because inventory metadata can become a raw-data leak if copied too broadly.
- Future inventory generation may use manual entry, a local script, an external tool, or an API, but this document does not choose or execute a collection method.
