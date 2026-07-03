# YouTube Corpus Post-Batch-03 Target Route Decision

Task: `youtube_corpus_post_batch_03_target_route_decision`

## 1. Objective

This note decides the next safe route for establishing an eligible YouTube
corpus target slice after the current Intermediate Batch 03 boundary.

It uses committed public repository Markdown only. It does not run source
access, threshold-discovery touches, metadata refresh, caption access, summary
creation, doctrine updates, Strategy changes, optimization, or trading
conclusion work.

## 2. Committed Docs Reviewed

Reviewed committed docs:

- `docs/video_research/youtube_corpus_threshold_discovery_stage_1.md`
- `docs/video_research/youtube_corpus_threshold_discovery_stage_2.md`
- `docs/video_research/youtube_corpus_access_cadence_failure_log_protocol.md`
- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_fallback_documentation_chain_closeout.md`
- `docs/video_research/channel_full_corpus_playlist_led_remaining_input_status_review.md`
- `docs/video_research/channel_playlist_metadata_reconciliation_report.md`
- `docs/video_research/channel_lightweight_summary_batch_08_selection_report.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_03_continuation_blocked_status.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_target_table.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_completed_summary_audit.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_target_table.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`

No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
live chat, community post, downloaded media, ASR, external source, private
repository content, local OHLC data, generated Strategy artifact, market-data
API, broker API, or live system was accessed.

## 3. Why Stage 2 Had No Eligible Target

Committed Batch 03 docs establish this source-order boundary:

| row window | committed status | target-route implication |
| --- | --- | --- |
| `15..20` | Completed first Intermediate Batch 03 slice with summaries and completed-summary audit. | Not eligible for threshold discovery. |
| `21..27` | Target-resolved continuation slice. Stage 1 touched all seven rows once and recorded `success_git_safe_summary_possible`; later registry docs still treat the older continuation bundle as blocked-status evidence only. | Exhausted as the stage 1 source-order slice; not a new stage 2 target. |
| `28` | Documented in the playlist metadata reconciliation report as already summarized/audited. | Should be referenced or skipped, not treated as a new unresolved target by default. |
| after `28` | The committed docs do not provide a full ordered table of exact next unresolved row numbers, video IDs, compact titles, and skip/completion status. | Not eligible for source access or threshold discovery until a new target slice is established. |

PR-stage evidence therefore supports the same stop reason recorded in stage 2:

`no_eligible_committed_unresolved_targets_after_rows_21_27`

The gap is not caption access. The immediate gap is target identity and
source-order accounting after the Batch 03 window. Without a committed target
slice, a stage 2 worker would have to choose videos from incomplete metadata or
title context, which would widen the task beyond the approved target boundary.

## 4. Route Options Reviewed

| option | decision | reason |
| --- | --- | --- |
| Docs-only target table extension | Not sufficient now | Committed docs do not include the exact post-27 unresolved row/ID/title table needed to extend the target table without a new bounded target-resolution step. |
| Bounded metadata-only target-resolution issue | Recommended | This is the smallest route that can establish the next source-order slice while keeping target resolution separate from caption-body threshold discovery. |
| Fallback-only inventory reconciliation task | Defer | The fallback chain is already closed for routine docs-only work, and broad inventory reconciliation would be wider than the immediate post-Batch-03 target-slice gap. |
| Deferral because committed docs are insufficient | Partial | Source access must defer now, but the actionable next step is a narrow metadata-only target-resolution issue rather than indefinite no-op. |

## 5. Recommended Next Route

Recommended route:

`bounded_metadata_only_post_batch_03_target_resolution`

Recommended next issue title:

`[codex] Establish next YouTube corpus target slice after Batch 03`

Recommended scope:

- use committed docs as the starting point;
- explicitly authorize only the minimal metadata resolution needed to establish
  the next source-order target slice after the Intermediate Batch 03 boundary;
- stay inside the owner-supplied playlist-led corpus route unless the issue
  explicitly authorizes a different source-order basis;
- preserve source order;
- skip or reference already summarized/audited rows such as committed row `28`
  instead of re-summarizing them by default;
- produce one Git-safe target table with exact row numbers, video IDs, compact
  titles, committed completion/skip status, and eligibility labels;
- do not fetch caption bodies, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, ASR, market data, or
  broker/live systems;
- do not create summaries;
- do not run threshold-discovery touches;
- do not update doctrine or Strategy conclusions.

The target-resolution issue should define a source-order slice large enough for
a future stage 2 threshold-discovery issue to select from, but it should not
perform stage 2 itself. If metadata resolution cannot be performed safely
without raw artifacts, broad scraping, bypass-like handling, or unrelated
channel access, it should stop with a blocker note.

## 6. Source-Access Decision

Source access remains blocked for threshold discovery until a new committed
target slice is established.

This note does not authorize:

- caption-body access;
- DownSub access;
- subtitle or transcript retrieval;
- target-slice source touches;
- threshold discovery;
- summary recovery;
- raw metadata dumps;
- broad playlist or channel scraping;
- Strategy A/B/B2/C changes;
- doctrine updates;
- parameter optimization;
- trading-readiness, win-rate, money-making, or profitability claims.

## 7. Guardrail Statement

Docs-only decision note. No raw transcript text, subtitle full text, caption
URL, request URL, raw response body, TXT/SRT/VTT, CSV, JSON, `data/`,
`results/`, downloaded media, credential, token, cookie, session, IP address,
or secret was added. No YouTube, DownSub, caption, subtitle, transcript-body,
comment, live chat, community post, browser source access, alternate source
route, media download, ASR, VPN, proxy, IP rotation, cookie/session swap,
CAPTCHA workaround, parallel scraping, market-data API, broker API, order
placement, auto-trading, or live system was used.

No Strategy A/B/B2/C behavior, code, parameters, configs, tests, runners,
backtests, market-data handling, broker/live behavior, doctrine conclusion, or
trading conclusion was changed. No Strategy B2 or Strategy C was created. No
parameter optimization was performed. No profitability, trading-readiness,
win-rate, money-making, or trading-recommendation claim was made. The YouTube
channel-wide corpus line remains separate from Strategy A/B verification.

## 8. Decision

Decision:

`post_batch_03_target_route_requires_bounded_metadata_only_target_resolution`

Reason: committed docs prove that rows `15..20` are complete, rows `21..27`
were the stage 1 source-order slice, and no exact later unresolved source-order
target table is committed. Stage 2 caption-body threshold discovery should not
continue until a separate bounded target-resolution issue establishes the next
eligible slice.
