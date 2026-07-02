# Channel Playlist-Led Intermediate Batch 01 Caption Access Plan

Task: `channel_playlist_led_intermediate_batch_01_caption_access_plan`

## 1. Objective And Scope

This docs-only planning PR defines the first playlist-led intermediate batch for:

`FX中級者のための勝率UP講座`

The plan uses source-order playlist logic, skips already summarized/audited intermediate entries where known, and selects a modest first batch of six not-yet-summarized videos.

This PR uses committed repository docs plus bounded YouTube playlist metadata access for the approved intermediate playlist only. It does not:

- access DownSub;
- fetch captions or subtitles;
- fetch transcript bodies;
- fetch caption URLs;
- summarize videos;
- create lightweight summaries;
- create candidate inventories from transcript content;
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

## 2. Evidence Base

| evidence item | committed state |
| --- | --- |
| beginner playlist line | Complete, summarized, audited, and synthesized. |
| next source-order line | Intermediate playlist: `FX中級者のための勝率UP講座`. |
| approved intermediate playlist ID | `PLNGEKxuiLyh0bxPacLi2w03CXmigUXIb6`. |
| intermediate playlist entries | 68 entries. |
| intermediate unique video IDs | 68 unique video IDs. |
| cross-playlist duplicates across approved playlists | 0. |
| already summarized/audited intermediate entries | 8. |
| not-yet-summarized intermediate entries | 60. |
| committed availability coverage for intermediate playlist | Limited to 8 intermediate entries in the merged metadata reconciliation. |
| DownSub use for intermediate playlist | Not yet used. |
| Strategy A/B state | Unchanged. |
| Doctrine Map v1 state | Unchanged. |
| final Doctrine Map v2 state | Not created. |
| Batch 08 state | Blocked and not completed. |

Known already summarized/audited intermediate entries from committed docs:

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

## 3. Metadata Access Note

This PR used bounded YouTube playlist metadata access because committed docs did not include the ordered compact titles for the first unsummarized intermediate playlist entries.

| field | value |
| --- | --- |
| access date | 2026-07-01 |
| approved playlist label | `FX中級者のための勝率UP講座` |
| playlist ID | `PLNGEKxuiLyh0bxPacLi2w03CXmigUXIb6` |
| method used | Python `urllib.request` metadata read of the YouTube playlist Atom feed: `https://www.youtube.com/feeds/videos.xml?playlist_id=PLNGEKxuiLyh0bxPacLi2w03CXmigUXIb6` |
| exact metadata fields collected | playlist order as feed order, video ID, compact title, canonical video URL |
| duplicate status checked | no duplicate among the collected first 15 feed entries; merged reconciliation already reports 0 cross-playlist duplicates across approved playlists |
| captions/subtitles/transcripts/caption URLs accessed | no |
| DownSub access | no |
| raw metadata dump committed | no |
| CSV/JSON/database/data/results committed | no |

The metadata access was limited to selecting the first modest unsummarized intermediate batch. No caption, subtitle, transcript body, caption URL, comment, live chat, community post, channel-wide scrape, unrelated video, video file, audio file, ASR, proxy, VPN, IP rotation, cookies, credentials, browser session token, platform bypass, rate-limit bypass, or downloader workaround was used.

## 4. Intermediate Batch 01 Target Selection

Selection rules applied:

- preserve retrieved playlist order;
- skip already summarized/audited entries where known;
- prefer first unsummarized entries in playlist order;
- keep batch size between 5 and 8 videos;
- do not include non-intermediate playlist videos;
- skip any playlist entry that cannot be safely resolved;
- do not infer caption availability from title alone.

Playlist order 2 (`_sx3dCvPXac`) is skipped because committed docs already identify it as summarized/audited. The first selected unsummarized batch is therefore playlist orders 1 and 3 through 7.

