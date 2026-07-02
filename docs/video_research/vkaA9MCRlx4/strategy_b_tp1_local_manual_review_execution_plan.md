# Strategy B TP1 Local Manual Review Execution Plan

Generated: 2026-06-26

This is a docs-only execution plan for a future local-only Strategy B TP1
manual chart review. It defines how the review should be run without committing
raw candidate data, chart packets, hidden mappings, filled worksheets, or any
other local review artifacts.

## 1. Objective and scope

Objective: define how the real Strategy B TP1 manual chart review will be
executed locally while preserving the approved worksheet, two-pass blinding
model, and Git guardrails.

Scope:

- docs-only local-only execution plan;
- no actual manual review execution;
- no actual candidate sampling;
- no raw candidate rows;
- no chart images;
- no reviewer packet generation;
- no hidden mapping file generation;
- no filled worksheets;
- no Strategy B behavior changes;
- no Strategy A/B code changes;
- no parameter changes;
- no config or test changes;
- no backtests;
- no optimization;
- no profitability evaluation.

This plan is procedural. It does not create any local review artifacts and does
not authorize Strategy B rule changes.

## 2. Relationship to prior docs

This plan follows the existing Strategy B TP1 review chain:

- `strategy_b_tp1_selection_review.md` identifies the current Strategy B TP1
  selection flow, the dominant TP1/RR rejection evidence, the stop/RR
  interaction, and the mismatch hypotheses that motivate manual review.
- `strategy_b_tp1_diagnostic_design.md` defines the future diagnostic buckets,
  label families, worksheet schema, interpretation rules, and first-pass sample
  proposal.
- `strategy_b_tp1_manual_review_worksheet_template.md` provides the approved
  Markdown worksheet structure, two-pass fields, label-locking policy,
  correction fields, and local-only review packet expectations.
- `strategy_b_tp1_manual_review_dry_run_protocol_check.md` confirms that the
  template can preserve Pass A / Pass B separation using mock candidates only.
- `strategy_b_tp_manual_chart_review_protocol.md` defines the older
  outcome-blinded chart-review mechanics, including opaque presentation IDs,
  hidden source mappings, fixed chart windows, and local-only artifacts.
- `channel_32_summary_interim_synthesis.md` provides the corpus context for
  structural TP, contextual RR, premise-based stop/invalidation, protective
  exits, and unresolved discretionary chart terms.

This plan turns the approved template into a future local workflow. It does not
execute that workflow.

## 3. Local-only artifact policy

The future manual review will create local artifacts. Those artifacts must stay
out of Git.

Local-only artifacts that must not be committed:

- raw candidate export CSV;
- sampled candidate list;
- chart window images;
- reviewer-facing chart packet;
- hidden source mapping;
- filled worksheets;
- reviewer notes with real candidate references;
- aggregate scratch calculations;
- any generated CSV, JSON, result, or intermediate file;
- any copied market data;
- any temporary chart-rendering cache;
- any manual-review archive package.

Recommended local-only paths:

- `data/local_manual_review/`
- `results/local_manual_review/`
- `results/local_manual_review/charts/`
- `results/local_manual_review/worksheets/`
- `results/local_manual_review/hidden_mappings/`

Repository `.gitignore` already ignores `data/` and `results/`, so these paths
are preferred for local review execution. If a reviewer wants a path such as
`local/review_packets/`, keep it outside the repository or add it to local
`.git/info/exclude` only. Do not modify repository `.gitignore` in this PR.

Before and after future review execution, run a local Git status check and
confirm that no local review artifact is staged or tracked.

## 4. Review roles and blinding model

Roles:

