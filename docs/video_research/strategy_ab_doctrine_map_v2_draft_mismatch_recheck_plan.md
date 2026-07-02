# Strategy A/B Doctrine Map v2 Draft Mismatch Re-check Plan

Task: `strategy_ab_doctrine_map_v2_draft_mismatch_recheck_plan`

Plan date: 2026-07-01

## 1. Objective and Scope

This is a docs-only plan to re-check Strategy A/B mismatch against the reviewed, non-final Channel Doctrine Map v2 draft proposal and reviewed candidate doctrine set.

This plan:

- Defines what a later docs-only mismatch re-check should compare.
- Defines conservative mismatch classes and guardrails.
- Uses the current Strategy A/B representation as read-only context.
- Preserves the non-final status of the Channel Doctrine Map v2 draft proposal.

This plan does not:

- Modify Strategy A/B code, parameters, configs, or tests.
- Create Strategy B2 or Strategy C.
- Run backtests.
- Run optimization.
- Make profitability claims.
- Access market data.
- Fetch market data.
- Use broker APIs.
- Add broker, live trading, or execution logic.
- Update `docs/video_research/channel_doctrine_map_v1.md`.
- Create or update `docs/video_research/channel_doctrine_map_v2.md`.
- Treat the Doctrine Map v2 draft proposal as final or accepted doctrine.
- Include Batch 08.
- Access DownSub or YouTube.
- Fetch captions.
- Download video or audio.
- Run ASR.
- Use proxies, VPN rotation, IP rotation, or platform-rate-limit bypass.
- Commit raw TXT, SRT, VTT, subtitle full text, caption URLs, CSV, JSON, database, `data/`, or `results/` artifacts.

## 2. Evidence Base

This plan uses only committed evidence and repository files.

Primary docs:

- `docs/video_research/channel_doctrine_map_v2_draft_proposal_human_review.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal_human_review_review.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal_review.md`
- `docs/video_research/doctrine_map_v2_candidate_review.md`
- `docs/video_research/doctrine_map_v2_drafting_plan.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`

Strategy A/B context inspected read-only:

- `docs/video_research/vkaA9MCRlx4/backtest_spec_v1.md`
- `docs/video_research/vkaA9MCRlx4/strategy_a_implementation_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_spec_design.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_implementation_notes.md`
- `src/strategies/ema_wave3_strategy_a.py`
- `src/strategies/ema_wave3_strategy_b.py`
- Strategy A/B tests were listed or searched read-only for current assumption checks only.

Known Corpus v2 Batch 01-07 synthesis coverage:

| metric | value |
| --- | ---: |
| completed-summary audit batches | 7 |
| audited videos | 56 |
| audited mechanical-rule candidates | 233 |

This plan does not add new evidence, access subtitles, access market data, run Strategy A/B, or generate result artifacts.

## 3. Why a Re-check Plan Is Needed

Strategy A/B was previously compared against the provisional Channel Doctrine Map v1 in `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`.

Since then, Corpus v2 Batch 01-07 and the non-final Doctrine Map v2 draft proposal have organized and clarified several candidate doctrine areas:

- higher-timeframe context;
- entries and confirmation;
- stop placement and invalidation;
- TP, exit, and RR;
- breakout, damashi, sweep, and false-break handling;
- range handling;
- wave context;
- EMA and reference-candle context;
- discretionary management and psychology.

The v2 draft proposal remains non-final. It is not accepted doctrine and does not authorize Strategy A/B changes. Therefore the correct next step is not implementation. The correct next step is to define what a future docs-only mismatch re-check should compare, how it should classify findings, and what outputs would remain safe.

## 4. Proposed Mismatch Re-check Dimensions

The future mismatch re-check should compare Strategy A/B against the reviewed non-final v2 draft proposal across the dimensions below. These are planning classifications only. Nothing in this table requires implementation change.

