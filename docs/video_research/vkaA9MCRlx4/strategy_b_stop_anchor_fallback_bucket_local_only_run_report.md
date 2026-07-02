# Strategy B Stop-Anchor Fallback Bucket Local-Only Run Report

## 1. Objective and scope

This report records a bounded local-only follow-up diagnostic focused only on
Strategy B reference-candle fallback stop-anchor cases.

The diagnostic objective was to use the fixed local-only data root and the
committed Pass A / Pass B protocol to test whether fallback stop anchors can be
structurally classified before revealing stop distance, RR, rejection reason,
acceptance status, or outcome-like fields.

Scope:

- use committed repository docs and Strategy B code;
- use existing local USDJPY/EURUSD 4H OHLC inputs and local-only Strategy B
  read-only outputs;
- select reference-candle fallback cases only;
- preserve the fixed Pass A label set;
- preserve Pass A / Pass B separation;
- commit only this aggregate Markdown report.

This report does not change Strategy B behavior.

## 2. Source docs and code used

Committed docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_local_only_run_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_sample_design_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_protocol_guardrails.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`

Committed code used read-only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`

No Strategy B code, test, runner, parameter, config, or backtest behavior was
modified.

## 3. Local-only artifact classes used

Fixed local-only root, redacted for Git:

- `<USER_HOME>\FX-local-data\FX-public`

Local-only artifact classes used:

- USDJPY/EURUSD 4H OHLC CSV inputs;
- Strategy B read-only candidate artifacts;
- Strategy B read-only event artifacts;
- Strategy B read-only trade artifacts;
- Strategy B read-only TP-candidate artifacts;
- Strategy B read-only metrics artifacts;
- local sample-design aggregate summary;
- local anonymized Pass A chart packets;
- local Pass A review worksheet;
- local hidden mapping and Pass B reveal table;
- local Pass B aggregate summary.

No local-only CSV, JSON, worksheet, mapping, chart packet, image, raw row,
market data, generated event row, generated candidate row, generated trade row,
or generated result artifact is committed.

## 4. Fallback-only sample design summary

The follow-up reused the committed diagnostic rules:

- fixed Pass A labels only;
- Pass A packets hide pair/time identifiers, price rows, stop distance, ATR,
  RR, TP rank, rejection reason, acceptance status, and outcome-like fields;
- Pass A labels are locked before reading hidden mapping or Pass B reveal
  fields;
- Pass B is aggregate interpretation only;
- shortfalls are recorded rather than filled from another bucket.

Fallback bucket target:

| Bucket | Planned base cases | Selected base cases | Shortfall |
| --- | ---: | ---: | ---: |
| Reference-candle fallback | 4 | 1 | 3 |

The local-only eligible pool contained only one base reference-candle fallback
case after exclusions. No nonfallback swing-anchor case was borrowed to fill
the bucket.

## 5. Fallback sample count and shortfalls

Aggregate fallback packet counts:

| Count type | Count |
| --- | ---: |
| Base fallback cases | 1 |
| Repeat fallback packets | 1 |
| Total fallback packets reviewed | 2 |
| Planned base fallback cases | 4 |
| Base-case shortfall | 3 |

The fallback-only result is therefore a shortfall diagnostic, not a stable
sample. It can identify the observed fallback bucket limitation, but it is too
small to support a Strategy B rule, parameter, or implementation change.

## 6. Pass A blindness confirmation

Pass A used only anonymized confirmation-time material needed to judge
structural stop-anchor validity.

Hidden until Pass A label lock:

- pair and time identifiers;
- raw prices and row mappings;
- stop distance and ATR multiple;
- TP1/TP2 RR fields;
- TP rank and target-selection context;
- first-fail and all-failed reasons;
- accepted status;
- trade or outcome-like fields.

The Pass A labels were recorded before Pass B reveal fields were inspected.

## 7. Aggregate Pass A label counts

Fallback-only Pass A label counts:

| Pass A label | Base cases | Repeat packets | Total fallback packets |
| --- | ---: | ---: | ---: |
| `structurally_valid_stop_anchor` | 0 | 0 | 0 |
| `questionable_stop_anchor` | 1 | 1 | 2 |
| `visually_uninterpretable_stop_anchor` | 0 | 0 | 0 |
| `insufficient_context_no_decision` | 0 | 0 | 0 |

The single base fallback case and its repeat packet were both labeled
`questionable_stop_anchor`.

## 8. Independent second-review summary or limitation

Independent second-review evidence is limited.

The local diagnostic did include a Pass A-only recheck trigger for fallback
ambiguity, and original labels were preserved. The fallback case remained
`questionable_stop_anchor` after the Pass A-only recheck.

However, this automation run did not add a separate independent human reviewer.
The result should therefore be treated as a Pass A-only recheck limitation, not
as fully independent second-review evidence.

## 9. Pass B aggregate interpretation

Pass B reveal was used only after Pass A label lock and only for aggregate
interpretation.

Fallback-only aggregate interpretation:

- the base fallback case was also a stop-width concern after reveal;
- the base fallback case failed the TP1 minimum RR gate after reveal;
- the first-fail reason was `stop_too_wide`;
- accepted-status count for the base fallback case was zero;
- no Pass A label was revised after Pass B reveal.

These fields support the existing separation between structural stop-anchor
validity and later RR/width diagnostics. They do not support changing fallback
stop-anchor behavior.

## 10. Ambiguity and blocker notes

Ambiguity notes:

- the fallback bucket had only one unique base case;
- the case was structurally questionable under Pass A;
- fallback ambiguity remained a second-review trigger;
- repeat agreement reduces packet-level inconsistency concern but does not
  solve the base-case shortfall.

Blocker:

- the fallback bucket is too small for a stable conclusion.

No conclusion should be generalized from this fallback-only sample.

## 11. No Strategy B behavior change confirmation

Confirmed: this report does not authorize any Strategy B rule, code, parameter,
config, test, runner, backtest, stop-anchor, stop-buffer, stop-width, stop
sanity, TP1/TP2, RR, ADX, management, Strategy B2, or Strategy C change.

The current Strategy B closure note remains controlling.

## 12. Git-safe output and guardrail confirmation

Confirmed:

- no `data/` or `results/` files are committed;
- no raw market data or normalized market CSV is committed;
- no candidate, event, trade, TP-candidate, result, worksheet, mapping, image,
  chart packet, CSV, JSON, row-level table, or generated artifact is committed;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT caption file, caption
  URL, downloaded video, downloaded audio, raw DownSub output, or ASR output is
  committed;
- no credentials, tokens, or secrets are committed;
- no market-data API, broker API, live-trading, auto-trading, or
  order-placement behavior is added;
- no Strategy C work is added;
- no parameter optimization is performed;
- no profitability, money-making, or live-readiness claim is made;
- Strategy A/B verification work remains separate from YouTube channel-wide
  corpus work.

## 13. Recommended next bounded task

Updated routing after the public diagnostic boundary:

Do not proceed next to fallback sample availability review, broader local-only
slice checks, Pass A / Pass B setup, or independent reviewer setup. Next
local-only diagnostic, packet, sample, Pass A / Pass B, worksheet, mapping,
reveal-table, chart-packet, or review-run work remains paused under
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md` until
explicit human approval is given after corpus input, visual evidence review, and
doctrine synthesis dependencies are addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.
