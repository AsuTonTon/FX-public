# Strategy A/B vs Channel Doctrine Map v1 Mismatch Analysis

Task: `strategy_ab_channel_doctrine_map_v1_mismatch_analysis`

## 1. Executive summary

This is a docs-only diagnostic comparison between the current Strategy A/B
mechanical assumptions and the provisional Channel Doctrine Map v1.

The main conclusion is that Strategy A/B is not "wrong" based on the doctrine
map, but it is materially narrower than the provisional channel doctrine in
several areas:

- Strategy A/B encodes a single 4H EMA/wave-style setup, while the doctrine map
  treats timeframe context as broader and setup-dependent.
- Strategy A/B has clear confirmation mechanics, but the doctrine map uses
  confirmation more broadly: candle close, reaction, return behavior, line
  credibility, and surrounding context.
- Strategy B adds structural TP, stop anchoring, partial exit, break-even, and
  ADX, but its current mechanics remain fixed proxies for concepts that the
  doctrine map treats as contextual or discretionary.
- Strategy B TP1, stop-anchor, and RR decisions remain frozen by the current
  TP1 decision cycle. This analysis does not reopen them.
- The doctrine map is a planning reference, not an implementation spec.

No Strategy A/B rule, parameter, code, test, data, result, transcript, caption,
video, or trading-execution artifact is changed by this report.

## 2. Evidence base used

This analysis uses only existing Git-tracked, Git-safe documents already present
on `main`.

Primary doctrine documents:

- `docs/video_research/channel_doctrine_map_v1.md`
- `docs/video_research/channel_doctrine_map_v1_executive_synthesis.md`
- `docs/video_research/channel_doctrine_map_v1_quality_review.md`
- `docs/video_research/channel_doctrine_evidence_index_v1.md`
- `docs/video_research/channel_doctrine_gap_backlog_v1.md`

Primary Strategy A/B documents:

- `docs/video_research/vkaA9MCRlx4/backtest_spec_v1.md`
- `docs/video_research/vkaA9MCRlx4/strategy_a_implementation_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_spec_design.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_implementation_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_memo.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`

Batch 08 is not treated as completed evidence. No new video information
collection was performed.

## 3. Current Strategy A/B mechanics summarized

Strategy A is the core mechanical baseline:

- 4H OHLC input.
- EMA20 and EMA200 calculated from close.
- Long setup after EMA20 crosses above EMA200.
- Short setup after EMA20 crosses below EMA200.
- First 20EMA touch after the cross becomes the reference candle.
- Confirmation requires a body-close break of the reference candle high or low.
- Entry is the next candle open after confirmation.
- Stop is the reference candle low or high plus a fixed buffer.
- Take profit is a fixed RR full exit.
- It deliberately excludes left-side structural TP, range filtering, partial
  exit, break-even movement, and discretionary wave/pattern evaluation.

Strategy B keeps Strategy A's setup and entry sequence, then adds fixed
video-like mechanical proxies:

- left-side fractal swing TP1 and TP2;
- TP1, TP2, and TP1-only minimum RR gates;
- ATR(14) buffer;
- stop distance sanity limits;
- 50% TP1 and 50% final management;
- break-even stop on the remaining 50% after TP1;
- ADX(14) range filter;
- detailed no-trade reasons.

The closed TP1 decision cycle freezes current Strategy B TP1 selection, TP1
minimum RR, TP2 minimum RR, TP1-only minimum RR, stop-anchor logic, stop-buffer
logic, stop sanity logic, ADX filter, and Strategy B2 status.

## 4. Channel Doctrine Map v1 principles summarized

The provisional doctrine map is based on completed Git-safe Batch 01 through
Batch 07 summaries. It is not final channel doctrine and is not implementation
guidance.

High-confidence planning principles:

- Higher-timeframe or monitored-timeframe context gates local signals.
- Entry is delayed until confirmation, reaction, or context appears.
- Structural context comes before trigger interpretation.
- RR is contextual rather than a universal fixed threshold.
- Discretionary chart-review terms remain a major blocker.
- ADX and repeatable session/time-of-day rules are not established in the
  completed summaries.

Medium-confidence planning principles:

- Stop or invalidation should be tied to premise, wave, pattern, range,
  pullback, or structural backing.