| Role | Purpose | May see | Must not do |
| --- | --- | --- | --- |
| Sampler / preparer | Select future review candidates locally and prepare hidden mappings and chart packets. | Raw candidate export, source references, hidden bucket assignment, chart window generation inputs. | Influence Pass A labels, expose hidden fields to reviewer, select examples by outcome or profitability. |
| Pass A reviewer | Judge visible chart structure using the worksheet. | Opaque `presentation_id`, anonymized chart context, direction if needed, neutral entry/stop/TP rank markers, pre-confirmation/setup-context candles. | See candidate IDs, pair names if avoidable, failure reasons, R multiples, selected bucket, accepted/rejected status, post-confirmation outcome, or profitability. |
| Adjudicator / second reviewer | Resolve low-confidence or ambiguous cases after Pass A lock. | Same Pass A material first; Pass B fields only after the relevant Pass A answers are locked. | Rewrite labels based on outcome or profitability. |
| Hidden mapping keeper | Preserve the source mapping and reveal fields after Pass A lock. | Full hidden mapping and source references. | Influence labels or leak hidden fields before Pass A lock. |
| Summarizer | Produce later aggregate findings. | Aggregate label counts, cross-tabs, correction counts, second-review counts, and anonymized presentation IDs if needed. | Commit raw rows, full worksheets, charts, market data, hidden mappings, or profitability claims. |

Blinding model:

- Pass A reviewer must not see candidate IDs, pair names if avoidable, failure
  reasons, R multiples, selected bucket, accepted/rejected status, or
  post-confirmation outcome.
- Hidden mapping keeper may see source references but must not influence labels.
- Summarizer may use aggregate label counts after review completion, but must
  not expose raw rows in Git.

## 5. Future candidate sampling procedure

This section defines future local sampling only. Do not sample actual candidates
in this PR.

Future first-pass target buckets:

| Bucket | Target count | Future selection basis |
| --- | ---: | --- |
| Accepted candidates | 2 | Accepted controls, hidden from Pass A reviewer. |
| Very low TP1 R below 0.25R | 4 | Rank-1 TP1 R below 0.25R. |
| TP1 R 0.25R-0.5R | 4 | Rank-1 TP1 R from 0.25R inclusive to below 0.5R. |
| Near-miss 0.8R-1.0R | 3 | Rank-1 TP1 R from 0.8R inclusive to below 1.0R, if available. |
| `stop_too_wide` plus TP1 failure | 4 | `stop_too_wide` and TP1 failure in the diagnostic failure set. |
| Later-rank-clears-1.0R | 4 | Rank 1 below 1.0R and any rank 2-5 at or above 1.0R. |
| Rank 1-5 all fail 1.0R | 4 | Rank 1 below 1.0R and all available ranks 2-5 below 1.0R. |
| `no_left_side_tp1` | 3 | No left-side TP1 available in the diagnostic export. |
| ADX-first-fail plus TP1 failure | 2 | ADX-first-fail cases that also fail TP1 after reveal. |
| Optional deterministic controls | 0-2 | Deterministic controls only if they replace examples from larger buckets. |

Sampling controls:

- Use deterministic ordering, such as export order or confirmation-time order,
  before assigning candidates to buckets.
- Apply de-duplication precedence before finalizing presentation IDs.
- Keep each source candidate in only one bucket.
- Use the listed target counts as the first-pass target; do not pad short
  buckets with outcome-selected examples.
- If a bucket has a shortfall, record the shortfall locally and keep the sample
  smaller.
- Do not use profitability, later outcome, or chart result to select or replace
  candidates.
- Do not cherry-pick visually interesting examples.
- Do not replace a selected case because the later outcome looks inconvenient.
- Keep accepted controls mixed into the reviewer-facing order without exposing
  accepted status.
- Keep optional controls deterministic and limited so the total review remains
  practical.

## 6. Chart-window preparation plan

Future chart windows must be prepared locally only. Do not create chart images
in this PR.

Pass A chart-window rules:

- Include only pre-confirmation and setup-context candles.
- Exclude all post-confirmation outcome candles.
- Use the fixed target lookback context required by the manual chart review
  protocol where feasible.
