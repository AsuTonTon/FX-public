# Channel High-Priority Availability Completion Report

Task: `channel_high_priority_transcript_availability_completion`

## 1. Objective

This report records a bounded transcript/caption availability accounting pass for exactly the 20 high-priority rows that remained `unknown` after PR #17.

This task does not summarize videos, extract channel doctrine, modify Strategy A/B, create Strategy C, or begin Strategy B2 design. Availability is only an accounting status; it is not evidence of transcript quality, channel doctrine, or mechanical rule validity.

## 2. Baseline

- Full deduplicated corpus from PR #17: 601 rows
- Title-only high-priority rows from PR #17: 115
- Previously known high-priority `auto_caption` rows: 95
- Target high-priority `unknown` rows for this pass: 20
- Regular-video targets: 5
- Shorts targets: 15
- Collection date: 2026-06-25

The pre-pass high-priority availability state was:

| primary_status | count |
| --- | ---: |
| manual_caption | 0 |
| auto_caption | 95 |
| unavailable | 0 |
| blocked | 0 |
| unknown | 20 |

## 3. Target Reconciliation

Target-set source:

- `docs/video_research/channel_transcript_availability_report.md`
- Section: `High-priority unknown rows that must remain queued before any summary batch is recommended`

Target validation before network inspection:

- Unique target video IDs: 20
- Regular-video targets: 5
- Shorts targets: 15
- Stream targets: 0
- Every target had availability status `unknown`: passed
- Every target had research priority `high`: passed
- Already-classified high-priority rows included: 0
- Medium- or low-priority rows included: 0

The local-only merged working inventory matched the report target list for all 20 IDs. No mismatch was found, so no row was added or removed outside the PR #17 report target list.

## 4. Method

- Tool: `yt-dlp` 2026.06.09 through the Python API
- Media download: disabled with `skip_download`
- Subtitle writing: disabled
- Automatic-subtitle writing: disabled
- Cookies/credentials/authenticated sessions: not used
- Request pattern: one target at a time, no parallel requests
- Request pacing: conservative sequential inspection with delay between targets
- Targets attempted: 20 of 20
- Stop condition: no rate-limit stop occurred

The inspection reduced in-memory caption availability metadata immediately to compact status fields. It did not persist subtitle format entries, caption URLs, complete language dictionaries, transcript bodies, subtitle bodies, extractor response bodies, or full error pages.

## 5. Per-Target Result Table

