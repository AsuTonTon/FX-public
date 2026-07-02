# Strategy B Diagnostic Authorization Template

## 1. Objective and scope

Use this template when a future issue wants to authorize a bounded local-only
Strategy B diagnostic for stop-validity or rejection-taxonomy gaps.

The future issue must define a diagnostic authorization, not a Strategy B design
change. It must state the exact diagnostic question, the allowed source classes,
the local-only boundary, the sample buckets, the Pass A / Pass B handling, the
Git-safe output shape, and the hard-stop conditions before any local data or
generated artifact is read.

This template applies to future diagnostic questions covering:

- case-level stop-width versus structural stop-validity review;
- no-valid-target / no-left-side-target sample review;
- no-trade-structure sample review;
- low-R-but-structural TP classification;
- independent second-review or ambiguity checks for those classes.

Out of scope for this template:

- running diagnostics;
- accessing local OHLC data or generated Strategy B artifacts;
- creating chart packets, worksheets, mappings, reveal tables, CSV, JSON,
  images, `data/`, or `results/`;
- changing Strategy A/B/B2/C behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior;
- creating Strategy B2 or Strategy C;
- optimizing parameters;
- making profitability, live-readiness, money-making, or trading-recommendation
  claims.

## 2. Source docs used

Committed repository docs used for this template:

