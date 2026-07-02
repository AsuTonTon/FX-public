# Channel Lightweight Summary Batch 08 Caption Access Recovery and Selection Rework Ledger

Task: `channel_lightweight_summary_batch_08_caption_access_recovery_and_selection_rework`

This ledger records the compact, Git-safe fields for the provisional Batch 08 carry-forward candidates retained during the blocked selection attempt. It paraphrases already merged timestamp-supported audit notes and does not include raw transcript text, subtitle text, caption URLs, videos, screenshots, CSV, JSON, data, or result files.

This ledger does not freeze a Batch 08 summary target set. No Batch 08 summaries should be created from this PR.

## Caption-access recovery status

- 2026-06-27 read-only recovery probe sample: `3B2dVpvZ3yE`, `H0E10F_yuDE`, and `Sb-C0G7R1Yg`.
- Subtitle availability metadata remained reachable, but caption body retrieval stayed blocked.
- Subtitle body download attempts returned HTTP 429 Too Many Requests.
- Transcript API attempts returned IP-blocked responses.
- Local ignored caption-cache filename review found only two unsummarized high-priority caption-available IDs available locally: `5SZn-cM0D4M` and `k4nDAp3t8js`.
- No final Batch 08 target set is frozen.

## Provisional carry-forward ledger

### 5SZn-cM0D4M

| field | value |
| --- | --- |
| video_id | 5SZn-cM0D4M |
| source_title | 【4時間足の衝撃】1日5分のチェックで月100万。チャートに張り付くほど負ける「逆説の真実」【FX講座Part3】 |
| content_type | regular_video |
| caption_status | auto_caption |
| timestamp references | 01:30-01:38; 02:18-03:40; 05:20-07:40; 08:20-09:20 |
| setup/context | Timeframe-doctrine lecture defining trade styles by timeframe. Four-hour trading is treated as a medium/longer axis, while scalping depends more on short-term price-action precision. |
| entry | For scalping, the evidence emphasizes two or more grounds and high-expectancy locations, but no individual entry trigger is stated. |
| stop/invalidation | not stated |
| TP/exit | not stated |
| range/trend filter | Four-hour Elliott wave, chart pattern, and trend-follow categories are ranked conceptually, but no repeatable setup filter is defined. |
| timeframe/session | Checking at 4H candle confirmation and using alerts are discussed; extending 4H logic to daily/weekly context is discussed; no market session rule is stated. |
| indicator usage | not stated |
| RR | Four-hour trading frequency, win rate, and lot sizing are discussed; no individual RR condition is stated. |
| trade management | Lot adjustment by expected monthly opportunity count and win rate is discussed as doctrine, not as a trade-by-trade management procedure. |
| discretionary elements | Trade style, risk, lot allocation, and timeframe choice remain trader-dependent. |
| relation to Batch 01-07 findings | Supports the cross-batch timeframe-hierarchy family, but does not add atomic setup, entry, stop, or TP mechanics. |
| audited relevance class | doctrine_or_context |
| confidence | medium |
| final selection decision and reason | provisional_carry_forward_only: retained for a future broader Batch 08 selection audit, but not selected here because caption-supported audit evidence could not be gathered for enough of the remaining unsummarized pool. |

### Sb-C0G7R1Yg

| field | value |
| --- | --- |
| video_id | Sb-C0G7R1Yg |
| source_title | 【誰でもできる】FX重要水平線の引き方と実際のエントリー方法〔ゆっくり実況〕 |
| content_type | regular_video |
| caption_status | auto_caption |
| timestamp references | 00:40-04:45 |
| setup/context | Horizontal lines are treated as auxiliary context rather than standalone entry grounds. |
| entry | Shorter-timeframe lines can help with pullback or break timing, but wave shape is emphasized as more important than the line itself. |
| stop/invalidation | not stated |
| TP/exit | Daily or weekly horizontal lines can become TP candidates, but earlier exit or chart watching can override. |
| range/trend filter | Nearby important lines can block entries when there is no reason for price to cross them. |
| timeframe/session | Monthly, weekly, and daily lines are drawn first; nearby relevant lines are preferred for a 4H monitoring axis. No session rule is stated. |
| indicator usage | not stated |
| RR | not stated |
| trade management | not stated |
| discretionary elements | Line importance, wave quality, and instrument context remain visual. |
| relation to Batch 01-07 findings | Useful horizontal-line doctrine. It overlaps prior line-construction evidence but adds a compact older row connecting line drawing, entry context, and possible TP candidate lines. |
| audited relevance class | partial_mechanical_rule |
| confidence | medium |
| final selection decision and reason | provisional_carry_forward_only: retained for a future broader Batch 08 selection audit, but not selected here because caption-supported audit evidence could not be gathered for enough of the remaining unsummarized pool. |

## Final selected IDs

No final Batch 08 selected IDs are frozen in this blocked revision.
