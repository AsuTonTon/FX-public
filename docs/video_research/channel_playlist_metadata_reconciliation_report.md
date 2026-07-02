# Channel Playlist Metadata Reconciliation Report

Task: `channel_playlist_metadata_reconciliation_execution`

## 1. Objective and scope

This is a bounded playlist metadata reconciliation report for the three project-owner-supplied YouTube playlists:

1. `完全初心者向けFX講座｜ゼロから月100万円稼ぐロードマップ`
2. `FX中級者のための勝率UP講座`
3. `本物のトレーダーになるためのFX上級講座`

YouTube access was limited to minimal playlist metadata reconciliation for these approved playlists. The work collected only playlist label, playlist order, video ID, compact title, playlist ID, and duplicate status. Content type and caption availability were taken only from existing committed docs where available.

This PR does not:

- access DownSub;
- fetch captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, or full descriptions;
- download video or audio;
- run ASR;
- summarize videos;
- regenerate the full channel inventory;
- update `docs/video_research/channel_doctrine_map_v1.md`;
- create or finalize `docs/video_research/channel_doctrine_map_v2.md`;
- modify Strategy A/B code, parameters, configs, or tests;
- modify Strategy B;
- create Strategy B2 or Strategy C;
- run backtests or optimization;
- access market data, broker APIs, live trading, order execution, or execution logic;
- make profitability claims.

Batch 08 remains blocked and not completed.

## 2. Access log

| item | result |
| --- | --- |
| access date | 2026-07-01, Asia/Tokyo |
| approved playlist labels | `完全初心者向けFX講座｜ゼロから月100万円稼ぐロードマップ`; `FX中級者のための勝率UP講座`; `本物のトレーダーになるためのFX上級講座` |
| method used | temporary local Python `urllib` metadata inspection of YouTube playlist pages and YouTube web playlist continuation responses |
| playlist ID resolution | the advanced playlist ID was resolved by exact-title YouTube search because an earlier candidate did not match the approved label; only the final matching approved playlist was used in the reconciliation counts |
| cookies or credentials used | no |
| proxy, VPN, IP rotation, platform bypass, or rate-limit bypass used | no |
| downloader workaround used | no |
| captions, subtitles, transcript bodies, or caption URLs accessed | no |
| video or audio downloaded | no |
| comments, live chat, community posts, or unrelated channel surfaces fetched | no |
| raw metadata files committed | no |
| CSV, JSON, database, `data/`, `results/`, or inventory output committed | no |

No raw extractor response or raw playlist metadata dump is included in this report.

## 3. Playlist aggregate summary

Interpretation note: `committed 601 match evidence` means the video ID appears in committed corpus docs derived from the 601-row baseline, such as the high-priority triage ledger, completed summary files, or Batch 08 provisional ledger. `baseline unresolved from committed docs` does not mean the video is outside the 601 baseline; it means this PR cannot prove row-level baseline membership from committed docs because the full 601-row inventory is not committed and this task did not regenerate it.

| playlist label | playlist ID | entries retrieved | unique video IDs | within-playlist duplicates | committed 601 match evidence | confirmed outside committed 601 | baseline unresolved from committed docs | Batch 01-07 summarized/audited | not summarized | committed availability known | availability not found in committed docs |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `完全初心者向けFX講座｜ゼロから月100万円稼ぐロードマップ` | `PLNGEKxuiLyh1OL0vrEmO7z_res2CGNZso` | 5 | 5 | 0 | 3 | 0 | 2 | 0 | 5 | 3 | 2 |
| `FX中級者のための勝率UP講座` | `PLNGEKxuiLyh0bxPacLi2w03CXmigUXIb6` | 68 | 68 | 0 | 8 | 0 | 60 | 8 | 60 | 8 | 60 |
| `本物のトレーダーになるためのFX上級講座` | `PLNGEKxuiLyh0osYYSxKBv6iAk2UXRIrfi` | 124 | 124 | 0 | 33 | 0 | 91 | 24 | 100 | 33 | 91 |
| Total | - | 197 | 197 | 0 | 44 | 0 | 153 | 32 | 165 | 44 | 153 |

The reconciliation found 197 playlist entries and 197 unique video IDs across the three approved playlists.

## 4. Cross-playlist duplicate summary

| metric | result |
| --- | --- |
| total unique video IDs across the three playlists | 197 |
| videos appearing in more than one playlist | 0 |
| cross-playlist duplicates found | none |

Future playlist-led intake can follow playlist order without needing duplicate skip rules across these three playlists. If a duplicate appears in a later playlist, the earlier playlist occurrence should own the first intake slot and later occurrences should reference the prior summary or audit rather than create another summary by default.

## 5. 601 / 607 reconciliation

