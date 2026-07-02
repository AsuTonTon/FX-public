# Channel Playlist-Led Intermediate Batch 02 Caption Access Plan

Task: `channel_playlist_led_intermediate_batch_02_caption_access_plan`

## 1. Objective and scope

This docs-only planning PR defines the second playlist-led intermediate batch for:

`FX中級者のための勝率UP講座`

The plan uses source-order playlist logic, skips already summarized/audited entries where known, and selects a modest Batch 02 of seven not-yet-summarized videos.

This PR uses committed repository docs plus bounded YouTube playlist metadata access for the approved intermediate playlist only. It does not:

- access DownSub;
- fetch captions or subtitles;
- fetch transcript bodies;
- fetch caption URLs;
- summarize videos;
- create lightweight summaries;
- create transcript-derived candidate inventories;
- modify Strategy A/B code, parameters, configs, or tests;
- modify Strategy B;
- create Strategy B2 or Strategy C;
- run backtests or optimization;
- access market data;
- use broker APIs or add broker/live execution logic;
- make profitability claims;
- update `docs/video_research/channel_doctrine_map_v1.md`;
- create, update, finalize, or accept `docs/video_research/channel_doctrine_map_v2.md`;
- mark Batch 08 completed.

Future caption access, if any, requires separate explicit project-owner approval.

## 2. Evidence base

| evidence item | committed state |
| --- | --- |
| beginner playlist line | Complete, summarized, audited, and synthesized. |
| intermediate Batch 01 | Planned, summarized, audited, and synthesized. |
| approved intermediate playlist label | `FX中級者のための勝率UP講座` |
| approved intermediate playlist ID | `PLNGEKxuiLyh0bxPacLi2w03CXmigUXIb6` |
| intermediate playlist entries | 68 entries. |
| intermediate unique video IDs | 68 unique video IDs. |
| cross-playlist duplicates across approved playlists | 0 in the merged metadata reconciliation report. |
| known already summarized/audited intermediate entries before Batch 01 | 8 entries. |
| playlist-led Batch 01 summarized/audited entries | 6 entries. |
| total known summarized/audited intermediate entries after Batch 01 | 14 entries. |
| approximate remaining unsummarized intermediate entries before Batch 02 | 54 entries. |
| planned Batch 02 size | 7 entries. |
| approximate remaining unsummarized intermediate entries after a future completed Batch 02 | 47 entries. |
| committed availability coverage for future Batch 02 rows | Not found in committed availability docs. |
| DownSub use for Batch 02 | Not used in this planning PR. |
| Strategy A/B state | Unchanged. |
| Strategy B state | Unchanged. |
| Doctrine Map v1 state | Unchanged. |
| final Doctrine Map v2 state | Not created. |
| Batch 08 state | Blocked and not completed. |

Known already summarized/audited intermediate entries from earlier corpus work:

| playlist order | video ID | status |
| ---: | --- | --- |
| 2 | `_sx3dCvPXac` | already summarized/audited |
| 28 | `gYkU8nVa-hE` | already summarized/audited |
| 39 | `6vGtLPFfWYQ` | already summarized/audited |
| 40 | `DeRVQNJtq3s` | already summarized/audited |
| 44 | `e4N22IkeOs4` | already summarized/audited |
| 48 | `HuNeo8FfBO8` | already summarized/audited |
| 57 | `16Kb39TFFek` | already summarized/audited |
| 66 | `GIHwOx6iwiw` | already summarized/audited |

Known already summarized/audited intermediate entries from playlist-led Intermediate Batch 01:

| playlist order | video ID | status |
| ---: | --- | --- |
| 1 | `-2gNKPqIpAs` | summarized/audited/synthesized in Intermediate Batch 01 |
| 3 | `4YcjlIvDkug` | summarized/audited/synthesized in Intermediate Batch 01 |
| 4 | `xnH6ODNMFHs` | summarized/audited/synthesized in Intermediate Batch 01 |
| 5 | `ICCkkPufugI` | summarized/audited/synthesized in Intermediate Batch 01 |
| 6 | `ZIg8SxoAEd0` | summarized/audited/synthesized in Intermediate Batch 01 |
| 7 | `9PIrE3TMjK8` | summarized/audited/synthesized in Intermediate Batch 01 |

