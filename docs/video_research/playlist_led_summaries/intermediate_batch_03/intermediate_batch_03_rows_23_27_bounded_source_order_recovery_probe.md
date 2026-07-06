# Intermediate Batch 03 Rows 23-27 Bounded Source-Order Recovery Probe

Task: `intermediate_batch_03_rows_23_27_bounded_source_order_recovery_probe`

Issue: #255

## 1. Objective

Run the explicitly authorized bounded source-order recovery probe for
Intermediate Batch 03 rows `23..27`.

This task uses only the route named by Issue #255:

`bundled_python_youtube_transcript_api_1_2_4`

It does not use DownSub, ASR, browser source access, direct caption endpoint
scraping, media download, comments, live chat, community posts, unrelated
videos, broader channel access, proxying, VPN, cookie/session swapping,
credential use, CAPTCHA workaround, downloader workaround, or fallback route.

## 2. Required Reference Review

Committed Markdown was reviewed before source touch:

| Reference | Relevant status carried forward |
| --- | --- |
| `intermediate_batch_03_rows_23_27_residual_blocker_handling_decision.md` | rows `23..27` required a separate explicit bounded authorization before any source touch |
| `intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md` | rows `23..27` retained prior blocker accounting; row `21` complete; row `22` blocked; row `62` blocked/quarantined and outside scope |
| `intermediate_batch_03_continuation_target_table.md` | frozen row IDs and prior `caption_access_blocked_http_429` status for rows `23..27` |

## 3. Source Authorization and Preflight

| Check | Result |
| --- | --- |
| Active issue check | Issue #255 was open immediately before source touch |
| Duplicate PR check | no open PR body, title, or head branch matched Issue #255 immediately before source touch |
| Recent duplicate check | no recent merged/closed PR closed Issue #255 or used a `codex/issue-255-*` head |
| Deterministic branch check | local branch `codex/issue-255-authorize-intermediate-batch-03-rows-23-27-bounded-source-order-recovery-probe` was active; no remote `codex/issue-255-*` branch existed before source touch |
| Authorized route | `bundled_python_youtube_transcript_api_1_2_4` |
| No-network runtime preflight | bundled Python `3.12.13`; `youtube_transcript_api` import ok; `youtube-transcript-api` distribution `1.2.4`; no dependency installation; no source identifier passed |

## 4. Source-Touch Accounting

Probe window:

`2026-07-06 09:28:27 JST` to `2026-07-06 09:28:31 JST`

| Row | Video ID | Source-touch count | Started | Completed | Result | Segment count | Character count | Summary status |
| --- | --- | ---: | --- | --- | --- | ---: | ---: | --- |
| `23` | `69XsLQQwo_M` | `1` | `2026-07-06 09:28:27 JST` | `2026-07-06 09:28:28 JST` | `success_git_safe_summary_possible` | `213` | `3505` | blocked: model-readable compact summary context was not retained in usable form |
| `24` | `8ityiaa4j8c` | `1` | `2026-07-06 09:28:28 JST` | `2026-07-06 09:28:28 JST` | `success_git_safe_summary_possible` | `269` | `4516` | blocked: model-readable compact summary context was not retained in usable form |
| `25` | `8tzBkeMR92g` | `1` | within probe window after row `24` | before row `27` started | `status_lost_after_runner_output_truncation` | not retained | not retained | blocked: auditable row-level status was not retained |
| `26` | `piuUBEWYeug` | `1` | within probe window after row `24` | before row `27` started | `status_lost_after_runner_output_truncation` | not retained | not retained | blocked: auditable row-level status was not retained |
| `27` | `ex-3Ywii0Qs` | `1` | `2026-07-06 09:28:30 JST` | `2026-07-06 09:28:31 JST` | `success_git_safe_summary_possible` | `181` | `2982` | blocked: model-readable compact summary context was not retained in usable form |

Known source-touch count for Issue #255 is `5`.

Rows `25` and `26` were source-touched because the source-order runner reached
row `27`, but their detailed Git-safe status lines were lost when the runner
output exceeded the retained command-output window. No retry or fallback source
access was performed after this status-retention problem was observed.

## 5. Probe Outcome

Decision marker:

`intermediate_batch_03_rows_23_27_probe_blocked_by_status_retention_and_unusable_context`

The approved runtime did not reproduce the prior HTTP 429 blocker for the
retained rows `23`, `24`, and `27`. However, the run still cannot create compact
paraphrased summaries safely:

- row `23`, row `24`, and row `27` retained Git-safe success counts, but the
  emitted internal context was not retained in model-readable usable form;
- row `25` and row `26` lost their detailed row-level status after the source
  touches;
- Issue #255 authorized one attempt per row and no retry or fallback route;
- therefore the correct repository state is a blocker record rather than
  reconstructed summaries.

## 6. Compact Summaries

No compact paraphrased summaries are created.

Reason: usable, auditable summary context was not retained for the full
source-order probe, and rows `25..26` lost detailed row-level status. Creating
summaries from memory, titles, incomplete terminal output, or another source
request would exceed Issue #255.

## 7. Excluded Rows

| Row or range | Status in this task |
| --- | --- |
| `21` | not touched; remains compact-summary recovered |
| `22` | not touched; remains blocked after the failed one-time recovery path |
| `62` | not touched; remains blocked/quarantined and outside this recovery |
| any other row | not touched |

## 8. Guardrail Statement

This document commits no raw transcript text, subtitle full text, raw
TXT/SRT/VTT, caption URL, request URL, raw source response, CSV, JSON,
`data/`, `results`, downloaded media, credential, token, cookie, session, IP
address, or secret.

It makes no Strategy A/B/B2/C behavior, code, parameter, config, test, runner,
backtest, market-data handling, broker/live, doctrine-map, or Strategy C
change. It performs no parameter optimization and makes no trading-readiness,
win-rate, money-making, trading-recommendation, performance, or profitability
claim.

This is an Issue #255 bounded-probe blocker record and is not a general retry
precedent.

## 9. Next Recommended Task

`[codex] Decide rows 23-27 handling after bounded probe status-retention blocker`

The next task should be a human/PM decision. It should not authorize automatic
retry by default, should preserve rows `21`, `22`, and `62` as out of scope,
and should keep the YouTube channel-wide corpus line separate from Strategy
A/B verification.