| item | result |
| --- | ---: |
| committed corpus baseline | 601 |
| project-owner-observed current count | 607 |
| owner-observed delta | +6 |
| playlist IDs with committed 601 match evidence | 44 |
| playlist IDs confirmed outside committed 601 baseline | 0 |
| playlist IDs unresolved from committed docs | 153 |
| portion of +6 explained by confirmed outside-baseline playlist IDs | none |
| remaining unresolved delta | +6 |

This PR did not regenerate the full current channel inventory. It therefore does not prove whether the 153 playlist IDs not found in committed row-level docs are inside or outside the committed 601 baseline. They remain a reconciliation queue for future bounded review.

The +6 owner-observed delta remains unresolved because no playlist ID was conclusively identified as outside the committed 601 baseline from committed docs alone.

## 6. Batch 01-07 status overlay

Batch 01 through Batch 07 remain complete and audited, covering 56 videos and 233 mechanical-rule candidates. Among the 197 playlist IDs, 32 already have completed lightweight summaries.

| playlist | already summarized/audited entries | count | future handling |
| --- | --- | ---: | --- |
| `完全初心者向けFX講座｜ゼロから月100万円稼ぐロードマップ` | none | 0 | eligible for first playlist-led intake after caption/access planning |
| `FX中級者のための勝率UP講座` | `2:_sx3dCvPXac`; `28:gYkU8nVa-hE`; `39:6vGtLPFfWYQ`; `40:DeRVQNJtq3s`; `44:e4N22IkeOs4`; `48:HuNeo8FfBO8`; `57:16Kb39TFFek`; `66:GIHwOx6iwiw` | 8 | reference existing summaries/audits rather than re-summarizing by default |
| `本物のトレーダーになるためのFX上級講座` | `4:CPKh323IyO8`; `5:SrWVDh_BpVs`; `10:iZuUWHc5bcI`; `11:JDjq7FrKdF8`; `13:CES2xzjeOTk`; `18:rG3ELeTim8U`; `20:V8DoVtiE-0Y`; `33:V5MJKN5YmIU`; `38:CFBpTH3T06E`; `39:6bZ-OG-133s`; `50:QTXMzTbGH5U`; `52:ILHbFmWPSOc`; `54:QErPg-ZvR1s`; `57:G3OTGwKAip4`; `58:5PXeBITxmI4`; `61:ezZxNuCLEKU`; `67:U9xsvLmdIOw`; `73:Mg09uk9I9JM`; `78:KEE4Dk8LM1A`; `81:FVXSJoK8pNs`; `87:AiOG_Qgvw2E`; `99:GIGLYCFBH9Q`; `109:zWOdiI0L_s4`; `113:8OpVGAO8_2Y` | 24 | reference existing summaries/audits rather than re-summarizing by default |

Future playlist-led intake should skip already completed summaries unless a separate project-owner-approved correction or re-audit task identifies a specific gap.

## 7. Caption availability overlay

Caption availability here uses committed docs only, especially `docs/video_research/channel_high_priority_relevance_triage_ledger.md` and related availability reports. This PR did not fetch captions, transcript bodies, subtitle bodies, or caption URLs, and it did not infer availability from current YouTube pages.

| playlist | caption-available from committed docs | caption-unknown in committed docs | blocked in committed docs | unavailable in committed docs | not found in committed availability docs |
| --- | ---: | ---: | ---: | ---: | ---: |
| `完全初心者向けFX講座｜ゼロから月100万円稼ぐロードマップ` | 3 | 0 | 0 | 0 | 2 |
| `FX中級者のための勝率UP講座` | 8 | 0 | 0 | 0 | 60 |
| `本物のトレーダーになるためのFX上級講座` | 33 | 0 | 0 | 0 | 91 |
| Total | 44 | 0 | 0 | 0 | 153 |

The 44 committed availability matches are all `auto_caption` and `regular_video` in the committed high-priority docs. For the remaining 153 playlist IDs, content type and caption availability remain not found in committed availability docs.

## 8. Recommended first playlist-led summary batch

Recommended first future summary batch:

`Playlist-led beginner batch 01`

Rationale:

- Start from playlist 1 because reconciliation found no duplicate or completed-summary blocker.
- Use playlist order.
- The batch size is modest: 5 videos.
- All 5 playlist 1 entries are not yet summarized/audited.
- Three entries already have committed `auto_caption` availability evidence.
- Two entries are not found in committed availability docs and need a bounded access/availability plan before summary work.
- No Shorts are identified in committed docs for playlist 1; two entries still lack committed content-type evidence.
- This report does not authorize DownSub, caption fetching, or summary generation by itself.

