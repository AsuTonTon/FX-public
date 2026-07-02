# Strategy B Stop-Anchor Diagnostic Local-Only Run Report After Handoff

## 1. Objective and scope

This report records the bounded local-only Strategy B stop-anchor diagnostic run
performed after local OHLC inputs were handed off.

Diagnostic question:

Can current Strategy B stop anchors be separated into
`structurally_valid_stop_anchor`, `questionable_stop_anchor`,
`visually_uninterpretable_stop_anchor`, and
`insufficient_context_no_decision` before revealing stop distance, RR, TP rank,
rejection reason, accepted/rejected status, or outcome-like fields?

Scope:

- use the committed Strategy B runner and strategy code only;
- use only local OHLC CSV inputs under the fixed local-only data root;
- generate Strategy B read-only artifacts under the fixed local-only output root;
- create local-only diagnostic packets, worksheets, mappings, and reveal tables;
- commit only this compact aggregate Markdown report.

Out of scope:

- no Strategy A/B/B2/C behavior change;
- no code, parameter, config, test, runner, or backtest behavior change;
- no market-data download, market-data API, broker API, order placement, auto
  trading, or live-readiness claim;
- no optimization or profitability claim.

Diagnostic status: `completed_with_bucket_shortfall_and_independent_review_limit`.

## 2. Source docs and code used

Controlling docs:

- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_local_only_run_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_run_authorization_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_sample_design_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_protocol_guardrails.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_backlog_issue_47_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`

Code inspected and used:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`
- `src/backtest/strategy_a_runner.py`
- `config/strategy_a_pairs.example.json`

Runner compatibility confirmed:

- `strategy_b_runner.py` accepts `--input-dir`, `--output-dir`,
  `--pair-settings`, and optional `--pairs`;
- pair CSV discovery accepts `PAIR_4h.csv`, which matches the handed-off local
  inputs.

## 3. Local-only input and artifact classes

Local-only data root used, Git-safe redacted form:

- `<USER_HOME>\FX-local-data\FX-public`

Local OHLC inputs were confirmed at a high level only:

| Local input | Columns | Rows | Date range |
|---|---|---:|---|
| USDJPY 4H | `timestamp`, `open`, `high`, `low`, `close`, `volume` | 42,769 | 1999-01-04 04:00:00 to 2026-06-24 04:00:00 |
| EURUSD 4H | `timestamp`, `open`, `high`, `low`, `close`, `volume` | 42,780 | 1999-01-04 08:00:00 to 2026-06-24 04:00:00 |

No raw market rows were printed or committed.

Local-only Strategy B artifact classes generated under the fixed output root:

- Strategy B summary artifact;
- candidate CSV artifacts;
- event CSV artifacts;
- trade CSV artifacts;
- TP-candidate CSV artifacts;
- metrics JSON/CSV artifacts.

Local-only diagnostic artifact classes generated under the fixed diagnostic root:

- anonymized Pass A chart packets;
- local sample design summary;
- local review worksheet;
- hidden case mapping and Pass B reveal table;
- local Pass B aggregate summary;
- local contact sheet for Pass A review convenience.

All generated artifacts remained outside Git.

## 4. Sample design summary

The diagnostic used a predeclared bounded sample design:

- deterministic seed: `20260703`;
- base sample plan: 12 cases;
- repeat plan: 2 packets;
- Pass A context: last 100 bars through confirmation only;
- Pass A packet fields: anonymized case ID, direction, stop side, setup/touch/
  confirmation markers, stop-anchor marker, reference high/low markers, packet
  completeness flag, fixed label field, and ambiguity note;
- hidden until Pass A lock: pair/time identifiers, entry/stop/TP prices, ATR,
  ADX, stop distance, RR, target rank, rejection reason, accepted/rejected
  status, and outcome-like fields.

Candidate universe, aggregate only:

| Aggregate class | Count |
|---|---:|
| Strategy B confirmation candidates | 373 |
| Candidates with an eligible stop anchor | 340 |
| Candidates without a stop anchor for this diagnostic | 33 |
| Candidates with missing local index context | 0 |

Bucket plan and shortfalls:

| Bucket | Planned | Selected | Shortfall |
|---|---:|---:|---:|
| Stop-width concern, hidden until after Pass A lock | 4 | 4 | 0 |
| Reference-candle fallback | 4 | 1 | 3 |
| Nonfallback swing anchor | 4 | 4 | 0 |

No substitute cases were borrowed to fill the reference-candle fallback
shortfall.

Final reviewed packet set:

| Packet class | Count |
|---|---:|
| Base packets | 9 |
| Repeat packets | 2 |
| Total Pass A packets | 11 |

## 5. Pass A blindness confirmation

Pass A labels were locked before opening the local hidden mapping or Pass B
reveal table.

Pass A review used only anonymized chart packets. It did not show:

- pair/time identifiers;
- raw rows;
- entry price, ATR, ADX, stop price, buffer, risk, or stop distance;
- stop-too-narrow or stop-too-wide pass/fail fields;
- TP prices, TP rank, RR values, or TP pass/fail fields;
- accepted/rejected status;
- first-fail or all-failed reasons;
- trade exit, TP hit, stop hit, final R, win/loss, or outcome-like fields.

No Pass A label was changed after Pass B reveal.