- Initial TP should usually be structural or realistic rather than arbitrary.
- Protective or early exit may apply when premise, path, price action, or
  expected wave weakens.
- Horizontal lines are context, construction, reaction, target, or scenario
  tools, not standalone entry permission.
- False-break, damashi, sweep, and stop-run filters recur but are incomplete as
  a coded system.
- Trend, range, scenario, and pattern quality can veto tempting entries.

Low-confidence or not-yet-codeable principles include staged partial/full exit,
break-even movement, advanced stop movement, EMA/MA as setup-specific context,
event timing, and scenario planning.

## 5. Mismatch table

| Theme | Strategy A/B classification | Mismatch summary |
| --- | --- | --- |
| Timeframe context | narrower than doctrine | Strategy A/B fixes a 4H EMA/wave setup, while the doctrine map treats timeframe hierarchy as broader and setup-dependent. |
| Confirmation logic | partially aligned | Strategy A/B waits for body-close confirmation, but the doctrine map includes additional reaction, return, line, and context forms. |
| Structural context | narrower than doctrine | Strategy B uses left-side fractal swings, but does not mechanize lines, channels, ranges, false breaks, sweep context, scenario quality, or pattern quality. |
| TP / exit doctrine | partially aligned | Strategy B uses left-side structural targets and staged management, but the doctrine map does not confirm the current target-priority or management procedure as universal. |
| Stop / invalidation doctrine | partially aligned | Strategy B uses structural stop anchors and ATR buffer, but exact premise-based anchors and stop-width tolerances remain under-specified in doctrine evidence. |
| Risk-reward doctrine | broader than doctrine | Strategy B uses fixed minimum RR gates; the doctrine map says RR appears contextual and does not confirm universal fixed thresholds. |
| Discretionary blockers | blocked by discretionary / non-mechanical concepts | Clean wave, valid line, strong reason, target realism, market fuel, and scenario coherence are not mechanically represented. |
| ADX / indicator usage | unsupported by current doctrine evidence | EMA/MA appears setup-specific; ADX is not established as a corpus-wide mechanical trend-strength rule. |
| Small-bankroll / asymmetric bet doctrine | unsupported by current doctrine evidence | The current doctrine map used here does not establish this as Strategy A/B rule evidence; it remains separate from rule design and capital allocation. |

## 6. Mismatch categories by theme

### 6.1 Timeframe context

Classification: `narrower than doctrine`.

Strategy A/B assumes the validation timeframe is 4H. This is consistent with
the source-video interpretation, but the doctrine map's timeframe hierarchy is
broader: local signals may need higher-timeframe context, monitored-timeframe
confirmation, trend context, wave context, or outside grounds.

Mismatch category:

- Strategy A/B encodes a fixed timeframe rather than a hierarchy of premise
  timeframe, monitored timeframe, and execution timeframe.
- Strategy A/B does not mechanically assign ownership of a line, wave, target,
  or stop to the timeframe that produced it.

No code change is authorized from this mismatch.

### 6.2 Confirmation logic

Classification: `partially aligned`.

Strategy A/B is aligned with the doctrine map's broad delayed-confirmation
principle because it avoids entry at the EMA cross alone and waits for a
reference-candle body break, with entry at the next open.

The mismatch is that the doctrine map treats confirmation as setup-specific:
close confirmation, reaction, return behavior, false-break response, line
credibility, second confirmation, and broader context can all matter. Strategy
A/B currently represents only one confirmation form.

Mismatch category:

- Strategy A/B confirmation may be too literal relative to the corpus.
- Strategy A/B does not encode line reaction, reclaim behavior, return checks,
  or context-before-trigger confirmation families.

No alternate trigger is proposed here.

### 6.3 Structural context

Classification: `narrower than doctrine`.

Strategy B adds structure through left-side swing targets and stop-side swing
anchors. That is directionally aligned with doctrine, but much narrower than
the map's structural context categories.

Missing or unresolved mechanical concepts:

- line construction and line execution;
- wave room and wave quality;
- channel or pattern objectives;
- range maturity and dirty-range vetoes;
- false-break, damashi, sweep, and stop-run context;
- scenario coherence;
- pattern-quality blockers;
- prior-swing relevance beyond nearest fractal rank.

Mismatch category:

