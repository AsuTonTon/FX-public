# Channel Transcript Availability Report

Task: `channel_transcript_availability_survey`

## 1. Objective

This report records a metadata-only transcript/caption availability survey for the channel corpus research track. It is not transcript analysis, lightweight summarization, doctrine extraction, Strategy A/B gap analysis, or a Strategy B2 design step.

This revision corrects the corpus scope: PR #15 measured the channel `/videos` tab only. The current full-channel working scope is the deduplicated union of `/videos`, `/shorts`, and `/streams` tab enumeration. The report therefore preserves the existing 509-row `/videos` transcript availability survey while explicitly marking newly discovered scope-reconciliation rows as uninspected `unknown`.

The survey only classifies whether caption-like availability appears to exist. It does not retrieve, store, summarize, or commit transcript bodies, subtitle bodies, caption URLs, or raw subtitle metadata.

## 2. Baseline and Scope Reconciliation

- PR #15 regular-video-tab baseline: 509 rows from `https://www.youtube.com/channel/UCsyzKL2_be8U8ns5gfr1y5Q/videos`
- Project owner observed YouTube channel count: 601 videos displayed
- Current `/videos` tab unique count: 509
- Current `/shorts` tab unique count: 92
- Current `/streams` tab unique count: 0
- Deduplicated `/videos` + `/shorts` + `/streams` union count: 601
- Difference between deduplicated union and owner-observed 601: 0
- Newly discovered rows outside the original 509-row `/videos` survey: 92
- Collection date: 2026-06-25
- Channel ID: `UCsyzKL2_be8U8ns5gfr1y5Q`
- Channel name: `ハイトレFX億トレーダーへの道`

Tab overlap counts using `video_id` deduplication:

| overlap | count |
| --- | ---: |
| videos_shorts | 0 |
| videos_streams | 0 |
| shorts_streams | 0 |
| all_three | 0 |

The `/streams` endpoint returned no playlist in this run. It is therefore recorded as 0 measured rows with the compact note `tab may be absent`; this report does not infer that no livestream archives have ever existed.

## 3. Method

- Tool: `yt-dlp` 2026.06.09
- Channel tab enumeration method: metadata-only flat playlist extraction for `/videos`, `/shorts`, and `/streams`
- Transcript availability method: preserved existing per-video Python API availability inspection for the original 509 `/videos` rows only
- Subtitle writing: disabled
- Automatic-subtitle writing: disabled
- Media download: disabled
- Credentials/cookies: not used
- Rate-limit bypass: not attempted
- Local row-level outputs: compact working files only under ignored `data/` and `results/` paths

The tab reconciliation immediately reduced flat playlist rows to compact local fields such as `video_id`, canonical URL, source title, tab membership, and compact content type. It did not collect transcript bodies, subtitle bodies, caption URLs, full descriptions, videos, audio, cookies, credentials, or raw subtitle dictionaries.

## 4. Title Locale Handling

For the scope reconciliation pass, metadata was requested with Japanese preference:

- HTTP `Accept-Language`: `ja-JP,ja;q=0.9,en-US;q=0.5,en;q=0.3`
- YouTube extractor language argument: `lang=ja`
- Local title field used for title-only routing: `source_title`
- Separate local `localized_title` field: reserved but empty in this flat playlist pass because a second title variant was not returned

Priority classification in this revision used `source_title` where available. The earlier PR #17 availability rows had environment-dependent localized/translated-looking titles in several places; those titles were not used as the primary classification source for the union recalculation.

## 5. Explicit Exclusions

This task did not retrieve or persist:

- Transcript bodies.
- Subtitle bodies.
- Caption URLs.
- Videos.
- Audio.
- Full descriptions.
- Raw subtitle dictionaries.
- Credentials, cookies, tokens, or browser session data.
- Market data.
- Broker data.
- Backtest outputs.

No Strategy A/B code, Strategy A/B parameters, Strategy C files, parameter optimization, or profitability claims were created or changed.

## 6. Availability Counts Over the Full Union

The original honest partial survey is preserved:

- Original regular-video input rows: 509
- Directly inspected before rate-limit stop: 485
- Regular-video rows classified from that inspection: 483 `auto_caption`, 1 `unavailable`, 1 `blocked`
- Regular-video rows not inspected after rate-limit stop: 24 `unknown`

