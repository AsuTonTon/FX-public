# Strategy B TP1 / Stop-Anchor Remaining Open Items Triage

## 1. Objective and scope

This note triages the remaining Strategy B TP1 / stop-anchor research items
after the current USDJPY/EURUSD 4H reference-candle fallback diagnostic line was
closed as underpowered.

Scope:

- use committed repository Markdown reports only;
- preserve the current fallback closure and Strategy B behavior freeze;
- classify remaining items into docs-only triage-ready, requiring separate
  local-only diagnostic authorization, deferred / blocked, and not allowed
  without executive decision;
- cover TP1 RR behavior, stop-anchor structural quality, no-valid-target /
  no-trade-structure taxonomy, future docs-only design review conditions, and
  corpus-separation constraints;
- recommend one bounded next task.

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

- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_backlog_cleanup_after_fallback_closure.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_fallback_availability_decision_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_cumulative_synthesis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market-data APIs, broker/live systems,
YouTube sources, DownSub, captions, subtitles, transcript bodies, caption URLs,
comments, live chat, community posts, downloaded media, ASR, or external sources
were used for this note.

## 3. Current closed/deferred/open state recap

Closed for the current USDJPY/EURUSD 4H local slice:

- another fallback-only blinded Pass A / Pass B diagnostic using the same
  one-case reference-candle fallback pool;
- filling a fallback bucket with nonfallback swing-anchor cases;
- using the one-case fallback result to support Strategy B behavior changes;
- treating the current fallback bucket as a stable structural stop-anchor
  conclusion.

The controlling closure state is:

`current_usdjpy_eurusd_4h_reference_candle_fallback_diagnostic_line_closed_as_underpowered`

Deferred:

- broader fallback availability review using additional pairs, timeframes, date
  ranges, or artifact classes;
- future fallback-only blinded diagnostics from a broader universe;
- independent second-review evidence for fallback cases;
- any Strategy B design review involving fallback stop anchors.

Still open outside the closed fallback line:

- TP1 minimum RR behavior as a separate diagnostic and design-review question;
- stop-anchor structural quality outside the reference-candle fallback class;
- stop-width versus stop-validity distinction;
- no-valid-target / no-left-side-target taxonomy;
- no-trade-structure taxonomy;
- future docs-only Strategy B design review conditions;
- Strategy/corpus separation for any later doctrine mismatch analysis.

## 4. Remaining item triage table

| Item | Current status | Triage class | Rationale | Next safe handling |
| --- | --- | --- | --- | --- |
| Current USDJPY/EURUSD 4H reference-candle fallback line | Closed as underpowered | Deferred / blocked | The committed broader availability review found one fallback candidate against a four-base-case target. | Keep closed unless a later issue authorizes a broader source universe and sample plan. |
| TP1 minimum RR behavior | Open | Docs-only triage-ready | Current docs show TP1 minimum RR dominates rejection counts, but that fact does not authorize changing RR gates. | Create a docs-only evidence-threshold note for what a future TP1 RR design review would need. |
| Rank-1 TP1 versus farther-target exception | Open but frozen | Docs-only triage-ready | Prior manual review and second review did not support a broad later-rank exception. | Keep as design-threshold planning only; do not propose an implementation rule. |
| Low-R-but-structural TP classification | Open | Requires separate local-only diagnostic authorization | The question depends on blinded labels over cases, not committed docs alone. | Require a future issue with source classes, sample design, hidden fields, and aggregate output shape. |
| Stop-anchor structural quality outside fallback cases | Open | Requires separate local-only diagnostic authorization | Structural-valid, questionable, and ambiguous stop anchors require Pass A / Pass B separation. | Use the local diagnostics runbook only after explicit authorization. |
| Stop-width versus stop-validity distinction | Open | Requires separate local-only diagnostic authorization | Width and structural validity must be separated before stop-distance fields are revealed. | Keep as future diagnostic work with locked Pass A labels before Pass B interpretation. |
| No-valid-target / no-left-side-target taxonomy | Open | Docs-only triage-ready | Existing docs already require this class to remain separate from low-RR failures. | Add a docs-only taxonomy preservation note before any diagnostic issue is drafted. |
| No-trade-structure taxonomy | Open | Docs-only triage-ready | Current backlog requires invalid setup or target structure to remain distinct from TP1 RR. | Define docs-only classification boundaries and stop conditions for future review. |
| Future Strategy B design review conditions | Open but gated | Docs-only triage-ready | The closure note lists evidence thresholds and confirmation-time requirements. | Draft a design-review gate checklist; do not change code or parameters. |
| YouTube corpus-to-Strategy translation | Deferred | Deferred / blocked | Corpus findings must not be mixed into executable Strategy B without a separate design decision. | Wait for a separate mismatch-analysis issue after corpus work materially advances. |
| Strategy B2 or Strategy C creation | Not authorized | Not allowed without executive decision | Current closure and guardrails explicitly forbid variant creation from this evidence. | Do not start. |
| RR, ADX, ATR, swing-width, lookback, or stop-threshold tuning | Not authorized | Not allowed without executive decision | Parameter tuning would be optimization and is outside the issue scope. | Do not start. |

