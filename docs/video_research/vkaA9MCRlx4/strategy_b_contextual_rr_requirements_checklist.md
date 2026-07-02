# Strategy B Contextual RR Requirements Checklist

## 1. Objective and scope

This checklist defines what a future Strategy B contextual RR proposal would
need to specify before it could enter docs-only review.

Scope:

- use committed repository Markdown reports only;
- preserve the current Strategy B behavior freeze;
- define required proposal fields for any future contextual RR review;
- keep contextual RR questions separate from stop-anchor validity, rejection
  taxonomy classes, outcome selection, source-specific fitting, and
  corpus-to-Strategy translation;
- identify evidence gates and insufficient evidence examples;
- recommend one bounded docs-only next task.

Out of scope:

- no contextual RR value, threshold, formula, or implementation rule is
  proposed;
- no diagnostic is run;
- no local OHLC data or generated Strategy B artifact is accessed;
- no chart packet, worksheet, mapping, reveal table, sample row, CSV, JSON,
  image, `data/`, or `results/` is created;
- no market-data API, broker API, live system, order placement, auto-trading,
  or live-trading access occurs;
- no Strategy A/B/B2/C behavior, code, parameter, config, test, runner, or
  backtest behavior is changed;
- no Strategy B2 or Strategy C is created;
- no parameter optimization is performed;
- no profitability, live-readiness, money-making, or trading-recommendation
  claim is made.

## 2. Source docs used

Committed repository docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_design_review_gate_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_no_valid_target_no_trade_structure_taxonomy_preservation.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_remaining_open_items_triage.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_cumulative_synthesis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market-data APIs, broker/live
systems, YouTube sources, DownSub, captions, subtitles, transcript bodies,
caption URLs, comments, live chat, community posts, downloaded media, ASR, or
external sources were used for this checklist.

## 3. Current RR freeze state

The current Strategy B RR state remains frozen:

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
- no Strategy B2 or Strategy C is authorized.

The committed TP1 decision closure keeps the current RR gates frozen until a
future review can satisfy stronger evidence requirements, use only
confirmation-time information, avoid parameter sweeps, preserve stop and target
taxonomy separation, and avoid outcome or profitability selection.

## 4. Required contextual RR proposal fields

A future contextual RR proposal would need to specify all fields below before
review. Missing fields should stop the review before any implementation,
diagnostic, or local artifact access is considered.

| Field | Required content | Hard-stop condition |
| --- | --- | --- |
| Proposal objective | The exact review question and why contextual RR is being considered as a design-review topic, not as an implementation request. | The proposal asks to change RR gates directly. |
| Mechanical rule boundary | A plain-language description of the proposed rule surface without numeric values, tuning, or executable behavior. | The proposal starts with thresholds or code changes. |
| Confirmation-time inputs | The complete list of inputs available at or before Strategy B confirmation. | Any required future candle, accepted status, result, profit, loss, or post-confirmation movement blocks review. |
| Fixed taxonomy boundary | How no-valid-target, no-trade-structure, low-RR TP availability, stop-width, stop-validity, and fallback availability remain separate. | Rejection classes are merged to make contextual RR easier to justify. |
| Stop-anchor separation | How stop-anchor structural validity remains independent from RR, stop width, accepted status, and outcomes. | RR failure or stop width is treated as proof of stop invalidity. |
| TP target boundary | How TP1 rank, farther-target exceptions, TP2 handling, and target absence remain frozen unless separately reviewed. | Contextual RR is used to smuggle in target-rank or farther-target changes. |
| Evidence source boundary | The committed docs, aggregate diagnostics, or separately authorized future source classes that would support review. | The proposal needs raw rows, chart packets, worksheets, mappings, CSV/JSON, `data/`, or `results/` in Git. |
| Sample and repetition requirement | What independent repeated evidence would be required before a design memo could consider a rule. | One diagnostic, one case bucket, or one manual-review cycle is treated as enough. |
| Ambiguity handling | How second-review disagreement, ambiguous structural labels, and shortfall states are handled before RR interpretation. | Ambiguous cases are counted as implementation support. |
| Anti-optimization controls | How the proposal avoids threshold search, pair-specific fitting, timeframe fitting, and performance-tuned selection. | Values are chosen by trying alternatives or selecting better-performing cases. |
| Corpus separation | Whether any channel-wide corpus finding is being used, and the separate design decision that would authorize that link. | Corpus themes are imported directly into executable Strategy B behavior. |
| Git-safe output shape | The exact Markdown-only, aggregate-only output expected from review. | Review requires committing raw/generated artifacts or source text. |

Passing this field checklist would not approve contextual RR. It would only
make a future docs-only design memo reviewable.

## 5. Evidence gates

