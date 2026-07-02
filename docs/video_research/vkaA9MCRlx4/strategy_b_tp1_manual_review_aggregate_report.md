# Strategy B TP1 Manual Review Aggregate Report

## Scope and guardrails

This report records the aggregate result of the local-only Strategy B TP1 manual chart review. It is a diagnostic artifact only.

- No Strategy B rule, parameter, code, config, or test change is included.
- No Strategy B2 or Strategy C work is included.
- No market-data API, broker API, download, runner execution, order placement, automation, or real-money workflow was used for this report.
- Local CSV data, generated charts, worksheets, hidden mappings, and result files remain outside Git.
- This report does not claim profitability or live-trading suitability.

## Execution status

Local manual review completed successfully against the existing local read-only artifacts.

- Base candidates reviewed: 30
- Repeat items reviewed: 3
- Total presentation items reviewed: 33
- Second-review candidates flagged: 7
- Correction-request count: 0

The repeated cases used separate opaque presentation IDs during review. Repeat relationships were kept in hidden local metadata and were not shown during Pass A.

## Documents inspected

- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_local_manual_review_execution_plan.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_local_artifact_preparation_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_manual_review_worksheet_template.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_manual_review_dry_run_protocol_check.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_diagnostic_design.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp_manual_chart_review_protocol.md`
- `docs/video_research/channel_32_summary_interim_synthesis.md`

## Code inspected

None. This execution was intentionally limited to the approved local artifacts and manual-review protocol. No source code was inspected or modified.

## Source artifact status

The required local source artifacts existed in the working tree and matched the expected high-level schemas:

- `data/strategy_a_ohlc/EURUSD_4h.csv`
- `data/strategy_a_ohlc/USDJPY_4h.csv`
- `results/strategy_b_readonly/candidates/EURUSD_strategy_b_candidates.csv`
- `results/strategy_b_readonly/candidates/USDJPY_strategy_b_candidates.csv`
- `results/strategy_b_readonly/tp_candidates/EURUSD_strategy_b_tp_candidates.csv`
- `results/strategy_b_readonly/tp_candidates/USDJPY_strategy_b_tp_candidates.csv`

No raw source rows, chart images, hidden mappings, worksheet rows, timestamps, prices, or pair-level case details are committed in this report.

## Local-only artifacts

The following local-only artifacts were created under ignored `results/` paths and are not part of this PR:

- `results/local_manual_review/charts/`
- `results/local_manual_review/worksheets/`
- `results/local_manual_review/hidden_mappings/`
- `results/local_manual_review/sample_summary.json`

## Sampling summary

All planned bucket targets were satisfied without shortfall.

| Bucket | Target | Selected | Shortfall |
|---|---:|---:|---:|
| accepted_candidates | 2 | 2 | 0 |
| very_low_tp1_r_below_0_25r | 4 | 4 | 0 |
| tp1_r_0_25r_to_0_5r | 4 | 4 | 0 |
| near_miss_0_8r_to_1_0r | 3 | 3 | 0 |
| stop_too_wide_plus_tp1_failure | 4 | 4 | 0 |
| later_rank_clears_1_0r | 4 | 4 | 0 |
| rank1_to_5_all_fail_1_0r | 4 | 4 | 0 |
| no_left_side_tp1 | 3 | 3 | 0 |
| adx_first_fail_plus_tp1_failure | 2 | 2 | 0 |

## Aggregate labels

### Chosen classification

| Label | Count |
|---|---:|
| current_rank1 | 22 |
| later_rank | 2 |
| no_trade_structure | 3 |
| no_valid_target | 3 |

### TP1 structural quality

| Label | Count |
|---|---:|
| tp1_reasonable_nearest_target | 19 |
| tp1_meaningful_structural_target | 9 |
| tp1_near_entry_micro_structure | 5 |
| tp1_inside_noise | 3 |
| tp1_not_visually_interpretable | 3 |
| tp1_minor_local_swing | 2 |

### Farther target

| Label | Count |
|---|---:|
| farther_structural_target_exists | 17 |
| no_clear_farther_target | 11 |
| farther_target_is_clearer_than_tp1 | 2 |
| farther_target_requires_discretion | 2 |

### Stop anchor

| Label | Count |
|---|---:|
| stop_structurally_valid | 17 |
| stop_too_wide_but_structural | 5 |
| stop_anchor_not_visually_interpretable | 5 |
| stop_too_wide_and_questionable | 3 |

### Corpus alignment

| Label | Count |
|---|---:|
| matches_structural_tp_doctrine | 23 |
| matches_contextual_rr_doctrine | 7 |
| matches_stop_invalidation_doctrine | 7 |
| corpus_alignment_unclear | 7 |

### RR interpretation

| Label | Count |
|---|---:|
| low_rr_but_structural_tp | 22 |
| low_rr_due_to_minor_tp1 | 5 |
| rr_failure_not_diagnosable | 3 |
| low_rr_due_to_questionable_stop | 3 |
| low_rr_due_to_wide_structural_stop | 1 |

### Reviewer confidence

| Label | Count |
|---|---:|
| medium | 22 |
| high | 6 |
| low | 2 |

## Repeat consistency

All three repeat checks matched their original review item on:

- chosen classification
- chosen target rank
- reviewer confidence

This is a small internal consistency check only. It is not a substitute for a second reviewer.

## Selected non-raw cross-tabs

### Bucket by classification

| Cross-tab | Count |
|---|---:|
| accepted_candidates x current_rank1 | 2 |
| very_low_tp1_r_below_0_25r x current_rank1 | 4 |
| tp1_r_0_25r_to_0_5r x current_rank1 | 4 |
| near_miss_0_8r_to_1_0r x current_rank1 | 3 |
| stop_too_wide_plus_tp1_failure x current_rank1 | 3 |
| stop_too_wide_plus_tp1_failure x no_trade_structure | 1 |
| later_rank_clears_1_0r x current_rank1 | 2 |
| later_rank_clears_1_0r x later_rank | 1 |
| later_rank_clears_1_0r x no_trade_structure | 1 |
| rank1_to_5_all_fail_1_0r x current_rank1 | 3 |
| rank1_to_5_all_fail_1_0r x no_trade_structure | 1 |
| no_left_side_tp1 x no_valid_target | 3 |
| adx_first_fail_plus_tp1_failure x current_rank1 | 1 |
| adx_first_fail_plus_tp1_failure x later_rank | 1 |

### Stop label by RR interpretation

| Cross-tab | Count |
|---|---:|
| stop_structurally_valid x low_rr_but_structural_tp | 16 |
| stop_too_wide_but_structural x low_rr_but_structural_tp | 5 |
| stop_anchor_not_visually_interpretable x rr_failure_not_diagnosable | 3 |
| stop_too_wide_and_questionable x low_rr_due_to_questionable_stop | 3 |
| stop_too_wide_and_questionable x low_rr_due_to_minor_tp1 | 3 |
| stop_anchor_not_visually_interpretable x low_rr_but_structural_tp | 1 |
| stop_anchor_not_visually_interpretable x low_rr_due_to_minor_tp1 | 1 |
| stop_structurally_valid x low_rr_due_to_minor_tp1 | 1 |
| stop_too_wide_but_structural x low_rr_due_to_wide_structural_stop | 1 |

## Main structural findings

1. Rank-1 TP1 was often visually defensible in this small diagnostic sample.
   - `current_rank1` was selected for 22 of 30 base candidates.
   - Many low-R TP1 cases still looked like structural or reasonable nearest targets, not purely noise.

2. The later-rank hypothesis has limited but real support.
   - `later_rank` was selected for 2 of 30 base candidates.
   - These cases suggest that some rank-1 targets may be minor or too near-entry while a farther structural target is clearer.

3. No-valid and no-trade structures remain important.
   - `no_trade_structure` appeared in 3 base cases.
   - `no_valid_target` appeared in 3 base cases, concentrated in the no-left-side-TP1 bucket.

4. Stop-anchor interpretation is mixed.
   - 17 base candidates had a structurally valid stop anchor.
   - 5 were too wide but still structural.
   - 3 were too wide and questionable.
   - 5 were not visually interpretable from the blinded chart context.

5. RR failures should not be treated as one single cause.
   - 22 cases were labeled `low_rr_but_structural_tp`.
   - 5 cases were labeled `low_rr_due_to_minor_tp1`.
   - 3 cases were labeled `low_rr_due_to_questionable_stop`.

## Ambiguity and second-review needs

The seven second-review candidates should be adjudicated before turning this into a rule change proposal. The main ambiguity classes are:

- no clean left-side structure under the fixed chart window
- micro-structure TP1 versus meaningful structural TP1
- structurally valid but wide stops
- corpus alignment unclear when TP1 is close but still visually repeated

## Interpretation boundaries

This review is intentionally small and diagnostic. It can identify failure modes and candidate hypotheses, but it cannot prove performance, profitability, or production readiness.

The review also depends on chart rendering choices and a single reviewer. Any proposed Strategy B change should be treated as a hypothesis requiring another fixed-spec diagnostic pass before implementation.

## Recommended next PR

The next PR should be a second-review or adjudication report for the seven flagged cases, not a Strategy B rule change. After that, a Strategy B TP1 design note can compare:

- keeping rank-1 TP1 as-is
- allowing a farther structural target only under a tightly specified rule
- separating low-R-but-structural TP from minor near-entry TP
- preserving no-valid-target rejection where no left-side structure is visible

No implementation or parameter change is recommended from this aggregate alone.

## Guardrail confirmations

- Raw CSV files were not committed.
- Normalized CSV files were not committed.
- Generated result CSVs were not committed.
- Hidden mappings were not committed.
- Chart images were not committed.
- Local worksheets were not committed.
- No Strategy B code, rule, or parameter was changed.
- No Strategy B2 or Strategy C work was performed.
- No runner, market-data API, broker API, download, auto-trading, order placement, or real-money action was performed for this report.
- No profitability claim is made.
