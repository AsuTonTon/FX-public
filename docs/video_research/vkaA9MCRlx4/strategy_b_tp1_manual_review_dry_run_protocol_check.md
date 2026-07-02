# Strategy B TP1 Manual Review Dry-Run Protocol Check

Generated: 2026-06-26

This document performs a docs-only dry-run protocol check for the Strategy B TP1
manual review workflow using synthetic placeholder candidates only. It confirms
workflow shape before any real candidate review happens.

## 1. Objective and scope

Objective: verify that the Strategy B TP1 manual review worksheet template can
support a two-pass, outcome-blinded review process without leaking diagnostic
information into Pass A.

Scope:

- docs-only dry-run protocol check;
- placeholder/mock candidates only;
- no real candidate sampling;
- no raw candidate rows;
- no real chart review;
- no filled worksheet rows with real data;
- no Strategy B behavior changes;
- no Strategy A/B code changes;
- no parameter changes;
- no backtests;
- no optimization;
- no profitability evaluation;
- no Strategy B2 or Strategy C.

The mock examples below do not come from Strategy B outputs. They use no real
candidate IDs, no real pair names, no real timestamps, no real prices, no raw
candidate rows, and no real failure reasons from candidate exports.

## 2. Inputs inspected

Documents inspected:

- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_manual_review_worksheet_template.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_diagnostic_design.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_manual_chart_review_protocol.md`

Code was not inspected. The worksheet template and protocol documents supplied
the needed field names and review rules.

## 3. Dry-run method

The dry run uses three synthetic placeholder candidates:

- `MOCK-001`: a clear Pass A case where the reviewer can select structural
  labels confidently.
- `MOCK-002`: an ambiguous Pass A case that requires second review.
- `MOCK-003`: a case where Pass B reveal would create a documented correction
  request because a visible marker was misread.

Dry-run constraints:

- Use only mock IDs: `MOCK-001`, `MOCK-002`, and `MOCK-003`.
- Do not use real pair names.
- Do not use real timestamps.
- Do not use real prices.
- Do not use real candidate IDs.
- Do not use real failure reasons from candidate rows.
- Do not imply the mock cases came from Strategy B outputs.
- Use placeholder marker names rather than price levels.
- Use placeholder reveal fields rather than raw diagnostic values.

The dry run checks workflow shape only: whether the template can separate
reviewer-visible structural judgment from later diagnostic reveal.

## 4. Mock candidate dry-run

### Mock Candidate MOCK-001

Synthetic placeholder only - not a real Strategy B candidate.

#### Pass A visible fields

- presentation_id: `MOCK-001`
- chart_window_id: `<mock_chart_window_alpha>`
- direction: `<mock_direction_alpha>`
- visible_markers:
  - entry: `<mock_entry_marker_alpha>`
  - stop: `<mock_stop_marker_alpha>`
  - tp_rank_1: `<mock_tp_rank_1_alpha>`
  - tp_rank_2: `<mock_tp_rank_2_alpha>`
  - tp_rank_3: `<mock_tp_rank_3_alpha>`
  - tp_rank_4: `<mock_tp_rank_4_alpha>`
  - tp_rank_5: `<mock_tp_rank_5_alpha>`
- chart_context_notes: Synthetic chart context where rank 1 appears to sit on a
  clear prior reaction area and the stop marker appears beyond the visible
  premise boundary.

#### Pass A label selections

TP1 structural quality:

- `[x] tp1_meaningful_structural_target`
- `[x] tp1_reasonable_nearest_target`

Farther target availability:

- `[x] farther_structural_target_exists`
- `[ ] farther_target_is_clearer_than_tp1`

Stop anchor quality:

- `[x] stop_structurally_valid`

Corpus alignment:

- `[x] matches_structural_tp_doctrine`
- `[x] matches_stop_invalidation_doctrine`

Management distinction:

- `[x] initial_tp1_candidate`
- `[x] not_a_management_case`

#### Pass A notes

- reviewer_notes: Rank 1 looks structurally interpretable from the synthetic
  chart context; farther markers exist but do not appear clearer than rank 1.
- reviewer_confidence: high
- requires_second_review: no

#### Pass B reveal fields

- stable_reference: `<mock_stable_reference_alpha>`
- pair: `<mock_pair_alpha>`
- timeframe: `<mock_timeframe_alpha>`
- confirmation_time: `<mock_confirmation_time_alpha>`
- selected_bucket: `<mock_bucket_alpha>`
- first_fail_reason: `<mock_hidden_failure_reason_alpha>`
- all_failed_reasons: `<mock_hidden_failure_reason_list_alpha>`
- stop_distance_atr: `<mock_stop_distance_metric_alpha>`
- tp1_r: `<mock_tp1_r_metric_alpha>`
- tp2_r: `<mock_tp2_r_metric_alpha>`
- target_ranks_available: `<mock_target_rank_count_alpha>`
- accepted_or_rejected_status: `<mock_acceptance_status_alpha>`

#### Pass B interpretation labels

RR interpretation:

- `[x] low_rr_but_structural_tp`

#### Pass B interpretation notes

- locked_pass_a_summary: Pass A treated rank 1 as a meaningful initial TP1.
- diagnostic_interpretation: Mock reveal demonstrates that a low-RR diagnostic
  can be interpreted after Pass A without changing the structural label.
- correction_needed_to_pass_a: no
- correction_reason: none

### Mock Candidate MOCK-002

Synthetic placeholder only - not a real Strategy B candidate.

#### Pass A visible fields

- presentation_id: `MOCK-002`
- chart_window_id: `<mock_chart_window_beta>`
- direction: `<mock_direction_beta>`
- visible_markers:
  - entry: `<mock_entry_marker_beta>`
  - stop: `<mock_stop_marker_beta>`
  - tp_rank_1: `<mock_tp_rank_1_beta>`
  - tp_rank_2: `<mock_tp_rank_2_beta>`
  - tp_rank_3: `<mock_tp_rank_3_beta>`
  - tp_rank_4: `<mock_tp_rank_4_beta>`
  - tp_rank_5: `<mock_tp_rank_5_beta>`
- chart_context_notes: Synthetic chart context where rank 1 and farther markers
  are visually crowded and the stop marker is difficult to classify from the
  available context.

#### Pass A label selections

TP1 structural quality:

- `[x] tp1_not_visually_interpretable`

Farther target availability:

- `[x] farther_target_requires_discretion`

Stop anchor quality:

- `[x] stop_anchor_not_visually_interpretable`

Corpus alignment:

- `[x] corpus_alignment_unclear`

Management distinction:

- `[x] not_a_management_case`

#### Pass A notes

- reviewer_notes: The synthetic markers are too visually crowded to classify
  TP1 or the stop anchor with confidence. A second review should check whether
  the chart context is sufficient.
- reviewer_confidence: low
- requires_second_review: yes

#### Pass B reveal fields

- stable_reference: `<mock_stable_reference_beta>`
- pair: `<mock_pair_beta>`
- timeframe: `<mock_timeframe_beta>`
- confirmation_time: `<mock_confirmation_time_beta>`
- selected_bucket: `<mock_bucket_beta>`
- first_fail_reason: `<mock_hidden_failure_reason_beta>`
- all_failed_reasons: `<mock_hidden_failure_reason_list_beta>`
- stop_distance_atr: `<mock_stop_distance_metric_beta>`
- tp1_r: `<mock_tp1_r_metric_beta>`
- tp2_r: `<mock_tp2_r_metric_beta>`
- target_ranks_available: `<mock_target_rank_count_beta>`
- accepted_or_rejected_status: `<mock_acceptance_status_beta>`

#### Pass B interpretation labels

RR interpretation:

- `[x] rr_failure_not_diagnosable`

#### Pass B interpretation notes

- locked_pass_a_summary: Pass A was low-confidence and requested second review.
- diagnostic_interpretation: Mock reveal can explain why the case exists in a
  hidden bucket, but it does not resolve the chart ambiguity.
- correction_needed_to_pass_a: no
- correction_reason: none

### Mock Candidate MOCK-003

Synthetic placeholder only - not a real Strategy B candidate.

#### Pass A visible fields

- presentation_id: `MOCK-003`
- chart_window_id: `<mock_chart_window_gamma>`
- direction: `<mock_direction_gamma>`
- visible_markers:
  - entry: `<mock_entry_marker_gamma>`
  - stop: `<mock_stop_marker_gamma>`
  - tp_rank_1: `<mock_tp_rank_1_gamma>`
  - tp_rank_2: `<mock_tp_rank_2_gamma>`
  - tp_rank_3: `<mock_tp_rank_3_gamma>`
  - tp_rank_4: `<mock_tp_rank_4_gamma>`
  - tp_rank_5: `<mock_tp_rank_5_gamma>`
- chart_context_notes: Synthetic chart context where rank 1 appears minor, but a
  farther marker appears potentially more meaningful. The stop marker appears
  far from the entry marker, but structural context is mixed.

#### Pass A label selections

TP1 structural quality:

- `[x] tp1_minor_local_swing`
- `[x] tp1_near_entry_micro_structure`

Farther target availability:

- `[x] farther_structural_target_exists`
- `[x] farther_target_is_clearer_than_tp1`

Stop anchor quality:

- `[x] stop_too_wide_and_questionable`

Corpus alignment:

- `[x] matches_structural_tp_doctrine`
- `[x] corpus_alignment_unclear`

Management distinction:

- `[x] initial_tp1_candidate`

#### Pass A notes

- reviewer_notes: Rank 1 looks like micro-structure in this synthetic context,
  while a farther marker looks clearer. The stop marker may have been read
  against the wrong visible reference.
- reviewer_confidence: medium
- requires_second_review: yes

#### Pass B reveal fields

- stable_reference: `<mock_stable_reference_gamma>`
- pair: `<mock_pair_gamma>`
- timeframe: `<mock_timeframe_gamma>`
- confirmation_time: `<mock_confirmation_time_gamma>`
- selected_bucket: `<mock_bucket_gamma>`
- first_fail_reason: `<mock_hidden_failure_reason_gamma>`
- all_failed_reasons: `<mock_hidden_failure_reason_list_gamma>`
- stop_distance_atr: `<mock_stop_distance_metric_gamma>`
- tp1_r: `<mock_tp1_r_metric_gamma>`
- tp2_r: `<mock_tp2_r_metric_gamma>`
- target_ranks_available: `<mock_target_rank_count_gamma>`
- accepted_or_rejected_status: `<mock_acceptance_status_gamma>`

#### Pass B interpretation labels

RR interpretation:

- `[x] low_rr_due_to_minor_tp1`
- `[x] low_rr_due_to_questionable_stop`

#### Pass B interpretation notes

- locked_pass_a_summary: Pass A found a minor rank-1 target and a questionable
  stop anchor.
- diagnostic_interpretation: Mock reveal shows where diagnostic fields would be
  consulted after label lock.
- correction_needed_to_pass_a: yes
- correction_reason: The synthetic dry run assumes the reviewer later noticed a
  marker-reading mistake. The original Pass A labels remain preserved, and the
  correction is documented rather than silently replacing the Pass A record.

## 5. Blinding protocol check

Blinding checks performed:

| Check | Dry-run result |
| --- | --- |
| Are failure reasons hidden in Pass A? | Yes. Mock failure fields appear only in Pass B reveal placeholders. |
| Are R multiples hidden in Pass A? | Yes. Mock `tp1_r`, `tp2_r`, and stop-distance metrics appear only in Pass B reveal placeholders. |
| Are bucket names hidden in Pass A? | Yes. Mock bucket placeholders appear only in Pass B. |
| Are accepted/rejected labels hidden in Pass A? | Yes. Mock acceptance status appears only in Pass B. |
| Are outcome candles excluded from Pass A? | Yes. Pass A examples use synthetic pre-confirmation context notes only. |
| Is Pass A locked before Pass B? | Yes. Every mock case records a locked Pass A summary before diagnostic interpretation. |
| Is post-reveal correction limited to documented correction fields? | Yes. `MOCK-003` demonstrates correction through `correction_needed_to_pass_a` and `correction_reason` only. |

The template preserves the Pass A / Pass B separation in this synthetic dry run.

## 6. Worksheet usability issues

No blocking usability issues were found.

Non-blocking observations for a future template-correction PR:

- The candidate template allows both `corpus_alignment_unclear` and a specific
  corpus-alignment label to be selected. This may be useful for uncertainty, but
  future instructions could clarify whether `corpus_alignment_unclear` should be
  exclusive or allowed with another label.
- The management distinction family allows `initial_tp1_candidate` and
  `not_a_management_case` together. This is workable if the intended meaning is
  "initial target, not a management case", but future instructions could state
  that explicitly.
- The correction fields are sufficient for a dry run, but a future local
  worksheet may also need separate `original_pass_a_labels` and
  `corrected_pass_a_labels` fields if actual clerical corrections occur.

No severe inconsistency prevents the dry run. The worksheet template is not
modified in this PR.

## 7. Label usability observations

TP1 structural quality:

- Usable for separating a meaningful structural target from minor, noisy, or
  non-interpretable rank-1 targets.
- The labels worked for both the clear `MOCK-001` case and the ambiguous
  `MOCK-002` case.

Farther target availability:

- Usable for distinguishing "farther target exists" from "farther target is
  clearer than TP1" and "requires discretion".
- The dry run suggests these labels should remain separate because a farther
  marker can exist without being a better first target.

Stop anchor quality:

- Usable for distinguishing structurally valid, questionable, and
  non-interpretable stop anchors.
- `MOCK-003` shows that stop labels can interact with correction policy when a
  marker is misread.

Corpus alignment:

- Usable as a high-level mapping back to the 32-summary synthesis.
- The dry run suggests that `corpus_alignment_unclear` may need exclusivity
  guidance in a future refinement.

Management distinction:

- Usable for separating initial TP1 interpretation from protective, partial, or
  break-even management cases.
- The dry run suggests `initial_tp1_candidate` plus `not_a_management_case` is
  understandable but should be documented as an allowed combination if retained.

RR interpretation after Pass B:

- Usable only after diagnostic reveal.
- The dry run confirms that RR interpretation labels should stay out of Pass A
  because they depend on hidden metrics or hidden failure context.

These observations are protocol usability comments only. They are not trading
conclusions.

## 8. Aggregation readiness

The dry-run outputs would support later aggregation because each mock candidate
has structured fields for Pass A labels, Pass B interpretation labels,
confidence, second-review need, and correction status.

The template can support:

- count by bucket;
- count by TP1 structural quality label;
- count by farther target label;
- count by stop anchor label;
- count by RR interpretation label;
- count by management distinction label;
- count requiring second review;
- bucket x TP1 label cross-tabs;
- `stop_too_wide` x stop label cross-tabs;
- low-RR x TP1 label cross-tabs;
- later-rank-clears x farther target label cross-tabs;
- management distinction x TP1 label cross-tabs.

No real counts are computed in this PR.

## 9. What this dry run does not prove

This dry run does not prove Strategy B is good or bad.

This dry run does not prove profitability.

This dry run does not validate TP1 changes.

This dry run does not validate minimum RR changes.

This dry run does not validate farther target selection.

This dry run does not validate stop changes.

This dry run does not execute manual review.

This dry run does not use real candidates.

This dry run does not inspect raw candidate rows.

This dry run does not create Strategy B2.

This dry run does not authorize Strategy A/B code or parameter changes.

## 10. Recommended next PR

Updated routing after the public diagnostic boundary:

Do not proceed next to local-only manual review execution planning, raw
candidate export handling, chart-window preparation, reviewer-facing files,
hidden mappings, or filled worksheets. Next local-only diagnostic, packet,
sample, Pass A / Pass B, worksheet, mapping, reveal-table, chart-packet, or
review-run work remains paused under
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md` until
explicit human approval is given after corpus input, visual evidence review, and
doctrine synthesis dependencies are addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.

Do not recommend Strategy B behavior changes yet.

## 11. Guardrails

Confirmed guardrails for this PR:

- docs-only;
- exactly one Markdown file created;
- mock candidates only;
- no real candidate sampling;
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
