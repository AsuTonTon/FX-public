# Strategy B No-Valid-Target / No-Trade-Structure Taxonomy Preservation

## 1. Objective and scope

This note preserves the Strategy B rejection and diagnostic taxonomy around
no-valid-target and no-trade-structure cases after the current USDJPY/EURUSD 4H
reference-candle fallback line was closed as underpowered.

Scope:

- use committed repository Markdown reports only;
- define category boundaries among no-valid-target, no-trade-structure,
  low-RR TP availability, stop-width, stop-validity, and fallback availability;
- state why these categories must not be collapsed into one rejection bucket;
- classify which taxonomy items are docs-only versus which require separate
  future diagnostic authorization;
- preserve the current Strategy B behavior freeze;
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
  claim.

## 2. Source docs used

Committed repository docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_remaining_open_items_triage.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_backlog_cleanup_after_fallback_closure.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_fallback_availability_decision_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_cumulative_synthesis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_memo.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market-data APIs, broker/live systems,
YouTube sources, DownSub, captions, subtitles, transcript bodies, caption URLs,
comments, live chat, community posts, downloaded media, ASR, or external sources
were used for this note.

## 3. Category boundary definitions

| Category | Boundary definition | Must remain separate from |
| --- | --- | --- |
| No-valid-target / no-left-side-target | The current Strategy B target-search process does not identify an eligible left-side target for the candidate under the current rule set. | Low-RR TP availability, stop-width, stop-validity, fallback availability. |
| No-trade-structure | The candidate lacks a valid setup or target structure for Strategy B review, independent of whether a later TP or stop diagnostic might be interesting. | No-valid-target, low-RR TP availability, stop-width, fallback availability. |
| Low-RR TP availability | A target may exist, but the current TP and stop relationship does not satisfy the current minimum RR gate. | No-valid-target, no-trade-structure, stop-anchor validity. |
| Stop-width | The stop distance is wide under current mechanics or review framing. | Structural stop-validity, low-RR TP availability, no-valid-target. |
| Stop-validity | The stop anchor is structurally valid, questionable, or ambiguous under a blinded structural review. | Stop-width, accepted status, RR outcome, target rank, fallback availability. |
| Fallback availability | The reference-candle fallback stop-anchor bucket has enough or insufficient cases for the predeclared diagnostic question. | Stop-validity, stop-width, no-valid-target, no-trade-structure. |

These categories describe different failure or diagnostic axes. A candidate can
touch more than one axis, but the axes should not be merged unless a later issue
explicitly authorizes a diagnostic that defines the merge rule, source boundary,
sample design, hidden fields, and Git-safe output shape.

## 4. Category conflation risks

Collapsing these categories would create several review risks:

| Conflation | Risk |
| --- | --- |
| No-valid-target into low-RR TP availability | Treats absence of an eligible target as if a target existed but failed RR, which would distort TP1 evidence thresholds. |
| No-trade-structure into no-valid-target | Hides the distinction between invalid setup structure and target-search absence. |
| Low-RR TP availability into stop-validity | Turns an RR gate failure into a structural stop conclusion without blinded Pass A review. |
| Stop-width into stop-validity | Treats distance as proof of structural invalidity before separating width from anchor quality. |
| Fallback availability into stop-validity | Generalizes from an underpowered reference-candle fallback pool as if it were a stable structural stop finding. |
| Any of the above into implementation evidence | Creates pressure to change Strategy B behavior without the required design decision, diagnostic authorization, or evidence threshold. |

The current docs support preserving separation, not simplifying rejection
labels into a single bucket.

## 5. Docs-only taxonomy decisions

The following decisions are docs-only and can be preserved without any local
data read or diagnostic run:

- no-valid-target / no-left-side-target remains a distinct taxonomy item;
- no-trade-structure remains a distinct taxonomy item;
- low-RR TP availability remains a TP/RR evidence item, not a structural stop
  conclusion;
- stop-width remains separate from structural stop-validity;
- fallback availability remains an availability and sample-power question for
  the current reference-candle fallback line;
- the current USDJPY/EURUSD 4H fallback line remains closed as underpowered for
  the current local slice;
- the existing Strategy B TP1, TP2, RR, stop-anchor, stop-buffer, stop sanity,
  ADX, ATR, swing-width, lookback, pair-setting, runner, config, test, and
  backtest behavior remains frozen.

These decisions do not add labels to generated artifacts and do not change any
Strategy B implementation behavior.

## 6. Items requiring separate diagnostic authorization

The following require a future issue before any local read, diagnostic run,
chart packet, worksheet, mapping, reveal table, row inspection, or generated
artifact inspection:

- reviewing no-valid-target / no-left-side-target examples as a case sample;
- reviewing no-trade-structure examples under blinded labels;
- deciding whether any no-valid-target case is actually low-RR TP availability;
- deciding whether any no-trade-structure case should move into a different
  structural taxonomy class;
- diagnosing low-R-but-structural TP cases;
- diagnosing stop-width versus structural stop-validity;
- diagnosing nonfallback stop-anchor structural quality;
- reopening reference-candle fallback work using a broader source universe;
- creating any independent second-review evidence from local-only artifacts.

A future diagnostic authorization issue must state the diagnostic question,
allowed source classes, local-only boundary, sample buckets, shortfall rules,
hidden fields, Pass A / Pass B handling, Git-safe aggregate output format, and
hard-stop conditions.

## 7. Hard-stop conditions

Stop instead of changing files or opening a PR if a future task requires any of
the following without explicit authorization:

- local OHLC data access;
- generated Strategy B artifact access;
- raw row, chart packet, worksheet, mapping, reveal table, image, CSV, JSON,
  `data/`, or `results/` access or creation;
- market-data API, broker API, live system, order placement, auto-trading, or
  live-trading access;
- YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
  live-chat, community-post, downloaded-media, or ASR access;
- Strategy B behavior, code, parameter, config, test, runner, or backtest
  changes;
- Strategy B2 or Strategy C creation;
- parameter optimization;
- profitability, live-readiness, money-making, or trading-recommendation
  claims;
- mixing YouTube channel-wide corpus findings into executable Strategy B
  behavior without a separate design decision.

If a task asks to collapse taxonomy categories into implementation behavior, it
requires an executive design decision and is not a safe automation task.

## 8. No Strategy behavior change confirmation

Confirmed:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B TP1, TP2, RR, stop-anchor, stop-buffer, stop sanity, ADX, ATR,
  swing-width, lookback, pair-setting, management, runner, config, test, or
  backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or generated artifact was accessed;
- no taxonomy decision in this note authorizes implementation work;
- no YouTube channel-wide corpus findings are mixed into Strategy B executable
  behavior.

The current Strategy B decision, closure, triage, fallback, and local
diagnostics guardrail documents remain controlling.

## 9. Guardrail confirmation

Confirmed:

- docs-only taxonomy preservation note;
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

`[codex] Strategy B docs-only design-review gate checklist`

Suggested scope:

- docs-only;
- use committed Strategy B TP1, stop-anchor, fallback closure, remaining-items
  triage, and taxonomy preservation docs only;
- define the evidence threshold before any future Strategy B design review can
  consider rule proposals;
- require confirmation-time information only, no outcome selection, no parameter
  sweep, no pair-specific tuning, and corpus-line separation;
- do not run diagnostics;
- do not access local data or generated artifacts;
- do not change Strategy B behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior.