| video_id | content_type | source_title | canonical_url | inspection_attempted | primary_status | transcript_type | compact_language_status | blocked_category |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `GIHwOx6iwiw` | regular_video | 借金まみれの負け組FXトレーダーが専業になれたきっかけ３選 | https://www.youtube.com/watch?v=GIHwOx6iwiw | yes | auto_caption | auto_caption | multiple | - |
| `K9oqYLAURwY` | regular_video | 海外FX/XM10万円チャレンジ/ロスカット連続で破産危機？/第2話 | https://www.youtube.com/watch?v=K9oqYLAURwY | yes | auto_caption | auto_caption | multiple | - |
| `exvd6NsrUHg` | regular_video | FXなぜ負ける？勝てない負け組トレーダー3つの特徴とは？ | https://www.youtube.com/watch?v=exvd6NsrUHg | yes | auto_caption | auto_caption | multiple | - |
| `kLgVB7Ixcsk` | regular_video | 【ゆっくり実況】XM10万円チャレンジ！リスクリワード最強トレード達成！ハイトレFX/第８話 | https://www.youtube.com/watch?v=kLgVB7Ixcsk | yes | auto_caption | auto_caption | multiple | - |
| `mQ1VGydnrZI` | regular_video | 【ゆっくり実況　FX】破産寸前!?１億円ロスカットで大損した友人Mの経緯を暴露!誰もが陥る落とし穴と対策について | https://www.youtube.com/watch?v=mQ1VGydnrZI | yes | auto_caption | auto_caption | multiple | - |
| `6SUZWdAUd6c` | short | ※大失態※ 1000万飛ばす寸前だった最悪のトレード | https://www.youtube.com/watch?v=6SUZWdAUd6c | yes | unavailable | unavailable | unknown | - |
| `8H_4AJR0llg` | short | 【1分でわかる】勝率9割超え「AB手法」の勝ちパターン連発 | https://www.youtube.com/watch?v=8H_4AJR0llg | yes | auto_caption | auto_caption | multiple | - |
| `FYPWegu43mo` | short | FXで負け続けているあなたへ#shorts #trading | https://www.youtube.com/watch?v=FYPWegu43mo | yes | auto_caption | auto_caption | multiple | - |
| `GB7wgE3GZtc` | short | 押し戻りの「待ち方」で負けを激減させる方法#shorts #trading | https://www.youtube.com/watch?v=GB7wgE3GZtc | yes | auto_caption | auto_caption | multiple | - |
| `HbnU3Ee3qic` | short | 知らないと絶対勝てない水平線の秘密を1分解説#shorts #trading | https://www.youtube.com/watch?v=HbnU3Ee3qic | yes | auto_caption | auto_caption | multiple | - |
| `S3Z3W7bRdoM` | short | エリオット波動の3波を取る方法は？#shorts #投資 #trading | https://www.youtube.com/watch?v=S3Z3W7bRdoM | yes | auto_caption | auto_caption | multiple | - |
| `SWDGYUMPvN8` | short | 【実証】公開済みの「3波手法」を実戦で使ったら一撃100万稼げました #shorts #trading | https://www.youtube.com/watch?v=SWDGYUMPvN8 | yes | auto_caption | auto_caption | multiple | - |
| `TzOwRNmaXrI` | short | 【FX】9割がやっている。三角持ち合いで「ダマシ」に遭う本当の理由#shorts #trading | https://www.youtube.com/watch?v=TzOwRNmaXrI | yes | auto_caption | auto_caption | multiple | - |
| `k4nDAp3t8js` | short | 【FX】三角持ち合いの「ダマシ」を完全に回避して700万稼いだ方法 #shorts #trading | https://www.youtube.com/watch?v=k4nDAp3t8js | yes | auto_caption | auto_caption | multiple | - |
| `qNcZIRfNueg` | short | 【FX】損切り位置が「ドンピシャ」で狩られる理由 #shorts #trading | https://www.youtube.com/watch?v=qNcZIRfNueg | yes | unavailable | unavailable | unknown | - |
| `qTrZJQiT5OE` | short | 【過去負けなし】12月のゴールドで一撃117万稼ぐ「本当の根拠」 #shorts #trading | https://www.youtube.com/watch?v=qTrZJQiT5OE | yes | unavailable | unavailable | unknown | - |
| `rj4lZBlUf8s` | short | 【これだけでOK】3波を狙うEMAトレード手法#shorts #trading | https://www.youtube.com/watch?v=rj4lZBlUf8s | yes | auto_caption | auto_caption | multiple | - |
| `skD5BokrUTs` | short | FXで破産する人のNG行動とは？ #shorts #trading | https://www.youtube.com/watch?v=skD5BokrUTs | yes | auto_caption | auto_caption | multiple | - |
| `tx4h1_ZSvXA` | short | エリオット波動3波を高確率で取る方法#shorts #trading | https://www.youtube.com/watch?v=tx4h1_ZSvXA | yes | auto_caption | auto_caption | multiple | - |
| `wESvPcbu2CM` | short | レンジ相場を見極めて爆益を生み出す方法#shorts  #trading | https://www.youtube.com/watch?v=wESvPcbu2CM | yes | auto_caption | auto_caption | multiple | - |

This table contains no subtitle URLs, transcript text, subtitle text, raw subtitle metadata, full descriptions, or raw extractor output.

## 6. Completion-Pass Counts

Counts for the 20 target rows:

| metric | count |
| --- | ---: |
| manual_caption | 0 |
| auto_caption | 17 |
| unavailable | 3 |
| blocked | 0 |
| unknown | 0 |
| attempted | 20 |
| not_attempted | 0 |
| live_chat present | 0 |
| live_chat only | 0 |