Full deduplicated union availability counts:

- `manual_caption`: 0
- `auto_caption`: 483
- `unavailable`: 1
- `blocked`: 1
- `unknown`: 116

Primary status count check:

- `0 + 483 + 1 + 1 + 116 = 601`

The 92 newly discovered Shorts rows were not checked for transcript availability in this correction. They are classified as `unknown` with compact category `scope_reconciliation_not_inspected`, not as `unavailable`.

## 7. Availability by Content Type

| content_type | manual_caption | auto_caption | unavailable | blocked | unknown |
| --- | ---: | ---: | ---: | ---: | ---: |
| regular_video | 0 | 483 | 1 | 1 | 24 |
| short | 0 | 0 | 0 | 0 | 92 |
| stream | 0 | 0 | 0 | 0 | 0 |
| multiple_tabs | 0 | 0 | 0 | 0 | 0 |
| unknown | 0 | 0 | 0 | 0 | 0 |

Inspection coverage by content type:

| content_type | directly_inspected | rate_limit_stop_not_inspected | scope_reconciliation_not_inspected |
| --- | ---: | ---: | ---: |
| regular_video | 485 | 24 | 0 |
| short | 0 | 0 | 92 |
| stream | 0 | 0 | 0 |
| multiple_tabs | 0 | 0 | 0 |
| unknown | 0 | 0 | 0 |

Content type counts:

| content_type | count |
| --- | ---: |
| regular_video | 509 |
| short | 92 |
| stream | 0 |
| multiple_tabs | 0 |
| unknown | 0 |

Every union row has exactly one compact content type. Rows appearing in multiple tabs would be classified as `multiple_tabs` and counted once in the union; this run found no cross-tab overlaps.

## 8. Title-Only Research Priority Recalculation

Priority is title-only weak routing metadata. It is not transcript-confirmed doctrine evidence.

Priority counts over the 601-row union:

- `high`: 115
- `medium`: 186
- `low`: 300
- `exclude`: 0
- `unknown`: 0

Priority count check:

- `115 + 186 + 300 + 0 + 0 = 601`

Priority by content type:

| content_type | high | medium | low | exclude | unknown |
| --- | ---: | ---: | ---: | ---: | ---: |
| regular_video | 100 | 150 | 259 | 0 | 0 |
| short | 15 | 36 | 41 | 0 | 0 |
| stream | 0 | 0 | 0 | 0 | 0 |
| multiple_tabs | 0 | 0 | 0 | 0 | 0 |
| unknown | 0 | 0 | 0 | 0 | 0 |

Priority by transcript availability status:

| priority | manual_caption | auto_caption | unavailable | blocked | unknown |
| --- | ---: | ---: | ---: | ---: | ---: |
| high | 0 | 95 | 0 | 0 | 20 |
| medium | 0 | 146 | 0 | 0 | 40 |
| low | 0 | 242 | 1 | 1 | 56 |
| exclude | 0 | 0 | 0 | 0 | 0 |
| unknown | 0 | 0 | 0 | 0 | 0 |

The classifier was conservative title-only routing based on explicit title terms for TP/target, stop/loss, range/filter, breakout, horizontal-line/support-resistance, 3-wave/wave completion, risk/reward, and closely related channel wording. `title_detected` priority remains separate from any future `transcript_confirmed` themes.

## 9. High-Priority Availability Queue

The high-priority queue was regenerated from the complete 601-row deduplicated union in the local-only working inventory. To avoid committing a generated row-level inventory, this report commits the aggregate high-priority counts and the still-unaccounted high-priority availability queue only.

- High-priority total: 115
- High-priority regular videos: 100
- High-priority Shorts: 15
- High-priority streams: 0
- High-priority rows still `unknown`: 20
- Newly discovered high-priority rows not inspected for transcript availability: 15

High-priority unknown rows that must remain queued before any summary batch is recommended:

