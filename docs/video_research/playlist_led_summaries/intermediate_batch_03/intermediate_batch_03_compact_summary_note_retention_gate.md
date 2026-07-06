# Intermediate Batch 03 Compact-Summary Note-Retention Gate

Task: `intermediate_batch_03_compact_summary_note_retention_gate`

Issue: #263

## 1. Objective

Apply the compact-summary note-retention workflow from PR #262 as a required
completion gate for any future explicitly authorized row recovery task.

This is a docs-only gate note. It uses committed Markdown only and performs no
source access, retry, re-fetch, summary creation, summary rewriting, doctrine
update, Strategy change, generated-artifact creation, market-data access,
broker/live work, or trading/performance/profitability claim.

No source access is authorized by this task.

## 2. References Used

This gate note relies only on committed Markdown:

- `intermediate_batch_03_compact_summary_note_retention_workflow.md`
- `intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`
- `intermediate_batch_03_rows_23_27_status_retention_blocker_handling_decision.md`

Those references establish the current rows `21..27` status, the row `62`
separation boundary, the PR #256 status-retention blocker, and the PR #262
minimum safe-note workflow.

## 3. Gate Decision

Gate marker:

`compact_summary_recovery_requires_retained_safe_note_before_completion`

Decision:

- future recovery work may not mark a row compact-summary complete from a
  success label, count, source-order touch, terminal output memory, title
  metadata, or later reconstruction;
- a row can become compact-summary complete only when the PR can cite a
  retained Git-safe note and a committed compact summary for that exact row;
- if the retained note is missing, incomplete, truncated, or ambiguous, the
  row remains blocked or deferred and the workflow stops before the next row;
- this gate applies before any future explicit recovery authorization can
  convert source-access status into a completion decision;
- this gate does not itself authorize source access.

Completion formula:

`compact_summary_complete = retained_safe_note + committed_compact_summary + audit_or_status_reference`

## 4. Required `retained_safe_note` Fields

Any future row recovery PR must retain a Git-safe `retained_safe_note` before
the row can be marked summary-ready or complete.

| Field | Required content | Completion impact |
| --- | --- | --- |
| `row_identity` | source-order row and public video ID only | Required; no row can be completed without it |
| `controlling_authorization` | issue number, exact allowed route, target rows, retry budget, and stop conditions | Required; proves the source touch belongs to the approved scope |
| `source_touch_accounting` | touch count, started/completed time window, final access-state label, and whether any retry budget remains | Required; prevents silent extra source touches |
| `retained_evidence_class` | safely retained segment/count metadata when available, plus whether bounded concept context was retained | Required; separates status from usable summary material |
| `git_safe_concept_notes` | compact paraphrased bullets without raw transcript text, subtitle text, caption URLs, request URLs, or raw output | Required; this is the minimum material needed for summary drafting |
| `uncertainty_notes` | missing-context, visual-discretion, confidence, or ambiguity caveats | Required; prevents overclaiming from weak retained notes |
| `forbidden_interpretation` | explicit no doctrine, Strategy, trading, performance, or profitability inference | Required; preserves the corpus/Strategy boundary |
| `completion_decision` | one of `summary_ready`, `blocked_no_retained_note`, `blocked_status_lost`, or `completed_skip` | Required; determines whether the row may continue |

If any required field is absent, the row is not complete and must not be
summarized from memory, title text, or another source request.

## 5. One-Row-at-a-Time Workflow

Future recovery work must be row-gated.

For each target row:

1. Confirm the controlling issue is still open and explicitly names the row,
   allowed route, retry budget, stop conditions, and raw-artifact exclusions.
2. Confirm duplicate PR, deterministic branch, same-title PR, same issue
   reference, and recently merged/closed duplicate checks before any source
   touch.
3. Run only the no-network preflight allowed by the controlling issue before
   passing any source identifier.
4. Touch at most one active row.
5. Immediately retain the `retained_safe_note` in Git-safe Markdown or in the
   PR draft text.
