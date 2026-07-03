# YouTube Corpus Access Attempt Ledger Template

Task: `youtube_corpus_access_attempt_ledger_template`

## 1. Objective

This template defines a Git-safe Markdown structure for future YouTube channel-wide corpus access-attempt ledgers.

It is planning-only. It does not authorize source access, caption probes, browser automation, downloads, ASR, transcript-body access, or any change to Strategy A/B/B2/C behavior.

## 2. Scope

Use this template only when a future controlling issue explicitly authorizes a corpus access-attempt ledger.

Allowed ledger purpose:

- record aggregate-friendly access-attempt metadata;
- preserve cooldown, cadence, and fallback routing decisions;
- keep blocked, metadata-only, and successful Git-safe summary states distinct;
- keep the channel-wide corpus line separate from the Strategy A/B verification line.

Forbidden ledger purpose:

- reconstruct source text;
- store raw subtitles, transcript bodies, caption URLs, request URLs, or downloaded media;
- promote metadata-only or blocked-status rows into doctrine claims;
- change Strategy A/B/B2/C rules, code, parameters, tests, runners, backtests, or conclusions;
- support profitability, trading-readiness, or trading-recommendation claims.

## 3. Ledger Header

```text
ledger_id:
created_date_jst:
controlling_issue:
run_owner:
source_authorization_scope:
cadence_rule:
daily_attempt_cap:
cooldown_state:
target_batch:
fallback_mode:
```

## 4. Attempt Table Template

| attempt_date_jst | run_type | cadence | target_batch | public_video_id | body_access_attempted | outcome_label | cooldown_state | fallback_task | short_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `YYYY-MM-DD HH:MM` | `scheduled_loop` / `manual_probe_window` / `fallback_only` | `15_minutes` / `30_minutes` / `fallback_only` | approved batch or slice | public ID only | `yes` / `no` | taxonomy value | `none` / `active` / `started` / `expired` | safe fallback task or `none` | compact Git-safe note only |

## 5. Outcome Label Reference

Use one of the outcome labels defined by `youtube_corpus_access_learning_loop_policy`:

| outcome_label | use |
| --- | --- |
| `success_git_safe_summary_possible` | Explicitly authorized body access produced enough evidence for a compact paraphrased summary without raw text commits. |
| `metadata_only_available` | Only approved metadata is available; no content evidence is available. |
| `caption_body_not_attempted` | Caption-body access was intentionally not attempted. |
| `caption_body_empty` | An explicitly authorized body attempt returned no usable body content. |
| `caption_body_unavailable` | Caption/body access was unavailable under the approved method. |
| `rate_limited_429` | A 429 or equivalent rate-limit response occurred. |
| `ip_limited` | The response indicates IP-based access limiting. |
| `blocked_by_policy` | The requested action was not allowed by repository guardrails or the controlling issue. |
| `deferred_to_fallback` | Work moved to a safe docs-only fallback task without further source access. |

## 6. Field Rules

| field | rule |
| --- | --- |
| `attempt_date_jst` | Use a JST date or timestamp. |
| `run_type` | Use `scheduled_loop`, `manual_probe_window`, or `fallback_only`. |
| `cadence` | Use the active loop cadence, such as `15_minutes`, `30_minutes`, or `fallback_only`. |
| `target_batch` | Name only the approved batch or slice. |
| `public_video_id` | Record only the public video ID. Do not record caption URLs or request URLs. |
| `body_access_attempted` | Use `yes` only when the controlling issue explicitly authorized the attempt. |
| `outcome_label` | Use one taxonomy value from Section 5. |
| `cooldown_state` | Use a compact state such as `none`, `active`, `started`, or `expired`. |
| `fallback_task` | Name the safe docs-only fallback task selected for blocked or cooldown states. |
| `short_notes` | Keep notes short, claim-level, and Git-safe. |

## 7. Optional Aggregate Summary

```text
attempt_count:
body_attempt_count:
metadata_only_count:
success_git_safe_summary_possible_count:
blocked_or_cooldown_count:
fallback_only_count:
cooldown_triggered:
next_allowed_probe_after_jst:
recommended_next_mode:
```

## 8. Forbidden Content Checklist

The ledger must not include:

- raw transcripts;
- subtitle full text;
- raw TXT, SRT, or VTT content;
- caption URLs;
- exact request URLs;
- downloaded video or audio;
- ASR output;
- CSV or JSON dumps;
- `data/` or `results/` files;
- generated candidate, event, trade, metric, or result artifacts;
- cookies, sessions, IP addresses, credentials, tokens, or secrets.

## 9. Separation Guardrail

This template belongs to the YouTube channel-wide corpus line only.

Ledger rows may support corpus inventory, blocked-status tracking, cooldown decisions, metadata-only routing, future audit prioritization, and fallback task selection. They must not change Strategy A/B/B2/C behavior, parameter values, tests, runners, backtests, or conclusions unless a separate Strategy-line review explicitly authorizes integration.

## 10. Validation Checklist

Before committing a completed ledger document derived from this template:

- confirm the controlling issue explicitly authorized any source access that was attempted;
- confirm no forbidden content from Section 8 is present;
- confirm metadata-only and blocked-status rows are not treated as content evidence;
- run `git diff --check`;
- run `git status --short`;
- run an encoding sanity check;
- confirm no `data/`, `results/`, CSV, JSON, raw subtitle, transcript, credential, token, or secret file is staged.

## 11. Guardrail Confirmation

This template adds a planning-only documentation structure. It performs no source access, authorizes no source access, commits no raw or generated artifacts, changes no Strategy behavior, performs no parameter optimization, and makes no profitability, trading-readiness, or trading-recommendation claim.

## 12. Next Safe Task

Use this template only in a future issue that explicitly authorizes a specific ledger population scope, or keep it as a reference for fallback-only access-state planning.
