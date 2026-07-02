# Strategy B TP1 / Stop-Anchor Follow-Up Diagnostic Backlog

## 1. Objective and scope

This is a docs-only diagnostic backlog for future Strategy B TP1 and stop-anchor research.

Scope:

- define future diagnostic work items only
- preserve the Strategy B TP1 decision memo's current-behavior freeze
- separate TP1, stop-anchor, RR, no-valid-target, no-trade, and corpus-translation questions before any future design proposal
- keep all raw artifacts local-only

Out of scope:

- no implementation approval
- no Strategy B rule change
- no parameter change
- no config or test change
- no Strategy B2
- no Strategy C
- no backtest
- no optimization
- no profitability claim
- no broker/API/live-trading/execution implication

## 2. Decision memo carry-forward

The Strategy B TP1 decision memo decided:

- keep Strategy B TP1 selection unchanged for now
- do not implement a later-rank exception yet
- do not lower or remove TP1 min RR yet
- do not change stop logic yet
- do not create Strategy B2 yet
- preserve no-valid-target / no-trade rejections as separate classes from low-RR cases
- separate low-R-but-structural TP from micro-structure TP in future diagnostics
- treat stop-anchor quality as a separate decision path
- do not approve implementation

Future work from this point is diagnostic only unless a later docs-only design memo explicitly changes scope.

## 3. Backlog principles

Backlog principles:

- Preserve current Strategy B behavior until stronger evidence exists.
- Separate diagnostic categories before any design proposal.
- Avoid parameter tuning.
- Avoid outcome/profitability-driven selection.
- Keep raw artifacts local-only.
- Keep YouTube corpus doctrine separate from direct implementation unless separately specified.
- Distinguish structural validity from RR acceptability.
- Use only information available at confirmation time when defining future mechanical criteria.
- Keep no-valid-target and no-trade-structure cases separate from low-RR cases.
- Treat stop-anchor quality as its own diagnostic path rather than a hidden subcase of TP1 RR failure.

## 4. Diagnostic backlog table

| ID | Topic | Research question | Inputs needed | Git-safe output | Implementation allowed? | Priority | Blocking dependency | Stop condition |
|---|---|---|---|---|---|---|---|---|
| B-TP1-FU-01 | Low-R-but-structural TP classification | How often does low-R TP1 appear structurally meaningful versus merely local/noisy? | Existing aggregate docs; future local-only blinded review labels; no raw rows in Git. | Aggregate label-count report separating `low_rr_but_structural_tp` from other RR failure labels. | No | High | Fixed review labels and outcome-blinded sample protocol. | Stop if labels require outcome, profit, future bars, or pair/time leakage. |
| B-TP1-FU-02 | Micro-structure TP1 classification | Can micro-structure TP1 be defined mechanically without hindsight? | Blinded chart windows; visible entry/TP ranks; existing TP1 structural label definitions. | Docs-only definition candidates and ambiguity count summary. | No | High | More examples where TP1 is labeled `tp1_minor_local_swing`, `tp1_inside_noise`, or `tp1_near_entry_micro_structure`. | Stop if the definition depends on visual discretion that cannot be stated before seeing outcomes. |
| B-TP1-FU-03 | No-valid-target / no-left-side-target preservation | Should no-valid-target cases remain hard rejects? | Future local-only sample of `no_left_side_tp1` cases; chart windows; second-review outcomes. | Aggregate report confirming whether no-valid-target remains separate from TP1 RR failure. | No | High | Enough no-left-side/no-valid-target cases in a fixed sample. | Stop if target absence is confused with low-RR target availability. |
| B-TP1-FU-04 | No-trade-structure separation | Should structurally invalid setup/target contexts be classified separately from TP1 RR failures? | Blinded review labels for `no_trade_structure`; corpus notes on dirty/range/invalid structure. | Docs-only taxonomy for no-trade-structure versus valid setup with low TP1 R. | No | High | Stable review criteria for invalid structure without outcome data. | Stop if reviewers cannot separate setup invalidity from post-entry performance. |
| B-TP1-FU-05 | Farther-target exception evidence threshold | What evidence would be required before proposing a narrow farther-target design? | Manual review aggregate; second-review adjudication; future cases where rank 2-5 visually outrank rank 1. | Evidence-threshold note defining required support before any design-only exception proposal. | No | Medium | Repeated, low-ambiguity farther-target findings across independent samples. | Stop if farther target selection cannot be stated without discretionary zone drawing or outcome selection. |
| B-TP1-FU-06 | Stop-anchor diagnostic path | Can structurally valid stops, questionable stops, and visually uninterpretable stops be separated before changing stop logic? | Blinded stop-marker charts; stop-anchor labels; 32-summary stop/invalidation doctrine. | Aggregate stop-anchor diagnostic report with label counts and unresolved classes. | No | High | Fixed stop-anchor labels and Pass A / Pass B separation. | Stop if stop validity is judged by later TP/SL outcome or by improving RR after the fact. |
| B-TP1-FU-07 | Stop-width versus stop-validity distinction | When is a wide stop structurally valid versus simply too wide? | Stop-anchor labels; hidden stop-distance ATR revealed only after Pass A; corpus invalidation notes. | Docs-only distinction matrix: wide-but-structural, wide-and-questionable, not interpretable. | No | High | Stop-distance reveal after structural label lock. | Stop if width alone is treated as invalidity or if shallow stops are accepted only to improve RR. |
| B-TP1-FU-08 | Contextual RR doctrine mapping | What would a non-optimized, mechanically testable contextual RR rule need to specify? | 32-summary doctrine map; manual RR labels; stop/TP structure labels. | Docs-only requirements checklist for any future contextual RR design. | No | Medium | Clear separation of structural TP, stop validity, and RR acceptability. | Stop if the proposed rule becomes a parameter sweep or uses performance to choose thresholds. |
| B-TP1-FU-09 | Corpus-to-rule translation blockers | Which 32-summary concepts remain too discretionary for code? | `channel_32_summary_interim_synthesis.md`; TP1/stop manual review labels; ambiguity counts. | Blocker register listing discretionary terms that are not implementation-ready. | No | Medium | Corpus concepts mapped to current Strategy B decision points. | Stop if the backlog starts converting vague terms like clean wave or target realism directly into code. |
| B-TP1-FU-10 | Future manual-review sample design | What fixed sample design would be needed before a design proposal? | Existing diagnostic design; prior manual-review sample results; local-only artifact policy. | Docs-only fixed sample protocol with buckets, hidden fields, second-review policy, and shortfall rules. | No | Medium | Agreement on whether to continue Strategy B diagnostics now. | Stop if sample selection uses outcomes, profitability, cherry-picking, or raw artifacts in Git. |