## 6. Aggregate Pass A label counts

Base packets only:

| Pass A label | Count |
|---|---:|
| `structurally_valid_stop_anchor` | 6 |
| `questionable_stop_anchor` | 3 |
| `visually_uninterpretable_stop_anchor` | 0 |
| `insufficient_context_no_decision` | 0 |

All packets including repeats:

| Pass A label | Count |
|---|---:|
| `structurally_valid_stop_anchor` | 6 |
| `questionable_stop_anchor` | 5 |
| `visually_uninterpretable_stop_anchor` | 0 |
| `insufficient_context_no_decision` | 0 |

These counts are diagnostic labels only. They are not a rule-change decision.

## 7. Repeat-check aggregate results

Repeat-check aggregate:

| Repeat-check class | Count |
|---|---:|
| Repeat packets | 2 |
| Same fixed label as original packet | 2 |
| Label disagreement | 0 |

Repeat identity stayed hidden until after Pass A label lock.

## 8. Second-review aggregate summary

Predeclared second-review triggers were evaluated after Pass A lock using Pass
A material only.

Trigger summary:

| Trigger class | Base cases | All packets |
|---|---:|---:|
| Unique triggered cases/packets | 3 | 5 |
| Trigger instances | 6 | 10 |

Trigger-instance breakdown across all packets:

| Trigger class | Count |
|---|---:|
| `questionable_with_high_impact_ambiguity` | 5 |
| `competing_nearby_swing_or_invalidation_ambiguity` | 3 |
| `reference_candle_fallback_ambiguity` | 2 |

Adjudication summary:

- original Pass A labels preserved: yes;
- Pass B fields used for label revision: no;
- label revisions after Pass B reveal: 0.

Limitation: no separate independent reviewer was introduced in this local run.
The triggered cases were rechecked under Pass A-only material and are reported
as an aggregate limitation rather than independent reviewer evidence.

## 9. Pass B aggregate interpretation

Pass B revealed hidden diagnostic fields only after Pass A labels were locked.
The reveal was used for aggregate interpretation only.

Base-case aggregate overlaps:

| Aggregate overlap | Count |
|---|---:|
| `questionable_stop_anchor` and stop-width concern | 3 |
| `structurally_valid_stop_anchor` and stop-width concern | 4 |
| `questionable_stop_anchor` and TP1 RR failure | 3 |
| `structurally_valid_stop_anchor` and TP1 RR failure | 6 |
| Reference-candle fallback base cases | 1 |
| Nonfallback base cases | 8 |

Aggregate interpretation:

- both structural-valid and questionable labels overlapped with stop-width
  concern cases;
- all reviewed base cases overlapped with TP1 RR failure after reveal;
- width and RR failure therefore cannot be used as a substitute for structural
  stop-anchor validity;
- the reference-candle fallback bucket was too small in this bounded run for a
  stable conclusion;
- the run supports preserving stop-anchor quality as a separate diagnostic axis,
  not changing the stop-anchor rule.

## 10. Blockers and ambiguity notes

Blockers:

- none that forced a full stop after local OHLC handoff and read-only artifact
  generation.

Ambiguity notes:

- the reference-candle fallback bucket had a 3-case shortfall;
- the bounded sample is small and should not be generalized as a final design
  decision;
- no independent second reviewer was used;
- several questionable labels were driven by visible competing invalidation
  areas or reference-candle fallback ambiguity, not by stop width, RR, rejection
  reason, accepted status, or outcome.

## 11. No Strategy B behavior change confirmation

Confirmed:

- no Strategy B rule changed;
- no stop-anchor logic changed;
- no stop-buffer logic changed;
- no stop sanity limit changed;
- no TP1/TP2 selection or RR gate changed;
- no ADX, ATR, swing width, lookback, pair setting, runner behavior, test, or
  config changed;
- no Strategy B2 or Strategy C was created;
- no implementation proposal is authorized by this report.

## 12. Local-only artifact and Git-safe output confirmation

Confirmed:

- no local-only artifact under `<USER_HOME>\FX-local-data\FX-public` is
  intended for Git;
- no `data/` or `results/` path is intended for Git;
- no CSV, JSON, chart image, screenshot, worksheet, mapping, sample row,
  candidate row, event row, trade row, TP-candidate row, raw market row,
  credential, token, or secret is intended for Git;
- this Markdown file is the only intended Git output.

## 13. Guardrail confirmation

Confirmed:

- local CSV input only;
- no market-data download;
- no market-data API call;
- no broker API call;
- no order placement;
- no auto trading;
- no live-readiness claim;
- no profitability claim;
- no parameter optimization;
- no rule proposal;
- no code/test/config/runner/backtest behavior change;
- no raw rows, hidden mappings, worksheets, chart packets, images, screenshots,
  CSV, JSON, `data/`, or `results/` committed.

## 14. Recommended next bounded task

Updated routing after the public diagnostic boundary:

Do not proceed next to fallback bucket follow-up design, fallback-focused sample
planning, independent Pass A-only second review, or review-run preparation.
Next local-only diagnostic, packet, sample, Pass A / Pass B, worksheet, mapping,
reveal-table, chart-packet, or review-run work remains paused under
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md` until
explicit human approval is given after corpus input, visual evidence review, and
doctrine synthesis dependencies are addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.
