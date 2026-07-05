# Playlist-Led Intermediate Batch 03 Rows 21-27 Caption-Access Recovery Plan

Task: `channel_playlist_led_intermediate_batch_03_rows_21_27_caption_access_recovery_plan`

Issue refresh: `#241 [codex] Plan Intermediate Batch 03 rows 21-27 caption-access recovery after blocker`

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
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_22_tiny_recovery_probe.md`
- `docs/video_research/channel_playlist_led_post_beginner_intake_decision.md`
- `docs/video_research/channel_playlist_led_intake_status_after_beginner_batch_01.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_fallback_only_backlog_review.md`
- `docs/video_research/youtube_corpus_post_batch_03_intermediate_tail_closure_review.md`

These docs are sufficient to establish the exact row window, the seven target video IDs, the original caption-access blocker, the later rows `21..22` tiny recovery status, the rows `23..27` residual blocker boundary, and the row `62` separation requirement.

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

## 9. Issue #241 status refresh and recovery gate

This section is the current docs-only status refresh for Issue `#241`. It uses committed Markdown only and performs no YouTube, DownSub, caption, subtitle, transcript-body, caption URL, browser, media, ASR, market-data, broker/live, or generated-artifact access.

Issue #241 must not be read as a new authorization to retry all seven rows. The committed status is now split by source-order row:

| playlist order | video ID | latest committed status for this recovery plan | current handling |
| ---: | --- | --- | --- |
| 21 | `bG3-_KfpskE` | later tiny probe recorded `success_git_safe_summary_possible` | eligible only for a separately authorized compact-summary recovery task |
| 22 | `-VNpaMQWGUE` | later tiny probe recorded `success_git_safe_summary_possible` | eligible only for a separately authorized compact-summary recovery task |
| 23 | `69XsLQQwo_M` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |
| 24 | `8ityiaa4j8c` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |
| 25 | `8tzBkeMR92g` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |
| 26 | `piuUBEWYeug` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |
| 27 | `ex-3Ywii0Qs` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |

Recovery-gate decision:

`rows_21_22_summary_recovery_first_rows_23_27_need_explicit_bounded_probe_authorization`

Reason: committed docs now show rows `21..22` as source-order recovery candidates after the later tiny probe, while rows `23..27` still retain the prior blocker status for planning purposes. A future rows `23..27` probe remains blocked unless a controlling issue explicitly authorizes that exact bounded probe and satisfies the cooldown, duplicate-check, source-route, stop-condition, and raw-artifact guardrails.

Row `62` separation marker:

`row_62_remains_blocked_quarantined_outside_rows_21_27_recovery_scope`

Row `62` / `kljZef5IXLc` remains `blocked_row_62_unusable_context_after_authorized_refetch`. It is outside rows `21..27`, is not compact-summary complete, is not counted in this recovery plan, and must not be source-touched without a separate explicit PM authorization issue. Issue #241 creates no row-62 retry precedent.

Source-touch accounting fields for any later authorized recovery task:

| field | required value or rule |
| --- | --- |
| `active_issue_check` | Pass immediately before any source touch; stop if the controlling issue is closed, superseded, or ambiguous. |
| `duplicate_check` | Check open PRs, deterministic branches, same-title PRs, same issue references, and recently merged PRs before source touch and again before PR creation. |
| `authorized_route` | Use only the exact route named by the future controlling issue; do not substitute DownSub, ASR, browser, media download, comments, live chat, community posts, or broader channel access. |
| `target_rows` | Use only the rows named by the future controlling issue; default source-order handling after this refresh is rows `21..22` before rows `23..27`. |
| `target_video_ids` | Record only Git-safe public video IDs from committed docs. |
| `caption_body_attempted` | Record `yes` or `no` per selected row without raw text, request URLs, caption URLs, or response bodies. |
| `result_label` | Use compact Git-safe labels such as `success_git_safe_summary_possible`, `caption_access_blocked_http_429`, `caption_body_empty`, `caption_body_unavailable`, or `ambiguous_access`. |
| `error_category` | Record only a compact category; do not store raw source output. |
| `stop_decision` | Stop on 429, empty body, unavailable, ambiguous access, bypass-like requirements, raw-artifact needs, or Strategy/Doctrine/market-data/broker/live/profitability drift. |
| `raw_artifact_committed` | Must remain `no`. |
| `source_url_or_request_url_committed` | Must remain `no`. |
| `generated_data_artifact_committed` | Must remain `no`. |

