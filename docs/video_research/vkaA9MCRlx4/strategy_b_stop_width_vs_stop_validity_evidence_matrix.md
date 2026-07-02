# Strategy B Stop Width Versus Stop Validity Evidence Matrix

## 1. Objective and scope

This matrix separates Strategy B stop width from structural stop validity and
adjacent evidence axes.

Scope:

- use committed repository Markdown reports only;
- preserve the current Strategy B behavior freeze;
- distinguish stop width, structural stop validity, RR availability, target
  absence, no-trade-structure, and fallback availability;
- identify which cells are supported by committed aggregate docs;
- identify which cells would require a separate future local-only diagnostic
  authorization;
- recommend one bounded docs-only next task.

Out of scope:

- no diagnostic run;
- no local OHLC data or generated artifact access;
- no chart packet, worksheet, mapping, reveal table, sample row, CSV, JSON,
  image, `data/`, or `results/` creation;
- no market-data API, broker API, live system, order placement, auto-trading,
  or live-trading access;
- no Strategy A/B/B2/C behavior, code, parameter, config, test, runner, or
  backtest behavior change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no profitability, live-readiness, money-making, or trading-recommendation
  claim;
- no direct import of YouTube channel-wide corpus findings into executable
  Strategy B behavior.

## 2. Source docs used

Committed repository docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_design_review_gate_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_contextual_rr_requirements_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_cumulative_synthesis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_remaining_open_items_triage.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_backlog_cleanup_after_fallback_closure.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_fallback_availability_decision_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_no_valid_target_no_trade_structure_taxonomy_preservation.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market-data APIs, broker/live systems,
YouTube sources, DownSub, captions, subtitles, transcript bodies, caption URLs,
comments, live chat, community posts, downloaded media, ASR, or external sources
were used for this matrix.

## 3. Current freeze state

The current Strategy B state remains frozen:

- TP1 minimum RR remains unchanged;
- TP2 minimum RR remains unchanged;
- TP1-only minimum RR remains unchanged;
- rank-1 TP1 selection remains unchanged;
- stop-anchor logic remains unchanged;
- stop-buffer logic remains unchanged;
- stop sanity limits remain unchanged;
- ADX, ATR, swing-width, lookback, pair-setting, management, runner, config,
  test, and backtest behavior remain unchanged;
- no-left-side / no-valid-target rejection behavior remains unchanged;
- no-trade-structure handling remains unchanged;
- no contextual RR implementation is authorized;
- no Strategy B2 or Strategy C is authorized;
- the current USDJPY/EURUSD 4H reference-candle fallback line remains closed as
  underpowered for the current local slice;
- corpus findings remain separate from executable Strategy A/B behavior unless
  a separate design decision authorizes integration.

This matrix is an evidence-boundary document only. It does not approve any
implementation or design change.

## 4. Evidence-axis definitions

| Axis | Definition | Must remain separate from |
| --- | --- | --- |
| Stop width | The distance of the stop under current mechanics or review framing. | Structural stop validity, RR availability, accepted status, outcomes. |
| Structural stop validity | Whether a stop anchor is structurally valid, questionable, or ambiguous under blinded structural review. | Stop width, RR, target rank, fallback availability, outcomes. |
| RR availability | Whether the current TP and stop relationship satisfies the current RR gates. | Structural stop validity, no-valid-target, no-trade-structure. |
| Target absence | Current Strategy B target search does not identify an eligible left-side target. | Low-RR target availability, stop-width, stop-validity. |
| No-trade-structure | The candidate lacks a valid setup or target structure for Strategy B review. | Target absence, low-RR TP availability, stop-width. |
| Fallback availability | Whether enough reference-candle fallback stop-anchor cases exist for the predeclared diagnostic question. | Structural validity, stop width, target absence, no-trade-structure. |

These axes can overlap in a candidate, but an overlap does not collapse them
into the same evidence category.

## 5. Stop-width versus stop-validity matrix

| Evidence question | Supported by committed docs? | Current interpretation | Needs separate future local-only authorization? |
| --- | --- | --- | --- |
| Is TP1 minimum RR a documented rejection driver? | Yes. The cumulative synthesis and design-gate docs preserve TP1 RR as a major documented rejection footprint. | RR availability is a distinct TP/RR axis. It is not proof of structural stop invalidity. | No for docs-only restatement; yes for new sample review or row-level diagnosis. |
| Can stop width alone prove structural stop invalidity? | No. Current docs explicitly prohibit width-only stop conclusions. | Stop width is a review axis, not a structural label. | Yes, if a future task wants to label cases or compare width against blinded structure. |
| Can structural stop validity be inferred from RR failure? | No. Current docs require stop-anchor separation from RR and width. | RR failure does not establish invalid anchor structure. | Yes, if a future task wants case-level structural labels. |
| Are structurally valid and questionable anchors both documented as overlapping with stop-width and RR concerns? | Yes, at aggregate level from committed local-only diagnostic reports summarized in the cumulative synthesis. | Existing aggregate evidence supports keeping axes separate, not changing rules. | Yes for any new diagnostic expansion or row-level interpretation. |
| Is no-valid-target the same as low-RR TP availability? | No. The taxonomy preservation note keeps target absence distinct. | Absence of an eligible target is not a low-RR target. | Yes, if future work wants to reclassify or review cases. |
| Is no-trade-structure the same as no-valid-target or low-RR TP availability? | No. The taxonomy preservation note keeps invalid structure separate. | Invalid setup or target structure should not be counted as ordinary RR failure. | Yes, if future work wants case-level diagnostic review. |
| Is fallback availability evidence enough to conclude fallback stop validity? | No. The fallback decision and backlog cleanup close the current local-slice line as underpowered. | One reference-candle fallback base case is an availability blocker, not a structural conclusion. | Yes, and only with a separately authorized broader source universe and sample plan. |
| Can any axis currently support Strategy B behavior changes? | No. The design gate, contextual RR checklist, and closure docs keep behavior frozen. | Current evidence supports conservative documentation and future gatekeeping only. | Yes, any behavior proposal would require executive design authorization before automation work. |