## 5. Docs-only next candidates

The remaining docs-only candidates are planning and evidence-boundary tasks, not
implementation tasks:

1. TP1 RR design-review evidence threshold note.
   - Summarize what evidence would be needed before any contextual RR or TP1 RR
     design memo could be considered.
   - Preserve fixed RR gates until a separate design memo authorizes a specific
     mechanical rule.
2. No-valid-target / no-trade-structure taxonomy preservation note.
   - Define the current separation between target absence, invalid trade
     structure, low-RR TP availability, and fallback stop-anchor availability.
   - State stop conditions for any future diagnostic that begins collapsing
     these classes.
3. Future Strategy B design-review gate checklist.
   - Restate required conditions: repeated independent evidence, low second-
     review ambiguity, confirmation-time information only, no outcome selection,
     no parameter sweep, no pair-specific tuning, and corpus-line separation.
4. Corpus-to-Strategy mismatch analysis plan.
   - Plan only the conditions under which channel doctrine could later be
     compared with Strategy A/B mechanics.
   - Do not import corpus findings into Strategy B rules.

The strongest next docs-only candidate is the no-valid-target /
no-trade-structure taxonomy preservation note, because it is already supported
by committed closure/backlog docs and does not require local data or generated
artifact access.

## 6. Items requiring separate local-only diagnostic authorization

The following items require a separate future issue before any local read,
diagnostic run, chart packet creation, worksheet use, hidden mapping, reveal
table, row inspection, or generated artifact inspection:

- low-R-but-structural TP classification;
- micro-structure TP1 classification;
- no-left-side/no-valid-target sample review;
- no-trade-structure blinded review;
- nonfallback stop-anchor structural-quality diagnostic;
- stop-width versus stop-validity diagnostic;
- broader fallback availability review;
- future fallback-only diagnostic from a broader source universe;
- independent second-review evidence for fallback cases;
- future manual-review sample design that uses local-only artifacts.

A future authorization issue must state the diagnostic question, allowed
source classes, local-only boundary, sample buckets, shortfall rules, hidden
fields, Pass A / Pass B handling, Git-safe aggregate output format, and hard-stop
conditions.

## 7. Items not allowed without executive decision

The following are not allowed from the current evidence base:

- changing Strategy B TP1 ranking;
- lowering, removing, or retuning TP1 minimum RR;
- changing TP2 minimum RR or TP1-only minimum RR;
- implementing a farther-target exception;
- implementing contextual RR;
- changing stop anchors, stop buffers, stop sanity limits, ATR settings, ADX
  settings, swing width, swing lookback, pair settings, runner behavior, tests,
  configs, or backtest behavior;
- creating Strategy B2 or Strategy C;
- running parameter optimization;
- using outcomes, money-making claims, or live-readiness claims to select a
  rule;
- mixing YouTube channel-wide corpus findings into executable Strategy B
  behavior without a separate design decision;
- committing raw market data, normalized CSVs, generated rows, chart packets,
  worksheets, mappings, images, JSON artifacts, `data/`, `results/`, raw
  transcripts, subtitle full text, raw TXT/SRT/VTT caption files, caption URLs,
  downloaded media, credentials, tokens, or secrets.

## 8. No Strategy behavior change confirmation

Confirmed:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B TP1, TP2, RR, stop-anchor, stop-buffer, stop sanity, ADX, ATR,
  swing-width, lookback, pair-setting, management, runner, config, test, or
  backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or generated artifact was accessed;
- no implementation proposal is authorized by this note;
- no YouTube channel-wide corpus findings are mixed into Strategy B executable
  behavior.

## 9. Guardrail confirmation

Confirmed:

- docs-only triage note;
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

`[codex] Strategy B no-valid-target / no-trade-structure taxonomy preservation note`

Suggested scope:

- docs-only;
- use committed Strategy B TP1, stop-anchor, fallback closure, and diagnostic
  backlog docs only;
- define the current boundaries between no-left-side/no-valid-target,
  no-trade-structure, low-RR TP availability, stop-width, stop-validity, and
  fallback stop-anchor availability;
- state which categories are docs-only taxonomy questions and which would
  require separate local-only diagnostic authorization;
- preserve the Strategy B behavior freeze;
- do not run diagnostics;
- do not access local data or generated artifacts;
- do not change Strategy B behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior.