- Strategy B represents structure as fractal swing levels, while the doctrine
  map treats structure as a broader context layer that changes signal meaning.

This is a research blocker, not an implementation instruction.

### 6.4 TP / exit doctrine

Classification: `partially aligned`.

Strategy B aligns with the structural-TP theme by using left-side swing TP1 and
TP2 instead of fixed RR targets. It also includes partial exit and break-even
movement after TP1.

The mismatch is that the doctrine map separates initial TP, structural TP,
protective exit, partial exit, mid-profit discretionary exit, break-even
movement, and advanced stop movement. Strategy B currently turns several of
these into one fixed procedure. The TP1 decision cycle already concluded that
current rank-1 TP1 and existing gates should remain frozen pending stronger
evidence.

Mismatch category:

- Strategy B may collapse multiple TP/exit concepts into one rule stack.
- Current rank-1 TP1 may be a narrow proxy for target realism, but the existing
  closure decision is preserved.
- Protective exit and initial TP should remain separate future evidence
  questions.

This report does not reopen TP1 implementation.

### 6.5 Stop / invalidation doctrine

Classification: `partially aligned`.

Strategy B uses a stop-side structural anchor, ATR-aware buffer, and stop
distance sanity limits. This is conceptually aligned with premise-based
invalidation, but the doctrine map does not provide one universal stop anchor,
buffer, or stop-width threshold.

Mismatch category:

- Strategy B defines a deterministic stop anchor; the doctrine map treats
  premise validity, wave origin, pullback, range boundary, and pattern
  invalidation as context-dependent.
- Strategy B defines numeric stop-width sanity limits; the doctrine map
  distinguishes stop-anchor validity from stop-width tolerance but does not
  mechanize either universally.

Stop-anchor and stop-buffer logic remain frozen by the Strategy B TP1 closure.

### 6.6 Risk-reward doctrine

Classification: `broader than doctrine`.

Strategy B uses fixed minimum RR gates:

- TP1 must be at least `1.0R`;
- TP2 must be at least `1.5R` when TP2 exists;
- TP1-only exits require TP1 at least `1.5R`.

The doctrine map says RR is contextual and tied to stop placement, target
quality, confirmation cost, timeframe, trader tolerance, and the burden of
holding through losses. It does not confirm a universal fixed RR replacement
threshold.

Mismatch category:

- Strategy B's RR gates are deterministic research constraints, not confirmed
  corpus doctrine.
- Lowering, removing, or optimizing RR gates is not authorized.
- Any future RR design memo would need non-outcome-selected evidence that
  separates RR threshold, RR tolerance, stop validity, and target validity.

### 6.7 Discretionary blockers

Classification: `blocked by discretionary / non-mechanical concepts`.

The doctrine map repeatedly preserves terms that are useful for human review
but not yet mechanically defined:

- clean wave;
- valid line;
- line strength;
- touch quality;
- strong reason;
- target realism;
- market fuel;
- momentum weakness;
- dirty structure;
- candle strength;
- wave room;
- horizontal-axis sufficiency;
- scenario coherence.

Mismatch category:

- Strategy A/B omits these concepts or replaces them with narrow proxies such
  as EMA cross, fractal swing, ATR, ADX, and RR gates.
- The doctrine map does not yet supply numeric definitions that could be used
  without adding overfitting risk.

These remain research blockers.

### 6.8 ADX / indicator usage

Classification: `unsupported by current doctrine evidence`.

Strategy B uses ADX(14) below `18` as a no-trade filter. The doctrine map says
ADX is not established as a corpus-wide mechanical trend-strength rule. EMA/MA
evidence exists, but appears setup-specific or secondary, and indicator-primary
entries are not supported.

Mismatch category:

- ADX may be a useful fixed research proxy, but it is not confirmed channel
  doctrine.
- The current evidence does not authorize removing, retuning, or replacing ADX.
- The future evidence question is whether remaining caption-supported examples
  establish any repeatable trend-strength proxy at all.

### 6.9 Small-bankroll / asymmetric bet doctrine

Classification: `unsupported by current doctrine evidence`.

The current evidence base used for this analysis does not establish
small-bankroll growth, high leverage, overseas FX execution, or asymmetric bet
thinking as Strategy A/B rule doctrine.