Intermediate playlist as a whole remains incomplete. Advanced playlist remains open. Full channel corpus research is not complete.

## 3. Metadata access note

This PR used bounded YouTube playlist metadata access because committed docs did not include ordered compact titles for the next unsummarized intermediate playlist entries after Batch 01.

| field | value |
| --- | --- |
| access date | 2026-07-02, Asia/Tokyo |
| approved playlist label | `FX中級者のための勝率UP講座` |
| playlist ID | `PLNGEKxuiLyh0bxPacLi2w03CXmigUXIb6` |
| method used | Python `urllib.request` metadata read of the YouTube playlist Atom feed for the approved playlist only |
| exact metadata fields collected | playlist order as feed order, video ID, compact title, canonical video URL |
| range of playlist rows inspected | rows 1 through 15 returned by the approved playlist feed |
| duplicate status checked | no duplicate among inspected rows; merged reconciliation already reports 68 unique IDs and 0 within-playlist duplicates for the intermediate playlist |
| captions/subtitles/transcripts/caption URLs accessed | no |
| DownSub access | no |
| comments/live chat/community posts accessed | no |
| raw metadata dump committed | no |
| CSV/JSON/database/data/results committed | no |

The metadata access was limited to selecting the next modest unsummarized intermediate batch. No caption, subtitle, transcript body, caption URL, comment, live chat, community post, channel-wide scrape, unrelated video, video file, audio file, ASR, proxy, VPN, IP rotation, cookies, credentials, browser session token, platform bypass, rate-limit bypass, or downloader workaround was used.

## 4. Intermediate Batch 02 target selection

Selection rules applied:

- preserve retrieved playlist order;
- skip already summarized/audited entries where known;
- prefer first unsummarized entries in playlist order after Intermediate Batch 01;
- keep batch size between 5 and 8 videos;
- do not include non-intermediate playlist videos;
- skip any playlist entry that cannot be safely resolved;
- do not infer caption availability from title alone;
- if a newly discovered entry is already summarized/audited in committed docs, skip it and document the evidence.

Playlist order 2 (`_sx3dCvPXac`) remains skipped because committed docs identify it as already summarized/audited. Playlist orders 1 and 3 through 7 are now covered by Intermediate Batch 01. No committed summary/audit evidence was found for playlist orders 8 through 14, so Batch 02 selects those seven source-order rows.

| playlist order | video ID | compact title | already summarized/audited status | committed availability status if known | planned access handling | notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 8 | `SDqllAryB2Y` | 【最重要】FXで1番大事なトレード日記の正しい書き方を教える。（実践披露） | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | First unsummarized source-order row after Batch 01. |
| 9 | `QTbD1gz1Otk` | 【神回】勝敗を左右する「リスク」の取り方について解説 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Included by source order; no caption availability inferred from title. |
| 10 | `5yjtVnTy_54` | 【超有料級】誰でも勝てるスキャルピング手法を教えます。 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Title is retained as metadata only and is not a profitability claim. |
| 11 | `wengmP7Ss2s` | 【超大事】テクニカル分析ができない人がFXで勝つ唯一の方法とは？ | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Title is retained as metadata only and is not a profitability claim. |
| 12 | `m8-6AA4gWDs` | 【今から勝てる】短期スキャルピング手法を完全解説 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Title is retained as metadata only and is not a profitability claim. |
| 13 | `onAw6eanokU` | 【神回】勝率20％以下のトレーダーが勝てるようになる方法 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Title is retained as metadata only and is not a profitability claim. |
| 14 | `sEUjtt8lL9g` | 【完全攻略】斜め線を使って簡単に稼ぐ方法を教える。 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Seventh selected row keeps Batch 02 modest. |

Batch 02 selected target IDs:

1. `SDqllAryB2Y`
2. `QTbD1gz1Otk`
3. `5yjtVnTy_54`
4. `wengmP7Ss2s`
5. `m8-6AA4gWDs`
6. `onAw6eanokU`
7. `sEUjtt8lL9g`

## 5. Already-summarized skip table

Known skipped entries relevant to Batch 02 selection:

| playlist order | video ID | skip reason | evidence source |
| ---: | --- | --- | --- |
| 1 | `-2gNKPqIpAs` | Already summarized, audited, and synthesized in Intermediate Batch 01. | `docs/video_research/playlist_led_summaries/intermediate_batch_01/intermediate_batch_01_synthesis.md` |
| 2 | `_sx3dCvPXac` | Already summarized/audited in earlier corpus work; do not re-summarize by default. | `docs/video_research/channel_playlist_metadata_reconciliation_report.md`; `docs/video_research/playlist_led_summaries/intermediate_batch_01_caption_access_plan.md` |
| 3 | `4YcjlIvDkug` | Already summarized, audited, and synthesized in Intermediate Batch 01. | `docs/video_research/playlist_led_summaries/intermediate_batch_01/intermediate_batch_01_synthesis.md` |
| 4 | `xnH6ODNMFHs` | Already summarized, audited, and synthesized in Intermediate Batch 01. | `docs/video_research/playlist_led_summaries/intermediate_batch_01/intermediate_batch_01_synthesis.md` |
| 5 | `ICCkkPufugI` | Already summarized, audited, and synthesized in Intermediate Batch 01. | `docs/video_research/playlist_led_summaries/intermediate_batch_01/intermediate_batch_01_synthesis.md` |
| 6 | `ZIg8SxoAEd0` | Already summarized, audited, and synthesized in Intermediate Batch 01. | `docs/video_research/playlist_led_summaries/intermediate_batch_01/intermediate_batch_01_synthesis.md` |
| 7 | `9PIrE3TMjK8` | Already summarized, audited, and synthesized in Intermediate Batch 01. | `docs/video_research/playlist_led_summaries/intermediate_batch_01/intermediate_batch_01_synthesis.md` |

Later known already summarized/audited intermediate entries were not encountered in the Batch 02 source-order window, but remain future skip rows:

| playlist order | video ID | skip reason | evidence source |
| ---: | --- | --- | --- |
| 28 | `gYkU8nVa-hE` | Already summarized/audited in earlier corpus work. | `docs/video_research/channel_playlist_metadata_reconciliation_report.md` |
| 39 | `6vGtLPFfWYQ` | Already summarized/audited in earlier corpus work. | `docs/video_research/channel_playlist_metadata_reconciliation_report.md` |
| 40 | `DeRVQNJtq3s` | Already summarized/audited in earlier corpus work. | `docs/video_research/channel_playlist_metadata_reconciliation_report.md` |
| 44 | `e4N22IkeOs4` | Already summarized/audited in earlier corpus work. | `docs/video_research/channel_playlist_metadata_reconciliation_report.md` |
| 48 | `HuNeo8FfBO8` | Already summarized/audited in earlier corpus work. | `docs/video_research/channel_playlist_metadata_reconciliation_report.md` |
| 57 | `16Kb39TFFek` | Already summarized/audited in earlier corpus work. | `docs/video_research/channel_playlist_metadata_reconciliation_report.md` |
| 66 | `GIHwOx6iwiw` | Already summarized/audited in earlier corpus work. | `docs/video_research/channel_playlist_metadata_reconciliation_report.md` |

## 6. Caption access strategy

Preferred future route:

- one bounded DownSub batch for exactly these selected intermediate Batch 02 video IDs:
  - `SDqllAryB2Y`
  - `QTbD1gz1Otk`
  - `5yjtVnTy_54`
  - `wengmP7Ss2s`
  - `m8-6AA4gWDs`
  - `onAw6eanokU`
  - `sEUjtt8lL9g`