| video_id | content_type | tabs | source_title | canonical_url | blocked category | matched title terms |
| --- | --- | --- | --- | --- | --- | --- |
| `GIHwOx6iwiw` | regular_video | videos | 借金まみれの負け組FXトレーダーが専業になれたきっかけ３選 | https://www.youtube.com/watch?v=GIHwOx6iwiw | rate_limited_stop_not_inspected | 負け |
| `K9oqYLAURwY` | regular_video | videos | 海外FX/XM10万円チャレンジ/ロスカット連続で破産危機？/第2話 | https://www.youtube.com/watch?v=K9oqYLAURwY | rate_limited_stop_not_inspected | ロスカット, 破産 |
| `exvd6NsrUHg` | regular_video | videos | FXなぜ負ける？勝てない負け組トレーダー3つの特徴とは？ | https://www.youtube.com/watch?v=exvd6NsrUHg | rate_limited_stop_not_inspected | 負け, 負ける |
| `kLgVB7Ixcsk` | regular_video | videos | 【ゆっくり実況】XM10万円チャレンジ！リスクリワード最強トレード達成！ハイトレFX/第８話 | https://www.youtube.com/watch?v=kLgVB7Ixcsk | rate_limited_stop_not_inspected | リスクリワード, リスクリ |
| `mQ1VGydnrZI` | regular_video | videos | 【ゆっくり実況　FX】破産寸前!?１億円ロスカットで大損した友人Mの経緯を暴露!誰もが陥る落とし穴と対策について | https://www.youtube.com/watch?v=mQ1VGydnrZI | rate_limited_stop_not_inspected | ロスカット, 大損, 破産 |
| `6SUZWdAUd6c` | short | shorts | ※大失態※ 1000万飛ばす寸前だった最悪のトレード | https://www.youtube.com/watch?v=6SUZWdAUd6c | scope_reconciliation_not_inspected | 飛ばす |
| `8H_4AJR0llg` | short | shorts | 【1分でわかる】勝率9割超え「AB手法」の勝ちパターン連発 | https://www.youtube.com/watch?v=8H_4AJR0llg | scope_reconciliation_not_inspected | 勝ちパターン |
| `FYPWegu43mo` | short | shorts | FXで負け続けているあなたへ#shorts #trading | https://www.youtube.com/watch?v=FYPWegu43mo | scope_reconciliation_not_inspected | 負け |
| `GB7wgE3GZtc` | short | shorts | 押し戻りの「待ち方」で負けを激減させる方法#shorts #trading | https://www.youtube.com/watch?v=GB7wgE3GZtc | scope_reconciliation_not_inspected | 負け |
| `HbnU3Ee3qic` | short | shorts | 知らないと絶対勝てない水平線の秘密を1分解説#shorts #trading | https://www.youtube.com/watch?v=HbnU3Ee3qic | scope_reconciliation_not_inspected | 水平線 |
| `S3Z3W7bRdoM` | short | shorts | エリオット波動の3波を取る方法は？#shorts #投資 #trading | https://www.youtube.com/watch?v=S3Z3W7bRdoM | scope_reconciliation_not_inspected | 3波 |
| `SWDGYUMPvN8` | short | shorts | 【実証】公開済みの「3波手法」を実戦で使ったら一撃100万稼げました #shorts #trading | https://www.youtube.com/watch?v=SWDGYUMPvN8 | scope_reconciliation_not_inspected | 3波 |
| `TzOwRNmaXrI` | short | shorts | 【FX】9割がやっている。三角持ち合いで「ダマシ」に遭う本当の理由#shorts #trading | https://www.youtube.com/watch?v=TzOwRNmaXrI | scope_reconciliation_not_inspected | ダマシ |
| `k4nDAp3t8js` | short | shorts | 【FX】三角持ち合いの「ダマシ」を完全に回避して700万稼いだ方法 #shorts #trading | https://www.youtube.com/watch?v=k4nDAp3t8js | scope_reconciliation_not_inspected | ダマシ |
| `qNcZIRfNueg` | short | shorts | 【FX】損切り位置が「ドンピシャ」で狩られる理由 #shorts #trading | https://www.youtube.com/watch?v=qNcZIRfNueg | scope_reconciliation_not_inspected | 損切, 損切り |
| `qTrZJQiT5OE` | short | shorts | 【過去負けなし】12月のゴールドで一撃117万稼ぐ「本当の根拠」 #shorts #trading | https://www.youtube.com/watch?v=qTrZJQiT5OE | scope_reconciliation_not_inspected | 負け |
| `rj4lZBlUf8s` | short | shorts | 【これだけでOK】3波を狙うEMAトレード手法#shorts #trading | https://www.youtube.com/watch?v=rj4lZBlUf8s | scope_reconciliation_not_inspected | 3波 |
| `skD5BokrUTs` | short | shorts | FXで破産する人のNG行動とは？ #shorts #trading | https://www.youtube.com/watch?v=skD5BokrUTs | scope_reconciliation_not_inspected | 破産 |
| `tx4h1_ZSvXA` | short | shorts | エリオット波動3波を高確率で取る方法#shorts #trading | https://www.youtube.com/watch?v=tx4h1_ZSvXA | scope_reconciliation_not_inspected | 3波 |
| `wESvPcbu2CM` | short | shorts | レンジ相場を見極めて爆益を生み出す方法#shorts  #trading | https://www.youtube.com/watch?v=wESvPcbu2CM | scope_reconciliation_not_inspected | レンジ相場 |