| area | v2 draft proposal direction | known Strategy A/B representation | potential mismatch type to inspect later | likely issue level | out of scope until Doctrine Map v2 acceptance? |
| --- | --- | --- | --- | --- | --- |
| higher-timeframe context | DM2-C01 proposes strengthening timeframe hierarchy by distinguishing premise timeframe, monitored timeframe, and execution timeframe. | Strategy A/B is centered on a fixed 4H EMA20/EMA200 setup and does not assign separate ownership for premise, trigger, stop, and target timeframes. | specification mismatch or proxy mismatch | specification-level for docs; implementation-level only if later accepted and approved | Yes for any Strategy change; docs-only comparison may proceed. |
| entries and confirmation | DM2-C02 proposes grouping confirmation families such as candle close, pullback or return behavior, line reaction, false-break recovery, and second confirmation. | Strategy A/B uses the first 20EMA touch as reference candle and a body-close break of that reference candle, with next-candle-open entry. | documentation mismatch or specification mismatch | specification-level | Yes for any alternate trigger or code behavior. |
| stop placement and invalidation | DM2-C03 proposes premise-based stop/invalidation language and separates stop-anchor validity from stop-width tolerance. | Strategy A uses reference-candle high/low plus buffer; Strategy B uses deterministic left-side swing or reference-candle anchors, ATR buffer, and stop-distance sanity gates. | specification mismatch, proxy mismatch, or unresolved discretionary mismatch | specification-level; implementation-level only after separate approval | Yes for any anchor, buffer, or sanity-gate change. |
| TP, exit, and RR | DM2-C04 proposes keeping target selection, protective exit, partial or staged management, RR threshold, RR tolerance, and trader execution burden distinct. | Strategy A uses fixed RR full exit. Strategy B uses left-side swing TP1/TP2, fixed RR gates, 50%/50% management, and break-even after TP1. | specification mismatch or proxy mismatch | specification-level | Yes for any TP, RR, partial exit, or break-even change. |
| breakout, damashi, sweep, and false-break handling | DM2-C05 proposes a context-filter family around line quality, outside grounds, higher-timeframe context, wave room, return behavior, and delayed confirmation. | Strategy A/B does not directly model breakout, damashi, sweep, false-break recovery, line quality, or reclaim behavior as distinct context families. | documentation mismatch or unresolved discretionary mismatch | documentation-only or unresolved | Yes; no new breakout or sweep logic until separate doctrine and Strategy approval. |
| range handling | DM2-C06 proposes structural and contextual range handling rather than an indicator-only proxy. | Strategy B uses ADX(14) below 18 as a mechanical no-trade range proxy; Strategy A has no range filter. | proxy mismatch | specification-level | Yes for changing, removing, or replacing ADX; docs-only comparison may identify the proxy issue. |
| wave context | DM2-C07 proposes preserving wave stage, wave-aligned stops and targets, pullback waiting, and timeframe overlap while keeping wave count and cleanliness discretionary. | Strategy A/B approximates one EMA/wave-style setup through cross, first 20EMA touch, and reference-candle confirmation; it does not define wave count or wave cleanliness. | proxy mismatch or unresolved discretionary mismatch | unresolved unless future terms are defined | Yes for any wave-count or wave-quality logic. |
| EMA and reference-candle context | DM2-C08 remains evidence note only and should not become broad indicator doctrine. | Strategy A/B is heavily centered on EMA20/EMA200 and reference-candle mechanics. | proxy mismatch or out of scope until doctrine acceptance | specification-level | Yes; weak evidence should produce explicit no-change recommendations unless later upgraded. |
| discretionary management and psychology | DM2-C09 remains evidence note only, mostly cautionary and conditional. | Strategy B implements fixed 50% TP1, 50% final management, and break-even after TP1; it does not encode psychology or trader execution tolerance. | proxy mismatch or unresolved discretionary mismatch | documentation-only or unresolved | Yes for any management or psychology change. |

The future re-check should keep all findings as comparison findings. It should not present any mismatch as an implementation requirement.

## 5. Mismatch Classification Framework

A future mismatch re-check should use conservative classes:

| class | meaning | allowed output |
| --- | --- | --- |
| no material mismatch | Strategy A/B representation is sufficiently aligned with the draft proposal direction for planning purposes. | Note alignment and preserve no-change recommendation. |
| documentation mismatch | Existing docs describe the relationship unclearly, but code/spec changes are not implicated. | Recommend documentation clarification only. |
| specification mismatch | Existing Strategy A/B specification differs from a draft doctrine direction, but the v2 draft is non-final. | Record for human review; do not recommend implementation. |
| implementation mismatch candidate | Existing code appears to differ from an accepted spec or later accepted doctrine direction. | Only identify as candidate; do not change code in the re-check PR. |
| proxy mismatch | Strategy A/B uses a mechanical proxy for a broader or more discretionary doctrine concept. | Record proxy limits and no-change default unless separately approved. |
| unresolved discretionary mismatch | The doctrine concept remains too visual, discretionary, or under-defined to compare mechanically. | Keep unresolved; recommend manual-review questions, not code. |
| out of scope until Doctrine Map v2 acceptance | A comparison topic depends on final Doctrine Map v2 acceptance or separate project-owner approval. | Defer Strategy implication and preserve no-change recommendation. |

The future re-check must not classify anything as requiring implementation change. At most, it may identify candidate areas for later human review and separate approval.

## 6. Specific Planning Questions

The future mismatch re-check should answer questions such as:

