# Strategy B TP1 Diagnostic Design

Generated: 2026-06-26

This document defines a future diagnostic design only. It does not implement
diagnostics, inspect raw candidate rows, run backtests, change Strategy B
behavior, or evaluate profitability.

## 1. Objective and scope

Objective: define a narrow, outcome-blinded design for later manual review of
Strategy B TP1 rejection modes. The design should help separate the following
failure modes before any rule or parameter discussion:

- structurally weak TP1;
- numerically low-RR TP1;
- nearest local swing that is not a meaningful target;
- valid first structural target rejected by fixed RR;
- missing farther structural target;
- proper structural stop that worsens RR;
- mechanically questionable stop anchor;
- protective management being confused with initial TP1.

Scope:

- Documentation-only diagnostic design.
- Uses merged Strategy B reports, TP diagnostics, and the 32-summary corpus
  synthesis as design inputs.
- Defines future sampling buckets, manual chart-review labels, worksheet schema,
  interpretation rules, and a minimum first-pass sample proposal.
- Preserves outcome blinding and separates chart-structure review from
  profitability review.

Out of scope:

- No Strategy B rule changes.
- No Strategy A/B code changes.
- No parameter changes.
- No Strategy B2.
- No Strategy C.
- No backtests.
- No optimization.
- No profitability evaluation.
- No candidate CSV committed.
- No raw candidate export rows inspected or reproduced in this PR.
- No market data, result files, CSV, JSON, transcripts, subtitles, videos, or
  audio added.

## 2. Prior evidence summary

Merged Strategy B diagnostics show a narrow but severe post-confirmation
collapse:

- 373 confirmation candidates.
- 2 accepted candidates.
- 371 rejected candidates.
- `tp1_below_min_rr` appears in 335 rejected candidates.
- All `stop_too_wide` candidates also fail `tp1_below_min_rr`.
- ADX is secondary: 25 rejected candidates have `adx_below_threshold`, and 20
  of those also fail TP1 minimum RR.
- Rank-1 TP1 is very low in R terms: the combined median rank-1 TP1 is
  0.1714R, and only 5 of 340 evaluable rank-1 TP1 values reach at least 1.0R.
- Later rank targets help only some cases: among 335 rank-1-below-1.0R cases,
  any rank 2-5 target reaches at least 1.0R in 76 cases, while 259 still have
  all available ranks 2-5 below 1.0R.
- For the `stop_too_wide` subset, later targets rarely solve the large risk
  denominator: only 8 of 101 stop-too-wide candidates have any rank 1-5 target
  at or above 1.0R.

The 32-summary corpus synthesis suggests structural TP and contextual RR as
recurring evidence families, but it does not mechanically specify a replacement
TP1 rule, a replacement RR threshold, or a universal stop rule. It also
preserves a major blocker: many useful video-derived terms depend on
discretionary chart interpretation, such as meaningful structure, target
realism, wave or pattern quality, and premise-based invalidation.

## 3. Diagnostic design principles

The later review should follow these principles:

- Read-only: use existing committed diagnostics or future local exports only as
  inputs; do not alter Strategy B behavior.
- Outcome-blinded: reviewers should not see trade outcome, accepted/rejected
  status, failure reason, target R, pair performance, or profitability during
  the structural chart pass.
- Small-sample first: start with a practical manual sample before designing any
  broader instrumentation or rule experiment.
- Manually reviewable: each reviewed example should fit in a fixed chart window
  and have enough visible context to judge TP1, farther targets, and stop
  structure.
- Reproducible: bucket definitions, hidden source identifiers, and review order
  should be deterministic when the review is later executed.
- Evidence-preserving: keep the mechanical diagnostics, hidden metadata, and
  reviewer-facing judgments separate so later readers can see what was observed
  without conflating evidence layers.
- Separated from profitability: label structural interpretation only; do not use
  outcome or performance to decide whether a target is structurally meaningful.
- Separated from parameter optimization: do not test threshold alternatives in
  this design step.
- Not an implementation spec: labels may inform future research decisions, but
  they do not define code behavior or authorize Strategy B changes.

## 4. Candidate sampling design

This PR only designs future buckets. It does not load data, sample candidates,
or inspect raw candidate rows beyond the aggregate evidence already committed in
merged docs.

Future sampling should use existing diagnostics concepts:

