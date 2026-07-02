# Strategy B Local Diagnostics Operations Runbook

## 1. Purpose

This runbook defines the operating boundary for future Strategy B local-only
diagnostics. It is an operations document, not a diagnostic result and not a
Strategy B design change.

Use it when a future issue explicitly authorizes local-only diagnostic work and
needs a repeatable checklist for keeping raw/generated artifacts outside Git.

This runbook is based on committed aggregate reports and protocol docs only:

- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_local_only_run_report_after_handoff.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_fallback_bucket_local_only_run_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_protocol_guardrails.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_sample_design_checklist.md`

No local data, diagnostic runner, Strategy B runner, local artifacts, market
data API, broker API, live system, YouTube source, caption source, transcript,
or external source was accessed for this runbook.

## 2. Fixed local-only directory layout

Future local-only diagnostics should use the fixed redacted root:

- `<USER_HOME>\FX-local-data\FX-public`

Expected local-only subareas, by artifact class only:

| Local-only area | Intended class | Git status |
| --- | --- | --- |
| `<USER_HOME>\FX-local-data\FX-public\ohlc\strategy_a_ohlc` | approved OHLC inputs for authorized local diagnostics | never commit |
| `<USER_HOME>\FX-local-data\FX-public\artifacts\strategy_b_readonly` | Strategy B read-only generated outputs | never commit |
| `<USER_HOME>\FX-local-data\FX-public\diagnostics\strategy_b_stop_anchor` | diagnostic packets, mappings, worksheets, and aggregate local summaries | never commit |

The exact user home path, raw rows, pair/time/price details, generated CSV/JSON
files, charts, worksheets, mappings, and images must remain local-only.

## 3. Local approval handling

Local-only diagnostics are allowed only when a future issue explicitly
authorizes them.

Operational rules:

- wait for the issue authorization before reading local data or running any
  diagnostic;
- use only the source classes named in the issue;
- do not bypass missing files, permissions, local approval prompts, rate limits,
  or unavailable local roots;
- stop if the local-only root is absent or contradicts the issue boundary;
- record only aggregate blocker status in Git-safe Markdown when work cannot
  proceed.

## 4. Allowed local reads/writes

Allowed only when a future issue explicitly authorizes a diagnostic run:

- read approved local OHLC input files under the fixed redacted root;
- run committed Strategy B read-only code against approved local inputs;
- write Strategy B read-only local outputs outside Git;
- create local-only Pass A packets, hidden mappings, worksheets, reveal tables,
  repeat-check material, and local aggregate summaries outside Git;
- inspect local-only artifacts only to produce aggregate counts, blocker notes,
  and guardrail-safe interpretation.

Not allowed in a docs-only planning or runbook issue:

- reading local OHLC files;
- running diagnostics;
- running the Strategy B runner;
- creating local artifacts;
- inspecting raw rows or generated row-level artifacts.

## 5. Git-allowed outputs

Allowed Git outputs:

- compact aggregate Markdown reports;
- protocol guardrails;
- sample-design checklists;
- operations runbooks;
- blocker notes;
- design-decision memos;
- validation summaries.

Git outputs must avoid:

- row-level market data;
- pair/time/price details;
- chart images or screenshots;
- hidden mappings;
- filled worksheet rows;
- generated CSV/JSON content;
- outcome/profitability claims;
- captions, transcript bodies, subtitle full text, caption URLs, or media.

## 6. Forbidden outputs

Never stage or commit:

- `data/`;
- `results/`;
- raw market data;
- normalized market CSVs;
- candidate, event, trade, TP-candidate, result, worksheet, mapping, packet, or
  local diagnostic CSV/JSON files;
- chart packets, chart images, screenshots, or contact sheets;
- raw transcripts;
- subtitle full text;
- raw TXT/SRT/VTT caption files;
- caption URLs;
- downloaded video or audio;
- credentials, tokens, or secrets.

## 7. Standard future issue notes

Future local-only diagnostic issues should state:

- exact diagnostic question;
- exact local-only root in redacted form;
- allowed local artifact classes;
- source docs/code to use;
- fixed sample buckets and shortfall rules;
- Pass A packet contents;
- hidden fields;
- repeat-check design;
- second-review triggers;
- Pass B reveal fields;
- Git-safe aggregate output format;
- hard-stop conditions;
- confirmation that no Strategy behavior change is authorized by the diagnostic
  run itself.

The issue should also state whether human decision is required. If human
decision is required, automation should stop without changing files.

## 8. PR merge-gate checklist

Before opening a PR for local-only diagnostic work, verify:

- the PR body includes `Closes #<issue_number>`;
- objective, scope, changed files, source-access statement, guardrail statement,
  validation performed, blockers, and next recommended task are present;
- only intended Markdown files are changed;
- no forbidden raw/generated artifacts are staged;
- no Strategy A/B/B2/C behavior, code, parameter, config, test, runner, or
  backtest behavior changed;
- no market-data API, broker API, order-placement, auto-trading, or live-trading
  behavior was added;
- no Strategy B2 or Strategy C was created;
- no parameter optimization was performed;
- no profitability, live-readiness, money-making, or trading-recommendation
  claim was made;
- Strategy A/B verification work remains separate from YouTube channel-wide
  corpus work.

## 9. Hard-stop conditions

Stop the work without creating Git changes when:

- the issue does not explicitly authorize the local read/run being attempted;
- the issue asks for Strategy behavior changes, parameter changes, optimization,
  broker/live behavior, or Strategy C work;
- local roots, local artifact classes, or source boundaries are ambiguous;
- Pass A / Pass B separation cannot be preserved;
- raw/generated artifacts would need to be committed to support the claim;
- row-level pair/time/price detail would be required in the PR;
- a reviewer can infer hidden fields from packet names, paths, or ordering;
- YouTube corpus material would be mixed into Strategy B behavior without a
  separate design decision;
- any output would imply profitability, live readiness, or money-making
  reliability.

## 10. Separation from YouTube corpus work

Strategy B local diagnostics belong to the Strategy A/B verification line.

They must not import YouTube channel-wide corpus findings into executable
Strategy B behavior, stop-anchor rules, TP selection, RR gates, filters, or
management logic unless a separate design decision explicitly authorizes that
integration.

YouTube corpus artifacts, captions, transcript bodies, subtitle files, caption
URLs, downloaded media, and doctrine-map findings are outside the default local
diagnostic source boundary.

## 11. No Strategy behavior change confirmation

This runbook confirms:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B rule, stop-anchor rule, TP rule, RR gate, ADX rule, management
  rule, parameter, config, test, runner, or backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or local artifact was read;
- no market-data API, broker API, live-trading, auto-trading, or order-placement
  behavior was added;
- no optimization was performed;
- no profitability or live-readiness claim was made.
