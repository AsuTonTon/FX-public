# Channel Metadata Inventory Report

Task: `channel_metadata_inventory_generation`

## 1. Objective

This report records a metadata-only inventory pass for the YouTube full-channel corpus research track. The goal was to confirm that the channel can be inventoried safely, collect compact channel-level video metadata locally, validate the resulting metadata shape, and report aggregate counts for later research planning.

This report does not introduce Strategy A/B changes and does not treat metadata as doctrine evidence.

## 2. Source Identifier Used

The source identifier was found in existing repository documentation:

- Source document: `docs/video_research/vkaA9MCRlx4/source_metadata.json`
- Source video: `https://www.youtube.com/watch?v=vkaA9MCRlx4`
- Channel ID: `UCsyzKL2_be8U8ns5gfr1y5Q`
- Channel name: `ハイトレFX億トレーダーへの道`
- Channel handle observed in collected metadata: `@fx860`

Because the repository already contained the channel ID, no guessing was required.

## 3. Collection Method

Collection used `yt-dlp` in metadata-only flat playlist mode against the channel videos page:

- Target: `https://www.youtube.com/channel/UCsyzKL2_be8U8ns5gfr1y5Q/videos`
- Tool: `yt-dlp`, installed into a temporary local tool directory
- Mode: flat playlist metadata extraction
- Download behavior: `skip_download`
- Collection date: 2026-06-25
- Raw output handling: local-only under an ignored `data/` path

No YouTube Data API key, credentials, cookies, browser session, broker API, market-data API, transcript fetch, subtitle fetch, video download, or audio download was used.

## 4. What Was Collected

The local metadata-only collection included flat playlist entries with approved navigation metadata, primarily:

- Video ID.
- Canonical URL.
- Title.
- Duration in seconds.
- Channel-level source identifier.

The collection did not provide reliable per-video published dates in the flat playlist result, so `published_at` remains `unknown` for this pass.

Title-based weak theme detection was performed locally from titles only. `transcript_confirmed_themes` remains empty for this task.

## 5. What Was Explicitly Not Collected

This task did not collect:

- Video files.
- Audio files.
- Transcript text.
- Subtitle text.
- Raw transcript files.
- Raw subtitle files.
- Full video descriptions.
- Full scraped JSON in Git.
- Generated raw CSVs in Git.
- Cookies, credentials, tokens, or private data.
- Market data.
- Broker data.
- Backtest results.

No Strategy A/B code, Strategy A/B parameters, or Strategy C files were created or changed.

## 6. Raw / Local-Only Artifact Location

Raw collection output was stored locally only:

- `data/video_research/channel_inventory_raw/yt_dlp_flat_channel_UCsyzKL2_be8U8ns5gfr1y5Q_20260625_100208.utf8.json`

The repository `.gitignore` ignores `data/`, so this raw file is not intended for Git. A first collection attempt produced an encoding-awkward local raw file via PowerShell redirection; it was not used for the report and was not committed.

## 7. Git Artifacts Added

Git artifacts added by this task:

- `docs/video_research/channel_metadata_inventory_report.md`

No derived full inventory CSV or JSON was committed. The full row-level inventory would contain 509 rows and is better kept local-only until a reviewer explicitly wants a compact derived inventory artifact.

## 8. Schema Conformance Summary

Local validation was run against an in-memory derived inventory shaped according to `docs/video_research/channel_video_inventory_design.md`.

Validation results:

- `video_id` unique: passed.
- `canonical_url` matches `video_id`: passed.
- No duplicate canonical URLs: passed.
- `priority` uses allowed enum: passed.
- `summary_status` uses allowed enum: passed.
- `review_status` uses allowed enum: passed.
- `title_detected_themes` and `transcript_confirmed_themes` remain separate: passed.
- `transcript_confirmed_themes` remains empty: passed.
- No transcript text fields were created: passed.
- No subtitle text fields were created: passed.
- No full description fields were created: passed.
- No downloaded media paths were created in committed artifacts: passed.
- `raw_local_path` points only to the ignored local-only `data/video_research/channel_inventory_raw/` path: passed.
- `do_not_commit_raw` is true for rows tied to the raw local source: passed.

Default inventory-state values used in validation:

- `summary_status`: `metadata_only`
- `review_status`: `unreviewed`
- `transcript_available`: `unknown`
- `transcript_type`: `unknown`
- `transcript_language`: `unknown`
- `transcript_quality`: `unknown`
- `reviewer`: `unassigned`
- `last_reviewed_at`: empty
- `notes_path`: empty

## 9. Counts

Inventory counts:

- Total videos found: 509
- Videos included in committed derived inventory: 0
- High priority count: 11
- Medium priority count: 51
- Low priority count: 447
- Exclude count: 0
- Unknown priority count: 0
- Transcript available `unknown`: 509
- Blocked / unavailable count: 0

Metadata availability:

- Duration available: 509
- Published date available: 0

## 10. Title-Detected Theme Count Summary

Title-detected themes are weak labels only. They are not transcript-confirmed doctrine.

Theme counts:

- Indicator usage: 68
- 3-wave / wave structure: 64
- Candlestick / price action: 54
- Stop placement: 23
- Losing patterns: 11
- Risk / reward: 7
- Breakout: 2
- Reversal: 2
- Range / filter logic: 2

Strategy relevance counts inferred from title-only themes:

- Unknown: 432
- Entry logic: 114
- Stop / invalidation: 23
- Risk / reward: 7
- Range filter: 2

The high number of `unknown` relevance labels is expected because this pass did not inspect transcripts or full descriptions.

## 11. Known Limitations

- This is metadata-only and title-only. It should not be used as doctrine evidence.
- No transcript availability was checked by fetching transcripts or subtitles; all transcript fields remain `unknown`.
- The flat playlist output did not provide per-video published dates in this run.
- Title-based theme detection is conservative and likely misses videos whose strategy relevance is not obvious from the title.
- No full derived row-level inventory was committed because 509 rows would be awkward to review in this PR.
- Raw metadata remains local-only and ignored.

## 12. Next Recommended Step

The next recommended step is a transcript availability report that checks availability status without committing transcript text, subtitle text, downloaded media, raw metadata dumps, or large generated outputs.

If reviewers want row-level navigation before transcript availability work, create a separate compact derived inventory PR that includes only approved fields and a generation note, then re-run the same validation rules.