| Bucket | Purpose | Future selection rule | Notes |
| --- | --- | --- | --- |
| Accepted candidates | Provide positive mechanical controls. | Include the 2 accepted candidates, if still present in the local diagnostic export. | Reviewer must not see accepted status during Pass A. |
| Earliest `tp1_below_min_rr` candidates | Inspect the dominant rejection mode without outcome selection. | Select earliest unique candidates whose first fail is `tp1_below_min_rr`. | "Earliest" should follow deterministic export ordering or confirmation time in the future local review. |
| Lowest TP1 R bucket | Test whether extremely close targets are minor structure. | Select candidates with rank-1 TP1 R below 0.25R. | Use hidden metadata only during Pass A. |
| 0.25R-0.5R bucket | Test low but less extreme TP1 cases. | Select candidates with rank-1 TP1 R from 0.25R inclusive to below 0.5R. | Keep separate from the very-low bucket. |
| Near-miss 0.8R-1.0R bucket | Test whether fixed 1.0R rejects visually acceptable first targets. | Select candidates with rank-1 TP1 R from 0.8R inclusive to below 1.0R, if available. | If fewer exist, record the lower count rather than padding with outcome-selected examples. |
| `stop_too_wide` plus TP1 failure | Test whether proper stops create low RR or whether stop anchors look questionable. | Select candidates with `stop_too_wide` and `tp1_below_min_rr` in all-failed reasons. | Do not assume wide stops are invalid. |
| `no_left_side_tp1` | Test target absence and lookback/structure limitations. | Select candidates with `no_left_side_tp1`. | These are not TP1-low-RR cases because TP1 was unavailable. |
| Later rank clears 1.0R | Test whether a farther structural target may be clearer than rank 1. | Select rank-1-below-1.0R cases where any rank 2-5 target is at least 1.0R. | Do not infer that farther target is valid before chart review. |
| Rank 1-5 all fail 1.0R | Test whether the entire visible target set is structurally constrained. | Select rank-1-below-1.0R cases where all available ranks 2-5 are below 1.0R. | Keep separate from cases where later ranks are absent. |
| ADX-first-fail plus TP1 failure | Verify whether ADX cases are really a separate family. | Select `adx_below_threshold` first-fail cases that also fail TP1 RR in all-failed reasons. | ADX should remain hidden during Pass A. |
| Random controls per pair or time period | Detect reviewer overfitting to failure buckets. | Add 1-2 deterministic random controls per pair or time period if feasible in the later local review. | Keep total sample practical by replacing from larger buckets, not by expanding indefinitely. |

Sampling controls:

- De-duplicate candidates across buckets by fixed precedence.
- Keep bucket assignment hidden from reviewers during the blinded pass.
- Preserve pair and time-period balance where feasible, but do not force balance
  by selecting outcome-convenient examples.
- Keep raw candidate CSVs local in the later review task; do not commit them.
- Use the existing manual chart-review protocol's opaque `presentation_id`
  approach when executing the future review.

## 5. Manual chart-review labels

Each label below is for a future manual chart review. Labels can be multi-select
within a family only when the definitions do not conflict. The expected evidence
source is the fixed pre-confirmation chart window, visible entry/stop/target
levels, hidden mechanical diagnostics revealed only after Pass A, and the
32-summary corpus synthesis for doctrine comparison.

### A. TP1 structural quality

| Label | Definition | Apply when | Do not apply when | Expected evidence source |
| --- | --- | --- | --- | --- |
| `tp1_meaningful_structural_target` | Rank-1 TP1 aligns with a visually meaningful prior swing, level, range edge, channel/pattern boundary, or other clear structure. | The target has visible structural relevance beyond being merely the nearest fractal. | The target is only a tiny fluctuation near entry or cannot be interpreted from the chart window. | Fixed chart window and visible rank-1 target. |
| `tp1_minor_local_swing` | Rank-1 TP1 is technically a swing but visually minor compared with surrounding structure. | The level exists but appears subordinate to clearer nearby structure. | The level is the clearest practical first target. | Fixed chart window, rank-1 target, nearby rank levels. |
| `tp1_inside_noise` | Rank-1 TP1 sits inside recent choppy price action rather than at a meaningful decision boundary. | The target is embedded in overlapping candles or noise. | The target marks a distinct reaction level or boundary. | Fixed chart window and candle context. |
| `tp1_near_entry_micro_structure` | Rank-1 TP1 is very close to entry and represents micro-structure near the trigger. | The target is visually near entry and not a broader trade objective. | The nearby level is a deliberate protective first target under corpus-aligned management logic. | Entry marker, rank-1 target, visible pre-entry candles. |
| `tp1_reasonable_nearest_target` | Rank-1 TP1 is a plausible first target even if not far enough for fixed RR. | The nearest structure looks like a reasonable first decision point. | The target is minor, noisy, or not interpretable. | Fixed chart window plus later Pass B TP1 R. |
| `tp1_not_visually_interpretable` | The review window is insufficient to judge TP1 structure. | Chart context, scale, or target placement prevents a clear label. | Another TP1 structural quality label can be applied with medium or high confidence. | Reviewer chart and notes. |