## 10. Prior recommended next issue

The following recommendation was correct for Issue #241, before PR #244, PR
#248, and PR #250 resolved the rows `21..22` branch into row `21` recovered
and row `22` blocked. It is retained as lineage, but is superseded by the Issue
#251 status refresh in section 12.

Prior recommended next issue title:

`[codex] Intermediate Batch 03 rows 21-22 compact summary recovery`

Recommended scope:

- use committed Markdown only before any source touch;
- require explicit issue authorization for any caption-body source touch;
- target rows `21..22` only, because those are the only rows with a later committed `success_git_safe_summary_possible` probe result;
- create compact paraphrased Markdown summaries only if the authorized route succeeds again without raw-artifact or bypass-like conditions;
- leave rows `23..27` blocked and untouched unless a later issue explicitly authorizes another bounded source-order probe;
- keep row `62` blocked/quarantined and outside this recovery scope.

If the PM wants to retry rows `23..27` instead, that should be a separate issue with explicit bounded probe authorization, cooldown handling, duplicate checks, route naming, per-row source-touch accounting, and immediate stop conditions. Without that explicit authorization, future automation should treat rows `23..27` as blocked documentation only.

## 11. Readiness decision

Readiness decision:

`intermediate_batch_03_rows_21_27_recovery_plan_issue_241_status_refresh_ready`

Reason: committed docs establish the exact rows `21..27` and all seven video IDs; the original bounded run recorded `caption_access_blocked_http_429` for all seven rows; later committed docs record rows `21..22` as `success_git_safe_summary_possible`; rows `23..27` retain blocked accounting absent a later authorized probe; row `62` remains blocked/quarantined and outside scope; and this refresh defines source-touch accounting, strict gatekeeping, stop conditions, and next-task routing without performing source access or touching raw artifacts, Strategy, Doctrine, market-data, broker/live, backtest, optimization, or profitability boundaries.

## 12. Issue #251 status refresh after row-22 blocked decision

This section is the current docs-only status update for Issue `#251`. It uses
committed Markdown only and performs no YouTube, DownSub, caption, subtitle,
transcript-body, caption URL, browser, media, ASR, market-data, broker/live, or
generated-artifact access.

PR #250 supersedes the earlier rows `21..22` recovery-next state in this plan.
The current row-level recovery status is:

| playlist order | video ID | latest committed status after PR #250 | current handling |
| ---: | --- | --- | --- |
| 21 | `bG3-_KfpskE` | compact paraphrased summary recovered in PR #244 | complete for this rows `21..27` recovery status slice; do not source-touch again for row-22 handling |
| 22 | `-VNpaMQWGUE` | PR #248 consumed the one authorized row-22 recovery attempt, and PR #250 decided row `22` remains blocked after failed one-time recovery | keep blocked; no automatic retry, fallback route, re-fetch, summary reconstruction, or title-based summary |
| 23 | `69XsLQQwo_M` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |
| 24 | `8ityiaa4j8c` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |
| 25 | `8tzBkeMR92g` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |
| 26 | `piuUBEWYeug` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |
| 27 | `ex-3Ywii0Qs` | no later committed recovery probe supersedes the prior `caption_access_blocked_http_429` status | keep blocked; no summary; no retry without explicit bounded authorization |

Status marker:

`intermediate_batch_03_rows_21_27_status_updated_after_row_22_blocked_decision`

Reason: row `21` is compact-summary recovered; row `22` is not
compact-summary complete and remains blocked after the failed one-time recovery
path; rows `23..27` still retain blocked accounting absent a later authorized
probe; row `62` remains blocked/quarantined and outside this recovery scope.

This status update does not authorize source access. It also does not treat PR
#248 as a retry precedent.

## 13. Current exact next recommended task

`[codex] Decide Intermediate Batch 03 rows 23-27 residual blocker handling after rows 21-22 closure`

That task should use committed Markdown only, decide whether rows `23..27`
remain blocked or need a separate future PM authorization path, preserve row
`21` as complete, preserve row `22` as blocked after the failed one-time
recovery path, keep row `62` blocked/quarantined and out of scope, and avoid
source access, doctrine updates, Strategy changes, market-data/broker/live
work, optimization, and trading or profitability claims.
