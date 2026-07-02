# Doctrine Map v2 Candidate Review

Task: `doctrine_map_v2_candidate_review`

Review date: 2026-07-01

## 1. Objective and Scope

This is a docs-only candidate review for possible future Doctrine Map v2 drafting.

This review:

- Uses only existing committed documentation.
- Reviews high-level candidate families from the Corpus v2 Batch 01-07 audit synthesis.
- Classifies candidate families against current Channel Doctrine Map v1.
- Produces a conservative candidate backlog for later human review.

This review does not:

- Update Channel Doctrine Map v1.
- Create Channel Doctrine Map v2.
- Write final Doctrine Map v2 doctrine text.
- Modify Strategy A/B code, parameters, configs, or tests.
- Create Strategy B2 or Strategy C.
- Include Batch 08.
- Access DownSub, YouTube, captions, audio, video, or ASR.
- Run backtests or optimization.
- Make profitability claims.
- Add broker, live trading, or execution logic.
- Commit raw TXT, SRT, VTT, subtitle full text, caption URLs, CSV, JSON, database, `data/`, or `results/` artifacts.

## 2. Evidence Base

Primary evidence:

- `docs/video_research/doctrine_map_v2_candidate_update_plan.md`
- `docs/video_research/doctrine_map_v2_candidate_update_plan_review.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis.md`
- `docs/video_research/corpus_v2_batch_01_07_audit_synthesis_review.md`
- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/downsub_access_policy_v2.md`
- Batch 01 through Batch 07 completed-summary audit reports.
- Batch 01 through Batch 07 aggregate reports and quality reviews where needed.
- `docs/video_research/strategy_ab_channel_doctrine_map_v1_mismatch_analysis.md`

Corpus v2 Batch 01-07 audit synthesis coverage:

| metric | value |
| --- | ---: |
| completed-summary audit batches synthesized | 7 |
| total videos audited | 56 |
| total mechanical-rule candidates audited | 233 |

This review does not add new evidence. It does not re-fetch captions, re-run DownSub comparison, inspect video/audio, or create new summaries.

## 3. Review Method

This review uses the dispositions defined in the merged candidate update plan:

| disposition | meaning in this review |
| --- | --- |
| keep v1 unchanged | Corpus v2 Batch 01-07 does not materially change the v1 treatment. |
| strengthen existing doctrine | Corpus v2 Batch 01-07 strengthens or clarifies a v1 doctrine area, but final Doctrine Map v2 text is not written here. |
| add candidate doctrine | Corpus v2 Batch 01-07 supports a possible new doctrine candidate not clearly separated in v1. |
| keep as weak/limited evidence | Evidence is useful but one-off, low-confidence, setup-specific, incomplete, or not ready for doctrine. |
| reject as too discretionary | Evidence relies on undefined visual judgment or chart-only discretion and should remain unresolved. |

Standards applied:

- Require multi-video support before treating a claim as a doctrine candidate.
- Prefer multi-batch support for broadly worded doctrine candidates.
- Do not treat one-off examples as doctrine.
- Do not convert chart-only visual judgment into mechanical doctrine.
- Do not convert doctrine candidates into Strategy A/B implementation changes.
- Preserve confidence and limitations.
- Do not invent exact frequencies unless explicitly present in committed docs.

## 4. Candidate Family Review Table

| candidate family | current v1 coverage | Corpus v2 support summary | v1 impact | discretion boundary | disposition | confidence | limitation | later Strategy A/B mismatch re-check? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| entries and confirmation | V1 treats entry confirmation and delayed trigger as strong recurring evidence, but setup-specific anchors differ. | Corpus v2 synthesis repeats that entries depend on concrete triggers or filters such as line close, pullback confirmation, reference candle behavior, breakout confirmation, false-break recovery, and delayed confirmation. | strengthens v1 | Confirmation forms remain setup-specific and should not become one universal trigger. | strengthen existing doctrine | high | Future wording must preserve multiple confirmation families rather than collapse them into one rule. | yes; Strategy A/B currently encodes one reference-candle confirmation form. |
| stop placement and invalidation | V1 says stops should tie to premise, wave, pattern, range, pullback, or structural backing, while exact anchors and widths remain under-specified. | Corpus v2 synthesis supports premise failure, pattern or wave invalidation, structural backing, relevant pivots, and rejection of unclear stop placement. | strengthens but narrows v1 | Exact stop anchor, buffer, width, and visual pivot choice remain unresolved. | strengthen existing doctrine | medium | Doctrine review can strengthen premise-based stop language but should not specify numeric buffers. | yes; Strategy B uses deterministic stop anchors, ATR buffer, and stop sanity proxies. |
| TP, exit, and RR | V1 separates TP, exit, RR, protective exit, partial exit, and management; RR is contextual rather than universal. | Corpus v2 synthesis supports structural or realistic targets, staged exits, stop distance interaction, target quality, and trader execution tolerance. | strengthens v1 | Target priority, partial-exit sizing, break-even movement, and fixed RR thresholds remain unresolved. | strengthen existing doctrine | medium | Keep TP, protective exit, management, and RR threshold separate; do not produce a universal TP/RR rule. | yes; Strategy B has fixed structural TP, partial management, break-even, and RR gates. |
| breakout, damashi, sweep, and false-break handling | V1 treats this as recurring but incomplete as a full system. | Corpus v2 synthesis supports line quality, higher-timeframe confirmation, wave shape, sweep/reclaim behavior, triangle false-break caution, and delayed confirmation. | strengthens v1 | Evidence is a context-filter family, not a complete entry-stop-TP-management system. | strengthen existing doctrine | medium | Any future doctrine should avoid "always fade" or one-size breakout language. | yes; Strategy A/B does not represent this context family directly. |
| range handling | V1 includes range maturity, trend/range context, pattern-quality blockers, and local-entry vetoes. | Corpus v2 synthesis supports structural range detection, boundary touch requirements, short-term range-entry caution, and higher-timeframe veto checks. | strengthens v1 | Range quality remains partly visual and not reducible to one indicator-only filter. | strengthen existing doctrine | medium | Keep range as structural and contextual; do not convert to a numeric or ADX-only range rule. | yes; Strategy B uses ADX as a proxy but v1 does not establish ADX doctrine. |
| wave context | V1 uses wave context across entry, stop, TP, timeframe, and pattern-quality doctrines. | Corpus v2 synthesis supports wave stage, wave-aligned stop/TP anchors, third-wave examples, pullback waiting, and higher-timeframe/monitored-timeframe overlap. | strengthens v1 | Wave count, wave cleanliness, pivot selection, and wave room remain discretionary. | strengthen existing doctrine | medium | Future doctrine can preserve wave as context, but mechanical wave rules remain unresolved. | yes; Strategy A/B encodes a narrow EMA/wave-style setup. |
| EMA and reference-candle context | V1 classifies EMA/MA as setup-specific or secondary; ADX is not established. | Corpus v2 synthesis notes EMA/reference-candle evidence in applied third-wave examples, including moving-average context, 20EMA touch, candle-close confirmation, 200EMA environment, and staged targets. | does not materially change v1 | EMA evidence is setup-specific and does not override non-indicator context. | keep as weak/limited evidence | low | Keep EMA/reference-candle evidence as a setup-specific candidate, not broad indicator doctrine. | yes; Strategy A/B is centered on EMA/reference-candle mechanics. |
| higher-timeframe context | V1 treats timeframe hierarchy as one of the strongest recurring doctrines. | Corpus v2 synthesis supports higher-timeframe context as a recurring veto or filter for local entries, range trades, breakout decisions, wave interpretation, and target/stop timeframe alignment. | strengthens v1 | Timeframe ownership still needs careful wording for premise, trigger, stop, target, and execution. | strengthen existing doctrine | high | Future wording should distinguish higher-timeframe context from a fixed single timeframe rule. | yes; Strategy A/B fixes the validation timeframe and narrower context mechanics. |
| discretionary management and psychology | V1 treats trade management as bounded and often case-specific; discretionary blockers are a major automation blocker. | Corpus v2 synthesis supports mid-profit taking, protective exit, break-even or stop-change warnings, execution tolerance, and warnings against copying advanced management without understanding. | narrows v1 | Most management and psychology evidence is cautionary, conditional, or not mechanically specified. | keep as weak/limited evidence | low | Preserve as caution and review context, not universal management doctrine. | yes, but only after a doctrine review separates protective exit, TP, partial exit, and psychology. |

No reviewed family contradicts v1 outright. The main effect of Corpus v2 Batch 01-07 is to strengthen several existing v1 areas while reinforcing that EMA/reference-candle and discretionary management evidence remain limited or setup-specific.

## 5. Candidate Doctrine Backlog

These are candidate items only. They are not accepted doctrine and are not final Doctrine Map v2 text.

| candidate label | source family | proposed disposition | confidence | limitation | required follow-up before Doctrine Map v2 drafting |
| --- | --- | --- | --- | --- | --- |
| DM2-C01 | higher-timeframe context | strengthen existing doctrine | high | Needs wording that separates premise timeframe, monitored timeframe, and execution timeframe. | Confirm that future wording preserves setup-specific timeframe ownership and avoids a fixed-timeframe rule. |
| DM2-C02 | entries and confirmation | strengthen existing doctrine | high | Confirmation categories remain setup-specific. | Group confirmation forms without converting them into one trigger. |
| DM2-C03 | stop placement and invalidation | strengthen existing doctrine | medium | Exact anchors, buffers, and stop width remain visual or absent in some examples. | Separate stop-anchor validity from stop-width tolerance and avoid numeric buffers. |
| DM2-C04 | TP, exit, and RR | strengthen existing doctrine | medium | Target priority, partial exit, protective exit, and RR threshold remain distinct. | Draft a taxonomy before proposing any Doctrine Map v2 wording. |
| DM2-C05 | breakout, damashi, sweep, and false-break handling | strengthen existing doctrine | medium | Full setup-entry-stop-TP-management sequence remains incomplete. | Preserve as context/filter doctrine, not a full breakout system. |
| DM2-C06 | range handling | strengthen existing doctrine | medium | Range maturity and dirty-range concepts remain visual. | Define structural range language without reducing it to ADX or another indicator. |
| DM2-C07 | wave context | strengthen existing doctrine | medium | Wave count and wave cleanliness remain discretionary. | Keep wave as context unless a later review defines mechanical labels. |
| DM2-C08 | EMA and reference-candle context | keep as weak/limited evidence | low | Setup-specific examples do not justify broad indicator doctrine. | Keep in evidence notes and compare later against Strategy A/B mismatch only as a narrow setup family. |
| DM2-C09 | discretionary management and psychology | keep as weak/limited evidence | low | Mostly cautionary or conditional, with limited implementation detail. | Separate management warnings from positive procedures before any doctrine drafting. |
| DM2-C10 | discretionary chart-reading terms | reject as too discretionary | unresolved | Terms such as clean wave, valid line, target realism, strong reason, market fuel, and scenario coherence are not mechanically specified. | Keep as unresolved blockers until a future manual-review protocol defines them. |

## 6. Weak, Limited, or Rejected Evidence

These evidence families should not become Doctrine Map v2 doctrine yet:

- EMA and reference-candle evidence as broad indicator doctrine: useful setup-specific evidence, but not enough to state channel-wide indicator doctrine.
- Universal partial-exit or staged-exit procedure: present in examples, but sizing, timing, and applicability are not established.
- Break-even movement as a universal rule: supported only as limited or cautionary evidence, not a repeatable procedure.
- Advanced stop movement: warning evidence exists, but warning evidence is not a positive implementation rule.
- Scenario planning as mechanical doctrine: useful concept, but scenario coherence remains visual and under-specified.
- Clean wave, valid line, line strength, target realism, market fuel, strong reason, wave room, and dirty structure: important review terms, but too discretionary for doctrine text unless future work defines them carefully.
- ADX and session/time-of-day rules: v1 treats these as not established in the completed summaries; Corpus v2 does not change that conclusion.
- Management or psychology cautions without implementation detail: valuable boundary evidence, but not enough for doctrine or Strategy rules.

## 7. Strategy A/B Mismatch Implications

This review does not modify Strategy A/B.

Potential later mismatch re-check areas, if a future Doctrine Map v2 candidate review is accepted by the project owner:

| area | why it may need later mismatch re-check |
| --- | --- |
| higher-timeframe context | Strategy A/B uses a narrower fixed setup/timeframe representation than the doctrine candidate family. |
| entries and confirmation | Strategy A/B encodes one reference-candle confirmation sequence while the candidate family includes multiple confirmation forms. |
| stop placement and invalidation | Strategy B uses deterministic stop anchors, buffers, and sanity limits while doctrine candidates keep premise-based anchors contextual. |
| TP, exit, and RR | Strategy B combines structural targets, partial exit, break-even movement, and fixed RR gates, while doctrine candidates keep these distinct. |
| breakout, damashi, sweep, and false-break handling | Strategy A/B does not directly model the context-filter family. |
| range handling | Strategy B's ADX proxy should remain a research proxy unless later doctrine review supports an indicator or structural range approach. |
| wave context | Strategy A/B uses a narrow EMA/wave interpretation while doctrine candidates keep wave context broader and discretionary. |
| EMA and reference-candle context | Strategy A/B depends heavily on this weak/limited setup-specific evidence, so any mismatch re-check should keep it narrow. |
| discretionary management and psychology | Strategy A/B should not absorb cautionary management or psychology evidence without a separate specification. |

This is planning guidance only. It does not authorize code changes, parameter changes, tests, Strategy B2, Strategy C, backtests, optimization, live trading, broker logic, or profitability claims.

## 8. Batch 08 Boundary

Batch 08 remains excluded from this Doctrine Map v2 candidate review.

Batch 08 should not be mixed into Doctrine Map v2 candidate review unless the project owner separately approves and audits a bounded Batch 08 workflow under `docs/video_research/downsub_access_policy_v2.md`. Until then, Batch 08 evidence should not be used to strengthen, weaken, add, or reject Doctrine Map v2 candidate items.

## 9. Readiness Decision

`doctrine_map_v2_candidate_review_ready_for_human_review`

Reason: this docs-only candidate review uses the merged Doctrine Map v2 candidate update plan, Corpus v2 Batch 01-07 audit synthesis, current Doctrine Map v1, and existing committed supporting docs to classify high-level candidate families and create a conservative candidate backlog. It is ready for human review as a planning document. It does not state that Doctrine Map v2 is ready, does not create Doctrine Map v2, does not update Doctrine Map v1, does not include Batch 08, and does not authorize Strategy A/B changes.
