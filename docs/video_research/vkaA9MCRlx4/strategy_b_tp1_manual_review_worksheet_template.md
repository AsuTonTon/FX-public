# Strategy B TP1 Manual Review Worksheet Template

Generated: 2026-06-26

This document is a Markdown-only worksheet and protocol template for a future
Strategy B TP1 manual chart review. It prepares the review mechanism only; it
does not execute the review.

## 1. Objective and scope

Objective: define a reusable Markdown worksheet template and protocol wrapper
for the future Strategy B TP1 manual chart review described by the TP1
diagnostic design.

Scope:

- docs-only worksheet/protocol template;
- no manual review execution;
- no candidate sampling execution;
- no raw candidate rows;
- no filled worksheet rows;
- no Strategy B behavior changes;
- no Strategy A/B code changes;
- no parameter changes;
- no backtests;
- no optimization;
- no profitability evaluation;
- no data, results, CSV, JSON, raw transcript, subtitle, video, or audio files.

The file may be copied into a future local-only review packet, but this PR does
not create that packet and does not populate this template with real candidates.

## 2. Relationship to prior docs

This file follows and operationalizes prior documents without replacing them:

- `strategy_b_tp1_selection_review.md` identified the current TP1 selection
  flow and the dominant rejection evidence: `tp1_below_min_rr`, stop/RR
  interaction, low rank-1 TP1 R, and the need to separate target-quality issues
  from numerical RR issues.
- `strategy_b_tp1_diagnostic_design.md` defined the future diagnostic buckets,
  label families, worksheet schema, interpretation rules, and a proposed first
  small sample. This file turns those labels and fields into a reusable
  Markdown worksheet format.
- `strategy_b_tp_manual_chart_review_protocol.md` defines the existing
  outcome-blinded manual chart review mechanics, including opaque
  `presentation_id` values, hidden source metadata, fixed chart windows, and
  two-pass review. This file keeps those blinding principles and narrows them
  to the TP1 diagnostic-design labels.
- `channel_32_summary_interim_synthesis.md` supplies the corpus context:
  structural TP, contextual RR, premise-based stop/invalidation, protective
  exits, and unresolved discretionary chart terms. This file uses those themes
  only as review labels, not as implementation rules.

This file prepares the future review format. It does not sample candidates,
inspect raw rows, judge charts, compute aggregates, change Strategy B behavior,
or make profitability claims.

## 3. Review phases

The future review uses two passes.

### Pass A: blinded structural chart review

Pass A is the primary human chart-structure judgment. Reviewer-facing material
may include only:

- opaque `presentation_id`;
- chart image or chart context prepared in a later local-only review task;
- direction, if necessary for interpreting entry, stop, and target markers;
- visible entry, stop, and TP rank markers if the later protocol permits them;
- pre-confirmation and setup-context candles only;
- no post-confirmation outcome candles.

Pass A reviewer-facing material must not include:

- accepted/rejected status;
- `first_fail_reason`;
- `all_failed_reasons`;
- `tp1_r`;
- `tp2_r`;
- `stop_distance_atr`;
- selected bucket;
- trade outcome;
- profitability;
- pair-level or strategy-level performance context.

Pass A output is the locked structural judgment: label selections, reviewer
notes, reviewer confidence, and whether a second review is required.

### Pass B: diagnostic reveal

Pass B happens only after Pass A labels and notes are locked. Pass B may reveal:

- selected bucket;
- `first_fail_reason`;
- `all_failed_reasons`;
- `tp1_r`;
- `tp2_r`;
- `stop_distance_atr`;
- target ranks available;
- accepted/rejected status if needed for controls.

Pass B is used to interpret label patterns and compare them with mechanical
diagnostics. Pass B must not be used to rewrite the original Pass A judgment.

## 4. Blinding rules

Strict blinding rules:

- No outcome candles in Pass A.
- No failure reasons in Pass A.
- No R multiples in Pass A.
- No bucket names in Pass A.
- No accepted/rejected label in Pass A.
- No trade outcome or profitability in Pass A.
- No pair-level performance summary in Pass A.
- Do not revise Pass A labels after Pass B except through the documented
  correction fields.
- Keep reviewer notes structural, not performance-based.
- If the reviewer cannot judge a structure confidently, mark the appropriate
  "not visually interpretable" or "unclear" label rather than forcing a
  conclusion.

Pass B can add diagnostic interpretation, but the original Pass A label state
must remain visible and recoverable.

## 5. Candidate presentation template

The following is a template for one future candidate. It uses placeholders only.
Do not fill actual candidate rows in this PR.

<candidate_template>

