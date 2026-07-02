# Strategy B Stop-Anchor Diagnostic Run Authorization Review

## 1. Objective and scope

This report decides whether a future local-only Strategy B stop-anchor
diagnostic run is warranted. It uses committed repository docs and code only,
and it does not run the diagnostic.

Scope:

- review the current controlling Strategy B TP1 / stop-anchor decision state;
- decide whether a future local-only stop-anchor diagnostic run is warranted;
- if warranted, define the exact future-run boundary specification;
- confirm that this report does not authorize any Strategy B behavior change.

Out of scope:

- no diagnostic run, backtest run, packet creation, review sheet, mapping,
  sample row, chart image, CSV, JSON, `data/`, `results/`, or generated
  artifact;
- no Strategy A/B/B2/C rule, code, parameter, config, test, runner, or backtest
  behavior change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, downloaded media, ASR, or external source access;
- no profitability, live-readiness, or trading-recommendation claim.

## 2. Source docs/code inspected

Committed docs inspected:

- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_sample_design_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_protocol_guardrails.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_backlog_issue_47_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`

Committed code inspected read-only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`

No uncommitted local files, raw data artifacts, generated outputs, market data,
broker/live systems, video sources, captions, transcripts, or external sources
were used.

## 3. Current controlling Strategy B decision state

The controlling Strategy B state remains frozen by the closure note:

- keep current rank-1 TP1 selection;
- keep current TP1, TP2, and TP1-only minimum RR gates;
- keep current stop-anchor logic, stop-buffer logic, and stop sanity limits;
- keep current ADX and management structure;
- do not create Strategy B2;
- do not approve implementation from the TP1 / stop-anchor review cycle.

The implementation remains aligned with that frozen state. The code still uses
nearest eligible left-side swings for TP1/TP2, selects the current stop anchor
from eligible left-side stop-side swings or the reference candle fallback, and
evaluates fixed RR, stop-width, and ADX gates. The read-only runner still writes
candidate, event, trade, metrics, and TP-candidate outputs only when explicitly
run against local CSV inputs; this authorization review did not run it.

Committed docs preserve the stop-anchor diagnostic path because stop quality is
not the same question as TP1 RR convenience. However, the same docs also state
that width alone must not become stop invalidity, shallow stops must not be
accepted merely to improve RR, and any future evidence may only reopen a later
design review rather than change Strategy B automatically.

## 4. Authorization decision: warranted

Decision:

`warranted_for_one_future_local_only_diagnostic_run_under_fixed_blinded_boundaries`

A future local-only stop-anchor diagnostic run is warranted because:

- the backlog explicitly preserves `B-TP1-FU-06 - Stop-anchor diagnostic path`;
- the protocol guardrails now define fixed labels and Pass A / Pass B
  separation;
- the sample design checklist defines packet fields, hidden fields, repeat
  checks, second-review triggers, shortfall rules, hard stops, and local-only
  artifact policy;
- the unresolved research question is structural: whether current stop anchors
  are structurally valid, questionable, or visually uninterpretable before
  viewing stop distance, RR, rejection reasons, or outcome-like fields;
- the current docs and code provide enough boundary material to specify a safe
  future issue without improvising source access, generated artifacts in Git,
  or Strategy B behavior changes.

This decision does not authorize the diagnostic run by itself. It says a future
issue may authorize one bounded local-only run if that issue repeats the
boundary specification below and accepts the local-only artifact constraints.

## 5. Exact future-run boundary specification

Diagnostic question:

Can current Strategy B stop anchors be separated into structurally valid,
questionable, visually uninterpretable, and insufficient-context classes before
revealing stop distance, RR, rejection reasons, acceptance status, or outcome-
like fields?

Allowed local-only source artifacts:

- existing local OHLC CSV inputs needed by `strategy_b_runner.py`;
- existing local Strategy B generated candidate/event/TP-candidate outputs if
  already present or explicitly regenerated by the future issue;
- local chart packets generated only for the diagnostic run;
- local hidden case mappings and review worksheets generated only for the run.

Allowed local-only artifact classes:

- chart packets, chart images, and screenshots;
- anonymized Pass A packets;
- hidden case-ID-to-row mappings;
- unfilled and filled review worksheets;
- sample selection tables;
- candidate, event, TP-candidate, or trade rows;
- Pass A label tables and Pass B reveal tables;
- generated CSV/JSON diagnostics used locally.

Sample buckets and shortfall rules:

- include cases where current stop logic has an eligible stop anchor;
- include cases where current stop logic falls back to the reference candle;
- include cases later revealed as stop-width concerns only after Pass A labels
  are locked;
- keep no-left-side/no-valid-target and no-trade-structure cases separate from
  low-RR cases;
- do not select rows because they are accepted, rejected, winning, losing, or
  convenient for a desired rule;
- if a bucket has too few cases, record the shortfall instead of borrowing from
  an outcome-selected bucket;
- stop the run if sample construction cannot preserve Pass A blindness.

Pass A packet fields:

- anonymized case ID;
- direction;
- setup, touch, and confirmation marker or window;
- entry-side orientation only when needed to interpret stop side;
- current stop-anchor marker and stop side;
- reference-candle high/low marker when needed to judge fallback logic;
- enough pre-confirmation left-side bars to judge swing context;
- packet-completeness flag;
- one fixed reviewer label;
- short ambiguity note.

Fixed Pass A labels:

- `structurally_valid_stop_anchor`;
- `questionable_stop_anchor`;
- `visually_uninterpretable_stop_anchor`;
- `insufficient_context_no_decision`.

Hidden fields:

