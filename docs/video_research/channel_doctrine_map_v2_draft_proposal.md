# Channel Doctrine Map v2 Draft Proposal

Task: `channel_doctrine_map_v2_draft_proposal`

Draft proposal date: 2026-07-01

## 1. Draft Status and Scope

This document is a draft proposal only.

It is not accepted doctrine. It does not replace `docs/video_research/channel_doctrine_map_v1.md`. It does not create final Channel Doctrine Map v2, and it does not create `docs/video_research/channel_doctrine_map_v2.md`.

This draft proposal does not authorize Strategy A/B changes, parameter changes, config changes, test changes, Strategy B2, Strategy C, backtests, optimization, broker logic, live trading, execution logic, or profitability claims.

Batch 08 is excluded. This draft proposal uses only committed Batch 01 through Batch 07 evidence and planning documents.

This draft proposal does not access DownSub, YouTube, captions, audio, video, or ASR. It does not commit raw TXT, SRT, VTT, subtitle full text, caption URLs, CSV, JSON, database, `data/`, or `results/` artifacts.

## 2. Evidence Base

Committed evidence used:

- `docs/video_research/doctrine_map_v2_drafting_plan.md`
- `docs/video_research/doctrine_map_v2_candidate_review.md`
- `docs/video_research/doctrine_map_v2_candidate_update_plan.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/downsub_access_policy_v2.md`
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`
- Batch 01 through Batch 07 completed-summary audit reports.
- Batch 01 through Batch 07 aggregate reports and quality reviews where needed.

Known Corpus v2 Batch 01-07 synthesis coverage:

| metric | value |
| --- | ---: |
| completed-summary audit batches synthesized | 7 |
| audited videos | 56 |
| audited mechanical-rule candidates | 233 |

This draft proposal does not add new evidence, new summaries, new caption access, new candidate extraction, or new source material.

## 3. Confidence Labels

| label | meaning in this draft proposal |
| --- | --- |
| high confidence draft doctrine | Candidate direction has strong support in the candidate review and clear continuity with Doctrine Map v1, but still needs human review before acceptance. |
| medium confidence draft doctrine | Candidate direction is supported and useful, but remains setup-specific, under-specified, or dependent on chart-reading judgment. |
| evidence note only | Evidence is useful for context or later mismatch review, but should not become draft doctrine yet. |
| unresolved blocker | Evidence identifies important discretionary concepts that are not sufficiently defined for doctrine text. |
| excluded from doctrine | Evidence should not be used as doctrine under current scope. |

These labels are qualitative review labels. They are not statistical proof, do not imply exact frequencies, and do not imply profitability.

## 4. Proposed Strengthened Doctrine Areas

The following items are draft-proposal directions only. They are not accepted Doctrine Map v2 doctrine and should not be treated as implementation-ready trading rules.

### DM2-C01: Higher-Timeframe Context

| field | draft proposal |
| --- | --- |
| candidate label | DM2-C01 |
| draft status | proposed strengthened doctrine direction |
| confidence | high confidence draft doctrine |
| relationship to Doctrine Map v1 | Strengthens v1 timeframe hierarchy doctrine, especially the idea that local signals are gated by higher-timeframe or monitored-timeframe context. |
| proposed draft doctrine direction | Future doctrine text may state that premise timeframe, monitored timeframe, and execution timeframe should remain distinct when judging local entries, stops, and targets. |
| limits and unresolved points | The draft should not force every example into one fixed timeframe or imply that a single timeframe rule replaces setup-specific context. |
| why it should not directly modify Strategy A/B yet | Strategy A/B uses a narrower fixed setup/timeframe representation; any mismatch re-check needs a separate PR after this draft proposal is reviewed. |

### DM2-C02: Entries and Confirmation

| field | draft proposal |
| --- | --- |
| candidate label | DM2-C02 |
| draft status | proposed strengthened doctrine direction |
| confidence | high confidence draft doctrine |
| relationship to Doctrine Map v1 | Strengthens v1 entry doctrine around delayed confirmation, reaction, and context-before-entry. |
| proposed draft doctrine direction | Future doctrine text may group confirmation families such as candle close, pullback or return behavior, reference-candle behavior, line reaction, false-break recovery, and second confirmation. |
| limits and unresolved points | The draft should not collapse these forms into one universal trigger or write implementation-ready entry rules. |
| why it should not directly modify Strategy A/B yet | Strategy A/B currently encodes one reference-candle confirmation sequence; broadening or comparing confirmation families requires a separate mismatch re-check. |

### DM2-C03: Stop Placement and Invalidation

| field | draft proposal |
| --- | --- |
| candidate label | DM2-C03 |
| draft status | proposed strengthened doctrine direction |
| confidence | medium confidence draft doctrine |
| relationship to Doctrine Map v1 | Strengthens v1 stop and invalidation doctrine around premise-based structural anchors. |
| proposed draft doctrine direction | Future doctrine text may distinguish stop-anchor validity from stop-width tolerance and emphasize that invalidation should relate to the trade premise. |
| limits and unresolved points | Exact anchors, buffers, numeric stop widths, and visual pivot choices remain unresolved. |
| why it should not directly modify Strategy A/B yet | Strategy B uses deterministic stop anchors, ATR buffer, and stop sanity proxies; doctrine evidence does not authorize changing those mechanics from this draft. |

### DM2-C04: TP, Exit, and RR

| field | draft proposal |
| --- | --- |
| candidate label | DM2-C04 |
| draft status | proposed strengthened doctrine direction |
| confidence | medium confidence draft doctrine |
| relationship to Doctrine Map v1 | Strengthens v1 separation among initial TP, structural TP, protective exit, trade management, and contextual RR. |
| proposed draft doctrine direction | Future doctrine text may keep target selection, protective exit, partial or staged management, RR threshold, RR tolerance, and trader execution burden as separate concepts. |
| limits and unresolved points | No universal TP procedure, partial-exit sizing, break-even movement, target priority hierarchy, or fixed RR threshold is accepted here. |
| why it should not directly modify Strategy A/B yet | Strategy B combines structural TP, partial exit, break-even, and RR gates; any comparison requires a separate mismatch re-check after draft review. |

### DM2-C05: Breakout, Damashi, Sweep, and False-Break Handling

| field | draft proposal |
| --- | --- |
| candidate label | DM2-C05 |
| draft status | proposed strengthened doctrine direction |
| confidence | medium confidence draft doctrine |
| relationship to Doctrine Map v1 | Strengthens v1 false-break, damashi, sweep, and stop-run doctrine as a context-filter family. |
| proposed draft doctrine direction | Future doctrine text may frame breakout and false-break evidence around line quality, outside grounds, higher-timeframe context, wave room, return behavior, and delayed confirmation. |
| limits and unresolved points | This is not a full breakout, reversal, or sweep system and should not define implementation-ready entry, stop, TP, or management rules. |
| why it should not directly modify Strategy A/B yet | Strategy A/B does not directly model this context-filter family; adding or comparing it requires separate authorization. |

### DM2-C06: Range Handling

| field | draft proposal |
| --- | --- |
| candidate label | DM2-C06 |
| draft status | proposed strengthened doctrine direction |
| confidence | medium confidence draft doctrine |
| relationship to Doctrine Map v1 | Strengthens v1 trend, range, and pattern-quality doctrine around structural range context. |
| proposed draft doctrine direction | Future doctrine text may describe range handling as structural and contextual, including range maturity, boundary quality, short-term range-entry caution, dirty-range rejection, and higher-timeframe veto. |
| limits and unresolved points | Range quality remains partly visual and should not be reduced to a numeric rule or indicator-only proxy. |
| why it should not directly modify Strategy A/B yet | Strategy B uses ADX as a research proxy, while this draft direction does not establish ADX or any indicator as doctrine. |

### DM2-C07: Wave Context

| field | draft proposal |
| --- | --- |
| candidate label | DM2-C07 |
| draft status | proposed strengthened doctrine direction |
| confidence | medium confidence draft doctrine |
| relationship to Doctrine Map v1 | Strengthens v1 use of wave context across entry, stop, TP, timeframe, and pattern-quality doctrines. |
| proposed draft doctrine direction | Future doctrine text may preserve wave stage, wave-aligned stops and targets, pullback waiting, and higher-timeframe/monitored-timeframe overlap as context categories. |
| limits and unresolved points | Wave count, wave cleanliness, pivot selection, wave room, and chart-only wave judgment remain discretionary. |
| why it should not directly modify Strategy A/B yet | Strategy A/B encodes a narrow EMA/wave-style setup; broader wave doctrine requires separate mismatch review before any strategy implication. |

## 5. Evidence Notes Only

The following items are useful evidence notes only. They are not draft doctrine.

### DM2-C08: EMA and Reference-Candle Context

| field | evidence note |
| --- | --- |
| why the evidence is useful | It preserves setup-specific evidence around moving-average context, 20EMA touch, reference-candle behavior, 200EMA environment, and applied third-wave examples. |
| why it remains weak or limited | Candidate review classified it as weak/limited because it does not justify broad indicator doctrine and remains setup-specific. |
| why it should not become broad doctrine yet | The current committed docs do not establish indicator-primary entries, broad EMA doctrine, or ADX doctrine. |
| why Strategy A/B should not change directly | Strategy A/B is already heavily tied to EMA/reference-candle mechanics; any re-check should keep this evidence narrow and separately authorized. |

### DM2-C09: Discretionary Management and Psychology

| field | evidence note |
| --- | --- |
| why the evidence is useful | It preserves cautionary evidence around mid-profit exit, protective exit, break-even or stop-change warnings, execution tolerance, and advanced management copying risk. |
| why it remains weak or limited | Much of the evidence is conditional, cautionary, psychology-bound, or lacks implementation detail. |
| why it should not become broad doctrine yet | Positive management procedures, sizing, trigger conditions, and universality are not established. |
| why Strategy A/B should not change directly | Strategy A/B should not absorb cautionary management or psychology evidence without a separate specification and mismatch review. |

## 6. Unresolved Blockers

### DM2-C10: Discretionary Chart-Reading Terms

DM2-C10 remains unresolved.

Examples of unresolved terms:

- clean wave;
- valid line;
- target realism;
- strong reason;
- market fuel;
- scenario coherence;
- wave room;
- dirty structure.

These terms remain visually discretionary. They should not be turned into mechanical doctrine, code behavior, parameters, thresholds, filters, or backtest criteria unless a future manual-review protocol defines them carefully.

## 7. Strategy A/B Boundary

This draft proposal does not modify Strategy A/B.

It does not recommend Strategy A/B parameter changes. Strategy A/B mismatch re-check requires a separate PR and explicit authorization. Strategy comparison should wait until this draft proposal is reviewed and either accepted, revised, or rejected as a candidate doctrine set.

Possible future mismatch areas only as planning references:

- higher-timeframe context;
- entries and confirmation;
- stop placement and invalidation;
- TP, exit, and RR;
- breakout, damashi, sweep, and false-break handling;
- range handling;
- wave context;
- EMA and reference-candle context;
- discretionary management and psychology.

No Strategy A/B rule, parameter, config, test, backtest, optimization, broker, live trading, or execution change is authorized by this draft proposal.

## 8. Batch 08 Boundary

Batch 08 is excluded.

Batch 08 must not be used to strengthen, weaken, add, or reject any v2 draft proposal item. Batch 08 requires separate bounded approval and audit under `docs/video_research/downsub_access_policy_v2.md` before it can be considered in any later doctrine work.

## 9. Non-Goals

This draft proposal does not authorize:

- Strategy A/B implementation.
- Strategy B2 or Strategy C.
- Parameter tuning.
- Backtests.
- Optimization.
- Profitability conclusions.
- Live trading.
- Broker or execution logic.
- Market-data access.
- Raw subtitle or generated data artifacts.
- Batch 08 inclusion.
- Final Doctrine Map v2 acceptance.
- Creation of `docs/video_research/channel_doctrine_map_v2.md`.

## 10. Review Checklist

Future human reviewer checklist:

| check | reviewer question |
| --- | --- |
| traceability | Does each draft item trace back to Doctrine Map v1 and the candidate review? |
| confidence | Is confidence labeled clearly? |
| weak/limited evidence | Are weak or limited items kept out of doctrine? |
| unresolved blockers | Are unresolved blockers preserved instead of mechanized? |
| mechanical overclaiming | Does the document avoid implementation-ready trading rules, parameters, thresholds, or code behavior? |
| Strategy A/B boundary | Does the document avoid Strategy A/B changes and recommendations? |
| Batch 08 boundary | Does the document exclude Batch 08? |
| profitability | Does the document avoid profitability claims? |
| source handling | Does the document avoid raw subtitle text, caption URLs, data, result artifacts, video, audio, and ASR? |

## 11. Recommended Next PR After This Draft Proposal

Recommended next docs-only PR:

`Doctrine Map v2 draft proposal review`

Reason: Strategy A/B mismatch work should wait until this draft proposal is reviewed and either accepted, revised, or rejected as a candidate doctrine set. A review PR should check traceability, confidence labels, weak-evidence handling, unresolved blockers, Strategy boundaries, Batch 08 exclusion, and guardrails before any Strategy A/B mismatch re-check plan is considered.

## 12. Readiness Decision

`channel_doctrine_map_v2_draft_proposal_ready_for_human_review`

Reason: this docs-only draft proposal uses the merged Doctrine Map v2 drafting plan, candidate review, Corpus v2 Batch 01-07 audit synthesis, current Doctrine Map v1, DownSub access policy v2, and existing Strategy A/B doctrine mismatch analysis to propose candidate doctrine directions, evidence notes, unresolved blockers, Strategy boundaries, and review gates. It is ready for human review as a draft proposal only. It does not state that Doctrine Map v2 is accepted, does not replace Doctrine Map v1, does not create `docs/video_research/channel_doctrine_map_v2.md`, does not include Batch 08, and does not state that Strategy A/B should change.