```markdown
## Candidate: <presentation_id>

### Pass A visible fields

* presentation_id:
* chart_window_id:
* direction:
* visible_markers:

  * entry:
  * stop:
  * tp_rank_1:
  * tp_rank_2:
  * tp_rank_3:
  * tp_rank_4:
  * tp_rank_5:
* chart_context_notes:

### Pass A labels

#### TP1 structural quality

* [ ] tp1_meaningful_structural_target
* [ ] tp1_minor_local_swing
* [ ] tp1_inside_noise
* [ ] tp1_near_entry_micro_structure
* [ ] tp1_reasonable_nearest_target
* [ ] tp1_not_visually_interpretable

#### Farther target availability

* [ ] farther_structural_target_exists
* [ ] farther_target_is_clearer_than_tp1
* [ ] farther_target_is_too_far_or_unrealistic
* [ ] no_clear_farther_target
* [ ] farther_target_requires_discretion

#### Stop anchor quality

* [ ] stop_structurally_valid
* [ ] stop_too_wide_but_structural
* [ ] stop_too_wide_and_questionable
* [ ] stop_anchor_minor_swing
* [ ] stop_anchor_reference_candle_only
* [ ] stop_anchor_not_visually_interpretable

#### Corpus alignment

* [ ] matches_structural_tp_doctrine
* [ ] matches_contextual_rr_doctrine
* [ ] matches_stop_invalidation_doctrine
* [ ] matches_protective_exit_not_initial_tp
* [ ] does_not_match_32_summary_evidence
* [ ] corpus_alignment_unclear

Corpus alignment selection rule:

* `corpus_alignment_unclear` should normally be exclusive with specific
  corpus-alignment labels.
* Do not select `corpus_alignment_unclear` together with:

  * `matches_structural_tp_doctrine`
  * `matches_contextual_rr_doctrine`
  * `matches_stop_invalidation_doctrine`
  * `matches_protective_exit_not_initial_tp`
  * `does_not_match_32_summary_evidence`
* If the reviewer sees partial alignment but remains uncertain, select the
  specific alignment label only if evidence is strong enough; otherwise select
  `corpus_alignment_unclear` and explain uncertainty in `reviewer_notes`.
* `corpus_alignment_unclear` means the case cannot be mapped confidently to the
  32-summary synthesis, not that it contradicts the synthesis.

#### Management distinction

* [ ] initial_tp1_candidate
* [ ] protective_exit_candidate
* [ ] partial_exit_candidate
* [ ] break_even_management_candidate
* [ ] not_a_management_case

Management distinction selection rule:

* `initial_tp1_candidate` and `not_a_management_case` may be selected together.
* This combination means the level is interpreted as an initial TP1 candidate,
  not as protective exit, partial exit, or break-even management.
* `not_a_management_case` should not be selected together with:

  * `protective_exit_candidate`
  * `partial_exit_candidate`
  * `break_even_management_candidate`
* If the reviewer cannot distinguish initial TP from management, do not force
  `not_a_management_case`; use `reviewer_notes` and
  `requires_second_review: yes`.

### Pass A notes

* reviewer_notes:
* reviewer_confidence: high / medium / low
* requires_second_review: yes / no

### Pass B reveal fields

* stable_reference:
* pair:
* timeframe:
* confirmation_time:
* selected_bucket:
* first_fail_reason:
* all_failed_reasons:
* stop_distance_atr:
* tp1_r:
* tp2_r:
* target_ranks_available:
* accepted_or_rejected_status:

### Pass B interpretation labels

#### RR interpretation

* [ ] low_rr_but_structural_tp
* [ ] low_rr_due_to_minor_tp1
* [ ] low_rr_due_to_wide_structural_stop
* [ ] low_rr_due_to_questionable_stop
* [ ] rr_failure_not_diagnosable

### Pass B interpretation notes

* locked_pass_a_summary:
* diagnostic_interpretation:
* correction_needed_to_pass_a: yes / no
* original_pass_a_labels:
* corrected_pass_a_labels:
* correction_scope: checkbox selection / visible marker interpretation / reviewer note wording / confidence / second-review flag
* correction_reason:
```

</candidate_template>

## 6. Review batch manifest template

The following Markdown-only manifest template is for a future review batch. It
uses placeholders only. Do not create actual manifest rows in this PR.

