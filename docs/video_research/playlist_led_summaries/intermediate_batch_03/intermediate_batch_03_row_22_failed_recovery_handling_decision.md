# Intermediate Batch 03 Row 22 Failed Recovery Handling Decision

Task: `intermediate_batch_03_row_22_failed_recovery_handling_decision`

Issue: #249

## 1. Objective

Decide how to handle Intermediate Batch 03 row `22` after PR #248 recorded
that the one authorized row-22 compact-summary recovery attempt did not retain
usable summary context.

This is a docs-only decision. It uses committed Markdown only and performs no
source access, retry, re-fetch, summary creation, or summary rewriting.

## 2. Required Reference Review

| Reference | Status carried forward |
| --- | --- |
| `intermediate_batch_03_row_22_compact_summary_recovery.md` | row `22` / `-VNpaMQWGUE` was touched exactly once under Issue #247; the fetch returned `success_git_safe_summary_possible` with `segment_count=275`, but usable bounded summary context was not retained |
| `intermediate_batch_03_row_22_compact_summary_recovery_audit.md` | the PR #248 blocker record passed audit and does not authorize another row-22 source touch |
| `intermediate_batch_03_row_22_status_lost_recovery_decision.md` | row `21` is recovered; row `22` needed exactly one separate authorization; if row `22` failed again or status was lost again, the next step was blocker reporting rather than retry |
| `intermediate_batch_03_rows_21_22_compact_summaries.md` | row `21` has a compact paraphrased summary; row `22` had no compact summary after PR #244 and was not to be reconstructed from memory, title text, or another source request |

## 3. Decision Result

Decision marker:

`row_22_remains_blocked_after_failed_one_time_recovery`

Selected handling:

- row `21` remains compact-summary recovered and must not be source-touched for
  this row-22 decision;
- row `22` is not compact-summary complete;
- PR #248 consumed the one authorized row-22 recovery attempt and produced a
  blocker record;
- row `22` remains blocked for automation purposes;
- no automatic retry, fallback route, source re-fetch, summary reconstruction,
  or title-based summary is authorized;
- any future row-22 source touch would require a new, explicit PM authorization
  issue and must not be inferred from PR #248;
- rows `23..27` remain out of scope and retain their existing blocked handling
  unless a separate issue explicitly authorizes a bounded source-order probe;
- row `62` remains blocked/quarantined and out of scope.

## 4. Row-Level Status

| Row or range | Current decision |
| --- | --- |
| `21` | `compact_summary_recovered`; no action in this task |
| `22` | `blocked_after_failed_one_time_recovery`; no compact summary is created |
| `23..27` | out of scope; no source access, retry, or summary work |
| `62` | out of scope; remains blocked/quarantined |

## 5. Future Handling Boundary

This decision does not permanently forbid a human from opening a future row-22
PM authorization issue, but future automation must treat row `22` as blocked
unless such an issue exists and narrowly authorizes the exact route, row, retry
budget, source-touch accounting, stop conditions, and raw-artifact exclusions.

PR #248 is not a retry precedent. It is a blocker record for one failed
authorized recovery path.

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

`[codex] Update Intermediate Batch 03 rows 21-27 recovery status after row 22 blocked decision`

That task should use committed Markdown only, update the row `21..27` recovery
status to reflect row `21` recovered and row `22` blocked after the failed
one-time recovery path, keep rows `23..27` blocked unless separately
authorized, keep row `62` blocked/quarantined, and avoid source access,
doctrine updates, Strategy changes, market-data/broker/live work,
optimization, and trading or profitability claims.
