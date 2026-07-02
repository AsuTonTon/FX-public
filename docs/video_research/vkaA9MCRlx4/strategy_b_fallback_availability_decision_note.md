# Strategy B Fallback Availability Decision Note

## 1. Objective and scope

This note decides the current status of the Strategy B reference-candle
fallback stop-anchor diagnostic line after the committed fallback sample
availability review.

Scope:

- use committed repository Markdown reports only;
- preserve the committed fallback availability counts and blocker decision;
- decide whether the current USDJPY/EURUSD 4H fallback line should continue,
  close, or defer;
- recommend one bounded next Strategy B research task, if any.

Out of scope:

- no diagnostic run;
- no local OHLC data access;
- no generated artifact access;
- no Strategy A/B/B2/C behavior, code, parameter, config, test, runner, or
  backtest behavior change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no market-data API, broker API, order-placement, auto-trading, live-trading,
  live-readiness, money-making, or trading-recommendation claim.

## 2. Source docs used

Committed repository docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_fallback_sample_availability_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_fallback_bucket_local_only_run_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_local_only_run_report_after_handoff.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_cumulative_synthesis.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market data APIs, broker/live systems,
YouTube sources, captions, subtitles, transcript bodies, caption URLs, or
external sources were used for this note.

## 3. Committed fallback availability evidence

The controlling committed evidence is:

| Evidence item | Committed value |
| --- | --- |
| Planned fallback base-case target | 4 |
| Fallback base cases selected in the fallback bucket diagnostic | 1 |
| Fallback base-case shortfall | 3 |
| Broader USDJPY/EURUSD 4H eligible Strategy B confirmation candidates | 340 |
| Reference-candle fallback candidates in the broader eligible universe | 1 |
| Nonfallback swing-anchor candidates in the broader eligible universe | 339 |
| Availability review decision | `blocked_insufficient_reference_candle_fallback_cases` |

The availability review found no additional reference-candle fallback cases
beyond the prior fallback bucket diagnostic. The current local USDJPY/EURUSD 4H
slice therefore still has one eligible fallback base case against the
four-base-case target.

## 4. Decision options considered

| Option | Decision | Rationale |
| --- | --- | --- |
| Proceed to another fallback-only diagnostic on the same one-case pool | Rejected | It would repeat the same underpowered sample and add review activity without new evidence. |
| Close the fallback line as fully resolved for all possible sources | Rejected | The committed evidence covers the current local USDJPY/EURUSD 4H slice only. |
| Close the current local-slice fallback diagnostic line as underpowered | Accepted | The broader committed availability review confirms only one fallback case and preserves the blocker decision. |
| Defer any broader fallback diagnostic until a separately authorized source universe exists | Accepted | A broader universe would need its own issue, source boundary, sample plan, and guardrails before any local read or diagnostic run. |

## 5. Chosen decision and rationale

Chosen decision:

`close_current_usdjpy_eurusd_4h_fallback_line_as_underpowered_defer_broader_universe`

Rationale:

- the current fallback target is four base cases;
- the current committed broader local slice contains one reference-candle
  fallback candidate;
- the shortfall remains three base cases;
- the fallback bucket diagnostic already recorded that the one base case was
  not a stable sample;
- the availability review confirms the blocker instead of expanding the case
  pool;
- another diagnostic on the same one-case pool would not materially improve
  evidence quality;
- a broader universe may be considered only under a separate future issue with
  explicit source authorization and a predeclared sample design.

This decision is a research-line triage decision only. It does not state or
imply that fallback stop anchors are mechanically invalid in general.

## 6. What is closed, deferred, or still open

Closed for the current USDJPY/EURUSD 4H local slice:

- another fallback-only blinded Pass A / Pass B diagnostic using the same
  one-case reference-candle fallback pool;
- attempts to fill the fallback bucket by borrowing nonfallback swing-anchor
  cases;
- using the one-case fallback result as a basis for Strategy B behavior,
  parameter, stop-anchor, stop-buffer, stop-width, TP, RR, ADX, runner, config,
  test, or backtest changes.

Deferred:

- any broader fallback availability review using additional pairs, timeframes,
  date ranges, or artifact classes;
- any future fallback-only diagnostic that depends on a different source
  universe;
- independent second-review evidence for fallback cases, because the current
  pool is too small for a useful fallback-specific review cycle.

Still open:

- whether a separately authorized source universe could produce enough
  reference-candle fallback cases for a stable diagnostic;
- whether future independently reviewed fallback cases, if enough cases become
  available, show repeated structural patterns;
- whether any future Strategy B design review can state a confirmation-time
  mechanical rule without parameter tuning.

## 7. Implications for Strategy B TP1 / stop-anchor research

The current fallback line should not drive Strategy B implementation work.

Implications:

- Strategy B TP1 minimum RR and stop-anchor structure remain separate research
  axes;
- stop width, TP1 RR failure, accepted status, and outcome-like fields remain
  unavailable as substitutes for structural stop-anchor validity;
- the reference-candle fallback bucket should be treated as an availability
  blocker in the current local slice, not as a resolved structural finding;
- the cumulative Strategy B research state remains conservative: document
  blockers, preserve diagnostic separation, and avoid rule changes without a
  later design decision.

## 8. No Strategy behavior change confirmation

Confirmed:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B stop-anchor rule changed;
- no stop-buffer, stop-width, stop sanity, TP1/TP2, RR, ADX, ATR, swing-width,
  lookback, pair-setting, runner, config, test, or backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic label set changed;
- no implementation proposal is authorized by this note.

The current Strategy B closure and diagnostic guardrail docs remain controlling.

## 9. Guardrail confirmation

Confirmed:

- docs-only decision note;
- committed Markdown reports only;
- no local OHLC data, local generated artifacts, raw rows, chart packets,
  worksheets, mappings, reveal tables, CSV, JSON, images, `data/`, or
  `results/` are committed;
- no raw market data or normalized market CSV is committed;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT caption file, caption
  URL, downloaded video, downloaded audio, raw DownSub output, or ASR output is
  committed;
- no credentials, tokens, or secrets are committed;
- no market-data API, broker API, order-placement, auto-trading, live-trading,
  or live-readiness behavior is added;
- no parameter optimization is performed;
- no profitability, money-making, or trading recommendation claim is made;
- Strategy A/B verification work remains separate from YouTube channel-wide
  corpus work.

## 10. Recommended next bounded task

Recommended next task:

`[codex] Strategy B stop-anchor diagnostic backlog cleanup after fallback closure`

Suggested scope:

- docs-only;
- use committed Strategy B TP1, stop-anchor, fallback bucket, availability, and
  decision-note reports only;
- update or add one backlog cleanup note that marks the current USDJPY/EURUSD
  4H fallback diagnostic line closed as underpowered;
- preserve separately open research questions for TP1 RR, stop-anchor structure,
  no-valid-target cases, and any future broader source-universe decision;
- do not run diagnostics;
- do not access local data or generated artifacts;
- do not change Strategy B behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior.