### B. Farther target availability

| Label | Definition | Apply when | Do not apply when | Expected evidence source |
| --- | --- | --- | --- | --- |
| `farther_structural_target_exists` | At least one rank 2-5 or visible farther level is structurally meaningful. | A farther target has clear prior reaction, wave, range, channel, or pattern relevance. | Farther levels are only arbitrary distance or weak swings. | Fixed chart window and rank 2-5 targets. |
| `farther_target_is_clearer_than_tp1` | A farther target is more visually meaningful than rank-1 TP1. | Rank 1 looks minor or noisy and a later rank aligns better with structure. | Rank 1 is already the clearest practical first target. | Fixed chart window, rank 1-5 targets. |
| `farther_target_is_too_far_or_unrealistic` | The farther target exists but appears unrealistic as an initial target for the setup. | The target would require excessive extension relative to the setup context. | The target is a normal reachable structural objective. | Fixed chart window and corpus target-realism doctrine. |
| `no_clear_farther_target` | No farther target in the visible context is clearly meaningful. | Rank 2-5 or visible farther levels do not provide a better structure. | At least one farther level is clearly interpretable. | Fixed chart window and rank 2-5 targets. |
| `farther_target_requires_discretion` | A farther target might be valid but depends on subjective line, wave, or zone drawing. | Reviewers can identify a possible target but not a deterministic anchor. | The target is directly visible as a clear swing/level/boundary. | Reviewer notes and corpus discretion blockers. |

### C. Stop anchor quality

| Label | Definition | Apply when | Do not apply when | Expected evidence source |
| --- | --- | --- | --- | --- |
| `stop_structurally_valid` | The stop anchor is visually aligned with the trade premise or invalidation structure. | The stop sits beyond a meaningful swing, reference candle, pattern, range, or premise boundary. | The stop only appears convenient for RR or cannot be tied to invalidation. | Fixed chart window, visible stop, setup structure. |
| `stop_too_wide_but_structural` | The stop is wide in ATR/RR terms but structurally justified. | The stop protects the relevant premise and a shallower stop would cut through the structure. | The stop is wide because the selected anchor is visually questionable. | Fixed chart window plus Pass B stop distance. |
| `stop_too_wide_and_questionable` | The stop is wide and the structural reason for that anchor is weak. | The stop anchor is far away without clear premise-based justification. | The stop is wide but protects a clear invalidation boundary. | Fixed chart window plus Pass B stop diagnostics. |
| `stop_anchor_minor_swing` | The stop uses a minor local swing that may not represent actual invalidation. | The stop-side swing is visually weak or inside noise. | The stop protects a clear structural boundary. | Fixed chart window and visible stop-side structure. |
| `stop_anchor_reference_candle_only` | The stop appears to rely on the reference candle rather than a broader structural anchor. | The visible stop aligns mainly with the reference candle high/low. | The reference candle itself is clearly the structural invalidation point. | Fixed chart window and implementation terminology. |
| `stop_anchor_not_visually_interpretable` | The stop cannot be judged from the review window. | The visible context does not support a confident stop label. | A stop anchor quality label can be applied with medium or high confidence. | Reviewer chart and notes. |

### D. RR interpretation

| Label | Definition | Apply when | Do not apply when | Expected evidence source |
| --- | --- | --- | --- | --- |
| `low_rr_but_structural_tp` | TP1 is structurally valid but fails or nearly fails fixed RR. | TP1 quality is meaningful while Pass B shows low TP1 R. | TP1 is minor, noisy, or not interpretable. | Pass A TP1 label plus Pass B TP1 R. |
| `low_rr_due_to_minor_tp1` | Low RR is mainly explained by a weak or overly local TP1. | TP1 is labeled minor, micro, or inside noise. | TP1 is structurally meaningful despite low R. | Pass A TP1 labels plus Pass B TP1 R. |
| `low_rr_due_to_wide_structural_stop` | Low RR is mainly explained by a wide but structurally valid stop. | Stop is structurally valid and wide, while target is not obviously invalid. | Stop is questionable or TP1 is clearly minor. | Stop labels, stop distance ATR, TP1 R. |
| `low_rr_due_to_questionable_stop` | Low RR is materially affected by a questionable stop anchor. | Stop anchor quality is weak and risk denominator appears inflated. | Stop is valid even if wide. | Stop labels plus Pass B stop diagnostics. |
| `rr_failure_not_diagnosable` | The review cannot determine why RR failed. | TP1, stop, or chart context cannot be labeled confidently. | Another RR interpretation label is available with medium or high confidence. | Reviewer notes and confidence. |

