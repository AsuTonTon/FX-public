# Channel Playlist Metadata Reconciliation Plan

Task: `channel_playlist_metadata_reconciliation_plan`

Plan date: 2026-07-01

## 1. Objective and scope

This is a docs-only plan for reconciling the three owner-supplied playlist orders with the existing committed corpus.

This plan:

- Defines the future playlist metadata reconciliation questions.
- Defines a minimal future metadata method without executing it.
- Defines the Git-safe future report shape.
- Preserves the committed 601-row baseline and the project-owner-observed 607 count as separate states.
- Keeps Batch 08 blocked and not completed.
- Uses only existing committed docs and repository files.

This plan does not:

- Fetch playlist metadata.
- Access YouTube or DownSub.
- Fetch captions.
- Download video or audio.
- Run ASR.
- Use proxies, VPN rotation, IP rotation, cookies, credentials, platform bypass, rate-limit bypass, or downloader workarounds.
- Summarize videos.
- Regenerate the full inventory.
- Commit raw transcripts, subtitle text, raw TXT, SRT, VTT, caption URLs, CSV, JSON, database, `data/`, `results/`, videos, audio, raw candidate rows, generated candidate CSV, or inventory outputs.
- Modify Strategy A/B code, parameters, configs, or tests.
- Modify Strategy B.
- Create Strategy B2 or Strategy C.
- Run backtests or optimization.
- Access market data.
- Use broker APIs or add broker, live trading, order execution, or execution logic.
- Make profitability claims.
- Update `docs/video_research/channel_doctrine_map_v1.md`.
- Create or update `docs/video_research/channel_doctrine_map_v2.md`.
- Treat the Doctrine Map v2 draft proposal as final or accepted doctrine.
- Mark Batch 08 as completed.

## 2. Current baseline

Committed baseline state:

| item | status/count | source |
| --- | ---: | --- |
| committed corpus baseline | 601 | `channel_full_corpus_playlist_led_remaining_input_status_review.md` |
| project-owner-observed current count | 607 | project-owner observation recorded in PR #87 docs |
| unresolved delta | +6 | 607 observed minus 601 committed baseline |
| completed/audited lightweight summary batches | 7 | Batch 01 through Batch 07 docs |
| completed/audited videos | 56 | `corpus_v2_batch_01_07_audit_synthesis.md` |
| audited mechanical-rule candidates | 233 | `corpus_v2_batch_01_07_audit_synthesis.md` |
| high-priority caption-available unsummarized rows before Batch 08 reservation | 56 | `channel_lightweight_summary_batch_08_selection_report.md` |
| Batch 08 | blocked, not completed | `channel_lightweight_summary_batch_08_selection_report.md` |
| playlist membership | unknown from committed docs | no committed playlist-to-video-ID mapping exists |
| playlist order | project-owner supplied | `channel_full_corpus_playlist_led_remaining_input_status_review.md` |

Project-owner supplied playlist learning order, inherited from merged PR #87 and preserved exactly as UTF-8 text:

| order | playlist label |
| ---: | --- |
| 1 | `完全初心者向けFX講座｜ゼロから月100万円稼ぐロードマップ` |
| 2 | `FX中級者のための勝率UP講座` |
| 3 | `本物のトレーダーになるためのFX上級講座` |

The current plan does not verify playlist membership or playlist counts. It only prepares the future reconciliation task.

## 3. Reconciliation questions

The future reconciliation task must answer:

- What are the video IDs in each of the three playlists?
- What is the playlist order for each video?
- Which playlist videos already exist in the committed 601 baseline?
- Which playlist videos are outside the committed 601 baseline?
- Do the three playlists explain the project-owner-observed +6 delta?
- Which playlist entries are already summarized or audited in Batch 01 through Batch 07?
- Which playlist entries are caption-available, caption-unknown, blocked, unavailable, or Shorts according to committed docs?
- Which playlist should be summarized first?
- Should Shorts be included in the same intake stream or separated?
- How should duplicate videos across playlists be handled?
- Does playlist order reveal beginner/intermediate/advanced dependencies that title-priority routing did not capture?
- Which rows require future subtitle acquisition after metadata reconciliation?

The future reconciliation must not answer these questions by fetching captions, downloading media, or generating summaries.

## 4. Proposed future metadata reconciliation method

This section defines a future execution task. It is not executed in this PR.

The future execution task may access YouTube only for playlist metadata if separately approved by the project owner.

Future collection should be minimal and should collect only fields needed for reconciliation:

- playlist label;
- playlist order index;
- video ID;
- title;
- canonical URL;
- content type if available;
- existing committed-corpus match status;
- existing summary/audit status if known from committed docs;
- existing caption availability status if known from committed docs.

The future task should avoid:

- transcript or caption body access;
- raw subtitle access;
- video or audio download;
- ASR;
- full descriptions unless specifically required for a documented gap;
- comments, live chat, community posts, or unrelated channel surfaces;
- proxy, VPN, IP rotation, cookies, credentials, platform bypass, rate-limit bypass, or downloader workarounds;
- committing raw row-level CSV, JSON, database, `data/`, `results/`, or inventory output files.

Future matching should compare playlist entries against committed docs first:

1. Normalize future playlist video IDs to canonical `video_id`.
2. Match IDs against the committed 601-row baseline where possible.
3. Match IDs against Batch 01 through Batch 07 completed summary filenames and audit docs.
4. Match IDs against committed availability/accounting docs where possible.
5. Identify entries outside the committed 601 baseline.
6. Report whether those outside-baseline entries explain the +6 owner-observed delta.
7. Keep any unresolved entries in a reconciliation queue rather than silently excluding them.

The future committed output should be a Git-safe Markdown reconciliation report, not raw inventory files.

