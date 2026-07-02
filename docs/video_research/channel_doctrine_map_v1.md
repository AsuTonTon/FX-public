# Channel Doctrine Map v1

Task: `channel_doctrine_map_v1_from_completed_summaries`

## 1. Objective and scope

This document is a provisional Channel Doctrine Map v1 built only from the already completed Git-safe YouTube corpus evidence in Batch 01 through Batch 07.

It is a corpus doctrine map, not Strategy B implementation guidance. It does not create Batch 08 summaries, create a Batch 08 quality review, create Batch 09 selection, freeze a final Batch 08 target set, modify Strategy A/B, create Strategy B2 or Strategy C, run backtests, optimize parameters, or make profitability claims.

## 2. Evidence base

| evidence item | value |
| --- | ---: |
| completed lightweight-summary batches | 7 |
| completed lightweight summaries | 56 |
| high-priority caption-available rows | 112 |
| remaining high-priority caption-available unsummarized rows | 56 |
| final Batch 08 target set frozen | 0 |

Sources inspected:

- Batch 01 through Batch 07 aggregate reports.
- Batch 01 through Batch 07 quality reviews.
- Batch 01 through Batch 07 per-video lightweight summaries.
- `docs/video_research/channel_32_summary_interim_synthesis.md`.
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`.
- `docs/video_research/channel_lightweight_summary_batch_08_selection_report.md`.
- `docs/video_research/channel_lightweight_summary_batch_08_selection_ledger.md`.

## 3. Methodology

This map treats the existing merged summaries and reports as the evidence source of record. It uses recurring observations, quality-review corrections, mechanical-candidate inventories, coverage matrices, one-off claims, and cross-batch comparisons. It does not inspect raw transcripts, subtitle text, caption URLs, downloaded media, local caption cache files, CSV/JSON/data/results artifacts, or screenshots.

Confidence means evidence strength inside the completed 56-summary corpus:

- `high`: repeated across several batches and supported by quality-reviewed recurring observations.
- `medium`: repeated but setup-specific, under-specified, or dependent on discretionary chart reading.
- `low`: one-off, weakly repeated, absent as a positive rule, or explicitly bounded by quality reviews.

Mechanical readiness is intentionally conservative. Even high-confidence doctrine can remain not ready for code if it depends on visual judgment, undefined thresholds, or setup-specific anchors.

## 4. Doctrine categories

| category | included concepts | current reading |
| --- | --- | --- |
| Entry doctrine | entry confirmation, delayed trigger, no first-touch entry, no line-only entry | Strong recurring evidence, but setup-specific anchors differ. |
| Stop / invalidation doctrine | stop anchor, invalidation anchor, stop width, stop movement | Structural premise is favored, but exact anchors and widths remain under-specified. |
| TP / exit doctrine | initial TP, structural TP, target realism, protective exit | Structural target evidence recurs, but TP priority and protective-exit triggers are not unified. |
| Risk/reward doctrine | RR threshold, RR tolerance, RR interaction with stop and target | RR is contextual; no universal replacement threshold is confirmed. |
| Trade-management doctrine | partial exit, break-even movement, stop movement, mid-profit discretionary exit, advanced management | Present but bounded, often case-specific, and not ready as a universal procedure. |
| Timeframe hierarchy doctrine | higher-timeframe context, monitored timeframe, lower-timeframe execution | High-confidence recurring doctrine. |
| Horizontal-line doctrine | line construction, line execution, line context, line targets | Lines are context and anchors, not standalone trade permission. |
| False-break / damashi / sweep doctrine | false-break filter, damashi, sweep, stop-run handling | Recurring but incomplete as a full system. |
| Trend / range / pattern-quality doctrine | trend context, range maturity, pattern-quality blocker, scenario planning | Recurring, but human judgment remains central. |
| Indicator doctrine | EMA, moving averages, RSI, ADX | EMA/MA/RSI are setup-specific or secondary; ADX is not established. |
| Session / time-of-day doctrine | session, time-of-day, event timing | General session rules are not confirmed; event timing appears only as context. |

## 5. High-confidence recurring principles

| doctrine_id | principle | supporting evidence | mechanical status |
| --- | --- | --- | --- |
| CDM-H01 | Higher-timeframe or monitored-timeframe context gates local signals. | B1-O1, B2-O3, B3-O1, B4-O4, B5-O3, B6-O3, B7-O1. | Candidate for future specification, not direct code. |
| CDM-H02 | Entry is delayed until confirmation, reaction, or context appears. | B1-O2, B2-O4, B3-O2, B4-O1, B6-O1, B7-O4. | Candidate for future specification. |
| CDM-H03 | Structural context comes before trigger interpretation. | B1-O3, B5-O5, B6-O1, B6-O5, B7-O1. | Not ready because valid structure is visual. |
| CDM-H04 | RR is contextual rather than a universal fixed threshold. | B1-O5, B2-O6, B5-O1, B7-O2, 32-summary synthesis. | Requires strategy-specific mismatch analysis. |
| CDM-H05 | Discretionary chart-review terms are a major blocker. | B1-O6, B2-O7, B4-O5, B5-O6, B6-O4, B7-O5. | Not ready for mechanical translation. |
| CDM-H06 | ADX and repeatable session/time-of-day rules are not established in the completed summaries. | B3-O7, B4-O6, B5-O7, B6-O6, B7-O6 and quality reviews. | Context-only absence finding. |

## 6. Medium-confidence recurring principles

| doctrine_id | principle | supporting evidence | limitation |
| --- | --- | --- | --- |
| CDM-M01 | Stop or invalidation should be tied to premise, wave, pattern, range, pullback, or structural backing. | B1-O4, B2-O1, B4-O2, B6-O2. | Exact anchor and stop width often remain visual or absent. |
| CDM-M02 | Initial TP should usually be structural or realistic rather than arbitrary. | B1-O4, B2-O2, B3-O3, B5-O4. | Priority among wave, line, pattern, channel, and nearer target is unresolved. |
| CDM-M03 | Protective or early exit may apply when premise, path, price action, or expected wave weakens. | B2-O8, B3-O4, B4-O3, B5-O2. | Trigger and sizing are setup-specific. |
| CDM-M04 | Horizontal lines are used for construction, context, reaction, targets, and scenarios, not as standalone entry permission. | B5-O5, B6-O5, Batch 01 line candidates, Batch 07 quality review. | Line quality and execution conditions remain discretionary. |
| CDM-M05 | False-break, damashi, sweep, and stop-run filters recur around lines, ranges, triangles, and dirty structure. | B1-O7, B3-O5, B5 one-off JDjq7FrKdF8, B7 one-off TzOwRNmaXrI. | Full setup-entry-stop-TP sequence is incomplete. |
| CDM-M06 | Trend, range, scenario, and pattern quality can veto tempting entries. | B2-O5, B4-O5, B6-O1, B7-O1, B7-O4. | Quality thresholds are not quantified. |

## 7. Low-confidence or under-specified principles

| doctrine_id | principle | evidence status | why low or under-specified |
| --- | --- | --- | --- |
| CDM-L01 | Staged partial/full exit can be useful in some examples. | vkaA9MCRlx4, Z2h_FkYn4VY, CxvfjD3CG8s, tw9gxJ7KXUs. | Sizing, timing, and universality are not established. |
| CDM-L02 | Break-even movement can be appropriate when the premise slows or invalidation risk changes. | qiV2W1wUidM plus management-boundary warnings. | One clear example plus cautions, not a repeated procedure. |
| CDM-L03 | Stop movement is an advanced management tool. | _sx3dCvPXac warns against copying advanced stop changes. | Warning evidence is not a positive rule. |
| CDM-L04 | EMA/MA can be part of a setup context. | vkaA9MCRlx4, k2_pm_TPgh0, CxvfjD3CG8s. | Other evidence rejects indicator-primary entries; ADX is absent. |
| CDM-L05 | Event timing can contextualize trades. | FwoDV2YrZOE. | Event timing is not a general session/time-of-day rule. |
| CDM-L06 | Scenario planning matters but remains difficult to code. | ezZxNuCLEKU, TzOwRNmaXrI, GB7wgE3GZtc plus cross-batch discretionary evidence. | Scenario coherence lacks numeric or deterministic criteria and should not become Strategy A/B implementation guidance without more evidence or later mismatch analysis. |

## 8. Entry doctrine

Entry doctrine is strongest where it delays action until a defined confirmation appears. The corpus repeatedly rejects first touch, first micro-break, line-only entry, and obvious local move without broader context. Confirmations include timeframe candle close, pullback or return behavior, reference-candle close, line credibility, second confirmation after false-break risk, and range or pattern quality.

This is not one universal trigger. The evidence distinguishes entry confirmation from line construction and from line execution. A line may be drawn correctly but still not authorize entry until context, reaction, or timeframe confirmation supports the trade idea.

## 9. Stop / invalidation doctrine

Stop and invalidation doctrine favors premise-based structure: wave origin, pattern invalidation, pullback pivot, range boundary, Dow shift, monitored structure, or structural backing. However, many examples retain unresolved visual anchors, colored stop lines, undefined buffers, and unclear stop-width tolerances.

Stop / invalidation anchor is distinct from stop width. The completed summaries support asking whether a stop is structurally valid before asking whether it is too wide, but they do not provide a single numeric stop-width rule or a universal buffer.

## 10. TP / exit doctrine

The corpus separates initial TP from structural TP, protective exit, partial exit, and mid-profit discretionary exit.

Initial TP evidence often points to structural candidates: wave projection, left-side swing levels, pattern width, channel target, horizontal target, daily/weekly line, or a nearer realistic target. Structural TP is not the same as arbitrary RR spacing. Target realism appears when a theoretical projection is too far, path weakens, or the trade drifts into a different timeframe idea.

Protective exit is not the same as initial TP. It appears when price action, premise, path, or expected wave weakens. Partial exit and staged exit appear in several examples, but they are not a universal TP procedure.

## 11. Risk/reward doctrine

RR is recurring but contextual. The completed summaries tie RR to stop placement, structural target quality, confirmation timing, target room, timeframe, win-rate context, trader tolerance, and the burden of holding through losses. They do not confirm one universal fixed RR threshold or a replacement threshold.

RR threshold and RR tolerance should remain distinct. A threshold is a rule boundary; tolerance is a discretionary or psychological ability to execute a style. The corpus supports the distinction but does not mechanize either into Strategy A/B.

## 12. Trade-management doctrine

Trade management evidence must be separated into:

- initial TP selection;
- structural TP target selection;
- partial exit;
- mid-profit discretionary exit;
- break-even movement;
- stop movement;
- protective early exit;
- advanced trade management.

The completed corpus supports bounded discussion of all except a repeatable universal management system. _sx3dCvPXac is especially important as a warning: copying partial TP, break-even, or stop movement without understanding is treated as a losing behavior, not a recipe.

## 13. Timeframe hierarchy doctrine

Timeframe hierarchy is one of the strongest recurring doctrines. Local or short-term entries remain incomplete without higher-timeframe environment, monitored-timeframe confirmation, trend context, wave context, or outside grounds. The source timeframe for a structure matters when confirming entry, stop, target, or management decisions. Lower-timeframe execution is not interchangeable with higher-timeframe premise.

## 14. Horizontal-line doctrine

Horizontal-line doctrine splits into line construction and line execution.

Line construction covers what level is drawn, which timeframe formed it, whether the line is functioning, and whether multiple lines or commodities/currencies interact. Line execution covers whether price reaction, break confirmation, context, wave shape, or target realism makes the line actionable.

The completed summaries repeatedly warn against treating a line alone as an entry, stop, or TP rule. Lines can organize context, invalidate a premise, define target candidates, or block trades, but they require surrounding structure.

## 15. False-break / damashi / sweep doctrine

False-break, damashi, sweep, and stop-run evidence appears across several batches. The recurring doctrine is not "always fade the break." It is: first break, ordinary triangle break, suspicious wick, dirty range, or stop-run move must be interpreted through outside grounds, return behavior, wave room, line credibility, and higher-timeframe context.

This remains incomplete as a full mechanical system because many examples lack complete stop, TP, RR, and management conditions.

## 16. Trend / range / pattern-quality doctrine

Trend, range, and pattern-quality doctrine recurs as a veto layer. Examples include range touch count, dirty or meaningless small ranges, weak structures, shallow first-wave breaks, local range plans vetoed by higher-timeframe context, and small reversal patterns rejected without a larger scenario.

Scenario planning and pattern-quality blocker are distinct. Scenario planning defines the broader path that would make a trade coherent; pattern-quality blockers reject local shapes that do not satisfy that scenario.

## 17. Indicator doctrine

Indicator evidence is weak and setup-specific. EMA/moving-average evidence appears in EMA-related examples and reference-candle setups, while other summaries explicitly reject moving averages or EMA200 as primary entry grounds. RSI appears as secondary evidence. ADX is repeatedly not confirmed as a mechanical trend-strength rule.

The current corpus does not support indicator-primary entries or ADX parameter changes.

## 18. Session / time-of-day doctrine

The completed 56 summaries do not confirm repeatable session or time-of-day rules. Event or calendar timing appears as context in one-off evidence, but it should not be converted into a general session doctrine.

## 19. Discretionary blockers

Recurring discretionary blockers include clean wave, valid line, line strength, touch quality, strong reason, market fuel, target realism, momentum weakness, dirty structure, candle strength, wave room, horizontal-axis sufficiency, and scenario coherence. These terms are central to the channel evidence and remain a major blocker to direct automation.

## 20. What should not be mechanized yet

Do not mechanize these yet:

- fixed universal RR replacement;
- universal break-even movement;
- universal partial-exit or staged-exit procedure;
- stop movement copied from advanced examples;
- ADX or session/time-of-day rules;
- indicator-primary entry;
- horizontal-line-only entry;
- false-break/sweep full system;
- target selection hierarchy across all setup families;
- discretionary terms such as clean wave, valid touch, strong reason, and target realism.

These may become future research questions, but not Strategy A/B implementation rules.

## 21. Relation to Batch 08 blocked status

Batch 08 remains blocked because caption body access is unavailable in the current environment and no final Batch 08 target set is frozen. Batch 08 summaries should not be created from this PR. Batch 09 selection should not be created while Batch 08 remains blocked.

This map is provisional because only 56 summaries are complete. The remaining 56 high-priority caption-available unsummarized rows may change the doctrine map when caption access recovers or sufficient local ignored caption-cache evidence becomes available.

## 22. Guardrails

Confirmed:

- docs-only doctrine map;
- no Batch 08 summaries;
- no Batch 08 quality review;
- no Batch 09 selection;
- no final Batch 08 target set;
- no Strategy A/B code or parameter changes;
- no Strategy B2 or Strategy C;
- no backtests or optimization;
- no profitability claims;
- no raw transcript, subtitle full text, raw subtitle files, caption URLs, downloaded video/audio, CSV, JSON, data files, result files, `data/`, `results/`, credentials, secrets, chart images, screenshots, worksheets, or hidden mappings.

## 23. Readiness decision

`ready_for_channel_doctrine_map_review_v1`

Reason: the completed 56-summary evidence has been organized into a provisional doctrine map with explicit confidence, distinction, non-mechanization, and Batch 08 blocked-status boundaries. The next appropriate step is review of this doctrine map, not Strategy implementation or later-batch selection.