6. Verify that every required note field is present.
7. Only then decide whether the row is `summary_ready`, blocked, or skipped.
8. Do not touch the next row until the current row has a retained note and an
   auditable decision.

This workflow favors retained evidence over throughput. A single completed row
with a durable safe note is preferred over multiple touched rows with lost
summary context.

## 6. Stop Rule

Future recovery must stop immediately when the safe note is not retained.

Stop conditions include:

- the source touch succeeds but only a status label or count is retained;
- the row-level status line is lost, truncated, or ambiguous;
- bounded concept context is not available after the source touch;
- a script error occurs before the note is written;
- the PR cannot report `source_touch_accounting` without relying on memory;
- any required `retained_safe_note` field is missing;
- the task would need another source request to reconstruct the note;
- the task would require raw transcript text, subtitle text, caption URL,
  request URL, raw output, TXT, SRT, VTT, CSV, JSON, `data/`, or `results`;
- the task begins to imply doctrine, Strategy, market-data, broker/live,
  optimization, trading, performance, or profitability conclusions.

After a stop condition, automation must record a blocker and wait for a new PM
authorization issue. It must not retry, switch route, widen scope, continue to
the next row, summarize from memory, or treat PR #256 or any other blocked
probe as a retry precedent.

## 7. Future PR Reporting Requirements

Any future recovery PR must include a note-retention section before claiming a
row is complete.

Required table:

| Row | Source ID | Touch count | Access state | `retained_safe_note` | Compact-summary status | Stop or continue |
| --- | --- | ---: | --- | --- | --- | --- |
| target row | public ID only | integer count | compact retained label | `yes` / `no` | `summary_ready` / blocker label | decision |

The PR body must also state:

- retry reason and controlling authorization, if any;
- source-touch accounting before and after the change;
- exact rows and public IDs in scope;
- whether each row retained every required safe-note field;
- whether any row stopped the workflow;
- changed files;
- guardrail statement;
- validation performed;
- exact next recommended task.

The PR must not present retained success labels, counts, or source-order
touches as retained concept notes.

## 8. Current Row Boundary Carried Forward

This gate does not change row status.

| Row or range | Current committed handling |
| --- | --- |
| `21` | compact-summary recovered; no action in this gate task |
| `22` | blocked after failed one-time recovery; no automatic retry |
| `23`, `24`, `27` | success labels and counts were retained in PR #256, but usable compact-summary context was not retained; remain blocked/deferred |
| `25`, `26` | touched once in PR #256, but detailed status was lost; remain blocked/deferred |
| `62` | blocked/quarantined outside this rows `21..27` lineage |

Rows `23..27` need a separate explicit PM authorization issue before any
future source touch, route substitution, manual reconstruction, or summary
recovery path. This gate is a prerequisite for that future path, not that
authorization.

## 9. Guardrail Statement

This document commits no raw transcript text, subtitle full text, raw
TXT/SRT/VTT, caption URL, request URL, raw source response, CSV, JSON,
`data/`, `results`, downloaded media, credential, token, cookie, session, IP
address, or secret.

It makes no Strategy A/B/B2/C behavior, code, parameter, config, test, runner,
backtest, market-data handling, broker/live, doctrine-map, or Strategy C
change. It performs no parameter optimization and makes no trading-readiness,
win-rate, money-making, trading-recommendation, performance, or profitability
claim.

## 10. Exact Next Recommended Task

`[codex] Authorize one-row compact-summary recovery with retained_safe_note gate`

That future task should be created only if the PM wants a new recovery attempt.
It must name the exact target row, allowed route, retry budget, duplicate
checks, source-touch accounting requirements, note-retention stop conditions,
and raw-artifact exclusions before any source touch. Without that explicit
authorization, automation should keep the affected row blocked/deferred and
no-op rather than retrying, reconstructing summaries, or widening source
access.
