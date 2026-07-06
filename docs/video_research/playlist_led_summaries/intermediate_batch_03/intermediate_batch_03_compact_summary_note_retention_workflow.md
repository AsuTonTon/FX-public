# Intermediate Batch 03 Compact-Summary Note Retention Workflow

Task: `intermediate_batch_03_compact_summary_note_retention_workflow`

Issue: #261

## 1. Objective

Define the minimum note-retention workflow required before any future
compact-summary recovery task can mark a row complete.

This is a docs-only workflow design note. It uses committed Markdown only and
performs no source access, retry, re-fetch, summary creation, summary
rewriting, doctrine update, Strategy change, generated-artifact creation,
market-data access, broker/live work, or trading/performance/profitability
claim.

## 2. Problem Pattern

Recent recovery work exposed the same failure mode more than once:

- a source-touch attempt returned a success label or count;
- the run did not retain the Git-safe notes needed to write a compact
  paraphrased summary;
- later review could prove that access happened, but could not prove enough
  safe summary material to complete the row;
- the correct committed outcome therefore had to remain blocked or deferred.

The repeated cases are:

| Lineage | Retained signal | Missing signal | Correct handling |
| --- | --- | --- | --- |
| row `22` one-time recovery | source access returned `success_git_safe_summary_possible` and counts | bounded, reviewable compact-summary context was not retained after the script error | row remains blocked; no second automatic retry |
| rows `23`, `24`, and `27` bounded probe | success labels and Git-safe counts were retained | usable compact-summary context was not retained in model-readable form | rows remain blocked/deferred |
| rows `25` and `26` bounded probe | source-order execution implies the rows were touched once | detailed row-level status was not retained | rows remain blocked/deferred |
| row `62` prior lineage | access reached a success-like state | usable compact-summary context was not retained after authorized touch/refetch | row remains blocked/quarantined |

These are workflow-retention failures, not evidence that the source material is
usable for Git-safe summaries.

## 3. Why Notes Are Being Lost

The main failure is treating access status as a substitute for retained
summary notes.

The unsafe pattern is:

1. run a source-access command across more than one row;
2. rely on terminal output or model context to remain available;
3. retain only coarse success labels, counts, or partial status lines;
4. move to the next row before the current row has a durable Git-safe note;
5. later attempt to reconstruct the compact summary from memory, title,
   incomplete output, or another source request.

That pattern is not acceptable. A success label can prove that the approved
runtime returned something, but it cannot prove that the repository retained
enough safe, reviewable material to summarize the row.

## 4. Minimum Safe Note Format

A row is eligible for compact-summary writing only after a retained Git-safe
note exists with all required fields below.

| Required field | Minimum content | Purpose |
| --- | --- | --- |
| row identity | source-order row and public video ID only | anchors the note without source URLs |
| controlling authorization | issue number, allowed route, and one-touch or retry budget | proves the note belongs to the authorized scope |
| source-touch accounting | touch count, started/completed time window, and final access-state label | prevents silent extra attempts |
| retained evidence class | segment/count metadata when safely available, plus whether bounded summary context was retained | separates status from usable summary material |
| Git-safe concept notes | compact paraphrased bullets written without raw transcript text | supplies the actual material needed for a summary |
| uncertainty notes | visual-discretion, missing-context, or confidence caveats | prevents overclaiming from weak notes |
| forbidden interpretation | no doctrine, Strategy, trading, performance, or profitability inference | keeps corpus work separate from Strategy A/B |
| completion decision | `summary_ready`, `blocked_no_retained_note`, `blocked_status_lost`, or `completed_skip` | makes the next step auditable |

If any required field is missing, the row is not compact-summary complete.

## 5. Smaller Per-Row Workflow

Future recovery tasks should use a row-gated workflow rather than a broad
multi-row output stream.

For each target row:

1. Confirm the controlling issue is still open and explicitly authorizes the
   exact row, route, retry budget, and stop conditions.
2. Confirm duplicate PR, duplicate branch, and recent merged/closed duplicate
   checks before any source touch.
3. Run only the authorized no-network runtime preflight before passing a source
   identifier.
4. Touch at most one active row.
5. Immediately convert the usable result into the minimum safe note format in
   Markdown or in the PR draft text.
6. Verify that the note is retained before touching the next row.
7. If the note is not retained, stop the recovery task before the next row.
8. Commit only Git-safe Markdown; do not commit raw source text, source URLs,
   request URLs, raw output, or generated data dumps.

This workflow deliberately values retained, reviewable notes over throughput.
It is better to finish one row safely than to touch several rows and lose the
summary material.

## 6. Completion Gate

A row is not complete merely because access returned a success status.

The completion rule is:

`compact_summary_complete = retained_safe_note + committed_compact_summary + audit_or_status_reference`

Therefore:

- success labels without retained concept notes are blockers;
- counts without retained concept notes are blockers;
- source-order evidence without row-level retained status is a blocker;
- model memory, video title memory, incomplete terminal output, or another
  source request cannot substitute for the retained safe note;
- no later PR should mark a row complete unless the retained note can be cited.

## 7. Stop Rule

Future recovery must stop immediately when the row note is not retained.

Stop conditions include:

- the source-access command succeeds but emits only status/count metadata;
- the row-level status line is lost, truncated, or ambiguous;
- the bounded context block is not available to the model after the command;
- a script error occurs before the note is written;
- the PR cannot state the row's note-retention status without relying on
  memory or another source request.

After a stop condition, automation should record a blocker and wait for a new
PM authorization issue. It should not retry, switch routes, widen scope,
summarize from memory, or continue to the next row.

## 8. Future PR Reporting Requirements

Any future compact-summary recovery PR should include a note-retention section
with the following table:

| Row | Source ID | Touch count | Access state | Safe note retained | Compact-summary status | Stop or continue |
| --- | --- | ---: | --- | --- | --- | --- |
| target row | public ID only | integer count | retained access label | `yes` / `no` | `summary_ready` / blocker label | decision |

The PR body should also state:

- retry reason and authorization source, if any;
- source-touch accounting before and after the change;
- whether each row retained the minimum safe note;
- whether any row stopped the workflow;
- changed files;
- guardrail statement;
- validation performed;
- next recommended task.

The PR must not present a retained success label as retained summary material.

## 9. Future Authorization Boundary

This note does not authorize source access, retry, re-fetch, fallback route,
manual reconstruction, summary creation, doctrine updates, Strategy changes,
market-data work, broker/live work, optimization, or trading conclusions.

Any future recovery issue must explicitly name:

- exact target rows;
- exact allowed route or manual-input source;
- retry budget;
- duplicate checks;
- source-touch accounting requirements;
- note-retention stop conditions;
- raw artifact exclusions;
- PR reporting requirements.

If those conditions are absent, automation should keep the affected rows
blocked and report the missing authorization instead of improvising.

## 10. Guardrail Statement

This document commits no raw transcript text, subtitle full text, raw
TXT/SRT/VTT, caption URL, request URL, raw source response, CSV, JSON,
`data/`, `results`, downloaded media, credential, token, cookie, session, IP
address, or secret.

It makes no Strategy A/B/B2/C behavior, code, parameter, config, test, runner,
backtest, market-data handling, broker/live, doctrine-map, or Strategy C
change. It performs no parameter optimization and makes no trading-readiness,
win-rate, money-making, trading-recommendation, performance, or profitability
claim.

## 11. Next Recommended Task

`[codex] Apply compact-summary note-retention gate to the next explicit recovery authorization`

That task should not perform source access by default. It should wait for a PM
issue that names the exact rows and allowed route, then require the
note-retention gate above before any row can be marked compact-summary
complete.