Mismatch category:

- If future Git-safe doctrine evidence mentions small-account or asymmetric
  risk framing, it should be treated as a separate capital-management research
  topic.
- It should not be mixed into Strategy A/B entry, stop, TP, RR, broker, or
  execution design from this report.

This report does not recommend real-money trading, overseas FX, high leverage,
broker execution, or capital allocation changes.

## 7. What is not authorized

This mismatch analysis does not authorize:

- Strategy A rule changes;
- Strategy B rule changes;
- Strategy B2;
- Strategy C;
- parameter changes;
- config or test changes;
- code changes;
- backtests;
- optimization;
- market-data fetches;
- broker/API/live-trading/execution work;
- profitability claims;
- real-money trading recommendations;
- overseas FX recommendations;
- high-leverage recommendations;
- Batch 08 summaries;
- Batch 08 quality review;
- Batch 09 selection;
- a final Batch 08 target set;
- raw transcript, subtitle full text, ASR full text, caption URL dump, audio,
  video, CSV, JSON, data, results, credential, or secret additions.

## 8. Future evidence questions

These are evidence questions only, not implementation proposals.

1. Which timeframe owns the premise, trigger, stop, and target in examples that
   look similar to Strategy A/B?
2. Are confirmation families separable into repeatable categories such as close
   confirmation, return behavior, line reaction, false-break recovery, and
   second confirmation?
3. Can structural context be decomposed without outcome selection into line,
   wave, channel, range, pattern, sweep, and scenario families?
4. Does the corpus support a target-priority hierarchy, or only the broad idea
   that targets should be structural or realistic?
5. Can stop-anchor validity be evaluated separately from stop width?
6. What evidence would justify a Strategy-specific RR design memo without
   optimizing thresholds on backtest outcomes?
7. Is ADX absent because the channel does not use it, or because the completed
   56-summary corpus has not yet covered the relevant examples?
8. Which discretionary terms are common enough to deserve a future manual
   review protocol before any mechanical proxy is considered?
9. Does any future evidence establish small-account or asymmetric risk framing,
   and if so, can it remain separate from Strategy A/B mechanics and live
   execution?

## 9. Recommended next research step

Recommended next step:

- keep Strategy A/B code, parameters, tests, and configs unchanged;
- keep Strategy B TP1, stop-anchor, RR, ADX, and Strategy B2 status frozen;
- use this mismatch analysis as a planning map for project-owner review;
- continue the channel doctrine line only when Git-safe evidence collection is
  available again;
- do not restart Batch 08 during the current waiting period;
- do not convert doctrine-map findings into Strategy changes without a later
  docs-only design memo that satisfies the existing reopen conditions.

The most useful next document, after evidence access recovers, would be a
targeted evidence-question plan that maps each mismatch category to the minimum
caption-supported evidence needed before any future Strategy-specific design
memo.

## 10. Guardrails confirmation

Confirmed:

- Docs-only mismatch analysis.
- Used only existing Git-tracked, Git-safe documents already present on `main`.
- No new video information collection was performed.
- No caption access probe was run.
- No metadata probe was run.
- No transcript probe was run.
- No subtitle fetch was run.
- No ASR attempt was run.
- No YouTube access attempt was run.
- No audio or video was downloaded.
- Batch 08 remains blocked / waiting and is not treated as completed evidence.
- The 48-hour waiting rule for any next Batch 08 tiny access probe was
  respected by not probing at all.
- No Strategy A/B rules changed.
- No Strategy B2 or Strategy C added.
- No code, parameter, config, or test changes.
- No backtests or optimization.
- No market data fetch.
- No broker/API/live-trading/execution code.
- No profitability claims.
- No real-money, overseas FX, or high-leverage recommendation.
- No raw transcript, subtitle full text, ASR full text, caption URL dump, audio,
  video, CSV, JSON, data, results, credential, or secret files added.

## 11. Readiness decision

`ready_for_project_owner_review_of_strategy_ab_doctrine_mismatch`

Reason: the current Strategy A/B mechanical assumptions have been compared
against the provisional Channel Doctrine Map v1 using only existing Git-safe
evidence, while preserving all Strategy B TP1 closure decisions and avoiding
new video collection, data generation, implementation work, optimization, or
profitability claims.