## 6. Supported cells from committed docs

Supported by committed docs:

- TP1 RR failure is documented as a major rejection footprint, while TP1 RR
  gates remain frozen.
- Stop-anchor quality is a separate axis from stop width, RR failure, accepted
  status, target rank, and outcome-like fields.
- Aggregate prior diagnostics support preserving the separation between
  structural stop labels and stop-width or RR interpretation.
- No-valid-target / no-left-side-target remains separate from low-RR TP
  availability.
- No-trade-structure remains separate from no-valid-target and low-RR TP
  availability.
- Reference-candle fallback availability remains closed as underpowered for the
  current USDJPY/EURUSD 4H local slice.
- The current fallback closure does not prove reference-candle fallback stops
  are generally invalid.
- Any future design review must use confirmation-time information, avoid
  outcome selection, avoid parameter sweeps, avoid pair-specific fitting, and
  keep corpus findings separate from Strategy B executable behavior.

These cells support evidence separation and guardrails only. They do not support
implementation work.

## 7. Evidence gaps and blocked cells

Evidence gaps or blocked cells:

- case-level stop-width versus structural-validity diagnosis cannot be produced
  from this docs-only issue;
- new structural stop labels require a separate local-only diagnostic
  authorization with Pass A / Pass B separation;
- deciding whether any no-valid-target case should be reclassified requires a
  separately authorized local-only sample review;
- deciding whether any no-trade-structure case belongs in another structural
  taxonomy class requires a separately authorized diagnostic;
- reopening reference-candle fallback work requires a broader source universe,
  sample target, shortfall rules, hidden-field handling, and Git-safe aggregate
  output shape;
- no contextual RR, stop, target, ADX, ATR, lookback, pair, timeframe, or
  management rule can be inferred from this matrix;
- no Strategy B design review can start from outcome-selected examples,
  performance-tuned thresholds, future bars, or live-readiness claims.

Blocked cells should stay blocked until a future issue explicitly authorizes
the source class, diagnostic question, sample design, and Git-safe output.

## 8. Prohibited interpretation shortcuts

Do not use this matrix to:

- treat a wide stop as structurally invalid without blinded structural labels;
- treat RR failure as proof of stop-anchor invalidity;
- treat an accepted or rejected status as structural stop evidence;
- treat target absence as low-RR TP availability;
- treat no-trade-structure as ordinary low-RR TP availability;
- treat the one-case fallback pool as a stable fallback stop-anchor conclusion;
- fill a fallback bucket with nonfallback swing-anchor cases;
- lower, remove, or retune TP1, TP2, or TP1-only RR gates;
- change rank-1 TP1 selection or add farther-target exceptions;
- change stop anchors, stop buffers, stop sanity limits, ADX, ATR, swing width,
  lookback, pair settings, timeframe settings, management, runner behavior,
  configs, tests, or backtest behavior;
- create Strategy B2 or Strategy C;
- import YouTube corpus findings directly into Strategy B behavior;
- use outcome, profit, loss, live-readiness, or money-making language to select
  or justify a rule.

Any future issue asking for one of these shortcuts is not a safe routine
automation task without explicit executive design authorization.

## 9. No Strategy behavior change confirmation

Confirmed:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B TP1, TP2, RR, contextual RR, stop-anchor, stop-buffer, stop
  sanity, ADX, ATR, swing-width, lookback, pair-setting, management, runner,
  config, test, or backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or generated artifact was accessed;
- no stop, RR, target, ADX, ATR, lookback, pair, timeframe, or management rule
  is proposed;
- no implementation proposal is authorized by this matrix;
- no YouTube channel-wide corpus findings are mixed into Strategy B executable
  behavior.

## 10. Guardrail confirmation

Confirmed:

- docs-only evidence matrix;
- committed Markdown reports only;
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
- no profitability, money-making, or trading recommendation claim is made;
- Strategy A/B verification work remains separate from YouTube channel-wide
  corpus work.

## 11. Recommended next bounded task

Recommended next task:

`[codex] Strategy B evidence-gap ledger for design-review gates`

Suggested scope:

- docs-only;
- use committed Strategy B gate, contextual RR, taxonomy, fallback closure, and
  stop-width versus stop-validity docs only;
- maintain a compact ledger of still-blocked Strategy B design-review gates;
- separate docs-only restatements from items requiring future local-only
  diagnostic authorization;
- do not run diagnostics;
- do not access local data or generated artifacts;
- do not change Strategy B behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior.