- pair/time identifiers;
- entry price, ATR, ADX, buffer, stop price, risk, and stop distance;
- stop-too-narrow and stop-too-wide pass/fail fields;
- TP1/TP2 prices, R values, ranks, and RR pass/fail fields;
- accepted status, first-fail reason, and all-failed reasons;
- trade exit, TP hit, stop hit, final R, win/loss, or any outcome-like field.

Repeat checks:

- predeclare repeat count or percentage;
- insert repeat packets under different anonymized IDs;
- keep repeat identity hidden until Pass A is locked;
- compare labels after lock;
- record disagreement as ambiguity, not as reviewer failure;
- do not resolve disagreement with Pass B fields.

Second-review triggers:

- `questionable_stop_anchor` with high-impact ambiguity;
- `visually_uninterpretable_stop_anchor` where packet construction may be the
  issue;
- repeat-case disagreement;
- competing nearby swing or fallback ambiguity;
- reviewer note implies RR, outcome, or later-candle leakage;
- packet-completeness flag is false.

Pass B reveal fields:

- stop distance and ATR multiple;
- TP1 RR and TP2 RR when relevant to aggregate interpretation;
- current stop sanity pass/fail;
- current TP RR pass/fail fields;
- first-fail and all-failed reasons;
- target-rank context.

Hard stops:

- future issue does not explicitly authorize the diagnostic run;
- sample design is not fixed before review starts;
- labels change during review;
- sample selection uses outcome, profitability, accepted status, or a desired
  rule conclusion;
- Pass A reveals stop distance, RR, TP rank, rejection reason, accepted status,
  or outcome-like fields;
- row-level artifacts, chart packets, mappings, worksheets, CSV/JSON outputs,
  `data/`, or `results/` are staged for Git;
- reviewers propose rule, parameter, Strategy B2, Strategy C, or live-trading
  changes during the run;
- the run starts optimizing thresholds, stop buffers, ATR multiples, RR gates,
  swing widths, lookbacks, ADX, or pair-specific settings;
- output makes profitability, live-readiness, or money-making claims.

Git-safe aggregate output format:

- one compact Markdown report;
- aggregate label counts and ambiguity counts only;
- bucket shortfalls and blocker notes;
- repeat-disagreement counts;
- second-review trigger counts and adjudication-summary counts;
- no pair/time/price rows, raw market data, chart images, hidden mappings,
  filled worksheet rows, generated CSV/JSON, transcript/subtitle content, or
  outcome/profitability claims.

## 6. Deferred or not-warranted replacement path

Not applicable. The decision is warranted under the fixed boundary above.

If a future issue cannot accept the local-only artifact policy, blinded Pass A
/ Pass B split, hidden-field list, or hard stops, the replacement path should
be a no-op or a narrower docs-only blocker note. It should not run diagnostics
with weakened controls.

## 7. No-diagnostic-run confirmation

Confirmed: this report did not run a diagnostic, backtest, runner, market-data
fetch, broker/live operation, chart-packet generation, review process, sample
selection, local artifact creation, or generated-output creation.

## 8. No Strategy B change authorization

Confirmed: this report does not authorize any Strategy B rule, code, parameter,
config, test, runner, backtest, stop-anchor, stop-buffer, stop sanity, TP1/TP2,
RR, ADX, management, Strategy B2, or Strategy C change.

Future diagnostic evidence, even if collected under the bounded protocol, may
only support a later docs-only design-review reopen. It cannot directly change
Strategy B behavior.

## 9. Local-only artifact and Git-safe output policy

All row-level and visual artifacts for a future run must remain local-only and
out of Git, including:

- chart packets, images, screenshots, mappings, worksheets, sample tables,
  candidate rows, event rows, trade rows, TP-candidate rows, label tables,
  reveal tables, generated CSV/JSON, raw market data, normalized CSVs,
  `data/`, and `results/`.

Git-safe outputs are limited to compact aggregate Markdown reports, diagnostic
taxonomies, blocker notes, and design-decision memos that exclude row-level
market data, pair/time/price details, chart images, hidden mappings, filled
worksheet rows, transcript/subtitle content, downloaded media, and
outcome/profitability claims.

## 10. Hard-stop confirmation

Confirmed: the future run should stop rather than continue if it cannot
preserve source limits, reviewer blindness, hidden-field separation, local-only
artifact handling, Strategy/corpus separation, or no-implementation boundaries.

## 11. Guardrail confirmation

Confirmed for this report:

- docs-only authorization review;
- committed repository docs and code only;
- one Markdown report added;
- no Strategy A/B/B2/C behavior change;
- no Strategy B rules, parameters, configs, tests, runner behavior, or backtest
  behavior changed;
- no Strategy B2 or Strategy C created;
- no parameter optimization;
- no diagnostics, backtests, chart packets, review sheets, mappings, sample
  rows, labels, CSV, JSON, `data/`, `results/`, or generated artifacts created
  or committed;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, downloaded media, ASR, or external sources accessed;
- no raw market data, normalized CSV, generated candidate/result/trade/event
  CSV, raw transcript, subtitle text, raw TXT/SRT/VTT, caption URL, downloaded
  media, credentials, tokens, or secrets committed;
- no profitability claim or trading recommendation.

## 12. Recommended next bounded task

Updated routing after the public diagnostic boundary:

Do not proceed next to a local-only blinded stop-anchor diagnostic run. Next
local-only diagnostic, packet, sample, Pass A / Pass B, worksheet, mapping,
reveal-table, chart-packet, or review-run work remains paused under
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md` until
explicit human approval is given after corpus input, visual evidence review, and
doctrine synthesis dependencies are addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.