### E. Corpus alignment

| Label | Definition | Apply when | Do not apply when | Expected evidence source |
| --- | --- | --- | --- | --- |
| `matches_structural_tp_doctrine` | The reviewed TP interpretation fits the corpus tendency toward structural TP. | TP uses prior structure, wave, range, channel, pattern, or realistic target logic. | TP is purely arbitrary or cannot be linked to structure. | 32-summary synthesis and chart labels. |
| `matches_contextual_rr_doctrine` | RR assessment depends on structure, stop, target, timeframe, or setup context. | The chart suggests RR cannot be judged by a number alone. | The review has no structural reason to reinterpret RR. | 32-summary synthesis plus TP/stop labels. |
| `matches_stop_invalidation_doctrine` | Stop placement aligns with premise-based invalidation. | The stop protects the setup premise or structural invalidation point. | Stop is shallow, arbitrary, or not interpretable. | 32-summary synthesis plus stop labels. |
| `matches_protective_exit_not_initial_tp` | The level is better interpreted as protective management than the first intended TP. | The chart suggests a defensive reduction or exit signal rather than the initial target objective. | The level is clearly a normal first target. | Corpus protective-exit doctrine and management labels. |
| `does_not_match_32_summary_evidence` | The mechanical interpretation conflicts with the summarized corpus evidence. | The target, stop, or RR logic appears arbitrary or unsupported by corpus families. | The mismatch is only unknown rather than contradicted. | 32-summary synthesis and reviewer notes. |
| `corpus_alignment_unclear` | Corpus alignment cannot be judged. | Chart evidence is ambiguous or corpus family mapping is uncertain. | A more specific corpus alignment label fits. | Reviewer notes and synthesis blockers. |

### F. Management distinction

| Label | Definition | Apply when | Do not apply when | Expected evidence source |
| --- | --- | --- | --- | --- |
| `initial_tp1_candidate` | The level is plausibly the first planned profit target. | The level is a structural objective for taking profit. | The level is primarily defensive management or not a target. | Fixed chart window and TP labels. |
| `protective_exit_candidate` | The level is better read as a defensive exit or reduction point. | The chart suggests premise weakness, path failure, or price-action deterioration would drive the exit. | The level is a normal structural target. | Corpus protective-exit doctrine and reviewer notes. |
| `partial_exit_candidate` | The level could be used for partial profit-taking. | The level is plausible for reducing size while leaving a runner. | There is no structural or management reason to reduce at the level. | Corpus management evidence and TP labels. |
| `break_even_management_candidate` | The case is more about moving stop to break-even after an event than selecting initial TP1. | The visible logic suggests post-TP or post-confirmation risk removal. | No break-even trigger or management event is visible. | Corpus break-even evidence and chart context. |
| `not_a_management_case` | The case is about initial target or stop selection, not management after entry. | No protective, partial, or break-even distinction is supported. | A management distinction label applies. | Reviewer notes. |

## 6. Review worksheet schema

This is a schema only. Do not create CSV, JSON, filled rows, or review results in
this PR.

Future review table fields:

| Field | Purpose |
| --- | --- |
| `candidate_id` or `stable_reference` | Hidden source reference for the reviewed candidate. |
| `presentation_id` | Reviewer-facing opaque ID for outcome-blinded review. |
| `pair` | Hidden in Pass A if pair blinding is required; revealed in Pass B. |
| `timeframe` | Strategy B review timeframe. |
| `direction` | Long or short. |
| `confirmation_time` | Hidden in Pass A; used for reproducibility. |
| `entry` | Entry price shown on chart. |
| `stop` | Stop price shown on chart. |
| `stop_distance_atr` | Hidden in Pass A; revealed in Pass B. |
| `tp1` | Rank-1 TP price shown as rank 1 in Pass A. |
| `tp1_r` | Hidden in Pass A; revealed in Pass B. |
| `tp2` | Rank-2 TP price, if available. |
| `tp2_r` | Hidden in Pass A; revealed in Pass B. |
| `target_ranks_available` | Count or list of rank 1-5 target prices available. |
| `first_fail_reason` | Hidden in Pass A; revealed in Pass B. |
| `all_failed_reasons` | Hidden in Pass A; revealed in Pass B. |
| `selected_bucket` | Hidden sampling bucket. |
| `tp1_structural_quality_labels` | Labels from family A. |
| `farther_target_labels` | Labels from family B. |
| `stop_anchor_labels` | Labels from family C. |
| `rr_interpretation_labels` | Labels from family D. |
| `corpus_alignment_labels` | Labels from family E. |
| `management_distinction_labels` | Labels from family F. |
| `reviewer_notes` | Short structural note, with no outcome or profitability wording. |
| `reviewer_confidence` | `high`, `medium`, or `low`. |
| `requires_second_review` | `yes` when labels are low-confidence or consequentially ambiguous. |