- Use neutral visible markers only:
  - entry;
  - stop;
  - TP rank 1;
  - TP rank 2;
  - TP rank 3;
  - TP rank 4;
  - TP rank 5.
- Label targets as rank markers only, not as accepted/rejected, failed/passed,
  or profitable/unprofitable.
- Do not display R values, failure reasons, selected bucket, accepted/rejected
  status, or outcome.
- Hide or anonymize pair and time metadata where feasible.
- Use relative bar labels if absolute timing would reveal hidden ordering or
  source identity.
- Keep chart packet files local-only and uncommitted.

Chart packet checks:

- Each chart file must map to exactly one `presentation_id`.
- Reviewer-facing filenames should use `presentation_id`, not source row
  references.
- Hidden metadata should live in the local hidden mapping only.
- The chart packet should not contain raw market-data tables.

## 7. Hidden mapping plan

The future local review should maintain one hidden mapping file or workbook
outside Git. Do not create that file in this PR.

Planned hidden mapping fields:

- `presentation_id`
- `stable_reference`
- `source_row_reference`
- `pair`
- `timeframe`
- `direction`
- `confirmation_time`
- `selected_bucket`
- `first_fail_reason`
- `all_failed_reasons`
- `tp1_r`
- `tp2_r`
- `stop_distance_atr`
- `target_ranks_available`
- `accepted_or_rejected_status`
- `chart_window_id`
- `worksheet_path_local`
- `pass_a_locked_at`
- `pass_b_revealed_at`
- `second_review_required`
- `correction_requested`

Hidden mapping rules:

- Hidden mapping remains local-only.
- Hidden mapping is not committed.
- Pass A reviewer must not see hidden mapping.
- Pass B uses hidden mapping only after labels are locked.
- Hidden mapping keeper must not use the mapping to influence Pass A labels.
- If the hidden mapping is updated, keep an audit note locally and do not commit
  the mapping.

## 8. Worksheet execution plan

Future worksheet execution should use the approved worksheet template locally.
Do not fill worksheets in this PR.

Execution steps:

1. Copy `strategy_b_tp1_manual_review_worksheet_template.md` into a local-only
   review folder.
2. Create either one worksheet per `presentation_id` or one combined local
   worksheet with one section per `presentation_id`.
3. Fill Pass A visible fields and labels first.
4. Keep hidden fields blank or inaccessible during Pass A.
5. Lock Pass A labels, notes, confidence, and second-review flag before Pass B.
6. Record the Pass A lock state locally.
7. Reveal Pass B fields only after Pass A lock.
8. Fill Pass B interpretation labels and diagnostic interpretation notes.
9. If corrections occur, preserve `original_pass_a_labels`, fill
   `corrected_pass_a_labels`, record `correction_scope`, and record
   `correction_reason`.
10. Flag low-confidence or consequentially ambiguous cases for second review
    rather than forcing classification.
11. Keep filled worksheets local-only unless a later PR explicitly requests a
    summarized, non-raw aggregate report.

Worksheet rules:

- Do not paste raw candidate CSV rows into worksheets.
- Do not paste market-data rows into worksheets.
- Do not include real pair/time/price row details in any Git-tracked report.
- Do not convert worksheet labels into Strategy B rule changes during review.

## 9. Quality-control checklist

Before future review:

- all sampled cases have a `presentation_id`;
- each `presentation_id` maps to exactly one hidden source row;
- bucket assignment is hidden from Pass A reviewer;
- no raw candidate data appears in reviewer packet;
- no failure reason, R multiple, accepted/rejected status, or selected bucket
  appears in Pass A material;
- no outcome candles appear in Pass A material;
- chart markers are visible and neutral;
- pair/time metadata is hidden or anonymized where feasible;
- local-only files are outside Git staging;
- `git status --short` shows no local review artifacts staged or tracked.

After future review:

