# Strategy A/B Doctrine Map v2 Draft Mismatch Re-check

Task: `strategy_ab_doctrine_map_v2_draft_mismatch_recheck`

Re-check date: 2026-07-01

## 1. Objective and Scope

This is a docs-only comparison of Strategy A/B against the reviewed, non-final Channel Doctrine Map v2 draft proposal and candidate doctrine set.

This re-check:

- Compares current Strategy A/B assumptions against reviewed v2 draft proposal dimensions.
- Uses conservative mismatch classes from `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_plan.md`.
- Records safe no-change, defer, or review-only recommendations.

This re-check does not:

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

This re-check uses only committed evidence and repository files.

Primary docs:

- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_plan.md`
- `docs/video_research/strategy_ab_doctrine_map_v2_draft_mismatch_recheck_plan_review.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal_human_review.md`
- `docs/video_research/channel_doctrine_map_v2_draft_proposal.md`
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
- Strategy A/B test files were searched read-only only to confirm existing assumption coverage.

Known Corpus v2 Batch 01-07 synthesis coverage:

| metric | value |
| --- | ---: |
| completed-summary audit batches | 7 |
| audited videos | 56 |
| audited mechanical-rule candidates | 233 |

This re-check does not add new evidence, access subtitles, access market data, run Strategy A/B, run tests, or generate result artifacts.

## 3. Method

This re-check uses the mismatch classes defined in the merged plan:

| class | use in this re-check |
| --- | --- |
| no material mismatch | Strategy A/B is sufficiently aligned for planning purposes. |
| documentation mismatch | Relationship between Strategy A/B and the draft proposal may need clearer documentation only. |
| specification mismatch | Strategy A/B specification differs from a draft proposal direction, but the v2 draft is non-final. |
| implementation mismatch candidate | Code may later need review only if a separate accepted spec or doctrine requires it. |
| proxy mismatch | Strategy A/B uses a mechanical proxy for a broader or more discretionary draft doctrine concept. |
| unresolved discretionary mismatch | Draft doctrine concept remains too visual, discretionary, or under-defined for mechanical comparison. |
| out of scope until Doctrine Map v2 acceptance | Any Strategy implication must wait for separate acceptance and approval. |

No item is classified as requiring implementation change. Severity labels below are for research review only and do not imply code priority.

## 4. Comparison Table

| dimension | v2 draft proposal direction | current Strategy A representation | current Strategy B representation | mismatch class | affected artifact type | research-review severity | safe recommendation | must future work wait until Doctrine Map v2 acceptance? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| higher-timeframe context | DM2-C01 proposes stronger timeframe hierarchy, distinguishing premise timeframe, monitored timeframe, and execution timeframe. | Fixed 4H EMA20/EMA200 setup; no separate premise, monitored, execution, stop, or target timeframe ownership. | Keeps Strategy A's fixed 4H entry setup; adds 4H ATR, ADX, and left-side swing targets but still does not assign separate timeframe ownership. | specification mismatch | docs/spec; code only after later approval | medium | keep as known baseline limitation | yes for any Strategy change |
| entries and confirmation | DM2-C02 groups confirmation families: candle close, pullback or return behavior, line reaction, false-break recovery, and second confirmation. | Uses first 20EMA touch as reference candle and body-close break of that reference high/low with next-candle-open entry. | Keeps Strategy A entry sequence unchanged; additional filters happen after the same reference-candle confirmation. | specification mismatch | docs/spec | medium | keep as known baseline limitation | yes for alternate trigger or code behavior |
| stop placement and invalidation | DM2-C03 strengthens premise-based stop/invalidation and separates stop-anchor validity from stop-width tolerance. | Uses reference-candle high/low plus configured buffer; no broader premise invalidation model. | Uses nearest valid left-side swing or reference candle anchor, ATR buffer, and `0.25 * ATR(14)` to `3.0 * ATR(14)` stop-distance sanity gates. | proxy mismatch | spec/parameters/code later only if approved | medium | candidate for later specification review only | yes |
| TP, exit, and RR | DM2-C04 keeps target selection, protective exit, staged management, RR threshold, RR tolerance, and trader execution burden distinct. | Uses fixed RR full exit, default `1.5R`, with no structural TP, partial exit, or protective exit. | Uses left-side swing TP1/TP2, TP1/TP2/RR gates, 50% TP1 and 50% final management, and break-even after TP1. | proxy mismatch | docs/spec/parameters | high | candidate for later specification review only | yes |
| breakout, damashi, sweep, and false-break handling | DM2-C05 frames breakout, damashi, sweep, and false-break as a context-filter family, not a full system. | Does not model breakout, damashi, sweep, false-break recovery, line quality, or reclaim context. | Does not model this family directly; left-side swings, ADX, and no-trade reasons do not represent false-break context. | unresolved discretionary mismatch | unresolved/docs | high | defer until manual-review protocol exists | yes |
| range handling | DM2-C06 keeps range handling structural and contextual; it should not be reduced to an indicator-only proxy. | No range filter. | Uses ADX(14) below 18 as a fixed no-trade proxy; EMA slope is documented as later comparison-only, not first-pass default. | proxy mismatch | spec/parameters | medium | keep as known proxy limitation | yes for changing ADX or adding structural range logic |
| wave context | DM2-C07 preserves wave stage, wave-aligned stops/targets, pullback waiting, and timeframe overlap while keeping wave count and cleanliness discretionary. | Approximates one EMA/wave-like setup through EMA cross, first 20EMA touch, reference-candle confirmation, and fixed RR. | Keeps the same EMA/reference-candle setup and adds swing target/stop proxies, but does not define wave count, wave room, or wave cleanliness. | proxy mismatch; unresolved discretionary mismatch | unresolved/spec | high | defer until manual-review protocol exists | yes |
| EMA and reference-candle context | DM2-C08 remains evidence note only and does not justify broad indicator doctrine. | Core strategy depends heavily on EMA20/EMA200, first 20EMA touch, and reference-candle confirmation. | Keeps the same EMA/reference-candle core and adds mechanical management/filter proxies. | proxy mismatch; out of scope until Doctrine Map v2 acceptance | docs/spec | high | no change because evidence is weak and non-final | yes |
| discretionary management and psychology | DM2-C09 remains evidence note only; much support is cautionary, conditional, or psychology-bound. | No partial exit, break-even, protective exit, stop movement, or psychology model. | Fixed 50% TP1, 50% final management, break-even after TP1, and same-bar assumptions; no psychology or execution-tolerance model. | proxy mismatch; unresolved discretionary mismatch | docs/spec/parameters | medium | no change; keep as research proxy limitation | yes |

## 5. Specific Issue Evaluation

| issue | conservative evaluation | safe recommendation |
| --- | --- | --- |
| EMA/reference-candle reliance | Strategy A/B relies heavily on EMA/reference-candle mechanics while DM2-C08 remains evidence note only. This is a material proxy limitation, but it is also the expected identity of the current baseline strategy. | no change because evidence is weak, non-final, and setup-specific |
| ADX range proxy | Strategy B's ADX(14) below 18 filter is an indicator proxy, while DM2-C06 frames range handling as structural and contextual. This is a proxy mismatch, not proof that ADX is wrong. | keep as known proxy limitation |
| TP/RR concept collapse | Strategy B combines structural TP1/TP2, fixed RR gates, partial exit, and break-even into one rule stack, while DM2-C04 keeps these concepts distinct. | candidate for later specification review only |
| stop anchor, buffer, and sanity gates | Strategy B over-specifies deterministic stop anchors, ATR buffer, and sanity gates relative to DM2-C03's premise-based stop doctrine. This makes Strategy B testable but narrower than draft doctrine. | candidate for later specification review only |
| missing breakout/damashi/sweep/false-break context | Strategy A/B does not represent the DM2-C05 context-filter family. Because the draft proposal does not define a complete mechanical system, this should remain unresolved. | defer until manual-review protocol exists |
| narrow wave/EMA setup | Strategy A/B encodes a narrow EMA/wave-style proxy while DM2-C07 keeps wave context broader and discretionary. | defer until manual-review protocol exists |
| management features | Strategy B's partial exit and break-even rules are fixed research proxies, not accepted doctrine; protective exit remains separate and not implemented. | no change; keep as research proxy limitation |
| design limitation versus simplification | Fixed 4H, EMA/reference-candle confirmation, ADX, fractal swings, RR gates, and 50/50 management are expected simplifications for a baseline research strategy. They become possible concerns only if treated as channel-wide doctrine. | keep as known baseline limitation |

No evaluated issue supports immediate Strategy A/B implementation change.

## 6. No-change and Defer Recommendations

| dimension | explicit recommendation |
| --- | --- |
| higher-timeframe context | keep as known baseline limitation |
| entries and confirmation | keep as known baseline limitation |
| stop placement and invalidation | candidate for later specification review only |
| TP, exit, and RR | candidate for later specification review only |
| breakout, damashi, sweep, and false-break handling | defer until manual-review protocol exists |
| range handling | keep as known proxy limitation |
| wave context | defer until manual-review protocol exists |
| EMA and reference-candle context | no change |
| discretionary management and psychology | no change |

This re-check does not recommend immediate Strategy A/B implementation changes.

Any candidate for later specification review requires separate project-owner approval. Any candidate for later implementation review requires Doctrine Map status review, a separate Strategy specification task, a separate code-change approval, and a separate PR.

## 7. Strategy A/B Implications

### Harmless Simplifications

These appear to be expected simplifications of the current baseline strategy rather than defects:

- fixed 4H validation timeframe;
- Strategy A's fixed RR full exit;
- reference-candle body-close confirmation as a narrow entry trigger;
- Strategy A omitting range filters, structural TP, partial exit, and discretionary wave judgment.

### Known Proxy Limitations

These should be documented as proxies, not doctrine:

- Strategy B's ADX range filter as a proxy for structural range context;
- Strategy B's left-side fractal swings as a proxy for structural targets and stop anchors;
- Strategy B's ATR buffer and stop-distance sanity gates as proxies for stop-width tolerance;
- Strategy B's 50% TP1 and break-even rules as proxies for broader management concepts.

### Possible Future Spec Review Areas

These may deserve later specification review only after human review and separate approval:

- whether stop-anchor validity and stop-width tolerance should be documented separately in Strategy B;
- whether Strategy B TP, RR gates, partial exit, and break-even should be documented as one fixed research stack or separated in future docs;
- whether the current mismatch findings should be reflected in Strategy A/B documentation before any future research run.

### Must Remain Unresolved

These must remain unresolved because the draft doctrine remains visual or discretionary:

- clean wave;
- valid line;
- target realism;
- strong reason;
- market fuel;
- scenario coherence;
- wave room;
- dirty structure;
- breakout, damashi, sweep, and false-break context as a full mechanical system.

### Explicit No-change Findings

No Strategy A/B change is recommended for:

- EMA/reference-candle reliance, because the evidence remains weak, setup-specific, and non-final.
- ADX, because it is a known research proxy and this PR does not authorize changing filters.
- TP/RR gates, because changing them would be parameter or spec work outside this PR.
- Partial exit and break-even, because management evidence remains limited and cautionary.
- Any Strategy B2 or Strategy C work.

## 8. Guardrails

This PR does not:

- modify Strategy A/B code, parameters, configs, or tests;
- create Strategy B2 or Strategy C;
- tune parameters;
- run backtests;
- run optimization;
- claim profitability;
- use Batch 08;
- access or fetch market data;
- use broker APIs;
- add broker, live trading, or execution logic;
- update `docs/video_research/channel_doctrine_map_v1.md`;
- create or update `docs/video_research/channel_doctrine_map_v2.md`;
- treat the Doctrine Map v2 draft proposal as final or accepted doctrine;
- access DownSub or YouTube;
- fetch captions;
- download video or audio;
- run ASR;
- use proxies, VPN rotation, IP rotation, or platform-rate-limit bypass;
- add raw subtitle, caption URL, CSV, JSON, database, `data/`, or `results/` artifacts.

## 9. Recommended Next PR

Recommended next docs-only PR:

`Strategy A/B mismatch re-check human review`

Reason:

- This re-check creates comparison findings.
- The findings should be reviewed before any Strategy B TP1 selection work resumes.
- Strategy B TP1 selection review should use the mismatch findings as context, but should not automatically inherit all doctrine candidates.
- Doctrine Map v2 remains non-final, so `Doctrine Map v2 acceptance decision plan` should not be used to skip human review of these mismatch findings.

The next PR should still be docs-only. It should not modify Strategy A/B, create Strategy B2 or Strategy C, run backtests, optimize, access market data, or make profitability claims.

## 10. Readiness Decision

`strategy_ab_doctrine_map_v2_draft_mismatch_recheck_ready_for_human_review`

Reason: this docs-only comparison identifies conservative Strategy A/B mismatch findings against the reviewed, non-final Channel Doctrine Map v2 draft proposal while preserving no-change, defer, and review-only recommendations. It uses committed docs and read-only Strategy A/B context, does not modify Strategy A/B, does not create Strategy B2 or Strategy C, does not run backtests or optimization, does not access market data, does not include Batch 08, does not create final Doctrine Map v2, and does not imply profitability.

This readiness decision does not state that Strategy A/B should change. It does not state that Doctrine Map v2 is final.