Schema rules:

- Do not expose `first_fail_reason`, `all_failed_reasons`, `tp1_r`, `tp2_r`,
  `stop_distance_atr`, `selected_bucket`, accepted status, or outcome during
  Pass A.
- Do not include post-confirmation outcome candles in the structural review.
- Do not fill this schema in this PR.

## 7. Decision rules for interpreting labels

Future label results should guide research questions, not code changes.

- If many low-RR cases are labeled `tp1_minor_local_swing`,
  `tp1_inside_noise`, or `tp1_near_entry_micro_structure`, the issue may be
  target-quality selection rather than the RR threshold alone.
- If many cases are labeled `low_rr_but_structural_tp`, fixed RR may be too
  strict for some structural first targets, but that would still require a
  separate non-optimized rule discussion.
- If many cases are labeled `stop_too_wide_but_structural`, the stop/RR
  interaction needs review, but shallow stops are not automatically valid.
- If many cases are labeled `stop_too_wide_and_questionable` or
  `low_rr_due_to_questionable_stop`, stop-anchor mechanics may need a later
  diagnostic review before target mechanics are changed.
- If many cases have `farther_target_is_clearer_than_tp1`, target ranking may be
  too local, but the review still must identify a repeatable structural ranking
  rule before any code discussion.
- If many cases have `farther_target_is_too_far_or_unrealistic`, skipping to
  farther targets is not supported.
- If many cases have `no_clear_farther_target`, the low-RR issue may reflect
  genuinely constrained structure rather than a rank-selection defect.
- If many cases are labeled `protective_exit_candidate`,
  `partial_exit_candidate`, or `break_even_management_candidate`, TP1 and trade
  management may be conflated.
- If many cases are labeled `corpus_alignment_unclear`, more corpus evidence or
  clearer doctrine definitions are needed before Strategy B changes.

No code change is recommended by this document. These decision rules only define
how future evidence would guide a later research decision.

## 8. Minimum sample proposal

This is a proposed future sample only. It is not executed in this PR.

Practical first-pass sample:

| Future sample group | Count |
| --- | ---: |
| Accepted candidates | 2 |
| Very low TP1 R cases below 0.25R | 4 |
| TP1 R 0.25R-0.5R cases | 4 |
| Near-miss TP1 R 0.8R-1.0R cases, if available | 3 |
| `stop_too_wide` plus TP1 failure cases | 4 |
| Later-rank-clears-1.0R cases | 4 |
| Rank 1-5-all-fail-1.0R cases | 4 |
| `no_left_side_tp1` cases | 3 |
| ADX-first-fail cases that also fail TP1 | 2 |
| Total proposed first pass | 30 |

If a bucket has fewer available candidates in the future local export, record
the shortfall rather than padding with outcome-selected examples. If random
controls are added, replace examples from the largest failure buckets so the
first pass remains around 25-30 reviewed examples.

## 9. What this design will not answer

This design will not answer profitability.

This design will not define a final TP1 rule.

This design will not justify a minimum RR adjustment.

This design will not create Strategy B2.

This design will not optimize parameters.

This design will not prove that video discretion can be mechanized.

This design will not prove that farther targets are better.

This design will not prove that current TP1 is wrong in all cases.

This design will not decide whether ADX should be changed.

This design will not authorize Strategy A/B code or config changes.

## 10. Recommended next step

Updated routing after the public diagnostic boundary:

Do not proceed next to worksheet preparation, packet preparation, sample
selection, or outcome-blinded manual review. Next local-only diagnostic, packet,
sample, Pass A / Pass B, worksheet, mapping, reveal-table, chart-packet, or
review-run work remains paused under
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md` until
explicit human approval is given after corpus input, visual evidence review, and
doctrine synthesis dependencies are addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.

## 11. Guardrails

Confirmed guardrails for this PR:

- docs-only;
- exactly one Markdown file created or updated;
- no Strategy A/B code change;
- no parameter, config, or test change;
- no backtest;
- no optimization;
- no data, results, CSV, or JSON;
- no raw candidate exports;
- no raw transcript or subtitle;
- no Strategy C or Strategy B2;
- no broker, API, live-trading, or execution change;
- no profitability claims.