- low-rate/manual or controlled access;
- no full-channel automation;
- no additional playlist, channel, or unrelated video access;
- no proxy/VPN/IP rotation/cookies/credentials/platform bypass/rate-limit bypass;
- no video/audio download;
- no ASR;
- no raw subtitle commit;
- no raw TXT/SRT/VTT commit;
- no caption URL commit;
- no raw DownSub response commit;
- no CSV/JSON/database/data/results commit;
- local-only raw material if needed;
- committed output only as paraphrased Markdown summaries, access-status notes, aggregate report, and review.

Future access result labels:

- `caption_body_available`
- `caption_body_unavailable`
- `downsub_blocked`
- `unavailable_or_removed`
- `skipped_due_to_guardrail`

Future execution requires explicit project-owner approval before any DownSub access occurs.

## 7. Summary output strategy after access

Future summaries should be paraphrased lightweight summaries only. They should not include raw transcript text, subtitle text, long quotes, caption URLs, raw TXT/SRT/VTT, generated datasets, result artifacts, or extractor responses.

Each future summary should include:

- source classification;
- access status;
- explicit no-raw-subtitle-text statement;
- compact paraphrased lesson summary;
- trading concept notes;
- mechanical-rule candidate observations only if supported;
- uncertainty notes;
- Strategy boundary;
- no profitability claim.

Any future aggregate report should record attempted IDs, access outcomes, omitted or blocked IDs, candidate wording boundaries, raw-artifact guardrails, and a recommendation for review. It should not update Doctrine Map v1, finalize Doctrine Map v2, modify Strategy A/B or Strategy B, create Strategy B2/C, access market data, run backtests, run optimization, use broker/live execution, or make profitability claims.

## 8. Relationship to Intermediate Batch 01 synthesis

Intermediate Batch 01 is the completed source-order layer covering playlist orders 1 and 3 through 7, while order 2 is skipped as an already summarized/audited earlier corpus entry.

Intermediate Batch 02 should be interpreted as the next source-order layer, beginning at playlist order 8 and proceeding through order 14. It should not rewrite `docs/video_research/playlist_led_summaries/intermediate_batch_01/intermediate_batch_01_synthesis.md` from a planning PR.

This plan does not update Doctrine Map v1, does not finalize Doctrine Map v2, does not treat any Doctrine Map v2 draft proposal as final doctrine, and does not modify Strategy A/B or Strategy B.

## 9. Recommended next PR

Recommended next PR:

`Channel playlist-led intermediate batch 02 DownSub access and summaries`

Reason:

- the intermediate Batch 02 target is now defined;
- future PR can access DownSub only for the selected IDs if project-owner approval is granted;
- future PR should produce paraphrased summaries, aggregate report, and review;
- future PR should not modify Strategy A/B or Strategy B.

## 10. Guardrails

This PR explicitly preserves these guardrails:

- no DownSub access in this PR;
- no caption/subtitle/transcript body access in this PR;
- no caption URL access or commits;
- no raw playlist metadata dump commits;
- no raw transcript/subtitle/caption URL commits;
- no CSV/JSON/database/data/results commits;
- no video/audio download;
- no ASR;
- no proxy/VPN/IP rotation/cookies/credentials/platform bypass/rate-limit bypass;
- no market data;
- no broker/live trading;
- no broker API or order execution;
- no Strategy A/B changes;
- no Strategy B changes;
- no Strategy B2/C;
- no Doctrine Map v1 update;
- no final Doctrine Map v2 creation;
- no Batch 08 completion;
- no backtests;
- no optimization;
- no profitability claims.

## 11. Readiness decision

Readiness decision:

`intermediate_batch_02_caption_access_plan_ready_for_review`

Reason: this plan defines a modest seven-video second intermediate playlist-led batch, uses retrieved source order, skips known already summarized/audited entries, records the bounded metadata-only access used to resolve the next target rows, preserves source-access and raw-artifact guardrails, and does not authorize summaries, DownSub access, Doctrine Map changes, Strategy changes, backtests, optimization, market-data access, broker/live execution, or profitability claims.

The selected Batch 02 is ready for a bounded DownSub access PR after explicit project-owner approval.
