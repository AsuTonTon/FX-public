# Intermediate Batch 03 Row 22 Compact Summary Recovery

Task: `intermediate_batch_03_row_22_compact_summary_recovery`

Issue: #247

## 1. Objective

Recover a compact paraphrased summary for Intermediate Batch 03 row `22`
only, after PR #244 recorded the row-22 status-lost blocker and PR #246
selected a separate explicit one-time row-22 recovery authorization.

## 2. Required Reference Review

Committed Markdown was reviewed before source touch:

| Reference | Relevant status carried forward |
| --- | --- |
| `intermediate_batch_03_row_22_status_lost_recovery_decision.md` | selected one explicit row-22-only recovery authorization and required no fallback or retry |
| `intermediate_batch_03_rows_21_22_compact_summaries.md` | row `21` recovered; row `22` blocked by status loss; rows `23..27` and row `62` untouched |
| `intermediate_batch_03_rows_21_22_compact_summary_audit.md` | confirmed the row-22 blocker was intentionally conservative and did not authorize a second source touch |
| `intermediate_batch_03_rows_21_22_tiny_recovery_probe.md` | earlier tiny probe showed row `22` was potentially recoverable, but did not itself create a compact summary |

## 3. Source Authorization and Preflight

| Check | Result |
| --- | --- |
| Active issue check | Issue #247 was open immediately before source touch |
| Duplicate PR check | no open PR body, title, or head branch matched Issue #247 immediately before source touch |
| Deterministic branch check | local branch `codex/issue-247-recover-intermediate-batch-03-row-22-compact-summary-after-status-lost-blocker` was active; no remote `codex/issue-247-*` branch existed before source touch |
| Authorized route | `bundled_python_youtube_transcript_api_1_2_4` |
| No-network runtime preflight | bundled Python `3.12.13`; `youtube_transcript_api` import ok; `youtube-transcript-api` distribution `1.2.4`; no dependency installation; no source identifier passed |

## 4. Row-Level Source-Touch Accounting

| Row | Video ID | Source-touch count | Started | Completed | Result |
| --- | --- | ---: | --- | --- | --- |
| `22` | `-VNpaMQWGUE` | `1` | `2026-07-06 06:42:04 JST` | `2026-07-06 06:42:05 JST` | fetch returned `success_git_safe_summary_possible` with `segment_count=275`, but bounded summary context was not retained because the script failed before emitting the bounded context block |

No second source request, fallback route, browser access, DownSub access,
direct caption endpoint scraping, media download, ASR, comments, live chat,
community posts, proxy, VPN, cookie/session swap, credential use, CAPTCHA
workaround, downloader workaround, or parallel source access was performed.

## 5. Row 22 Outcome

Decision marker:

`intermediate_batch_03_row_22_recovery_blocked_context_not_retained_after_one_authorized_touch`

Row `22` is not compact-summary complete in this repository state.

The authorized source touch confirmed that the approved runtime could return
source segments for row `22`, but the run did not retain bounded, reviewable
summary context after the script error. Because Issue #247 allowed exactly one
row-22 source-touch attempt, and explicitly prohibited fallback or retry,
creating a compact summary from memory, the video title, or another source
request would exceed the authorization.

## 6. Compact Summary

No compact paraphrased summary is created.

Reason: usable Git-safe summary context was not retained after the one
authorized row-22 source-touch attempt.

## 7. Excluded Rows

| Row or range | Status in this task |
| --- | --- |
| `21` | not touched; remains compact-summary recovered from PR #244 |
| `23..27` | not touched; remain blocked/out of this recovery |
| `62` | not touched; remains blocked/quarantined/out of this recovery |

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

This is a one-off Issue #247 blocker record and is not a general retry
precedent.

## 9. Next Recommended Task

`[codex] Decide row 22 handling after failed one-time compact-summary recovery`

The next task should be a human/PM decision. It should not authorize another
automatic row-22 retry by default, should preserve rows `23..27` and row `62`
as untouched, and should keep the YouTube channel-wide corpus line separate
from Strategy A/B verification.