## 5. Minimal artifact design

Recommended future file:

`docs/video_research/channel_playlist_metadata_reconciliation_report.md`

The future report should include:

- aggregate counts;
- per-playlist summary table;
- duplicate handling summary;
- existing corpus match summary;
- summarized/audited status summary;
- caption availability summary from committed docs only;
- +6 delta analysis;
- recommended first playlist-led summary batch.

If a small per-video table is necessary, it must be Markdown-only and compact. It should include only approved reconciliation fields:

| field | allowed? | note |
| --- | --- | --- |
| playlist label | yes | preserve exact UTF-8 text |
| playlist order index | yes | numeric order within playlist |
| video ID | yes | stable ID only |
| title | yes | compact title only |
| canonical URL | yes | video URL only if needed for review navigation |
| content type | yes | only if available from approved metadata or committed docs |
| committed-corpus match status | yes | matched / outside baseline / unresolved |
| summary/audit status | yes | from committed docs only |
| caption availability status | yes | from committed docs only |
| transcript body | no | disallowed |
| subtitle text | no | disallowed |
| raw TXT/SRT/VTT | no | disallowed |
| caption URL | no | disallowed |
| full description | no by default | use only if a future plan explicitly approves it |
| raw extractor response | no | disallowed |

The report should not commit CSV, JSON, database, `data/`, `results/`, raw candidate rows, generated candidate CSV, or regenerated inventory outputs.

## 6. DownSub relation

DownSub is not used for playlist metadata reconciliation.

DownSub is for future subtitle acquisition after playlist metadata reconciliation identifies a bounded, project-owner-approved summary or audit batch.

Future DownSub use must be:

- bounded;
- low-rate;
- project-owner-approved per batch or exact video ID set;
- honestly classified in the related PR and report;
- paraphrase-only in committed docs;
- Git-safe.

Future DownSub use must not include:

- raw subtitle text commits;
- raw TXT, SRT, or VTT commits;
- caption URL commits;
- video or audio downloads;
- ASR;
- proxy, VPN, IP rotation, cookies, credentials, platform bypass, or rate-limit bypass;
- automated downloader commits;
- CSV, JSON, database, `data/`, or `results/` artifacts.

## 7. Batch design after reconciliation

After playlist metadata reconciliation, future summary batches should be selected from playlist order rather than title-priority-only routing.

Expected approach:

- Start with playlist 1: `完全初心者向けFX講座｜ゼロから月100万円稼ぐロードマップ`.
- Proceed in playlist order.
- Exclude or separately handle videos already summarized and audited in Batch 01 through Batch 07.
- Keep Batch 08 blocked until a new playlist-led plan explicitly replaces or re-plans it.
- Separate Shorts unless playlist context requires inclusion.
- If Shorts are included, label them as Shorts and avoid treating them as equivalent to full-length lessons by default.
- Use DownSub only after separate project-owner batch approval.
- Use paraphrased lightweight summaries only.
- Do not mix findings into Strategy A/B immediately.
- Do not modify Strategy B.
- Do not create Strategy B2 or Strategy C.
- Do not run backtests or optimization.
- Do not make profitability claims.

The first playlist-led summary batch should not be selected until the future reconciliation report identifies playlist membership, existing summary status, and committed availability status.

## 8. Recommended next PR

Recommended next docs-only PR:

`Channel playlist metadata reconciliation execution`

Reason:

- The current PR is only the plan.
- The next PR should perform the minimal playlist metadata reconciliation if project-owner approval is granted.
- It should still avoid captions, subtitles, raw transcripts, and summaries.
- It should not use DownSub yet.
- It should not commit raw CSV, JSON, database, `data/`, `results/`, or inventory outputs.
- It should not modify Strategy A/B or Strategy B.
- It should preserve Batch 08 as blocked unless a later playlist-led plan explicitly replaces or re-plans it.
- It should keep 607 as project-owner-observed until reconciliation identifies the delta.

This recommendation does not authorize YouTube access by itself. The future execution PR requires explicit project-owner approval for playlist metadata access before any metadata fetch occurs.

## 9. Guardrails

Confirmed guardrails for this planning PR:

- No raw transcript, subtitle text, raw TXT, SRT, VTT, or caption URL commits.
- No CSV, JSON, database, `data/`, or `results/` commits.
- No video or audio download.
- No ASR.
- No YouTube or DownSub access in this PR.
- No caption fetching.
- No playlist metadata fetching.
- No inventory regeneration.
- No proxy, VPN, IP rotation, cookies, credentials, platform bypass, rate-limit bypass, or downloader workaround.
- No downloader added.
- No market data.
- No broker, live trading, order execution, or execution logic.
- No Strategy A/B code, parameter, config, or test changes.
- No Strategy B change.
- No Strategy B2 or Strategy C.
- No backtests.
- No optimization.
- No profitability claims.
- No Channel Doctrine Map v1 update.
- No final Channel Doctrine Map v2 creation or update.
- No Batch 08 completion claim.
- The 607-video observation remains project-owner-observed and not verified regenerated inventory.

## 10. Readiness decision

Decision:

`channel_playlist_metadata_reconciliation_plan_ready_for_human_review`

Reason: this docs-only plan defines how a future approved task should reconcile the three owner-supplied playlist orders against the committed 601-row corpus baseline and the project-owner-observed 607 count without fetching captions, summarizing videos, regenerating the full inventory, or changing strategy code. It preserves Batch 08 as blocked, keeps DownSub out of playlist metadata reconciliation, recommends a bounded `Channel playlist metadata reconciliation execution` PR only after approval, and maintains all raw-artifact, Doctrine, Strategy, market-data, broker/live, backtest, optimization, and profitability guardrails.