- `docs/video_research/vkaA9MCRlx4/strategy_b_design_review_evidence_gap_ledger.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_width_vs_stop_validity_evidence_matrix.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_design_review_gate_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_contextual_rr_requirements_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_no_valid_target_no_trade_structure_taxonomy_preservation.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_remaining_open_items_triage.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_cumulative_synthesis.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market-data APIs, broker/live systems,
YouTube sources, DownSub, captions, subtitles, transcript bodies, caption URLs,
comments, live chat, community posts, downloaded media, ASR, or external sources
were used for this template.

## 3. When this template applies

This template applies only when a future GitHub Issue explicitly asks for a
bounded local-only diagnostic authorization package before case-level Strategy B
review begins.

Use it for routine bounded diagnostic authorization when all of the following
are true:

- the question is docs-defined before any local artifact access;
- the diagnostic belongs to the Strategy A/B verification line;
- the issue names the allowed source classes;
- the fixed local-only root is stated in redacted form;
- the expected Git output is compact aggregate Markdown only;
- raw/generated artifacts remain outside Git;
- the diagnostic does not propose or imply Strategy behavior changes.

Do not use it as permission to run a diagnostic, inspect raw rows, or change
Strategy B behavior. The future diagnostic issue must separately authorize the
run itself.

## 4. Required authorization fields

A future diagnostic authorization issue must include every field below before
automation may proceed.

| Field | Required content | Hard-stop condition |
| --- | --- | --- |
| Diagnostic question | The exact question to answer, such as stop-width versus structural validity, no-valid-target review, no-trade-structure review, or low-R-but-structural TP classification. | The issue asks for general exploration or unspecified review. |
| Diagnostic class | One or more named classes: stop-validity, no-valid-target, no-trade-structure, low-R-but-structural TP, or second-review ambiguity. | The class is mixed with implementation, optimization, or design-change work. |
| Source docs/code | The committed docs and code that define the boundary for the diagnostic. | The issue relies on external sources or uncommitted material without authorization. |
| Allowed local source classes | Artifact classes only, such as approved OHLC inputs, read-only Strategy B outputs, chart packets, mappings, worksheets, or aggregate local summaries. | Exact raw paths, rows, filenames that reveal hidden fields, or unrestricted artifact classes are required in Git. |
| Fixed local-only root | The redacted local-only root, expected to remain under `<USER_HOME>\FX-local-data\FX-public` unless explicitly authorized otherwise. | The root is missing, ambiguous, outside the boundary, or requires committing local paths. |
| Sample buckets | Predeclared buckets, target counts, shortfall rules, and whether replacement buckets are allowed. | Buckets are selected after reading outcomes or performance. |
| Hidden fields | Fields hidden during Pass A, including stop distance, RR, target rank, accepted status, rejection reason, and outcome-like fields where relevant. | Structural labels depend on hidden fields. |
| Revealed fields | Fields allowed only after Pass A labels are locked for Pass B aggregate interpretation. | Pass B fields are used to revise Pass A labels without a predeclared rule. |
| Reviewer handling | Whether single review, independent second review, adjudication, or ambiguity tracking is required. | Ambiguous labels are treated as implementation support. |
| Git-safe output | The exact Markdown-only aggregate output, including allowed tables and prohibited row-level details. | The report needs raw rows, chart images, mappings, worksheets, CSV/JSON, `data/`, or `results/` in Git. |
| Stop conditions | Conditions that stop the run before local access, during sample selection, during Pass A, during Pass B, and before PR creation. | The issue has no hard-stop list. |
| No behavior change | Explicit confirmation that the diagnostic authorizes no Strategy B behavior, code, parameter, config, test, runner, or backtest change. | The issue requests implementation or threshold changes. |

Missing fields should stop automation without file changes.

## 5. Pass A / Pass B requirements

Pass A must lock structural or taxonomy labels before fields that can bias the
diagnostic are revealed.

Pass A requirements:

- use only the fields allowed by the future issue;
- label structural stop validity without stop distance, RR, target rank,
  accepted status, rejection reason, or outcome-like fields unless the issue
  explicitly states a narrower allowed field set;
- label no-valid-target and no-trade-structure cases without collapsing them
  into low-RR TP availability;
- record ambiguity and shortfall states as diagnostic results, not failures to
  be patched around;
- stop if the reviewer can infer hidden fields from packet names, ordering,
  paths, or surrounding metadata.

Pass B requirements:

- begin only after Pass A labels are locked;
- reveal only the fields named in the issue;
- summarize results in aggregate Markdown;
- keep row-level pair, time, price, chart, worksheet, mapping, and generated
  artifact detail out of Git;
- preserve the difference between stop width, stop validity, RR availability,
  target absence, no-trade-structure, and fallback availability;
- treat ambiguity or shortfall as a blocker for design review, not as support
  for a rule change.

## 6. Git-safe output requirements

Allowed Git outputs:

- compact aggregate Markdown reports;
- authorization checklists;
- protocol guardrails;
- blocker notes;
- aggregate counts without row-identifying detail;
- shortfall summaries;
- ambiguity summaries;
- docs-only next-task recommendations.

Forbidden Git outputs:

- `data/` or `results/`;
- raw market data or normalized market CSVs;
- candidate, event, trade, TP-candidate, result, worksheet, mapping, packet, or
  diagnostic CSV/JSON files;
- chart packets, chart images, screenshots, or contact sheets;
- row-level pair, time, price, candle, or outcome detail;
- hidden mappings or reveal tables;
- raw transcripts, subtitle full text, raw TXT/SRT/VTT files, caption URLs, or
  downloaded media;
- credentials, tokens, or secrets.

The PR output must be reviewable without exposing raw/generated artifacts.

## 7. Hard-stop conditions

Stop without local access or file changes when:

- the issue does not explicitly authorize the local read or diagnostic run;
- the diagnostic question, source classes, local root, sample buckets, hidden
  fields, Pass A / Pass B split, output shape, or stop conditions are missing;
- the issue asks for Strategy behavior, code, parameter, config, test, runner,
  or backtest changes;
- the issue asks for Strategy B2, Strategy C, parameter optimization, or
  performance-tuned threshold search;
- the issue asks for market-data API, broker API, order placement,
  auto-trading, live-trading, or live-readiness work;
- local roots, artifact classes, or reviewer inputs contradict the issue;
- raw/generated artifacts would need to be committed to support the conclusion;
- row-level pair, time, price, chart, mapping, worksheet, or outcome detail
  would be needed in Git;
- YouTube corpus findings would be mixed into Strategy B behavior without a
  separate design decision;
- any output would imply profitability, money-making reliability,
  live-readiness, or trading advice.

## 8. Routine versus executive-decision boundary

Routine bounded local-only diagnostic authorization is allowed only when it
stays inside the predeclared Strategy A/B verification boundary and produces
Git-safe aggregate Markdown.

Routine authorization can cover:

- stop-width versus structural stop-validity sample review;
- no-valid-target / no-left-side-target sample review;
- no-trade-structure sample review;
- low-R-but-structural TP classification;
- independent second-review or ambiguity checks;
- shortfall reporting when a predeclared sample is underpowered.

Executive decision is required before automation proceeds on:

- Strategy A/B/B2/C behavior, code, parameter, config, test, runner, or backtest
  changes;
- Strategy B2 or Strategy C creation;
- parameter optimization or performance-tuned threshold search;
- broader source universes not named by the issue;
- merging rejection taxonomy categories into implementation behavior;
- direct integration of YouTube channel-wide corpus findings into executable
  Strategy A/B behavior;
- any market-data API, broker API, order-placement, auto-trading, live-trading,
  or live-readiness work;
- committing raw/generated artifacts, row-level details, images, worksheets,
  mappings, CSV/JSON, `data/`, or `results/`;
- making or relying on profitability, money-making, live-readiness, or trading
  recommendation claims.

## 9. No Strategy behavior change confirmation

This template confirms:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B TP1, TP2, RR, contextual RR, stop-anchor, stop-buffer, stop
  sanity, ADX, ATR, swing-width, lookback, pair-setting, management, runner,
  config, test, or backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or generated artifact was accessed;
- no stop, RR, target, ADX, ATR, lookback, pair, timeframe, or management rule
  is proposed;
- no implementation proposal is authorized by this template;
- no YouTube channel-wide corpus findings are mixed into Strategy B executable
  behavior.

## 10. Guardrail confirmation

Confirmed:

- docs-only diagnostic authorization template;
- committed repository docs only;
- exactly one Markdown file added;
- no diagnostic was run;
- no local OHLC data or generated Strategy B artifact was accessed;
- no chart packet, worksheet, mapping, reveal table, sample row, CSV, JSON,
  image, `data/`, or `results/` was created or committed;
- no raw market data or normalized market CSV is committed;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT caption file, caption
  URL, downloaded video, downloaded audio, raw DownSub output, or ASR output is
  committed;
- no credentials, tokens, or secrets are committed;
- no market-data API, broker API, order-placement, auto-trading, live-trading,
  or live-readiness behavior is added;
- no parameter optimization is performed;
- no profitability, money-making, live-readiness, or trading recommendation
  claim is made;
- Strategy A/B verification work remains separate from YouTube channel-wide
  corpus work.

## 11. Recommended next bounded task

Post-boundary routing: this section is superseded for task routing by
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md`.

Do not use this template to draft or authorize another local-only diagnostic
issue, packet, sample, Pass A / Pass B, worksheet, mapping, reveal-table,
chart-packet, or review-run task. Next local-only diagnostic work remains
paused under the public boundary until explicit human approval is given after
corpus input, visual evidence review, and doctrine synthesis dependencies are
addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.
