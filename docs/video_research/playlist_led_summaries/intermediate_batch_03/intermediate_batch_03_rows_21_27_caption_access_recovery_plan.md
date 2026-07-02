# Playlist-Led Intermediate Batch 03 Rows 21-27 Caption-Access Recovery Plan

Task: `channel_playlist_led_intermediate_batch_03_rows_21_27_caption_access_recovery_plan`

## 1. Objective and scope

This docs-only recovery plan defines the conservative next handling for Intermediate Batch 03 rows `21..27` after the bounded target-resolution run documented all seven rows as caption-blocked.

This plan uses committed repository docs only. It performs no new source access and does not authorize immediate caption retry by itself.

This plan does not:

- access YouTube;
- access DownSub;
- access captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, downloaded media, or unrelated channel surfaces;
- run ASR;
- modify rows `15..20`;
- change row, ID, title, or access-status evidence for rows `21..27`;
- update Doctrine Map v1 or create a final Doctrine Map v2;
- modify Strategy A/B/B2/C code, rules, parameters, configs, tests, or conclusions;
- run backtests or optimization;
- access market data;
- use broker APIs or add broker/live execution behavior;
- make profitability claims.

## 2. Committed source docs used

This recovery plan relies only on these committed repository docs:

- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_target_table.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_aggregate_report.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_review.md`

These docs are sufficient to establish the exact unresolved row window, the seven target video IDs, and the known caption-access blocker.

## 3. Known blocker summary

Rows `21..27` are now mechanically target-resolved but not summary-complete.

| playlist order | video ID | committed caption status | summary status |
| ---: | --- | --- | --- |
| 21 | `bG3-_KfpskE` | `caption_access_blocked_http_429` | not created |
| 22 | `-VNpaMQWGUE` | `caption_access_blocked_http_429` | not created |
| 23 | `69XsLQQwo_M` | `caption_access_blocked_http_429` | not created |
| 24 | `8ityiaa4j8c` | `caption_access_blocked_http_429` | not created |
| 25 | `8tzBkeMR92g` | `caption_access_blocked_http_429` | not created |
| 26 | `piuUBEWYeug` | `caption_access_blocked_http_429` | not created |
| 27 | `ex-3Ywii0Qs` | `caption_access_blocked_http_429` | not created |

Committed docs record that caption access was attempted only for the exact seven selected IDs and returned HTTP 429 for every row. They also record that the run stopped without retries at scale, alternate caption routes, DownSub access, media download, ASR, comments, live chat, community posts, unrelated videos, or broader channel surfaces.

The recovery decision is:

`wait_then_small_probe_only`

Reason: HTTP 429 indicates an access instability or rate-limit condition, so the next step should wait before any future bounded probe and should stop immediately if the same blocker persists.

## 4. Wait-period guidance

Before any future caption-access recovery probe, wait at least `24` hours from the last documented HTTP 429 caption-access run or from the last failed recovery probe, whichever is later.

The wait period is a project hygiene rule for this recovery path. It is not evidence that access will later succeed, and it does not authorize broader collection.

If the wait period has not elapsed, the next issue should remain planning-only or no-op. It should not attempt captions, alternate access routes, or broader playlist/channel checks.

## 5. Future small-probe criteria

A future issue may authorize a small recovery probe only if all criteria below are met:

- the issue explicitly authorizes a caption-access recovery probe after the wait period;
- the target set is exactly rows `21..27`;
- the probe uses only the seven frozen video IDs from the committed target table;
- the probe starts with the earliest unresolved row, row `21`;
- the first probe batch is limited to at most `2` selected IDs;
- any expansion beyond the first `2` IDs requires those first probes to return caption bodies without HTTP 429, empty-body, unavailable, or ambiguous-access failures;
- no raw caption text, caption URL, raw response body, TXT, SRT, VTT, CSV, JSON, `data/`, or `results` artifact is committed;
- no DownSub, media download, ASR, comments, live chat, community posts, unrelated channel surfaces, proxy, VPN, IP rotation, cookies, credentials, platform bypass, rate-limit bypass, or downloader workaround is used.

The probe should remain source-order preserving. It should not skip ahead to later rows merely to find an easier accessible item.

## 6. Stop conditions

A future recovery probe must stop immediately if any of these conditions occur:

- any selected ID returns HTTP 429 again;
- any selected ID returns a zero-byte or empty caption body;
- caption availability is ambiguous or inconsistent across clients;
- access requires credentials, cookies, account state, proxying, IP rotation, or other bypass-like handling;
- the probe would require DownSub, downloaded media, ASR, comments, live chat, community posts, or unrelated channel surfaces;
- the probe would require raw transcript, subtitle text, caption URL, raw response body, TXT, SRT, VTT, CSV, JSON, `data/`, or `results` files to be committed;
- the task begins to imply Strategy, Doctrine, backtest, market-data, broker/live, optimization, or profitability conclusions.

If a stop condition occurs, the PR should document only the blocked status, the exact selected IDs checked, and the conservative next recommendation. It should not create paraphrased summaries from titles alone.

## 7. Reporting requirements

Any future recovery PR should include:

- exact rows and IDs probed;
- source-access statement;
- wait-period confirmation;
- access outcome per probed ID;
- whether captions were available, blocked, unavailable, or ambiguous;
- summary files created only for rows with available caption bodies;
- blocked-row accounting for every selected row that remains unresolved;
- explicit statement that title language is metadata only;
- raw-artifact and source-access guardrail statement;
- Strategy, Doctrine, market-data, broker/live, backtest, optimization, and profitability guardrail statement;
- validation commands and changed-file sanity check.

If the first `2` IDs remain blocked, the future PR should not continue to the remaining five IDs. It should record a continued-blocker outcome for rows `21..27` and recommend another wait or a human decision before any later probe.

## 8. Deliverable matrix

| outcome | future deliverables | next recommendation |
| --- | --- | --- |
| full success | target table status update, one paraphrased summary per accessible row, aggregate report, review document | proceed to a completed-summary audit for rows `21..27` |
| partial success | summaries only for accessible source-order rows, blocked-row note for the rest, aggregate report, review document | plan a narrow repair step for remaining blocked rows |
| continued blocker | access-status note, blocker summary, no per-video summaries | wait again or request human decision before any further probe |
| unsafe or ambiguous access | blocker note only, no summaries | stop and preserve current docs without widening source access |

No outcome should update Strategy A/B/B2/C, Doctrine Map, backtests, market-data handling, broker/live behavior, optimization settings, or profitability conclusions.

## 9. Recommended next issue

Recommended next issue title:

`[codex] Channel playlist-led intermediate batch 03 rows 21-27 caption-access recovery probe`

Recommended scope:

- wait-period confirmation;
- exact target set limited to rows `21..27`;
- initial source-order probe limited to rows `21..22`;
- stop if HTTP 429, empty body, unavailable, ambiguous, or bypass-like access appears;
- create paraphrased Markdown summaries only for rows with successfully available caption bodies;
- otherwise document the continued blocker without summary creation.

The next issue should explicitly state that it authorizes the small probe. Without that explicit authorization, future automation should treat this recovery plan as documentation only.

## 10. Readiness decision

Readiness decision:

`intermediate_batch_03_rows_21_27_recovery_plan_ready_for_review`

Reason: committed docs already establish the exact rows `21..27`, all seven video IDs, and the current `caption_access_blocked_http_429` outcome; this plan defines a conservative wait-before-probe path, strict probe limits, stop conditions, reporting requirements, and outcome-specific deliverables without performing new source access or touching raw artifacts, Strategy, Doctrine, market-data, broker/live, backtest, optimization, or profitability boundaries.