| order | video ID | compact title | committed content type | committed caption status | Batch 01-07 summary status | note |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `P4BQPNEFQf4` | 【ダウ理論の真実】月100万稼ぐプロが隠す「たった1つの鉄則」だけでFXは勝てます【FX講座Part5】 | not found in committed docs | not found in committed docs | not summarized | needs availability/accounting before summary |
| 2 | `XcewGIuVI0k` | 【波の支配者】月100万への最短切符「エリオット波動第3波」｜プロが左側の波形にこだわる理由【FX講座Part4】 | regular_video | auto_caption | not summarized | eligible after bounded summary approval |
| 3 | `5SZn-cM0D4M` | 【4時間足の衝撃】1日5分のチェックで月100万。チャートに張り付くほど負ける「逆説の真実」【FX講座Part3】 | regular_video | auto_caption | not summarized | was a provisional Batch 08 carry-forward candidate; Batch 08 remains blocked |
| 4 | `WQ-oZx5afrc` | 【資金管理の極意】月100万稼ぐための「退場しない立ち回り」とチャンスで一気に増やす思考法【FX講座Part2】 | not found in committed docs | not found in committed docs | not summarized | needs availability/accounting before summary |
| 5 | `ljeELFS-OQk` | 【聖杯探しの終焉】月100万稼ぐための最短ルートと「負け組」が共通してハマる罠【FX講座Part1】 | regular_video | auto_caption | not summarized | eligible after bounded summary approval |

The next task should not summarize these videos unless it receives explicit project-owner approval for bounded DownSub or another approved caption-access route.

## 9. Remaining issues

- The owner-observed +6 delta remains unresolved.
- No playlist ID is confirmed outside the committed 601 baseline, but 153 playlist IDs are not found in committed row-level docs.
- Playlist 1 has two entries whose caption availability and content type are not found in committed docs: `P4BQPNEFQf4` and `WQ-oZx5afrc`.
- Across all three playlists, 153 entries are not found in committed availability docs.
- Shorts handling remains unresolved for entries not found in committed availability docs because this PR did not infer content type from current YouTube pages.
- Cross-playlist duplicates are not an issue for these three playlists.
- The advanced playlist required exact-title ID resolution; the final matching playlist ID is `PLNGEKxuiLyh0osYYSxKBv6iAk2UXRIrfi`.

## 10. Recommended next PR

Recommended next docs-only PR:

`Channel playlist-led beginner batch 01 caption access plan`

Reason:

- The first playlist-led summary batch should start with playlist 1 in order.
- Playlist 1 has five unsummarized entries, which is an appropriate 5-video batch size.
- Three entries have committed `auto_caption` availability evidence, but two entries are not found in committed availability docs.
- Availability uncertainty is high enough that the next PR should plan bounded caption/access handling before any summary PR.
- The next PR should use this report and existing committed availability docs as the source of truth.
- The next PR should not summarize videos unless it separately receives explicit project-owner approval for bounded DownSub access or another approved caption-access method.
- The next PR should not commit raw transcripts, subtitle text, caption URLs, CSV, JSON, database, `data/`, `results/`, raw metadata dumps, videos, audio, or raw candidate rows.
- The next PR should not modify Strategy A/B or Strategy B, create Strategy B2/C, run backtests, run optimization, access market data, use broker/live execution, update Doctrine Map v1, finalize Doctrine Map v2, or make profitability claims.

## 11. Guardrails

Confirmed guardrails for this PR:

- No raw transcript, subtitle text, raw TXT, SRT, VTT, or caption URL commits.
- No CSV, JSON, database, `data/`, `results/`, inventory output, raw candidate row, generated candidate CSV, market CSV, or backtest output commits.
- No video or audio download.
- No ASR.
- No DownSub access.
- YouTube access was limited to approved playlist metadata only.
- No captions, subtitles, transcript bodies, or caption URLs were fetched.
- No comments, live chat, community posts, unrelated channel surfaces, or full descriptions were fetched.
- No proxy, VPN, IP rotation, cookies, credentials, platform bypass, rate-limit bypass, or downloader workaround was used.
- No downloader was added.
- No market data was accessed.
- No broker, live trading, order execution, or execution logic was added.
- No Strategy A/B changes.
- No Strategy B changes.
- No Strategy B2 or Strategy C.
- No backtests.
- No optimization.
- No profitability claims.
- No Doctrine Map v1 update.
- No final Doctrine Map v2 creation.
- Batch 08 was not marked completed.

## 12. Readiness decision

Readiness decision:

`playlist_metadata_reconciliation_ready_for_human_review`

Reason: the bounded playlist metadata reconciliation retrieved minimal metadata for the three approved playlists, identified 197 unique playlist video IDs, found no cross-playlist duplicates, overlaid 32 existing Batch 01-07 completed summaries, preserved Batch 08 as blocked, and kept caption availability classification to committed docs only. The report does not commit raw metadata dumps, captions, subtitles, transcript text, caption URLs, CSV/JSON/data/results artifacts, strategy files, market data, or backtest outputs, and it makes no profitability claim.