Primary status count check:

- `0 + 17 + 3 + 0 + 0 = 20`

## 7. Revised Full-Union Availability

PR #17 full-union availability before this pass:

- `manual_caption`: 0
- `auto_caption`: 483
- `unavailable`: 1
- `blocked`: 1
- `unknown`: 116

Completion-pass delta:

- `auto_caption`: +17
- `unavailable`: +3
- `unknown`: -20
- `manual_caption`: no change
- `blocked`: no change

Revised full-union availability across all 601 rows:

| primary_status | count |
| --- | ---: |
| manual_caption | 0 |
| auto_caption | 500 |
| unavailable | 4 |
| blocked | 1 |
| unknown | 96 |

Full-union status count check:

- `0 + 500 + 4 + 1 + 96 = 601`

## 8. Revised High-Priority Availability

Revised availability across the 115 title-only high-priority rows:

| primary_status | count |
| --- | ---: |
| manual_caption | 0 |
| auto_caption | 112 |
| unavailable | 3 |
| blocked | 0 |
| unknown | 0 |

High-priority status count check:

- `0 + 112 + 3 + 0 + 0 = 115`

High-priority availability by content type:

| content_type | manual_caption | auto_caption | unavailable | blocked | unknown | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| regular_video | 0 | 100 | 0 | 0 | 0 | 100 |
| short | 0 | 12 | 3 | 0 | 0 | 15 |

## 9. Readiness Gate

High-priority availability accounting status:

| gate item | count |
| --- | ---: |
| High-priority rows directly attempted across availability passes | 115 |
| High-priority rows with usable captions | 112 |
| High-priority rows unavailable | 3 |
| High-priority rows blocked | 0 |
| High-priority rows still unknown after attempted inspection | 0 |
| High-priority rows never attempted | 0 |

Availability accounting gate: complete.

No high-priority target remains unattempted. The 3 `unavailable` rows are accounted for, but they are not eligible for caption-based summarization unless a later task uses a separately approved non-caption method. No such workaround was used in this task.

## 10. Guardrail Validation

Validation status:

- Only the new report should be committed: `docs/video_research/channel_high_priority_availability_completion_report.md`
- No `data/` files are staged or committed.
- No `results/` files are staged or committed.
- No row-level CSV or JSON inventory is committed.
- No transcript text is committed.
- No subtitle text is committed.
- No caption URL is committed.
- No video or audio was downloaded.
- No cookies, credentials, tokens, or authenticated browser sessions were used.
- No local speech-to-text or OCR was used.
- No Strategy A/B code or parameter was changed.
- No Strategy C was created.
- No market data or broker API was used.
- No backtest was run.
- No profitability claim was added.

Local `git diff --name-only` and `git status --short` are unavailable in this desktop workspace because it is not a valid Git worktree. Final changed-file validation must therefore use the GitHub PR changed-files list.

## 11. Limitations

- Caption availability does not imply caption quality.
- Automatic captions may contain recognition errors.
- Title-only high priority includes false positives.
- Shorts may be promotional, compressed summaries, or context-light excerpts.
- The 3 `unavailable` rows must not be silently removed from the high-priority research queue.
- Blocked and attempted-unknown rows must not be silently removed in future passes.
- This task does not establish channel doctrine.
- This task does not determine whether any video contains repeatable setup, entry, stop, TP, range, risk/reward, or invalidation rules.

## 12. Next Recommended Step

Do not summarize videos in this PR.

Because every high-priority target has now been attempted, the next recommended task is a separate high-priority relevance-triage pass before lightweight summaries. That triage should reduce the title-only 115 high-priority rows to videos likely to contain explicit setup, entry, stop, TP, range, risk/reward, or invalidation rules.

The triage task must remain docs/research-only and must not use immediate retry loops, cookies, audio transcription, OCR, access-control workarounds, Strategy A/B changes, Strategy C, or backtests.