- Pass A labels are locked;
- Pass B reveal is performed only after lock;
- corrections are additive and preserve original Pass A state;
- low-confidence cases are flagged;
- second-review cases are identified;
- aggregate summary uses counts only;
- hidden mappings remain local-only;
- chart packets remain local-only;
- no raw rows or filled worksheets are committed;
- no outcome or profitability analysis is added to the aggregate summary.

## 10. Aggregate summary plan

A future Git-safe aggregate summary may contain:

- aggregate counts by label;
- aggregate counts by bucket;
- aggregate counts by reviewer confidence;
- aggregate counts requiring second review;
- correction-request counts by correction scope;
- cross-tabs without raw row details;
- examples described only as anonymized `presentation_id` values if needed;
- unresolved ambiguity categories;
- recommendation for the next research step.

A future Git-safe aggregate summary must not contain:

- raw candidate rows;
- real pair/time/price rows;
- full worksheet contents;
- chart images;
- market data;
- hidden mapping rows;
- per-trade outcome;
- profitability;
- generated CSV, JSON, or result files.

## 11. Failure modes and mitigations

| Failure mode | Mitigation |
| --- | --- |
| Pass A leakage from failure reason or R multiple | Keep failure reasons, R multiples, buckets, and accepted/rejected status only in hidden mapping until Pass B. |
| Outcome leakage from chart window | Render Pass A charts with pre-confirmation/setup-context candles only and exclude post-confirmation outcome candles. |
| Reviewer overfitting to bucket patterns | Randomize or hash-sort reviewer-facing order and hide bucket assignments during Pass A. |
| Ambiguous labels | Allow `requires_second_review: yes`; use unclear/not-interpretable labels rather than forced classification. |
| Correction after reveal becomes hindsight bias | Preserve `original_pass_a_labels`; allow corrections only for clerical mistakes or chart misreadings; record `correction_scope` and `correction_reason`. |
| Accidental commit of local artifacts | Use ignored `data/` or `results/` local subpaths, run `git status --short`, and stage only intended Markdown reports. |
| Label counts treated as profitability evidence | State in aggregate report that label counts are structural review evidence only, not outcome or profitability evidence. |
| Discretionary labels converted directly into code | Require a separate Strategy B design decision before any behavior change; do not treat manual labels as implementation specs. |
| Hidden mapping keeper influences labels | Separate the mapping keeper role from the Pass A reviewer role where feasible. |
| Pair/time metadata reveals source identity | Hide or anonymize pair/time metadata in Pass A material where feasible. |

## 12. What this plan does not answer

This plan does not answer profitability.

This plan does not define a TP1 rule change.

This plan does not define a minimum RR change.

This plan does not define a stop rule change.

This plan does not define a farther-target rule change.

This plan does not create Strategy B2.

This plan does not prove that video discretion is mechanizable.

This plan does not produce a backtest result.

This plan does not establish live trading readiness.

This plan does not authorize broker, API, or execution work.

## 13. Recommended next PR

Recommended next step: execute the local-only manual review outside Git using
this approved plan, then create a Git-safe aggregate manual review report PR.

That later report PR should summarize only non-raw aggregate findings, such as
label counts, bucket counts, cross-tabs, ambiguity categories, second-review
counts, and correction counts. It should not include raw candidate rows, chart
images, hidden mappings, filled worksheets, market data, generated CSV/JSON,
backtests, profitability claims, or Strategy B behavior changes.

Do not recommend Strategy B behavior changes yet.

## 14. Guardrails

Confirmed guardrails for this PR:

- docs-only;
- exactly one Markdown file created;
- no actual candidate sampling;
- no raw candidate CSV;
- no hidden mapping file;
- no reviewer packet;
- no chart images;
- no filled worksheet rows;
- no data, results, CSV, or JSON;
- no Strategy A/B code change;
- no parameter, config, or test change;
- no backtest;
- no optimization;
- no Strategy C or Strategy B2;
- no broker, API, live-trading, or execution change;
- no profitability claims.