## 5. Evidence thresholds

Before any future design proposal, the evidence should meet qualitative thresholds:

- repeated finding across independent samples
- low ambiguity after second review
- mechanical rule can be stated without outcome data
- rule uses only information available at confirmation time
- no conflict with stop/invalidation doctrine
- no raw outcome/profitability selection
- no parameter sweep
- no future bars or post-confirmation outcome candles
- no pair-specific tuning
- no collapse of no-valid-target / no-trade-structure cases into low-RR cases
- stop validity is evaluated separately from stop width and RR convenience

Evidence that fails these thresholds may still be useful diagnostically, but it should not advance to implementation design.

## 6. Explicitly non-approved changes

The following changes are not approved:

- use rank 2 or farther target automatically
- lower TP1 min RR
- remove TP1 min RR
- change stop buffer
- change stop width sanity limits
- add discretionary chart-reading filters
- create Strategy B2
- implement contextual RR
- add new indicators
- use trade outcomes to choose targets
- tune ADX, ATR, swing width, swing lookback, or RR thresholds
- make shallow stops solely to improve RR
- convert YouTube corpus doctrine directly into Strategy B code without a separate design memo

## 7. Local-only artifact policy

Local-only artifacts must stay out of Git:

- raw CSVs stay local-only
- normalized OHLC CSVs stay local-only
- candidate CSVs stay local-only
- TP candidate CSVs stay local-only
- charts stay local-only
- hidden mappings stay local-only
- worksheets stay local-only
- reviewer packets stay local-only
- generated CSV/JSON/results stay local-only

Git-safe outputs may include only aggregate Markdown reports, diagnostic taxonomies, decision memos, and backlog notes that exclude raw candidate rows, pair/time/price details, chart images, hidden mapping rows, filled worksheet rows, and outcome/profitability claims.

## 8. Recommended next PR

Recommended next PR: create a docs-only Strategy B TP1 decision closure note that freezes Strategy B behavior pending broader evidence.

Alternative next PRs:

- pause Strategy B TP1 changes and return to the YouTube full-corpus doctrine analysis after the parallel line completes
- create a fixed future diagnostic protocol if the user wants to continue Strategy B diagnostics now

Do not recommend implementation. Any implementation would first require a separate docs-only design proposal that satisfies the evidence thresholds above.

## 9. Guardrails

Confirmed:

- docs-only
- exactly one Markdown file
- no code changes
- no rule changes
- no parameter/config/test changes
- no backtests
- no optimization
- no market data fetch
- no API call
- no broker/API/live trading
- no raw CSV
- no data/results/CSV/JSON
- no chart images
- no hidden mappings
- no worksheets
- no Strategy B2/C
- no profitability claims