This table contains no subtitle URLs, transcript text, subtitle text, full descriptions, or raw subtitle metadata.

## 10. Failure and Blocker Summary

Compact blocker categories now include both the previous rate-limit stop and the scope reconciliation rows:

- `rate_limited`: 1
- `rate_limited_stop_not_inspected`: 24
- `scope_reconciliation_not_inspected`: 92
- `unavailable/deleted`: 0
- `private`: 0
- `login required`: 0
- `geographic restriction`: 0
- `extractor error`: 0
- `ambiguous response`: 0
- `other`: 0

The previous transcript availability survey stopped when YouTube returned a rate-limit response. The remaining regular-video rows were not retried aggressively. The newly discovered Shorts rows were not checked for transcript availability in this correction and were not converted to `unavailable`.

## 11. Validation

Validation checks:

- `/videos` unique count is 509: passed.
- `/shorts` unique count is 92: passed.
- `/streams` measured unique count is 0 after absent-tab response: passed.
- Tab overlap arithmetic is correct: passed.
- Deduplicated union count is 601: passed.
- Difference from project owner observed 601 is 0: passed.
- Every union row has one `video_id`: passed.
- Every union row has one compact content type: passed.
- Every union row has one primary availability status: passed.
- Primary availability counts equal the deduplicated union count: passed.
- High/medium/low/exclude/unknown priority counts equal the deduplicated union count: passed.
- `live_chat` is excluded from caption classification: preserved from prior availability survey.
- `transcript_quality` remains `unknown`: passed.
- `transcript_confirmed_themes` remains empty: passed.
- No transcript or subtitle text exists in committed files: passed by file review.
- No caption URLs exist in committed files: passed by file review.
- No raw row-level inventory is committed: to be verified in the PR changed-files list.
- No files under `data/` or `results/` are committed: to be verified in the PR changed-files list.
- The committed diff must contain only this report: to be verified in the PR changed-files list.

Required local Git command results remain unavailable in this desktop folder:

- `git diff --name-only`: failed because the local desktop folder is not a valid Git worktree.
- `git status --short`: failed because the local desktop folder is not a valid Git worktree.

Because local Git is unavailable in this workspace, final changed-file validation must use the GitHub PR changed-files list. The PR must contain only:

- `docs/video_research/channel_transcript_availability_report.md`

## 12. Limitations

- Availability does not imply transcript quality.
- Automatic captions may contain recognition errors.
- Language availability does not establish that the content is strategy-relevant.
- Title-based priority remains weak evidence.
- Blocked and unknown rows must not be silently discarded.
- This task does not establish channel doctrine.
- The survey encountered rate limiting before all original regular-video rows could be directly inspected, leaving 24 regular-video rows as `unknown`.
- The 92 Shorts rows discovered during scope reconciliation were not inspected for transcript availability and remain `unknown`.
- The `/streams` tab returned no playlist in this run; this should be treated as measured absence of a tab response, not historical proof about all livestream archives.
- Compact language status from the prior survey is retained only for inspected regular-video rows.

## 13. Next Recommended Step

Do not start or recommend a lightweight-summary batch yet.

Before summary batching, every high-priority item from the complete deduplicated union must at least be accounted for at the transcript availability stage. The immediate next step is a bounded availability retry/accounting pass for the 20 high-priority `unknown` rows, including 15 newly discovered high-priority Shorts, without using cookies, credentials, transcript body retrieval, subtitle downloads, video/audio downloads, or rate-limit bypass tactics.
