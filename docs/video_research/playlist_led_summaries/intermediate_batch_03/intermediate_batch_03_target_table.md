# Playlist-Led Intermediate Batch 03 Target Table

Task: `channel_playlist_led_intermediate_batch_03_caption_execution`

## 1. Scope

This target table freezes the first modest Intermediate Batch 03 slice inside playlist orders 15 through 27 for:

`FX中級者のための勝率UP講座`

This execution stays on the first unresolved rows in source order and stops after the first six rows. It does not widen into later rows 21 through 27 in the same run.

## 2. Frozen target rows

| playlist order | video ID | compact title | metadata resolution status | caption access status | summary file |
| ---: | --- | --- | --- | --- | --- |
| 15 | `eBJ9OwHXPz8` | 【超有料級】FX専業がトレード時に絶対見ている「５つ」を全部教える。 | `metadata_resolved_via_bounded_playlist_check` | `caption_body_available` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/eBJ9OwHXPz8_summary.md` |
| 16 | `iRj9w9Ku1fc` | 【神回】最速で稼ぐために必要なたった１つのこと | `metadata_resolved_via_bounded_playlist_check` | `caption_body_available` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/iRj9w9Ku1fc_summary.md` |
| 17 | `UnRs896Utnc` | 【永久保存版】チャートパターンの全てがわかる完全講義 | `metadata_resolved_via_bounded_playlist_check` | `caption_body_available` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/UnRs896Utnc_summary.md` |
| 18 | `fbTWY8U4h9A` | 【完全版】ダウ理論を使ってFXで稼ぐための方法を教える。 | `metadata_resolved_via_bounded_playlist_check` | `caption_body_available` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/fbTWY8U4h9A_summary.md` |
| 19 | `fexGcPTNlN0` | 【FX初心者必見】少額トレーダーから専業になるまでの具体的な立ち回り | `metadata_resolved_via_bounded_playlist_check` | `caption_body_available` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/fexGcPTNlN0_summary.md` |
| 20 | `L1a9LT-ioeM` | 【最重要】勝ち組トレーダーになれる人の思考と行動とは？ | `metadata_resolved_via_bounded_playlist_check` | `caption_body_available` | `docs/video_research/playlist_led_summaries/intermediate_batch_03/L1a9LT-ioeM_summary.md` |

## 3. Boundary notes

- The slice stays inside the committed Batch 03 planning window of playlist orders 15 through 27.
- The slice size is 6 videos, which matches the preferred modest 6- or 7-video shape from the planning document.
- Rows 21 through 27 remain unresolved future work and are not accessed in this run.
- No skipped, unavailable, blocked, or guardrail-stopped row occurred inside the selected 15 through 20 slice.

## 4. Guardrails

- Only minimal playlist metadata needed for rows 15 through 20 was resolved.
- Caption access was limited to the exact six frozen IDs above.
- No raw caption text, transcript full text, caption URL, TXT, SRT, VTT, CSV, JSON, `data/`, `results/`, media, credential, or secret is committed.
- No Strategy A/B/B2/C, Doctrine Map, market-data, broker/live, backtest, optimization, or profitability-conclusion change is authorized by this table.