| playlist order | video ID | compact title | already summarized/audited status | committed availability status if known | planned access handling | notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `-2gNKPqIpAs` | 【FXの勝ち方】億トレが実践する利益を積み上げるシンプルな方法 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | First retrieved intermediate entry and not known as already summarized. |
| 3 | `4YcjlIvDkug` | 【環境が激変】2026年最新版のFX会社の選び方と立ち回り方 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Order 2 skipped as already summarized/audited. |
| 4 | `xnH6ODNMFHs` | 【永久保存版】2025年ゴールド総評と必ず勝つためのゴールドの全てを教えます。 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Included by source order; no caption availability inferred from title. |
| 5 | `ICCkkPufugI` | 【完全版】FXで超重要の波形の正しい見方とは？ | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Included by source order; no summary is created in this PR. |
| 6 | `ZIg8SxoAEd0` | 【神回】FX専業トレーダーがこれだけは大切にしている２つのこと | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Included by source order; no candidate inventory is created in this PR. |
| 7 | `9PIrE3TMjK8` | 【永久保存版】環境認識の全てがわかる完全講義 | no | not found in committed docs | `DownSub availability probe and caption body attempt`; `skip if unavailable or blocked` | Sixth selected target keeps Batch 01 modest. |

Skipped known summarized/audited row:

| playlist order | video ID | compact title | skip reason |
| ---: | --- | --- | --- |
| 2 | `_sx3dCvPXac` | 【FXの負け方】この行動を取れば確実に負けます。 | Already summarized/audited in committed Batch 01-07 corpus work; reference existing summary/audit rather than re-summarizing by default. |

## 5. Caption Access Strategy

Preferred future route:

- one bounded DownSub batch for exactly these selected intermediate Batch 01 video IDs:
  - `-2gNKPqIpAs`
  - `4YcjlIvDkug`
  - `xnH6ODNMFHs`
  - `ICCkkPufugI`
  - `ZIg8SxoAEd0`
  - `9PIrE3TMjK8`
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

## 6. Summary Output Strategy After Access

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

## 7. Relation To Beginner Synthesis

The beginner playlist line is complete, summarized, audited, and synthesized. Intermediate Batch 01 should be interpreted as the next source-order layer after the completed beginner playlist, not as a rewrite of the beginner synthesis.

Intermediate material may later clarify or challenge how concepts develop after the beginner line, but it should not retroactively rewrite `docs/video_research/playlist_led_summaries/beginner_playlist_synthesis.md` in the access-planning PR.

This plan does not update Doctrine Map v1, does not finalize Doctrine Map v2, does not treat the Doctrine Map v2 draft proposal as final doctrine, and does not modify Strategy A/B.

## 8. Recommended Next PR

Recommended next PR:

`Channel playlist-led intermediate batch 01 DownSub access and summaries`

Reason:

- the intermediate Batch 01 target is now defined;
- future PR can access DownSub only for the selected IDs if project-owner approval is granted;
- future PR should produce paraphrased summaries, aggregate report, and review;
- future PR should not modify Strategy A/B or Strategy B.

## 9. Guardrails

This PR explicitly preserves these guardrails:

- no DownSub access in this PR;
- no caption/subtitle/transcript body access in this PR;
- no caption URL access or commits;
- no raw transcript/subtitle/caption URL commits;
- no raw playlist metadata dump commits;
- no CSV/JSON/database/data/results commits;
- no video/audio download;
- no ASR;
- no proxy/VPN/IP rotation/cookies/credentials/platform bypass/rate-limit bypass;
- no market data;
- no broker/live trading;
- no Strategy A/B changes;
- no Strategy B changes;
- no Strategy B2/C;
- no backtests;
- no optimization;
- no profitability claims;
- no Doctrine Map v1 update;
- no final Doctrine Map v2 creation;
- Batch 08 remains blocked and not completed.

## 10. Readiness Decision

Readiness decision:

`intermediate_batch_01_caption_access_plan_ready_for_review`

Reason: this plan defines a modest six-video first intermediate playlist-led batch, uses retrieved playlist order, skips the known already summarized/audited order-2 entry, records the bounded metadata-only access used to resolve the first target rows, preserves source-access and raw-artifact guardrails, and does not authorize summaries, DownSub access, Doctrine Map changes, Strategy changes, backtests, optimization, market-data access, broker/live execution, or profitability claims.

The selected batch is ready for a bounded DownSub access PR after explicit project-owner approval.
