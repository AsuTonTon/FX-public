# Strategy B TP1 Selection Review

Generated: 2026-06-26

This is a read-only diagnostic report for Strategy B TP1 selection after the
merged 32-summary corpus synthesis. It does not change Strategy A/B code,
parameters, tests, data, exports, or backtest outputs.

## 1. Objective and scope

Objective: review whether the current Strategy B TP1 selection and rejection
flow is plausibly aligned with the video-derived rule corpus, especially after
the 32-summary interim synthesis identified recurring themes around structural
targets, contextual RR, proper stop anchoring, and discretionary chart
judgment.

Scope:

- Inspect merged Strategy B design, implementation, diagnostics, and corpus
  synthesis documents.
- Inspect Strategy B code paths that select TP1, stops, and RR gates.
- Summarize existing candidate rejection evidence from merged diagnostics.
- Identify TP1 mismatch hypotheses for future research.
- Recommend one next research step.

Out of scope:

- No parameter changes.
- No Strategy A/B code changes.
- No new tests, configs, exports, CSVs, data, or results.
- No backtests or optimization.
- No Strategy C, Strategy B2, broker, API, or execution logic.
- No profitability claims.

## 2. Documents and code inspected

Documents inspected:

- `docs/video_research/channel_32_summary_interim_synthesis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_spec_design.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_implementation_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_readonly_validation_report.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_filter_funnel_diagnostics.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_candidate_export_notes.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_candidate_export_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_instrumentation.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_candidate_diagnostics_analysis.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_manual_chart_review_protocol.md`
- `docs/video_research/vkaA9MCRlx4/strategy_spec.yaml`