A future contextual RR design review should not start unless all applicable
evidence gates are satisfied:

| Gate | Required evidence | Not enough |
| --- | --- | --- |
| Repeated independent evidence | Multiple separately authorized samples or committed aggregate diagnostics repeat the same review-relevant pattern. | The documented `tp1_below_min_rr` footprint alone. |
| Confirmation-time availability | Every proposed input is known at confirmation time or earlier. | Future bars, later outcome candles, accepted status, or final result data. |
| Low ambiguity | Second-review ambiguity is low enough that the proposed rule surface is not built on disputed labels. | Unresolved structural disagreement or unreviewed labels. |
| Taxonomy preservation | Target absence, invalid structure, low-RR TP availability, stop width, stop validity, and fallback availability stay separately auditable. | One combined rejection bucket. |
| Stop/RR separation | Structural stop labels are locked before RR or width interpretation. | RR failure treated as stop-anchor invalidity. |
| No tuning | The proposal can be stated without trying many RR values, stop values, ADX values, ATR values, lookbacks, pairs, or timeframes. | Threshold search or source-specific fitting. |
| Git-safe review | Evidence can be summarized as aggregate Markdown without forbidden artifacts. | Need to commit local rows, generated outputs, raw source bodies, or media. |

If any gate fails, the contextual RR topic remains a research gap or planning
item, not a Strategy B design-review candidate.

## 6. Insufficient evidence examples

The following examples are insufficient for contextual RR review:

- the current TP1 minimum RR rejection footprint by itself;
- the current one-case reference-candle fallback bucket;
- repeated review of the same underpowered fallback pool;
- stop width without locked structural stop labels;
- RR failure without an eligible target and valid trade structure distinction;
- no-valid-target cases treated as if a target existed;
- no-trade-structure cases treated as ordinary low-RR cases;
- rank-1 TP1 discomfort without repeated low-ambiguity evidence;
- later-rank examples without a separate TP target-ranking review;
- outcome-selected examples;
- pair-specific or timeframe-specific examples selected after seeing results;
- corpus themes that have not gone through a separate Strategy/corpus mismatch
  decision;
- any evidence path requiring committed raw rows, chart packets, worksheets,
  mappings, images, CSV/JSON, raw transcripts, subtitle full text, caption
  URLs, `data/`, or `results/`.

These examples may justify future diagnostic planning only when a separate
issue authorizes the source boundary and Git-safe output shape.

## 7. Prohibited shortcuts

Do not use contextual RR language to authorize any shortcut below:

- lowering, removing, or retuning TP1 minimum RR;
- lowering, removing, or retuning TP2 minimum RR or TP1-only minimum RR;
- adding a contextual RR threshold;
- implementing a farther-target exception;
- changing rank-1 TP1 selection;
- changing stop anchors, stop buffers, or stop sanity limits;
- treating wide stops as structurally invalid without blinded structural
  labels;
- accepting shallower stops only to improve RR;
- filling a fallback bucket with nonfallback swing-anchor cases;
- using outcome, profit, loss, accepted status, or live-readiness to select a
  rule;
- tuning ADX, ATR, swing width, lookback, pair settings, or timeframe settings;
- creating Strategy B2 or Strategy C;
- importing YouTube corpus findings directly into Strategy B behavior;
- committing raw/generated artifacts or raw source text.

Any future issue that asks for one of these shortcuts needs an explicit
executive design decision and is not a safe routine automation task.

## 8. No Strategy behavior change confirmation

Confirmed:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B TP1, TP2, RR, contextual RR, stop-anchor, stop-buffer, stop
  sanity, ADX, ATR, swing-width, lookback, pair-setting, management, runner,
  config, test, or backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or generated artifact was accessed;
- no contextual RR value, threshold, formula, or implementation rule is
  proposed;
- no implementation proposal is authorized by this checklist;
- no YouTube channel-wide corpus findings are mixed into Strategy B executable
  behavior.

This checklist is a requirements boundary for future docs-only review, not an
approval to change Strategy B.

## 9. Guardrail confirmation

Confirmed:

- docs-only contextual RR requirements checklist;
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

## 10. Recommended next bounded task

Recommended next task:

`[codex] Strategy B stop-width versus stop-validity evidence matrix`

Suggested scope:

- docs-only;
- use committed Strategy B TP1, stop-anchor, local diagnostic, fallback,
  taxonomy, design-review gate, and contextual RR requirements docs only;
- distinguish stop width, structural stop validity, RR availability, target
  absence, and fallback availability as separate evidence axes;
- identify which cells are supported by committed aggregate docs and which
  would require separate local-only diagnostic authorization;
- do not run diagnostics;
- do not access local data or generated artifacts;
- do not propose Strategy B behavior, code, parameter, config, test, runner, or
  backtest changes.