```markdown
# Strategy B TP1 Manual Review Batch Manifest: <review_batch_id>

## Batch metadata

* review_batch_id:
* source_export_reference: <local-only reference; do not commit raw export>
* sampling_date:
* reviewer:
* blinding_method:
* candidate_count:

## Bucket counts

* accepted_candidates:
* earliest_tp1_below_min_rr:
* lowest_tp1_r_below_0_25r:
* tp1_r_0_25r_to_0_5r:
* near_miss_0_8r_to_1_0r:
* stop_too_wide_plus_tp1_failure:
* no_left_side_tp1:
* later_rank_clears_1_0r:
* rank_1_to_5_all_fail_1_0r:
* adx_first_fail_plus_tp1_failure:
* random_controls:

## Selection controls

* de_duplication_rule:
* randomization_rule:
* presentation_id_rule:
* repeat_case_rule:

## Reviewer-facing file list

* <presentation_id_001>: <chart_context_or_image_placeholder>
* <presentation_id_002>: <chart_context_or_image_placeholder>
* <presentation_id_n>: <chart_context_or_image_placeholder>

## Local-only raw source reminder

* Raw candidate exports remain local only.
* Filled worksheets remain local unless a later PR explicitly requests a
  summarized, non-raw aggregate report.
* No raw CSV, JSON, market data, chart-image packet, or result file is committed
  by this manifest.

## Guardrail checklist

* [ ] docs-only protocol/worksheet use
* [ ] no Strategy A/B behavior changes
* [ ] no parameter/config/test changes
* [ ] no backtests
* [ ] no optimization
* [ ] no raw candidate rows committed
* [ ] no data/results/CSV/JSON committed
* [ ] no post-confirmation outcome candles in Pass A material
* [ ] no profitability claims
```

## 7. Label locking and correction policy

Pass A labels are locked before Pass B reveal.

Corrections after reveal are allowed only for clerical mistakes or chart
misreadings, such as selecting the wrong checkbox by accident or realizing that
a visible marker was misread. Corrections are not allowed merely because the
revealed diagnostics show a surprising failure reason, R multiple, accepted
status, or bucket.

Correction rules:

- Preserve the original Pass A labels and notes in `original_pass_a_labels`.
- Set `correction_needed_to_pass_a` to `yes`.
- Fill `corrected_pass_a_labels` only if a clerical mistake or chart misreading
  is identified.
- Set `correction_scope` to identify whether the correction affects checkbox
  selection, visible marker interpretation, reviewer note wording, confidence,
  or the second-review flag.
- Record a short `correction_reason`.
- Keep the original Pass A state visible and recoverable.
- Make corrections additive, not silent replacements.
- Do not correct labels merely because Pass B reveals a surprising failure
  reason, R multiple, selected bucket, or accepted/rejected status.
- Do not use corrected labels alone to draw Strategy conclusions.
- Low-confidence or consequentially ambiguous cases should trigger second review
  rather than forced correction or forced classification.

Second-review triggers:

- `reviewer_confidence` is `low`;
- `requires_second_review` is `yes`;
- TP1 quality and farther-target labels conflict;
- stop validity is unclear but materially affects RR interpretation;
- management distinction is unclear between initial TP1 and protective exit;
- a correction is requested after Pass B reveal.

## 8. Aggregation plan

A future completed manual review should summarize aggregate label patterns
without exposing raw candidate rows or profitability outcomes.

Aggregate counters to compute later:

- count by bucket;
- count by TP1 structural quality label;
- count by farther target label;
- count by stop anchor label;
- count by RR interpretation label;
- count by corpus alignment label;
- count by management distinction label;
- count requiring second review;
- count by reviewer confidence;
- count with post-reveal correction requested.

Suggested cross-tabs:

- bucket x TP1 label;
- `stop_too_wide` x stop label;
- low-RR bucket x TP1 label;
- later-rank-clears x farther target label;
- management distinction x TP1 label;
- stop label x RR interpretation label;
- corpus alignment x TP1 structural quality label;
- second-review requirement x label family.

Do not compute any counts in this PR. This section defines only how a future
completed review could be summarized.

## 9. Interpretation boundaries

A label pattern can suggest a future research direction.

A label pattern cannot prove profitability.

A label pattern cannot prove a parameter change.

A label pattern cannot by itself justify removing minimum RR.

A label pattern cannot by itself justify using farther targets.

A label pattern cannot by itself justify changing stops.

A label pattern cannot create Strategy B2.

A label pattern cannot convert discretionary video doctrine directly into code.

A label pattern cannot replace a separate, scoped Strategy B design decision.

## 10. Recommended next PR

Recommended next PR: create a local-only manual review execution plan.

The next PR should specify how real candidate sampling, chart-window
preparation, reviewer-facing materials, hidden mappings, and filled worksheets
will remain local-only. It should not commit raw candidate rows, chart images,
CSV/JSON, data/results files, or filled worksheet rows.

Do not recommend another placeholder/mock dry run unless a new blocking template
issue is found.

## 11. Guardrails

Confirmed guardrails for this file:

- docs-only correction;
- exactly one Markdown file updated;
- no actual candidate sampling;
- no filled worksheet rows;
- no raw candidate CSV;
- no data, results, CSV, or JSON;
- no chart images;
- no Strategy A/B code change;
- no parameter, config, or test change;
- no backtest;
- no optimization;
- no Strategy C or Strategy B2;
- no broker, API, live-trading, or execution change;
- no profitability claims.
