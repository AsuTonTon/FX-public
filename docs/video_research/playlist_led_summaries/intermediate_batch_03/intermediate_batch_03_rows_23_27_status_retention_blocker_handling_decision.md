# Intermediate Batch 03 Rows 23-27 Status-Retention Blocker Handling Decision

Task: `intermediate_batch_03_rows_23_27_status_retention_blocker_handling_decision`

Issue: #257

## 1. Objective

Decide how to handle Intermediate Batch 03 rows `23..27` after PR #256
recorded a bounded source-order probe blocker caused by status and context
retention failure.

This is a docs-only decision. It uses committed Markdown only and performs no
source access, retry, re-fetch, summary creation, summary rewriting, doctrine
update, Strategy change, generated-artifact creation, market-data access,
broker/live work, or trading/performance/profitability claim.

## 2. Required Reference Review

| Reference | Status carried forward |
| --- | --- |
| `intermediate_batch_03_rows_23_27_bounded_source_order_recovery_probe.md` | Issue #255 touched rows `23..27` once in source order; rows `23`, `24`, and `27` retained success labels/counts; rows `25` and `26` lost detailed status; no compact summaries were created |
| `intermediate_batch_03_rows_23_27_bounded_source_order_recovery_probe_audit.md` | audit passed the blocker record and confirmed no retry/fallback was performed or authorized |
| `intermediate_batch_03_rows_23_27_residual_blocker_handling_decision.md` | rows `23..27` previously required explicit PM bounded authorization before any source touch |
| `intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md` | row `21` is compact-summary recovered; row `22` remains blocked after the failed one-time recovery path; row `62` remains blocked/quarantined and outside scope |

## 3. Decision Result

Decision marker:

`rows_23_27_remain_blocked_deferred_after_status_retention_probe`

Selected handling:

- row `21` remains `compact_summary_recovered` and complete for this recovery
  status slice;
- row `22` remains `blocked_after_failed_one_time_recovery` and must not be
  retried from this decision;
- rows `23`, `24`, and `27` retained `success_git_safe_summary_possible`
  labels and Git-safe counts in PR #256, but no usable compact-summary context
  was retained in a model-readable auditable form;
- rows `25` and `26` lost detailed status after the one authorized source
  touch;
- no compact paraphrased summaries were created for rows `23..27`;
- rows `23..27` therefore remain blocked/deferred for automation purposes;
- PR #256 consumed the one authorized rows `23..27` source-order probe and is
  not a general retry precedent;
- any future source-touch, retry, fallback route, manual reconstruction path,
  or summary recovery path for rows `23..27` requires a separate explicit PM
  authorization issue;
- row `62` remains blocked/quarantined and outside this rows `23..27`
  decision.

## 4. Row-Level Status

| Row or range | Source ID | Latest committed status | Current handling |
| --- | --- | --- | --- |
| `21` | `bG3-_KfpskE` | compact paraphrased summary recovered in PR #244 | complete; no action in this task |
| `22` | `-VNpaMQWGUE` | PR #248 consumed the one authorized row-22 recovery attempt; PR #250 decided row `22` remains blocked | blocked; no retry or reconstruction |
| `23` | `69XsLQQwo_M` | PR #256 retained `success_git_safe_summary_possible`, segment count `213`, character count `3505`, but no usable compact-summary context | blocked/deferred; no summary |
| `24` | `8ityiaa4j8c` | PR #256 retained `success_git_safe_summary_possible`, segment count `269`, character count `4516`, but no usable compact-summary context | blocked/deferred; no summary |
| `25` | `8tzBkeMR92g` | PR #256 source-touched the row once, but detailed status was not retained | blocked/deferred; no summary |
| `26` | `piuUBEWYeug` | PR #256 source-touched the row once, but detailed status was not retained | blocked/deferred; no summary |
| `27` | `ex-3Ywii0Qs` | PR #256 retained `success_git_safe_summary_possible`, segment count `181`, character count `2982`, but no usable compact-summary context | blocked/deferred; no summary |
| `62` | `kljZef5IXLc` | blocked/quarantined from a separate lineage | outside this scope |

## 5. Future Authorization Boundary

Automation must not treat the retained success labels for rows `23`, `24`, and
`27` as enough to create summaries. They are evidence that the approved runtime
returned Git-safe counts, not retained summary material.

Automation must also not treat rows `25` and `26` as available or complete.
Their detailed status was lost after source touch, and Issue #255 did not
authorize a second attempt.

Any future rows `23..27` path must be a new PM authorization issue that names
the exact target rows, the exact allowed route or manual-input source, the retry
budget, duplicate checks, source-touch accounting, stop conditions, and raw
artifact exclusions. If those conditions are absent or ambiguous, automation
should keep rows `23..27` blocked and report the blocker rather than
improvising.

No future issue should cite PR #256 as general permission to retry source
access. PR #256 is a blocker record only.

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

`[codex] Update Intermediate Batch 03 rows 21-27 recovery status after rows 23-27 blocked decision`

That task should use committed Markdown only, update the current rows `21..27`
recovery status to reflect that rows `23..27` remain blocked/deferred after
the PR #256 status-retention blocker, preserve row `21` as recovered, preserve
row `22` as blocked, keep row `62` blocked/quarantined and out of scope, and
avoid source access, summary creation, doctrine updates, Strategy changes,
market-data/broker/live work, optimization, and trading or profitability
claims.
