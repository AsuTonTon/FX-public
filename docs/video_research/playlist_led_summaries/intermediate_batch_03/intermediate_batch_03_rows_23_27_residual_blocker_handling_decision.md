# Intermediate Batch 03 Rows 23-27 Residual Blocker Handling Decision

Task: `intermediate_batch_03_rows_23_27_residual_blocker_handling_decision`

Issue: #253

## 1. Objective

Decide how to handle Intermediate Batch 03 rows `23..27` after rows `21..22`
were closed into one recovered row and one blocked row.

This is a docs-only decision. It uses committed Markdown only and performs no
source access, retry, re-fetch, summary creation, summary rewriting, doctrine
update, Strategy change, generated-artifact creation, market-data access,
broker/live work, or trading/performance/profitability claim.

## 2. Required Reference Review

| Reference | Status carried forward |
| --- | --- |
| `intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md` | row `21` is complete for this recovery status slice; row `22` remains blocked after the failed one-time recovery path; rows `23..27` retain blocked accounting unless a later issue explicitly authorizes a bounded path; row `62` remains blocked/quarantined and out of scope |
| `intermediate_batch_03_row_22_failed_recovery_handling_decision.md` | PR #248 is not a retry precedent; row `22` remains blocked; rows `23..27` stay out of that row-22 decision unless separately authorized |
| `intermediate_batch_03_rows_21_22_compact_summaries.md` | row `21` has a compact paraphrased summary; row `22` has no compact summary; rows `23..27` and row `62` were not touched |
| `intermediate_batch_03_continuation_target_table.md` | rows `23..27` have frozen video IDs and prior `caption_access_blocked_http_429` status; no summary files exist for these rows |

## 3. Decision Result

Decision marker:

`rows_23_27_remain_blocked_pending_explicit_pm_bounded_authorization`

Selected handling:

- row `21` remains `compact_summary_recovered` and complete for this status
  slice;
- row `22` remains `blocked_after_failed_one_time_recovery` and must not be
  retried from this decision;
- rows `23..27` remain blocked/deferred under the prior
  `caption_access_blocked_http_429` accounting;
- automation must not source-touch rows `23..27` from this decision alone;
- any future rows `23..27` source touch requires a separate issue that
  explicitly authorizes the exact bounded route, target rows, retry budget,
  source-touch accounting, cooldown/preflight checks, stop conditions, and raw
  artifact exclusions;
- no title-only summary, memory reconstruction, fallback route, DownSub route,
  ASR route, browser source route, media download, comments/live-chat/community
  source, broader channel probe, or unrelated row substitution is authorized;
- row `62` remains blocked/quarantined and outside this rows `23..27`
  residual-blocker decision.

## 4. Row-Level Status

| Row or range | Source ID | Current handling |
| --- | --- | --- |
| `21` | `bG3-_KfpskE` | `compact_summary_recovered`; no action in this task |
| `22` | `-VNpaMQWGUE` | `blocked_after_failed_one_time_recovery`; no retry or reconstruction |
| `23` | `69XsLQQwo_M` | `blocked_deferred_pending_explicit_pm_bounded_authorization` |
| `24` | `8ityiaa4j8c` | `blocked_deferred_pending_explicit_pm_bounded_authorization` |
| `25` | `8tzBkeMR92g` | `blocked_deferred_pending_explicit_pm_bounded_authorization` |
| `26` | `piuUBEWYeug` | `blocked_deferred_pending_explicit_pm_bounded_authorization` |
| `27` | `ex-3Ywii0Qs` | `blocked_deferred_pending_explicit_pm_bounded_authorization` |
| `62` | `kljZef5IXLc` | blocked/quarantined; outside this scope |

## 5. Future Authorization Boundary

Rows `23..27` should not be treated as ready for automatic retry. They may move
only through a future controlling issue that is explicit enough for automation
to audit before any source touch.

Minimum requirements for that future issue:

- active issue check immediately before any source-touch;
- duplicate PR, deterministic branch, same-title PR, same-issue PR, and recent
  merged/closed PR checks before source-touch and before PR creation;
- target rows exactly `23..27` or a narrower source-order subset named by the
  issue;
- route explicitly named by the issue;
- no fallback route unless the issue separately names it;
- source-touch count recorded per row;
- stop on HTTP 429, empty body, unavailable body, ambiguous access, route drift,
  raw-artifact pressure, or Strategy/market-data/broker/live/profitability
  drift;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, request
  URL, raw response body, CSV, JSON, `data/`, `results`, downloaded media,
  credential, token, cookie, session, or secret committed.

If the future issue does not satisfy these requirements, automation should keep
rows `23..27` blocked and report the blocker rather than improvising a probe.

## 6. Guardrail Statement

This document commits no raw transcript text, subtitle full text, raw
TXT/SRT/VTT, caption URL, request URL, raw source response, CSV, JSON,
`data/`, `results`, downloaded media, credential, token, cookie, session, IP
address, or secret.

It makes no Strategy A/B/B2/C behavior, code, parameter, config, test, runner,
backtest, market-data handling, broker/live, doctrine-map, or Strategy C
change. It performs no parameter optimization and makes no trading-readiness,
win-rate, money-making, trading-recommendation, performance, or profitability
claim.

## 7. Exact Next Recommended Task

No automatic source-touch task is recommended from this decision alone.

If the PM wants to attempt recovery, the next issue should be:

`[codex] Authorize Intermediate Batch 03 rows 23-27 bounded source-order recovery probe`

That issue must explicitly authorize the bounded route and source-touch budget,
preserve rows `21` and `22` as already decided, keep row `62`
blocked/quarantined and out of scope, and require immediate stop on any
repeated blocker or guardrail drift.