Code inspected:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`

This report is kept under `docs/video_research/vkaA9MCRlx4/` because that
directory already contains the Strategy B design, validation, diagnostics, and
TP-review documents connected to the original video-derived Strategy B work.

## 3. Current Strategy B TP1 selection flow

The current Strategy B implementation keeps the Strategy A setup sequence:

1. 20EMA/200EMA trend-cross context.
2. First 20EMA touch after the setup.
3. Body-close confirmation break.
4. Entry at the next bar open after confirmation.

After a confirmation candidate exists, Strategy B builds the order with fixed
rules:

- ADX gate: reject if ADX(14) is below the configured minimum.
- TP candidates: collect valid left-side fractal swings using width 2 and
  lookback 100, without using future bars.
- Long TP candidates: swing highs above entry, sorted by nearest price first.
- Short TP candidates: swing lows below entry, sorted by nearest price first.
- TP1: first sorted target candidate.
- TP2: second sorted target candidate, if available.
- Stop anchor: nearest valid left-side swing beyond the reference candle, or
  the reference candle level if no eligible swing exists.
- Stop buffer: maximum of configured pair buffer, 0.10 * ATR(14), and tick size.
- Stop sanity: reject if stop distance is below 0.25 ATR or above 3.0 ATR.
- RR gates: reject if TP1 is below 1.0R; if only TP1 exists, reject below 1.5R;
  if TP2 exists, reject if TP2 is below 1.5R.

The important TP1 behavior is therefore mechanical and price-rank based:

- TP1 is not selected by prominence.
- TP1 is not selected by wave count, channel boundary, range boundary, or
  pattern objective.
- TP1 is not selected by a discretionary "near realistic target" label.
- TP1 is the nearest valid left-side swing level beyond entry.

The first-fail order means `stop_too_wide` can appear before
`tp1_below_min_rr`. The diagnostic `all_failed_reasons` field is therefore
important because it shows later failures that also apply to the same candidate.

## 4. Candidate rejection evidence

Merged diagnostics show that Strategy B currently accepts very few confirmation
candidates:

| Measure | Count |
| --- | ---: |
| Confirmation candidates | 373 |
| Accepted candidates | 2 |
| Rejected candidates | 371 |

First-fail rejection counts from the candidate export analysis:

| First fail reason | Count | Share of rejected candidates |
| --- | ---: | ---: |
| `tp1_below_min_rr` | 218 | 58.4% |
| `stop_too_wide` | 97 | 26.0% |
| `no_left_side_tp1` | 28 | 7.5% |
| `adx_below_threshold` | 25 | 6.7% |
| `tp1_only_below_min_rr` | 2 | 0.5% |
| `tp2_below_min_rr` | 1 | 0.3% |

All-failed-reason counts show the broader TP1 issue:

| Failed reason in all-failed set | Count |
| --- | ---: |
| `tp1_below_min_rr` | 335 |
| `tp2_below_min_rr` | 270 |
| `stop_too_wide` | 101 |
| `tp1_only_below_min_rr` | 66 |
| `no_left_side_tp1` | 33 |
| `adx_below_threshold` | 25 |

Key rejection evidence:

- `tp1_below_min_rr` appears in 335 of 371 rejected candidates.
- Every candidate with `stop_too_wide` also fails `tp1_below_min_rr`.
- ADX rejects 25 candidates; 20 of those also fail `tp1_below_min_rr`.
- `no_left_side_tp1` appears in 33 candidates and is a separate target-absence
  problem, not merely a low-RR problem.
- Among 340 evaluable rank-1 TP1 candidates, the median TP1 distance is
  0.1714R and only 5 are at least 1.0R.
- Accepted candidates have much larger TP1 R than rejected candidates in the
  existing analysis: accepted median TP1 R 1.4491R versus rejected median TP1 R
  0.1710R.

The current evidence points to TP1 target distance and the TP1/RR gate as the
dominant rejection mechanism. ADX is visible but secondary in this diagnostic
set.

## 5. TP1 / stop / RR interaction

The TP candidate diagnostics show that the nearest valid swing target is often
too close to satisfy the fixed RR gate:

| Target rank | Evaluable rows | Median R | Rows at least 1.0R |
| --- | ---: | ---: | ---: |
| Rank 1 | 340 | 0.1714R | 5 |
| Rank 2 | 273 | 0.3338R | 20 |
| Rank 3 | 193 | 0.5109R | 33 |
| Rank 4 | 146 | 0.6993R | 42 |
| Rank 5 | 118 | 0.9169R | 50 |

For the 335 cases where rank-1 TP1 is below 1.0R:

- Rank 2 reaches at least 1.0R in only 18 cases.
- Any rank 2-5 target reaches at least 1.0R in 76 cases.
- 259 cases remain below 1.0R across ranks 2-5.

This means a simple "use rank 2 instead of rank 1" rule would not resolve most
TP1 failures. Later targets help some candidates, but most low-rank-1 cases do
not have any rank 2-5 target that clears 1.0R.

The stop interaction is also material:

- 101 candidates have `stop_too_wide`.
- All 101 also fail `tp1_below_min_rr`.
- Only 8 of those 101 have any rank 1-5 target at or above 1.0R.
- 93 have all rank 1-5 targets below 1.0R.

The interaction is therefore structural, not just a gate-order artifact. A
wider stop increases the risk denominator, making nearby left-side targets fail
RR even when those targets exist. At the same time, the corpus synthesis warns
against treating shallow stops as valid merely to improve RR; stop placement
must preserve the trade premise or invalidation logic.

## 6. Comparison with 32-summary corpus synthesis

The 32-summary interim synthesis broadly supports the idea that targets should
be structural, but it does not confirm the current exact TP1 model.

Aligned areas:

- Strategy B uses left-side structure for TP selection.
- Strategy B checks RR before accepting the trade.
- Strategy B includes partial exit and break-even movement after TP1.
- Strategy B uses a stop/invalidation anchor rather than a purely fixed-pip
  stop.

Potential mismatches:

- The corpus repeatedly frames TP as contextual structure, not necessarily the
  nearest fractal swing beyond entry.
- Several summaries preserve wording around realistic reachable targets,
  left-side highs/lows, wave structure, horizontal levels, channel/range
  boundaries, and applied chart judgment.
- The synthesis treats contextual RR as a medium-confidence doctrine, but does
  not confirm a universal fixed 1.0R TP1 gate for all candidates.
- The synthesis identifies staged exit, partial exit, and break-even movement
  as weaker or less consistently defined than structural target selection.
- Stop/invalidation anchoring is recurring, but many applied examples leave the
  exact stop anchor under-specified.
- Discretionary chart judgment remains a strong blocker: many useful video
  rules rely on chart terms that are not yet mechanically defined.
- ADX is not confirmed as a corpus-wide mechanical trend-strength rule, so the
  TP1 issue should not be explained primarily as an ADX issue.

The corpus synthesis therefore supports investigating whether Strategy B's TP1
selection is too narrow or too literal, while also warning against immediately
loosening RR or stops without structural evidence.

## 7. TP1 mismatch hypotheses

The following hypotheses are diagnostic, not implementation recommendations.

| ID | Hypothesis | Supporting Strategy B evidence | Corpus comparison | Confidence |
| --- | --- | --- | --- | --- |
| H1 | Nearest fractal swing may be too local to represent the intended first structural target. | Rank-1 TP1 median is 0.1714R; only 5 of 340 rank-1 targets reach 1.0R. | The synthesis supports structural targets but also preserves broader target language such as left-side highs/lows, wave structure, channel/range boundaries, and realistic reachable targets. | High |
| H2 | Fixed 1.0R TP1 gating may reject some structurally valid first targets. | `tp1_below_min_rr` appears in 335 rejected candidates. | Corpus evidence supports contextual RR, but does not confirm a universal fixed TP1 minimum for every setup. | Medium |
| H3 | Proper structural stops may create wide risk denominators that make nearby structural targets fail RR. | All 101 `stop_too_wide` candidates also fail TP1 RR; 93 have no rank 1-5 target at or above 1.0R. | Corpus favors premise-based invalidation and does not support moving stops shallow solely to improve RR. | High |
| H4 | Current TP ranking cannot distinguish a weak nearby swing from a meaningful target zone. | TP diagnostics rank by price distance; simple prominence analysis was inconclusive. | The synthesis repeatedly flags discretionary chart terms and structural judgment as unresolved blockers. | High |
| H5 | Some rejected cases may need a farther structural target, but not all later targets are valid. | Any rank 2-5 target reaches 1.0R in only 76 of 335 low-rank-1 cases. | The corpus supports structural targets, but not an automatic "skip to farther rank" rule. | Medium |
| H6 | Partial exit and break-even logic may be overrepresented as an entry-acceptance requirement. | Strategy B requires TP1 RR before any staged management can occur. | The synthesis marks staged exit/partial/BE as weaker than structural TP and contextual RR. | Medium |
| H7 | ADX is unlikely to be the main explanation for Strategy B collapse. | ADX first-fail count is 25, far below TP1 and stop/RR failures. | The synthesis does not confirm ADX as a corpus-wide mechanical doctrine. | High |

Mismatch hypothesis count: 7.

## 8. What cannot be concluded

This review cannot conclude that Strategy B is profitable or unprofitable.

This review cannot conclude that TP1 minimum RR should be lowered, removed, or
optimized.

This review cannot conclude that rank 2, rank 3, or a farther target should
replace the current rank-1 TP1 rule.

This review cannot conclude that stop-width limits should be widened or that
stops should be made shallower.

This review cannot conclude that ADX should be removed or retuned.

This review cannot convert discretionary corpus language into mechanical rules
without additional evidence definition.

This review cannot justify Strategy C, Strategy B2, live trading, broker
integration, optimization, or new backtests.

## 9. Recommended next research step

Recommended next step: create a small docs-only TP1 diagnostic design update
that connects the existing manual chart review protocol to the 32-summary
corpus synthesis.

The next research step should define how to classify rejected candidates into
evidence buckets such as:

- nearest swing is a minor local swing, not a meaningful target;
- rank 1 is a valid first target but fixed RR rejects it;
- later rank is a clearer structural target;
- no rank 1-5 target is structurally valid;
- stop anchor is structurally valid but creates low RR;
- stop anchor is under-specified or mechanically questionable;
- TP1 is being confused with protective management rather than a first target.

That step should remain outcome-blinded and read-only. It should not change the
Strategy B parameters or select a replacement TP1 rule until the chart-review
labels show a repeatable structural distinction.

## 10. Guardrails

Confirmed guardrails for this report:

- Documentation-only diagnostic report.
- Exactly one Markdown report updated.
- No Strategy A code changes.
- No Strategy B code changes.
- No parameter, config, or test changes.
- No data, result, CSV, JSON, raw transcript, subtitle, caption, video, or audio
  files added.
- No backtests run.
- No optimization performed.
- No Strategy C or Strategy B2 created.
- No broker, API, live-trading, or execution changes.
- No profitability claims.
