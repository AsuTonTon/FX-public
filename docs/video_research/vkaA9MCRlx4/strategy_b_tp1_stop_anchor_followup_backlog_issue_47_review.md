# Strategy B TP1 Stop-Anchor Follow-Up Backlog Issue 47 Review

## 1. Objective and scope

This report reviews the committed Strategy B TP1 / stop-anchor follow-up
diagnostic backlog and chooses exactly one safe future diagnostic question to
preserve, defer, or close.

Scope:

- recap the current Issue #45 TP1 review decision;
- summarize the committed TP1 / stop-anchor backlog;
- choose exactly one backlog question;
- classify the chosen question;
- explain why the choice does not authorize any Strategy B change;
- recommend one bounded docs-only next task.

Out of scope:

- no Strategy A/B/B2/C rule, code, parameter, config, test, runner, or backtest
  change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no new diagnostics generation;
- no new backtest;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, ASR, or external
  source access;
- no raw market data, normalized CSV, generated candidate/result/trade/event
  CSV, raw transcript, subtitle text, raw TXT/SRT/VTT, caption URL, downloaded
  media, `data/`, or `results/` content;
- no profitability claim or trading recommendation.

## 2. Source files and docs used

Committed docs inspected:

- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_memo.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_candidate_export_analysis.md`

Committed code inspected read-only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`

No uncommitted local files, raw data artifacts, generated outputs, market data,
broker/live systems, video sources, captions, transcripts, or external sources
were used.

## 3. Issue #45 TP1 review decision recap

Issue #45 classified the current Strategy B TP1 evidence as:

`structural_proxy_limitation_with_stop_to_tp_geometry_evidence_insufficient_for_rule_change`

The review found that current TP1 selection is deterministic and narrow:
Strategy B chooses the nearest eligible left-side fractal swing beyond entry as
TP1, then evaluates fixed RR gates against the selected stop. The committed
diagnostics show TP1 RR as the broadest rejection footprint, with stop width
interacting strongly with the TP1 RR denominator.

The Issue #45 conclusion did not authorize a rule change. The current closure
note keeps TP1 ranking, TP1 minimum RR, TP2 minimum RR, TP1-only minimum RR,
stop-anchor logic, stop-buffer logic, stop sanity limits, ADX, management
structure, and Strategy B2 status frozen pending broader evidence.

## 4. Backlog items summarized

The committed backlog contains ten diagnostic-only questions:

| ID | Topic | Current review read |
| --- | --- | --- |
| B-TP1-FU-01 | Low-R-but-structural TP classification | Preserve as useful later, but it still requires a fixed blinded review protocol. |
| B-TP1-FU-02 | Micro-structure TP1 classification | Preserve as useful later, but definitions remain vulnerable to visual discretion. |
| B-TP1-FU-03 | No-valid-target / no-left-side-target preservation | Preserve as a separate class; not the same as low-RR target availability. |
| B-TP1-FU-04 | No-trade-structure separation | Preserve as a diagnostic taxonomy path; not an execution rule. |
| B-TP1-FU-05 | Farther-target exception evidence threshold | Defer; this is closest to a later rule-design path and must wait for stronger repeated evidence. |
| B-TP1-FU-06 | Stop-anchor diagnostic path | Preserve for later as the one selected question in this review. |
| B-TP1-FU-07 | Stop-width versus stop-validity distinction | Preserve later, but treat as dependent on stop-anchor label stability. |
| B-TP1-FU-08 | Contextual RR doctrine mapping | Defer; easy to become parameter or doctrine-to-code drift without stronger boundaries. |
| B-TP1-FU-09 | Corpus-to-rule translation blockers | Defer to the separate corpus line; do not mix into Strategy B behavior. |
| B-TP1-FU-10 | Future manual-review sample design | Preserve as an enabling protocol task, but not the chosen diagnostic question here. |

This report does not add new backlog items.

## 5. Selected diagnostic question

Selected backlog item:

`B-TP1-FU-06 - Stop-anchor diagnostic path`

Backlog question:

Can structurally valid stops, questionable stops, and visually uninterpretable
stops be separated before changing stop logic?

Classification decision:

`preserve for later`

## 6. Rationale for preserving B-TP1-FU-06

B-TP1-FU-06 should be preserved because the committed evidence repeatedly
separates stop quality from TP1 RR convenience:

- Issue #45 says stop-to-TP geometry is a material interaction, but evidence is
  insufficient for changing stop anchors, stop buffers, stop limits, RR gates,
  or TP1 ranking.
- The decision memo says stop-anchor quality should be treated as a separate
  decision path and not hidden inside TP1 RR analysis.
- The closure note freezes stop-anchor logic and requires stronger evidence
  before any TP1 or stop-anchor design work is reopened.
- Candidate diagnostics show every `stop_too_wide` case also failed
  `tp1_below_min_rr`, while TP-candidate diagnostics show only a small subset
  of wide-stop cases had any rank 1-5 target at or above `1.0R`.
- Because wide stops may be structurally valid, questionable, or not
  interpretable, width alone should not become a proxy for stop invalidity.

Preserving this question keeps the diagnostic line available without approving
a stop-rule change. It also prevents a weaker shortcut: changing stops merely
to improve RR after the fact.

## 7. Why this does not change Strategy B now

This selection does not authorize any Strategy B change because:

- B-TP1-FU-06 is diagnostic-only in the committed backlog;
- no fixed stop-anchor label set or blinded stop-review protocol is approved in
  this issue;
- no new sample, chart packet, local artifact, or generated diagnostic output
  was created;
- no replacement stop-anchor rule is specified;
- stop validity must not be judged from later TP/SL outcome;
- shallow stops chosen only to improve RR would violate the current
  premise/invalidation guardrail;
- the closure note remains controlling until explicit reopen conditions are
  met.

Current Strategy B behavior therefore remains unchanged.

## 8. Guardrail confirmation

Confirmed:

- docs-only backlog review;
- committed repository docs and code only;
- one Markdown report added;
- no Strategy A/B/B2/C behavior change;
- no Strategy B rules, parameters, configs, tests, runner behavior, or backtest
  behavior changed;
- no Strategy B2 or Strategy C created;
- no parameter optimization;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, ASR, or external
  sources accessed;
- no raw market data, normalized CSV, generated candidate/result/trade/event
  CSV, raw transcript, subtitle text, raw TXT/SRT/VTT, caption URL, downloaded
  media, `data/`, `results/`, credentials, tokens, or secrets committed;
- no profitability claim or trading recommendation.

## 9. Recommended next bounded task

Recommended next task:

`[codex] Strategy B stop-anchor diagnostic protocol guardrails`

Scope:

- docs-only;
- define fixed labels for structurally valid, questionable, and visually
  uninterpretable stop anchors;
- define Pass A / Pass B separation so structural stop labels are locked before
  stop distance, RR, or outcome-like information is considered;
- keep all chart packets, rows, mappings, and generated artifacts local-only;
- do not run diagnostics;
- do not change Strategy B behavior;
- keep the Issue #45 closure note controlling.
