# Intermediate Batch 03 Row 22 Status-Lost Recovery Decision

Task: `intermediate_batch_03_row_22_status_lost_recovery_decision`

Issue: `#245 [codex] Decide row 22 compact-summary recovery after status-lost blocker`

## 1. Objective

Decide the next safe handling for Intermediate Batch 03 row `22` / `-VNpaMQWGUE` after PR #244 recorded `status_lost_unrecoverable_after_runner_output_overflow`.

This decision is docs-only. It uses committed Markdown only and performs no source access, caption/subtitle/transcript-body access, retry, re-fetch, summary creation, summary rewriting, doctrine update, Strategy change, generated-artifact creation, market-data work, broker/live work, or trading/performance analysis.

## 2. Evidence Reviewed

Committed Markdown reviewed:

- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_22_compact_summaries.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_22_compact_summary_audit.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_22_tiny_recovery_probe.md`

Live GitHub state was used only for active issue, duplicate PR, branch, and PR creation checks. No source site or transcript/caption body was accessed.

## 3. Current Row Status

| Row | Public video ID | Current status | Evidence | Decision handling |
| ---: | --- | --- | --- | --- |
| `21` | `bG3-_KfpskE` | `compact_summary_recovered` | PR #244 compact-summary file and audit | Treat row `21` as recovered for this Intermediate Batch 03 slice. Do not source-touch again. |
| `22` | `-VNpaMQWGUE` | `status_lost_unrecoverable_after_runner_output_overflow` | PR #244 compact-summary file and audit | Not compact-summary complete. Eligible only for a separate, explicit, row-22-only one-time recovery authorization. |
| `23..27` | committed target-table IDs | `caption_access_blocked_http_429` retained | Issue #241 recovery plan | Keep blocked and out of this row-22 decision. Do not source-touch. |
| `62` | `kljZef5IXLc` | blocked/quarantined outside rows `21..27` | Issue #241 recovery plan and PR #244 boundary notes | Keep blocked/quarantined and out of scope. Do not source-touch. |

## 4. Options Considered

### Option A: Keep row 22 blocked with no follow-up

Decision: `rejected_as_next_handling`

Reason:

- the earlier tiny recovery probe recorded `success_git_safe_summary_possible` for row `22`;
- PR #244 did not assert a successful row `22` source-touch count or usable summary context;
- the blocker is an automation output/status-retention failure, not committed evidence that row `22` content is unavailable;
- permanent blocking would leave the row unresolved despite a committed signal that a bounded recovery path may be possible.

### Option B: Create a separate row-22-only recovery authorization issue

Decision: `selected`

Reason:

- Issue #245 itself forbids source access, retry, re-fetch, and summary creation;
- Issue #243's one-attempt/no-retry boundary must remain intact and must not be silently extended in a decision PR;
- a new source touch, if attempted, needs a fresh explicit controlling issue, active issue check, duplicate check, deterministic branch check, and no-network runtime preflight;
- row `22` should be isolated from rows `23..27` and row `62` so the future task cannot widen into a broader probe;
- a one-time row-22-only task can require exact source-touch accounting, retry reason, and stop conditions without creating a general retry precedent.

### Option C: Defer row 22 without selecting a next issue

Decision: `rejected_for_traceability`

Reason:

- the committed chain now has a single unresolved row in this two-row slice;
- leaving no exact next issue title would make later automation selection ambiguous;
- a deferred state would not clearly distinguish row `22` from still-blocked rows `23..27` or quarantined row `62`.

## 5. Decision Result

Decision marker:

`row_22_status_lost_requires_separate_one_time_recovery_authorization`

Selected handling:

- row `21` is compact-summary recovered and should not be touched again;
- row `22` is not compact-summary complete;
- row `22` should receive a separate explicit recovery authorization issue, if PM wants completion of this source-order slot;
- the future authorization must be row `22` only and one attempt only;
- rows `23..27` remain blocked and out of this decision unless separately authorized;
- row `62` remains blocked/quarantined and out of scope;
- this decision does not authorize source access by itself.

## 6. Future Row-22 Recovery Requirements

If the selected next issue is opened, it should require:

- active issue check immediately before any source touch;
- duplicate PR and deterministic branch checks before any source touch and again before PR creation;
- no-network runtime preflight before any source identifier is passed;
- authorized route only: `bundled_python_youtube_transcript_api_1_2_4`;
- target row only: row `22` / `-VNpaMQWGUE`;
- exactly one source-touch attempt;
- no fallback route;
- no retry if the attempt fails, returns empty/unavailable/ambiguous output, hits HTTP 429, requires bypass-like handling, or loses status again;
- no rows `23..27`, no row `62`, and no unrelated source-order rows;
- resulting PR must record retry reason, source-touch accounting, row-level outcome, raw-artifact exclusion, and whether compact summary context was retained;
- this recovery must not become a general retry precedent.

## 7. Guardrail Statement

Docs-only decision. No source access was run. No caption, subtitle, transcript-body, caption URL, request URL, raw response body, browser source access, DownSub, media download, ASR, comment, live chat, community post, unrelated channel surface, generated data artifact, market-data API, broker API, or live system was accessed.

No raw transcript text, subtitle full text, raw TXT/SRT/VTT, caption URL, request URL, raw response body, CSV, JSON, `data/`, `results`, downloaded media, credential, token, cookie, session, IP address, or secret was added.

No Strategy A/B/B2/C behavior, code, parameters, configs, tests, runners, backtests, market-data handling, broker/live behavior, doctrine conclusion, or trading conclusion was changed. No Strategy C was created. No parameter optimization was performed. No profitability, trading-readiness, win-rate, money-making, or trading-recommendation claim was made. The YouTube corpus line remains separate from Strategy A/B verification.

## 8. Exact Next Recommended Task

Recommended next issue title:

`[codex] Recover Intermediate Batch 03 row 22 compact summary after status-lost blocker`

Recommended scope:

- explicitly authorize one row-22-only source-touch attempt;
- use only `bundled_python_youtube_transcript_api_1_2_4`;
- repeat active issue, duplicate PR, deterministic branch, and no-network runtime preflight checks before source touch;
- create a compact paraphrased summary only if usable Git-safe summary context is retained;
- if row `22` fails again or status is lost again, record a blocker and do not retry;
- keep rows `23..27` blocked and untouched;
- keep row `62` blocked/quarantined and untouched;
- commit no raw artifacts, URLs, generated data artifacts, doctrine updates, Strategy changes, market-data or broker/live work, or trading/performance/profitability claims.
