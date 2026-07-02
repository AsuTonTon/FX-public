# Strategy B TP1 Stop-Anchor Cumulative Synthesis

## 1. Objective and scope

This report summarizes the current cumulative Strategy B TP1 / stop-anchor
research state after the TP1 decision cycle, the stop-anchor protocol work, the
local-only stop-anchor diagnostic, and the fallback bucket follow-up report.

Scope:

- use committed repository documents only;
- summarize the research sequence and current decision state;
- separate TP1 minimum RR behavior from structural stop-anchor quality;
- identify answered, unresolved, blocked, and parallel work items;
- recommend one bounded next task after the fallback availability line reports.

Out of scope:

- no diagnostic run;
- no local data access;
- no Strategy A/B/B2/C rule, code, parameter, config, test, runner, or backtest
  behavior change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no market-data API, broker API, order placement, auto trading, or live
  trading;
- no profitability, live-readiness, or trading recommendation claim.

## 2. Source docs used

Committed repository docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_backlog_issue_47_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_protocol_guardrails.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_sample_design_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_run_authorization_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_local_only_run_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_local_only_run_report_after_handoff.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_fallback_bucket_local_only_run_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_memo.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`

No uncommitted local files, local OHLC inputs, generated diagnostics,
candidate rows, chart packets, worksheets, hidden mappings, raw market data,
broker/live systems, video sources, captions, transcripts, or external sources
were used for this synthesis.

## 3. Research sequence recap

The current sequence starts with the Strategy B TP1 selection review. That
review documented the implemented TP1 behavior: Strategy B selects the nearest
eligible left-side fractal swing beyond entry as TP1, then applies fixed RR,
stop-width, and ADX gates. The review found that TP1 minimum RR dominates the
post-confirmation rejection footprint, but it did not prove that rank-1 TP1
selection, RR gates, or stop rules should change.

The follow-up backlog then preserved stop-anchor quality as a separate
diagnostic path. It explicitly avoided treating stop width, TP1 RR failure, or
post-entry results as substitutes for structural stop-anchor validity.

The protocol and sample-design documents defined a blinded Pass A / Pass B
workflow for future local-only stop-anchor diagnostics. Pass A locks structural
stop-anchor labels before stop distance, RR fields, target ranks, rejection
reasons, accepted status, or outcome-like fields can be considered.

The first local-only diagnostic run was initially blocked because the required
local artifacts were unavailable in the automation worktree. After local OHLC
inputs were handed off, a bounded aggregate diagnostic was completed. It found
both structurally valid and questionable stop anchors overlapping with stop
width concerns and TP1 RR failures. That supported preserving stop-anchor
quality as a separate diagnostic axis, not changing Strategy B behavior.

The later fallback bucket follow-up focused on reference-candle fallback
stop-anchor cases. It found only one eligible base fallback case in the
bounded fallback-only sample, producing a three-case shortfall against the
planned four-case target. That result is a sample-availability limitation, not
a stable fallback stop-anchor conclusion.

## 4. Cumulative findings table

| Finding | Evidence source | Interpretation | Allowed next action | Forbidden action |
| --- | --- | --- | --- | --- |
| Strategy B initial accepted count remains very low. | TP1 selection review and decision memo. | The rejection collapse happens after confirmation, with TP1 minimum RR as the largest documented rejection footprint. | Preserve the rejection facts in docs and keep diagnostics aggregate-only. | Claim Strategy B is profitable, unprofitable, live-ready, or mechanically fixed by one change. |
| `tp1_below_min_rr` is central. | TP1 selection review, decision memo, and closure note. | TP1 minimum RR is the direct reason in many failures, but it is not the same as stop-anchor validity. | Keep TP1 RR as a distinct diagnostic category. | Collapse every TP1 RR failure into a stop-anchor-quality conclusion. |
| Rank-1 TP1 remains frozen. | Decision memo and closure note. | Existing evidence does not justify rank replacement, farther-target exceptions, or contextual RR implementation. | Require a later docs-only design review before any rule proposal. | Switch to later-rank TP, lower RR gates, remove RR gates, or tune thresholds. |
| Stop-anchor quality is a separate axis. | Backlog review, protocol guardrails, and post-handoff diagnostic report. | Wide or RR-failing stops can be structurally valid, questionable, or ambiguous. | Keep structural stop labels separate from Pass B RR and width interpretation. | Treat width alone as stop invalidity or accept shallower stops merely to improve RR. |
| PR #59-era local diagnostic supports separation, not implementation. | Post-handoff local-only run report. | Structural-valid and questionable labels both overlapped with TP1 RR failures and stop-width concerns. | Use the aggregate result as evidence that stop-anchor diagnostics should remain separate. | Change stop anchors, stop buffers, stop sanity limits, TP rules, ADX, or Strategy B behavior. |
| Reference-candle fallback evidence remains insufficient. | Fallback bucket local-only run report. | Only one base fallback case was available in the bounded fallback-only sample. | Wait for the separate sample-availability line before deciding whether another fallback diagnostic is feasible. | Generalize from one fallback base case or fill the bucket from nonfallback cases. |
| No-valid-target and no-trade-structure remain separate classes. | Decision memo, closure note, and backlog. | These cases should not be merged into low-RR or stop-width buckets. | Preserve the taxonomy in future diagnostics. | Reclassify absence of a valid target or invalid setup structure as ordinary TP1 RR failure. |
| Corpus findings remain separate from Strategy A/B verification. | Closure note and repository guardrails. | Channel-wide doctrine may later motivate mismatch analysis, but it does not directly change Strategy B. | Use a separate docs-only mismatch analysis after corpus work materially advances. | Mix YouTube corpus findings into executable Strategy B behavior without a design decision. |

## 5. What is answered

Answered:

- Current Strategy B TP1 selection is mechanically documented and remains
  nearest eligible left-side swing rank 1.
- Current TP1 minimum RR is a major documented rejection driver.
- The current evidence does not authorize TP1 rank changes, RR threshold
  changes, stop-rule changes, Strategy B2, or Strategy C.
- Stop-anchor quality must remain separate from stop width, TP1 RR, and
  outcome-like fields.
- The post-handoff local-only diagnostic supports diagnostic separation rather
  than implementation.
- The fallback-only diagnostic is underpowered because the bounded fallback
  sample had a material shortfall.

## 6. What remains unresolved

Unresolved:

- Whether a broader but predeclared local-only slice contains enough additional
  reference-candle fallback cases for another blinded diagnostic.
- Whether fallback stop anchors show repeated low-ambiguity structural patterns
  after enough cases are available and independently reviewed.
- Whether future independent samples repeat the stop-anchor label patterns with
  low ambiguity.
- Whether any future mechanical TP1, contextual RR, or stop-anchor design can
  be stated using only confirmation-time information without parameter tuning.
- Whether full-corpus doctrine work, after separate review, materially changes
  the Strategy A/B mismatch map.

## 7. Active parallel line note for fallback sample availability

The fallback sample-availability line is active and separate. Its purpose is to
determine whether additional reference-candle fallback cases exist under a
broader but predeclared local-only slice.

This synthesis does not run that review, inspect local artifacts, or decide the
fallback question. Until that line reports, the fallback state should remain:

`underpowered_bounded_fallback_sample_waiting_on_availability_review`

## 8. Guardrail confirmation

Confirmed:

- docs-only synthesis;
- committed repository docs only;
- one Markdown report added;
- no diagnostic run;
- no local data access;
- no Strategy A/B/B2/C behavior change;
- no Strategy B rules, parameters, configs, tests, runner behavior, or backtest
  behavior changed;
- no Strategy B2 or Strategy C created;
- no parameter optimization;
- no market-data API, broker API, order-placement, auto-trading, or
  live-trading behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, ASR, or external
  sources accessed;
- no raw market data, normalized market CSV, generated candidate/event/trade/
  TP-candidate/result CSV, worksheet, mapping, chart packet, image, JSON
  artifact, raw transcript, subtitle full text, raw TXT/SRT/VTT caption file,
  caption URL, downloaded media, `data/`, `results/`, credentials, tokens, or
  secrets committed;
- no profitability, money-making, live-readiness, or trading recommendation
  claim;
- Strategy A/B verification work and YouTube channel-wide corpus work are not
  mixed.

## 9. Recommended next bounded task after fallback availability reports

Recommended next task after the fallback availability line reports:

`[codex] Strategy B fallback availability decision note`

Scope:

- docs-only;
- use the fallback sample-availability aggregate report as the controlling
  source;
- decide whether the fallback line should proceed to another blinded Pass A /
  Pass B diagnostic, remain blocked for insufficient cases, or close as
  underpowered;
- require independent Pass A-only second review if another diagnostic is
  proposed;
- do not run diagnostics in the decision note;
- do not change Strategy B behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior.
