# Strategy B Stop-Anchor Fallback Sample Availability Review

## 1. Objective and scope

This report records one bounded local-only availability review for Strategy B
reference-candle fallback stop-anchor cases.

The objective is not to label more cases and not to change Strategy B. The
objective is to determine whether enough additional fallback cases exist under a
broader, predeclared local-only slice to justify another blinded Pass A / Pass B
fallback-only diagnostic.

Scope:

- use committed repository docs and Strategy B code only to define the fallback
  case class;
- use the existing local USDJPY/EURUSD 4H inputs and existing local-only
  Strategy B read-only artifacts under the fixed local-only root;
- count fallback-case availability at aggregate level only;
- report only aggregate counts, high-level bucket definitions, feasibility
  decision, blockers, and guardrails;
- commit only this Git-safe Markdown report.

This report does not perform Pass A labeling, does not inspect chart packets,
does not create worksheets or mappings, and does not change Strategy B behavior.

## 2. Source docs and code used

Committed docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_fallback_bucket_local_only_run_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_local_only_run_report_after_handoff.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_sample_design_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_protocol_guardrails.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`

Committed code inspected read-only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`

No Strategy B code, test, runner, parameter, config, or backtest behavior was
modified.

## 3. Local-only artifact classes used

Fixed local-only root, redacted for Git:

- `<USER_HOME>\FX-local-data\FX-public`

Local-only artifact classes used:

- USDJPY/EURUSD 4H OHLC CSV inputs;
- Strategy B read-only candidate CSV artifacts;
- Strategy B read-only event artifact classes for context verification only;
- prior local diagnostic aggregate summaries for comparison to the earlier
  fallback shortfall.

Local-only artifact classes not used for this availability count:

- Pass A chart packets;
- contact sheets;
- hidden mapping and Pass B reveal row data;
- Pass A review worksheet row data;
- generated trade rows;
- generated TP-candidate rows;
- generated result rows.

No local-only CSV, JSON, worksheet, mapping, chart packet, image, raw row,
market data, generated event row, generated candidate row, generated trade row,
or generated result artifact is committed.

## 4. Fallback-case definition used for availability counting

The committed Strategy B stop-anchor logic selects a stop-side swing anchor when
a valid left-side swing exists beyond the EMA-touch reference candle level. If
no such swing exists, the logic falls back to the EMA-touch reference candle
level itself.

Availability definition used here:

| Direction | Fallback definition |
| --- | --- |
| Long | selected `stop_anchor` equals the EMA-touch reference candle low |
| Short | selected `stop_anchor` equals the EMA-touch reference candle high |

The definition is mechanical and uses only confirmation-time or earlier
information. It does not use outcome, trade result, profit/loss, final R, or
future bars.

## 5. Predeclared availability slice

The broader availability slice was:

- pairs: USDJPY and EURUSD;
- timeframe: 4H;
- local input class: existing local Strategy A OHLC input files;
- Strategy B artifact class: existing read-only Strategy B candidate exports
  from the local stop-anchor run;
- candidate universe: all Strategy B confirmation candidates in those read-only
  candidate exports;
- eligibility filter: candidate has a selected stop anchor;
- fallback test: selected stop anchor matches the EMA-touch reference candle
  stop-side level under the definition above;
- exclusions: candidates without any selected stop anchor and any candidate
  whose touch bar could not be matched in local OHLC context.

This slice is broader than the earlier blinded sample because it counts the
entire eligible candidate universe in the existing local read-only run rather
than only the prior bounded sample buckets.

## 6. Aggregate fallback candidate counts

Aggregate availability count:

| Count class | Count |
| --- | ---: |
| Strategy B confirmation candidates | 373 |
| Candidates with an eligible stop anchor | 340 |
| Candidates without a selected stop anchor | 33 |
| Candidates with missing local touch-bar context | 0 |
| Reference-candle fallback candidates | 1 |
| Nonfallback swing-anchor candidates | 339 |

Fallback aggregate breakdown:

| Fallback aggregate class | Count |
| --- | ---: |
| Fallback candidates, USDJPY | 1 |
| Fallback candidates, EURUSD | 0 |
| Fallback candidates, long direction | 1 |
| Fallback candidates, short direction | 0 |
| Fallback candidates with left-side TP1 available | 1 |
| Fallback candidates accepted by current Strategy B gates | 0 |
| Fallback candidates failing current stop-width gate | 1 |
| Fallback candidates failing current TP1 minimum RR gate | 1 |
| Fallback candidates whose first fail reason is `stop_too_wide` | 1 |

The previous fallback-only diagnostic selected one base fallback case against a
target of four base cases. This broader availability review found the same
aggregate base availability: one fallback candidate in the eligible local
read-only universe.

## 7. Sample feasibility decision

Decision:

`blocked_insufficient_reference_candle_fallback_cases`

Rationale:

- the predeclared fallback-only target remains four base cases;
- the broader eligible candidate universe contains only one reference-candle
  fallback candidate;
- the shortfall remains three base cases;
- the broader count does not reveal additional fallback candidates beyond the
  prior local-only diagnostic sample;
- another blinded fallback-only Pass A / Pass B diagnostic would repeat the
  same underpowered one-case limitation unless a separately authorized future
  issue changes the source universe or sample design.

Therefore, a future blinded fallback-only diagnostic is not feasible under the
current local USDJPY/EURUSD 4H read-only slice.

## 8. Blockers and ambiguity notes

Blocker:

- the eligible local read-only universe contains only one reference-candle
  fallback candidate, below the four-base-case target.

Ambiguity notes:

- this availability review counts candidate existence only; it does not classify
  structural stop-anchor quality;
- the fallback candidate overlaps with stop-width and TP1 RR failure fields, but
  those fields are not used as proof of stop-anchor invalidity;
- the review does not introduce an independent second reviewer;
- no row-level pair, time, price, mapping, worksheet, or chart-packet detail is
  Git-safe for this report.

## 9. No Strategy B behavior change confirmation

Confirmed:

- no Strategy B rule changed;
- no stop-anchor logic changed;
- no stop-buffer logic changed;
- no stop sanity limit changed;
- no TP1/TP2 selection or RR gate changed;
- no ADX, ATR, swing width, lookback, pair setting, runner behavior, test, or
  config changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic label set was changed;
- no implementation proposal is authorized by this report.

The current Strategy B closure note remains controlling.

## 10. Git-safe output and guardrail confirmation

Confirmed:

- this is an aggregate Markdown report only;
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
- no profitability, money-making, live-readiness, or trading recommendation
  claim is made;
- Strategy A/B verification work remains separate from YouTube channel-wide
  corpus work.

## 11. Recommended next bounded task

Recommended next task:

`[codex] Strategy B fallback availability decision note`

Suggested scope:

- docs-only;
- use this availability shortfall and the prior fallback bucket report as
  committed evidence;
- decide whether the fallback-specific diagnostic line should be closed as
  underpowered for the current USDJPY/EURUSD 4H local slice or deferred until a
  separately authorized source universe exists;
- do not run another blinded fallback-only diagnostic on the same one-case
  availability pool;
- do not change Strategy B behavior, parameters, code, configs, tests, runner
  behavior, or backtest behavior.
