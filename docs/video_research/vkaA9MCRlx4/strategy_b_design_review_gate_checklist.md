# Strategy B Design Review Gate Checklist

## 1. Objective and scope

This checklist defines the evidence threshold required before any future
Strategy B design review may consider rule proposals.

Scope:

- use committed repository Markdown reports only;
- preserve the current Strategy B behavior freeze;
- define entry gates for any future docs-only design review;
- separate TP1 RR, stop-anchor structural quality, rejection taxonomy, fallback
  availability, and corpus-to-Strategy translation;
- define insufficient evidence, prohibited shortcuts, and executive-decision
  triggers;
- recommend one bounded next docs-only task.

Out of scope:

- no diagnostic run;
- no local OHLC data or generated artifact access;
- no chart packet, worksheet, mapping, reveal table, sample row, CSV, JSON,
  image, `data/`, or `results/` creation;
- no market-data API, broker API, live system, order placement, auto-trading, or
  live-trading access;
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

- `docs/video_research/vkaA9MCRlx4/strategy_b_no_valid_target_no_trade_structure_taxonomy_preservation.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_remaining_open_items_triage.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_backlog_cleanup_after_fallback_closure.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_fallback_availability_decision_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_cumulative_synthesis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market-data APIs, broker/live systems,
YouTube sources, DownSub, captions, subtitles, transcript bodies, caption URLs,
comments, live chat, community posts, downloaded media, ASR, or external sources
were used for this checklist.

## 3. Current frozen state

The current Strategy B state remains frozen:

- rank-1 TP1 selection remains unchanged;
- TP1 minimum RR remains unchanged;
- TP2 minimum RR remains unchanged;
- TP1-only minimum RR remains unchanged;
- stop-anchor logic remains unchanged;
- stop-buffer logic remains unchanged;
- stop sanity limits remain unchanged;
- ADX, ATR, swing-width, lookback, pair-setting, management, runner, config,
  test, and backtest behavior remain unchanged;
- no-left-side / no-valid-target rejection behavior remains unchanged;
- no-trade-structure handling remains unchanged;
- no Strategy B2 or Strategy C is authorized;
- the current USDJPY/EURUSD 4H reference-candle fallback line remains closed as
  underpowered for the current local slice;
- corpus findings remain separate from executable Strategy A/B behavior unless
  a separate design decision authorizes integration.

Frozen means no code, parameter, config, test, runner, backtest, or rule-change
proposal may proceed from the current evidence base.

## 4. Design-review entry gates

A future Strategy B design review may be considered only if all applicable gates
below are satisfied before the design review starts.

| Gate | Required evidence before design review | Failure state |
| --- | --- | --- |
| Repeated independent evidence | The same finding repeats across separately authorized samples or committed aggregate diagnostics. | A single diagnostic, one fallback case, or one manual-review cycle is insufficient. |
| Low second-review ambiguity | Second-review or adjudication leaves few unresolved structural disagreements for the proposed rule surface. | Ambiguous, disputed, or unreviewed labels remain diagnostic material only. |
| Confirmation-time information only | The proposed rule can be stated using information available at confirmation time or earlier. | Any need for future bars, outcome candles, accepted status, or later profitability information blocks design review. |
| No outcome selection | Evidence selection does not depend on outcome, profit, loss, later favorable movement, or performance. | Outcome-selected examples cannot support a mechanical Strategy B rule. |
| No parameter sweep | The proposal does not choose thresholds by trying many values or selecting a performance-tuned setting. | Threshold search, RR tuning, ADX tuning, ATR tuning, pair tuning, or lookback tuning blocks design review. |
| No pair-specific tuning | The proposed rule is not tailored only to USDJPY, EURUSD, one timeframe, or one local slice unless a separate design decision authorizes that boundary. | Pair/timeframe-specific fitting remains outside safe design-review scope. |
| Taxonomy separation | No-valid-target, no-trade-structure, low-RR TP availability, stop-width, stop-validity, and fallback availability remain separate unless a future diagnostic explicitly authorizes a merge rule. | Collapsed rejection buckets block design review. |
| TP1 RR separation | TP1 minimum RR behavior is treated as an RR/target-geometry question, not proof of structural stop invalidity. | Treating RR failure as stop-anchor failure blocks design review. |
| Stop-anchor separation | Structural stop validity is reviewed independently from stop width, RR, accepted status, and outcome-like fields. | Width-only or RR-only stop conclusions block design review. |
| Fallback availability | Reference-candle fallback proposals use a sufficient predeclared fallback case pool, not the current one-case blocker. | The current fallback line remains closed as underpowered. |
| Corpus-line separation | Channel-wide corpus findings have gone through a separate mismatch-analysis decision before being considered for Strategy A/B behavior. | Corpus themes cannot directly become executable Strategy B rules. |
| Git-safe evidence shape | The supporting evidence can be summarized in aggregate Markdown without raw/generated artifacts. | Any need to commit rows, CSV/JSON, chart packets, mappings, images, or raw source text blocks design review. |

Passing these gates does not approve implementation. It only permits a future
docs-only design memo to consider a specific mechanical proposal.

## 5. Insufficient evidence examples

The following are insufficient for Strategy B design review:

- the documented `tp1_below_min_rr` rejection footprint by itself;
- the current one-case reference-candle fallback bucket;
- another diagnostic over the same one-case fallback pool;
- a single manual-review sample without repeated independent evidence;
- cases where second-review ambiguity remains high;
- examples selected because they later worked or failed;
- visual preference without a confirmation-time mechanical rule;
- stop width alone;
- RR failure alone;
- accepted status alone;
- post-confirmation outcome candles;
- no-valid-target cases treated as if an eligible target existed;
- no-trade-structure cases treated as ordinary low-RR cases;
- corpus themes that have not gone through a separate Strategy/corpus mismatch
  analysis and design decision;
- any evidence requiring committed raw market data, generated rows, chart
  packets, worksheets, mappings, images, CSV/JSON, `data/`, or `results/`.

These examples may remain useful as diagnostic planning inputs, but they do not
clear the design-review gate.

## 6. Prohibited shortcuts

Do not use any shortcut below to move from diagnostic evidence to Strategy B
rule proposals:

- lower, remove, or retune TP1 minimum RR to increase accepted candidates;
- lower, remove, or retune TP2 minimum RR or TP1-only minimum RR;
- implement a farther-target exception from limited later-rank examples;
- replace rank-1 TP1 selection without repeated low-ambiguity evidence;
- accept shallower stops only to improve RR;
- treat a wide stop as structurally invalid without locked structural labels;
- treat a structurally valid stop as acceptable because outcome later worked;
- fill a fallback bucket with nonfallback swing-anchor cases;
- generalize from the current one-case fallback pool;
- tune ADX, ATR, swing width, lookback, pair settings, stop buffers, or stop
  sanity limits;
- convert corpus doctrine directly into Strategy B code;
- create Strategy B2 or Strategy C;
- use outcome, profitability, live-readiness, or money-making language to select
  or justify a rule.

Any future issue asking for one of these shortcuts is not a safe automation task
unless it includes an explicit executive design decision and a narrow authorized
scope.

## 7. Executive-decision triggers

The following require executive decision before any automation work proceeds:

- authorizing Strategy B behavior, code, parameter, config, test, runner, or
  backtest changes;
- authorizing Strategy B2 or Strategy C;
- authorizing parameter optimization or performance-tuned threshold search;
- authorizing market-data API, broker API, live system, order placement,
  auto-trading, or live-trading work;
- authorizing a broader source universe for fallback diagnostics;
- authorizing local OHLC data or generated artifact access;
- authorizing a merge of rejection taxonomy categories into implementation
  behavior;
- authorizing direct integration of YouTube channel-wide corpus findings into
  executable Strategy A/B behavior;
- requiring raw/generated artifacts, row-level details, chart packets,
  worksheets, mappings, images, CSV/JSON, `data/`, or `results/` in Git;
- making or relying on profitability, live-readiness, money-making, or trading
  recommendation claims.

If any trigger appears without explicit authorization, stop without changing
files.

## 8. Allowed docs-only next steps

Allowed next steps remain planning, synthesis, and guardrail work only:

- maintain a docs-only evidence-gap ledger for Strategy B design-review gates;
- draft a docs-only contextual RR design requirements checklist that does not
  propose a threshold;
- draft a docs-only stop-width versus stop-validity evidence matrix;
- draft a docs-only no-valid-target / no-trade-structure diagnostic
  authorization template;
- draft a docs-only Strategy A/B versus corpus doctrine mismatch-analysis plan
  after the corpus line materially advances;
- update operations checklists that keep raw/generated artifacts outside Git.

Each allowed next step must use committed repository docs only unless a future
issue explicitly authorizes a different source class.

## 9. No Strategy behavior change confirmation

Confirmed:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B TP1, TP2, RR, stop-anchor, stop-buffer, stop sanity, ADX, ATR,
  swing-width, lookback, pair-setting, management, runner, config, test, or
  backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or generated artifact was accessed;
- no implementation proposal is authorized by this checklist;
- no YouTube channel-wide corpus findings are mixed into Strategy B executable
  behavior.

This checklist is a gate for future docs-only review, not an approval to change
Strategy B.

## 10. Guardrail confirmation

Confirmed:

- docs-only design-review gate checklist;
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

`[codex] Strategy B contextual RR requirements checklist`

Suggested scope:

- docs-only;
- use committed Strategy B TP1, stop-anchor, closure, triage, taxonomy, and
  design-review gate docs only;
- define what any future contextual RR proposal would need to specify before it
  could be reviewed;
- keep RR requirements separate from parameter tuning, pair-specific tuning,
  outcome selection, stop-anchor validity, and corpus-line translation;
- do not run diagnostics;
- do not access local data or generated artifacts;
- do not change Strategy B behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior.
