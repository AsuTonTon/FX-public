# Channel Playlist-Led Beginner Batch 01 Caption Access Plan

Task: `channel_playlist_led_beginner_batch_01_caption_access_plan`

## 1. Objective and scope

This is a docs-only caption access plan for the first playlist-led beginner batch. It plans future access only for the five beginner playlist entries identified by the merged playlist metadata reconciliation report.

This PR does not:

- access YouTube;
- access DownSub;
- fetch captions, subtitles, transcript bodies, or caption URLs;
- download video or audio;
- run ASR;
- summarize videos;
- create lightweight summaries;
- create candidate inventories from transcript content;
- modify Strategy A/B code, parameters, configs, or tests;
- modify Strategy B;
- create Strategy B2 or Strategy C;
- run backtests or optimization;
- access market data, broker APIs, live trading, order execution, or execution logic;
- update `docs/video_research/channel_doctrine_map_v1.md`;
- create or update `docs/video_research/channel_doctrine_map_v2.md`;
- treat any Doctrine Map v2 draft proposal as final or accepted doctrine;
- mark Batch 08 as completed;
- make profitability claims.

The titles below are compact source titles carried forward from committed playlist metadata docs. They are not endorsed as performance, income, or profitability claims.

## 2. Evidence base

This plan uses only existing committed docs, especially:

- `docs/video_research/channel_playlist_metadata_reconciliation_report.md`
- `docs/video_research/channel_playlist_metadata_reconciliation_report_review.md`
- `docs/video_research/channel_playlist_metadata_reconciliation_plan.md`
- `docs/video_research/channel_full_corpus_playlist_led_remaining_input_status_review.md`
- `docs/video_research/channel_transcript_availability_report.md`
- `docs/video_research/channel_metadata_inventory_report.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- Batch 01 through Batch 07 lightweight summary reports and completed-summary audit reports
- `docs/video_research/downsub_access_policy_v2.md`
- `docs/video_research/downsub_txt_corpus_v2_transition_plan.md`

Committed evidence from PR #89:

| item | committed state |
| --- | --- |
| playlist metadata reconciliation | completed for three project-owner-supplied playlists |
| total playlist entries | 197 |
| total unique playlist video IDs | 197 |
| cross-playlist duplicates | 0 |
| Batch 01-07 summarized/audited playlist entries | 32 |
| beginner playlist entries | 5 |
| beginner playlist already summarized/audited entries | 0 |
| beginner playlist entries with committed `auto_caption` evidence | 3 |
| beginner playlist entries not found in committed availability docs | 2 |
| Batch 08 | blocked, not completed |
| DownSub use in PR #89 | none |

No new metadata access, caption access, or inventory regeneration was performed for this planning PR.

## 3. Target batch table

| playlist order | video ID | compact title | committed availability status | committed content type if known | existing summary/audit status | planned access handling | risk/notes |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `P4BQPNEFQf4` | 【ダウ理論の真実】月100万稼ぐプロが隠す「たった1つの鉄則」だけでFXは勝てます【FX講座Part5】 | not found in committed docs | not found in committed docs | not summarized | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | committed docs do not prove caption availability; no aggressive retry or bypass |
| 2 | `XcewGIuVI0k` | 【波の支配者】月100万への最短切符「エリオット波動第3波」｜プロが左側の波形にこだわる理由【FX講座Part4】 | `auto_caption` | regular_video | not summarized | `DownSub caption body attempt expected`; `skip if unavailable or blocked` | future summary should remain paraphrased and uncertainty-labeled |
| 3 | `5SZn-cM0D4M` | 【4時間足の衝撃】1日5分のチェックで月100万。チャートに張り付くほど負ける「逆説の真実」【FX講座Part3】 | `auto_caption` | regular_video | not summarized | `DownSub caption body attempt expected`; `skip if unavailable or blocked` | provisional Batch 08 carry-forward candidate; Batch 08 remains blocked |
| 4 | `WQ-oZx5afrc` | 【資金管理の極意】月100万稼ぐための「退場しない立ち回り」とチャンスで一気に増やす思考法【FX講座Part2】 | not found in committed docs | not found in committed docs | not summarized | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | committed docs do not prove caption availability; no aggressive retry or bypass |
| 5 | `ljeELFS-OQk` | 【聖杯探しの終焉】月100万稼ぐための最短ルートと「負け組」が共通してハマる罠【FX講座Part1】 | `auto_caption` | regular_video | not summarized | `DownSub caption body attempt expected`; `skip if unavailable or blocked` | future summary should remain paraphrased and uncertainty-labeled |

The five-video batch is intentionally modest and follows the creator's beginner playlist order.

## 4. Caption access strategy

Preferred future execution route:

- one bounded DownSub batch for exactly these 5 video IDs;
- low-rate manual or controlled access;
- no unrestricted full-channel automation;
- no proxy, VPN, IP rotation, cookies, credentials, platform bypass, or rate-limit bypass;
- no downloader workaround;
- no video or audio download;
- no ASR;
- no caption URL commit;
- no raw subtitle commit;
- no raw TXT, SRT, or VTT commit;
- no CSV, JSON, database, `data/`, or `results/` commit;
- local-only raw material only if needed for temporary comparison;
- committed output only as paraphrased Markdown summaries, batch aggregate notes, and access-status notes.

Future execution requires explicit project-owner approval before any DownSub access. If DownSub is accessed, the report and PR body should use honest source classification, including:

- `codex_accessed_downsub_third_party_subtitle_source`
- `downsub_accessed_by_codex_for_caption_derivative_review`

Each future video should be classified as one of:

- `caption_body_available`
- `caption_body_unavailable`
- `downsub_blocked`
- `unavailable_or_removed`
- `skipped_due_to_guardrail`

If access fails for a target, the execution PR should record the outcome and proceed only where the remaining accessible videos still support a coherent bounded batch.

## 5. Summary output strategy after access

Future summaries should be paraphrased lightweight summaries only. They should not include raw transcript text, subtitle text, long quotes, caption URLs, raw TXT/SRT/VTT, generated datasets, or result artifacts.

Each future per-video summary should include:

- source classification;
- access status;
- an explicit no-raw-subtitle-text statement;
- compact paraphrased lesson summary;
- mechanical-rule candidate observations only where caption-derived material supports them;
- uncertainty notes for chart-only, discretionary, or visually dependent evidence;
- no Strategy A/B changes;
- no Strategy B changes;
- no Strategy B2/C;
- no backtests or optimization;
- no market data or broker/live execution;
- no profitability claims.

The future execution PR should also add:

- one batch aggregate report;
- one companion review;
- a clear readiness decision;
- validation with `git diff --check`, `git diff --cached --check` if staging is used, and `git status --short`.

## 6. Handling the two not-found videos

The two beginner playlist entries not found in committed availability docs are:

- `P4BQPNEFQf4`
- `WQ-oZx5afrc`

Committed docs do not prove caption availability for these two videos. A future execution PR may attempt bounded DownSub access because the project owner prefers DownSub and these videos are part of the approved first playlist-led beginner batch.

If access fails:

- do not retry aggressively;
- do not use proxy, VPN, IP rotation, cookies, credentials, platform bypass, rate-limit bypass, or downloader workarounds;
- do not fall back to video/audio download or ASR;
- record the outcome as `caption_body_unavailable`, `downsub_blocked`, `unavailable_or_removed`, or `skipped_due_to_guardrail`;
- continue with the remaining accessible videos only if doing so remains useful and honest;
- keep unavailable or blocked videos out of completed-summary claims.

## 7. Why not use existing title-priority route

The playlist-led beginner order is now preferred because it preserves the creator's intended learning sequence. It also reduces overfitting to scattered high-priority titles and makes it easier to distinguish foundational beginner doctrine from later tactical or advanced topics.

The earlier title-priority route remains useful as historical evidence for Batch 01 through Batch 07 and high-priority availability accounting. It should not control the first playlist-led beginner batch by default.

Strategy A/B should not be updated from this plan. Strategy work should wait until playlist-led corpus evidence is summarized, audited, synthesized, and separately approved for strategy comparison.

## 8. Recommended next PR

Recommended next PR:

`Channel playlist-led beginner batch 01 DownSub access and summaries`

Reason:

- This plan defines the exact 5-video beginner playlist batch.
- DownSub is the preferred future caption-access route for this workflow.
- The batch is small, bounded, and reviewable.
- A future PR can access DownSub only for these 5 video IDs if project-owner approval is granted.
- The future PR should create paraphrased per-video lightweight summaries, one batch aggregate report, and one companion review.
- The future PR should honestly classify DownSub access and per-video access outcomes.
- The future PR should not modify Strategy A/B, modify Strategy B, create Strategy B2/C, run backtests, run optimization, access market data, use broker/live execution, update Doctrine Map v1, finalize Doctrine Map v2, or make profitability claims.

This recommendation does not authorize DownSub access by itself. The future execution PR requires explicit project-owner approval before any DownSub access occurs.

## 9. Guardrails

Confirmed guardrails for this planning PR:

- No YouTube access.
- No DownSub access.
- No captions fetched.
- No subtitles fetched.
- No transcript bodies fetched.
- No caption URLs fetched or committed.
- No raw transcript, subtitle text, raw TXT, SRT, or VTT commits.
- No CSV, JSON, database, `data/`, `results/`, raw metadata dump, raw candidate row, generated candidate CSV, inventory output, market CSV, or backtest output commits.
- No video or audio download.
- No ASR.
- No proxy, VPN, IP rotation, cookies, credentials, platform bypass, rate-limit bypass, or downloader workaround.
- Future DownSub access only after explicit project-owner approval for the exact bounded batch or video ID set.
- No market data.
- No broker APIs, live trading, order execution, or execution logic.
- No Strategy A/B changes.
- No Strategy B changes.
- No Strategy B2 or Strategy C.
- No backtests.
- No optimization.
- No profitability claims.
- No Doctrine Map v1 update.
- No final Doctrine Map v2 creation or update.
- Batch 08 was not marked completed.

## 10. Readiness decision

Readiness decision:

`beginner_batch_01_caption_access_plan_ready_for_human_review`

Reason: this docs-only plan defines the exact five-video playlist-led beginner batch, preserves the creator's playlist order, distinguishes known `auto_caption` entries from entries not found in committed availability docs, defines a bounded future DownSub route, requires honest access-status classification, and keeps all raw-artifact, strategy, Doctrine, market-data, broker/live, backtest, optimization, and profitability guardrails intact.