1. Does Strategy A/B over-rely on EMA/reference-candle mechanics relative to the draft proposal, where EMA/reference-candle evidence remains evidence note only?
2. Does Strategy B's ADX proxy conflict with the draft proposal's structural range framing, or should ADX remain a fixed research proxy with explicit no-change guidance?
3. Does Strategy B's TP/RR implementation collapse separate concepts that the draft proposal keeps distinct, including structural TP, protective exit, staged management, RR threshold, and RR tolerance?
4. Does Strategy B's stop logic over-specify anchors, buffers, or sanity gates relative to premise-based stop doctrine?
5. Does Strategy A/B fail to represent breakout, damashi, sweep, and false-break context families, and should that remain an unresolved doctrine-to-strategy gap?
6. Does Strategy A/B encode a narrow wave/EMA setup while the draft proposal keeps wave context broader and discretionary?
7. Are management features such as partial exit, break-even, and protective exit supported as doctrine, or still separate research proxies?
8. Which issues are Strategy design limitations versus expected simplifications of a baseline strategy?
9. Which mismatch candidates are only documentation issues, and which would require separate Strategy specification review if Doctrine Map v2 is later accepted?
10. Which topics should receive explicit no-change recommendations because evidence remains weak, limited, or unresolved?

These are planning questions only. They do not authorize code, config, test, parameter, backtest, optimization, broker, live trading, or execution work.

## 7. Outputs for a Later Mismatch Re-check

A later actual `Strategy A/B mismatch re-check` PR should output:

- A comparison table for each v2 draft proposal dimension.
- Mismatch severity labels, if used, with conservative meanings.
- Affected Strategy A/B components, such as docs, spec, code, tests, config, parameters, or runner behavior.
- Whether each issue is docs-only, spec-only, code-relevant only after later approval, or unresolved.
- Explicit no-change recommendations where evidence is weak, limited, non-final, or unresolved.
- A list of possible future research questions, not implementation tasks.
- A guardrail section confirming no Strategy A/B modifications, no backtests, no optimization, no Batch 08, no market data, no broker logic, and no profitability claims.

The later re-check should not produce:

- Strategy A/B patches.
- Strategy B2 or Strategy C.
- Parameter proposals.
- Backtest commands or result tables.
- Market-data outputs.
- Live-trading or broker-execution changes.
- Profitability conclusions.

## 8. Guardrails for Future Mismatch Work

Any later mismatch re-check must not:

- Modify Strategy A/B code, parameters, configs, or tests.
- Create Strategy B2 or Strategy C.
- Tune parameters.
- Run backtests.
- Run optimization.
- Claim profitability.
- Use Batch 08.
- Access or fetch market data.
- Use broker APIs.
- Add broker, live trading, or execution logic.
- Access DownSub or YouTube unless separately authorized for a different bounded source-review task.
- Fetch captions.
- Download video or audio.
- Run ASR.
- Use proxies, VPN rotation, IP rotation, or platform-rate-limit bypass.
- Add raw subtitle, caption URL, CSV, JSON, database, `data/`, or `results/` artifacts.

The default recommendation for weak, limited, non-final, or unresolved evidence should be no Strategy change.

## 9. Decision Gates After a Future Re-check

After a future docs-only mismatch re-check, any additional work should pass explicit gates:

| gate | requirement |
| --- | --- |
| human review of mismatch findings | A project owner must review the mismatch findings before any Strategy implication is considered. |
| Doctrine Map status check | Confirm whether Doctrine Map v2 is still draft or has been separately accepted. |
| separate approval before spec change | Any Strategy A/B spec change requires a new approval and PR. |
| separate approval before code change | Any code, config, parameter, or test change requires a new approval and PR. |
| separate approval before backtest | Any backtest or result generation requires a new approval and PR. |
| no Strategy B2/C by default | Strategy B2 or Strategy C must not be created unless explicitly approved later. |
| no parameter optimization | Parameter optimization must remain out of scope unless a later task explicitly authorizes it. |
| no live execution path | Broker, live trading, and execution logic remain prohibited unless separately authorized in a different workflow. |

If any gate is not satisfied, the work should remain docs-only planning or review.

## 10. Recommended Next PR After This Plan

Recommended next docs-only PR:

`Strategy A/B mismatch re-check`

Reason:

- This plan defines comparison dimensions and guardrails.
- The next PR should perform the docs-only comparison.
- The next PR should still not modify Strategy A/B.
- The next PR should still not run backtests.
- The next PR should still not treat Doctrine Map v2 draft proposal as final doctrine.
- The next PR should still not include Batch 08.

The expected next PR should compare Strategy A/B against the non-final v2 draft proposal and reviewed candidate doctrine set, then record conservative no-change or defer recommendations where evidence remains weak, non-final, or unresolved.

## 11. Readiness Decision

`strategy_ab_doctrine_map_v2_draft_mismatch_recheck_plan_ready_for_human_review`

Reason: this docs-only plan defines safe comparison dimensions, conservative mismatch classes, future output expectations, guardrails, and decision gates for a later Strategy A/B mismatch re-check against the reviewed non-final Doctrine Map v2 draft proposal. It uses committed docs and read-only Strategy A/B context, does not modify Strategy A/B, does not create Strategy B2 or Strategy C, does not run backtests or optimization, does not access market data, does not include Batch 08, does not create final Doctrine Map v2, and does not imply profitability.

This plan does not state that Strategy A/B should change. It does not state that Doctrine Map v2 is final.
