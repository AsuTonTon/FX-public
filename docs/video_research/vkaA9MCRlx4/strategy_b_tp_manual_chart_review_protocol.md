# Strategy B TP Manual Chart Review Protocol

## 1. Scope and Guardrails

This document defines a protocol only. It is a reproducible, outcome-blinded
manual chart review procedure for Strategy B TP candidate interpretation.

This document does not change Strategy B code, rules, parameters, runner
behavior, stop placement, trade acceptance, or TP1/TP2 selection. It does not
change TP1 minimum RR, switch to rank 2 targets, change `swing_width`, change
`swing_lookback_bars`, create Strategy B2, create Strategy C, or make any
profitability claim.

This document must not incorporate or depend on the separate channel-wide
YouTube corpus research line. The only scope here is Strategy B TP candidate
manual chart review for the `vkaA9MCRlx4` research thread.

Do not commit:

- raw market CSVs
- normalized OHLC CSVs
- generated candidate or TP-candidate CSVs
- trade, event, metrics, summary, or results files
- chart images generated from market data
- filled review worksheets or review CSVs
- transcripts, subtitles, videos, secrets, or credentials

## 2. Review Objective

The review answers structural questions that the mechanical TP candidate export
cannot answer alone:

- Is the current rank 1 TP only a minor local swing?
- Does a later-ranked target represent a clearer left-side structural target?
- Are later ranks merely farther away without greater structural significance?
- Is there no clean left-side target?
- Is the candidate better classified as no-trade structure?
- Is stop distance too large relative to all visible targets?

The review should produce structured evidence for a later design discussion. It
must not directly create a new trading rule.

## 3. Outcome-blinding Rules

During Pass A, reviewers must not see:

- accepted or rejected status
- `first_fail_reason`
- existing pass/fail gate flags
- sample bucket
- accepted-control status
- target-R bucket
- source `review_id`
- absolute confirmation timestamp
- trade result
- TP or SL outcome
- entry candle high, low, close, or any indicator values calculated from the
  completed entry candle
- post-confirmation price action, except the next-bar open as an entry-price
  marker
- candles after the confirmation candle
- profitability metrics
- pair-level or strategy-level performance summaries for the reviewed sample

The chart may show only information available at decision time:

- candles up to and including the confirmation candle
- EMA20 and EMA200 calculated only through the confirmation candle
- next-bar open shown only as an entry-price marker
- stop price
- rank 1 through rank 5 target prices
- mechanically detected swing markers from the existing Strategy B diagnostic
  logic
- reviewer-facing opaque `presentation_id`

Target labels may be shown as `rank 1`, `rank 2`, `rank 3`, `rank 4`, and
`rank 5`. In Pass A, do not show `target_r`, prominence values, accepted status,
failure reason, sample bucket, source identifier, absolute timestamp, or
eventual outcome.

## 4. Fixed Chart Window

Use one fixed chart window for every reviewed candidate:

- Include the full existing 100-bar Strategy B target lookback.
- End the completed-candle view at the confirmation candle.
- Show the next-bar entry open only as a horizontal or point marker for entry
  price.
- Do not render the entry candle body, high, low, close, volume, or completed
  indicator values.
- Do not show candles after the confirmation candle.
- Use the same visual scale rule for every candidate.
- Use the same indicator set for every candidate: candles, EMA20, EMA200,
  entry price, stop price, target ranks 1-5, and existing swing markers.
- Use the same color and marker scheme for every candidate.
- Use relative bar labels during Pass A so the absolute confirmation timestamp
  is not visible.

Recommended chart framing:

- X-axis: completed candles from `confirmation_index - 100` through
  `confirmation_index`.
- Add the entry-open marker at the next-bar open without rendering the entry
  candle.
- If fewer than 100 prior candles exist, start at the first available candle.
- Y-axis: fit all visible candles, entry, stop, and rank 1-5 target prices.
- Do not zoom differently to make a target appear more or less meaningful.

## 5. Deterministic Sample Selection

Use only local ignored CSVs:

- `results/strategy_b_readonly/candidates/*_strategy_b_candidates.csv`
- `results/strategy_b_readonly/tp_candidates/*_strategy_b_tp_candidates.csv`

Do not fetch data, download data, call external APIs, or commit generated
outputs.

Select candidates independently for USDJPY and EURUSD using confirmation-time
order. A candidate is uniquely identified by pair, direction, setup time, touch
time, confirmation time, and entry time.

For each pair, select candidates into hidden sampling buckets in this precedence
order:

1. Earliest 5 unique candidates with rank 1 `< 0.25R`.
2. Earliest 5 unique candidates with `0.25R <= rank 1 < 0.5R`.
3. Earliest 5 unique candidates with `0.5R <= rank 1 < 1.0R`.
4. Earliest 5 unique candidates where rank 1 `< 1.0R` and any rank 2-5
   `>= 1.0R`.
5. Earliest 5 unique candidates where rank 1 `< 1.0R`, at least one rank 2-5
   target is available, and all available ranks 2-5 are `< 1.0R`.
6. Earliest 5 unique candidates where rank 1 `< 1.0R` and no rank 2-5 target is
   available.
7. All accepted candidates as hidden control examples.

Bucket 5 and bucket 6 must remain separate. Do not treat the absence of rank
2-5 targets as vacuously satisfying "all later targets are below 1.0R."

Duplicate removal:

- Apply the bucket order above as precedence.
- If a candidate qualifies for multiple buckets, keep it only in the first
  bucket it reaches.
- Record the assigned bucket in hidden local metadata only.
- Do not replace duplicates with outcome-selected examples.
- If a bucket has fewer than 5 remaining unique candidates, record the lower
  count rather than cherry-picking replacements.

Do not select examples based on eventual profit, loss, TP hit, SL hit, or any
other post-entry result.

Reviewer-facing presentation order:

1. After bucket selection and duplicate removal, build a hidden source mapping
   table.
2. Compute a deterministic hash key for each selected source candidate, for
   example:

   ```text
   sha256("strategy_b_tp_review_v1|" + review_id)
   ```

3. Sort all selected candidates by this hash key, not by pair, bucket, target R,
   accepted-control status, or confirmation time.
4. Assign reviewer-facing `presentation_id` values after sorting:
   `R0001`, `R0002`, `R0003`, and so on.
5. Mix accepted controls into this same hash-sorted order.
6. During Pass A, show only `presentation_id`, the blinded chart, and visible
   review fields. Do not show sample bucket, accepted-control status, target-R
   bucket, source `review_id`, pair grouping order, or absolute confirmation
   timestamp.
7. Reveal bucket and source metadata only in Pass B.

## 6. Stable Review Identifier

Use two identifiers:

- `presentation_id`: reviewer-facing opaque ID, such as `R0001`.
- source `review_id`: hidden local mapping key that links the blinded review
  item back to the source candidate.

Only `presentation_id` is visible in Pass A. The source `review_id`,
confirmation time, bucket, pair metadata ordering, accepted-control status, and
repeat relationships stay hidden until Pass B.

The hidden source `review_id` must be deterministic and contain no raw market
row data and no secret information.

Recommended format:

```text
{PAIR}_{DIRECTION}_{CONFIRMATION_TIME_COMPACT}
```

Example:

```text
USDJPY_short_20220120T000000
```

Rules:

- Use uppercase pair.
- Use lowercase direction.
- Convert confirmation time by removing `-`, `:`, and timezone punctuation.
- If two candidates ever collide, append `_entry_{ENTRY_TIME_COMPACT}`.
- Do not commit raw market rows or generated candidate CSVs.
- Do not expose the source `review_id` to reviewers during Pass A.

Recommended presentation ID assignment:

```text
R0001
R0002
R0003
```

Assign presentation IDs only after deterministic hash-based ordering has been
applied to the full selected set.

## 7. Review Form Schema

Each reviewed candidate must be recorded with the following fields:

| field | required | Pass A visible | Pass B visible | allowed values or format |
| --- | --- | --- | --- | --- |
| `presentation_id` | yes | yes | yes | Opaque ID such as `R0001`. |
| `source_review_id` | yes | no | yes | Hidden stable source identifier from section 6. |
| `pair` | yes | no | yes | `USDJPY`, `EURUSD`, or later approved pair. |
| `direction` | yes | yes | yes | `long` or `short`. |
| `sample_bucket` | yes | no | yes | Hidden bucket name from deterministic sample selection. |
| `accepted_control_status` | yes | no | yes | `accepted_control` or `not_control`. |
| `target_r_bucket` | yes | no | yes | Hidden sampling bucket based on rank 1 R. |
| `confirmation_time` | yes | no | yes | Absolute timestamp from source candidate. |
| `repeat_group_id` | conditional | no | yes, after all Pass A reviews are locked | Hidden repeat relationship. |
| `pass_name` | yes | yes | yes | `pass_a_blinded` or `pass_b_reveal`. |
| `chosen_classification` | yes | yes | yes | Fixed vocabulary below. |
| `chosen_target_rank` | conditional | yes | yes | `1`, `2`, `3`, `4`, `5`, or blank when no target is chosen. |
| `structural_reason` | yes | yes | yes | Fixed vocabulary below. |
| `secondary_reasons` | no | yes | yes | Semicolon-separated fixed vocabulary. |
| `confidence` | yes | yes | yes | `low`, `medium`, or `high`. |
| `notes` | no | yes | yes | Short reviewer note. Do not include outcome or profit/loss. |

Pass A reviewer-visible fields are limited to:

- `presentation_id`
- `direction`
- `pass_name`
- `chosen_classification`
- `chosen_target_rank`
- `structural_reason`
- `secondary_reasons`
- `confidence`
- `notes`

Pass A backend-only fields include:

- `source_review_id`
- `pair`
- `sample_bucket`
- `accepted_control_status`
- `target_r_bucket`
- `confirmation_time`
- `repeat_group_id`
- accepted or rejected status
- first failure reason
- target R and prominence values

`chosen_classification` must use one of:

- `current_rank1`
- `later_rank`
- `no_valid_target`
- `no_trade_structure`
- `insufficient_context`

`structural_reason` and `secondary_reasons` must use this fixed vocabulary:

- `minor_local_swing`
- `clear_major_swing`
- `repeated_reaction_zone`
- `isolated_swing`
- `clustered_targets_same_zone`
- `target_too_close`
- `target_too_far`
- `stop_too_wide`
- `no_clean_left_structure`
- `ambiguous_structure`

Confidence must use:

- `low`
- `medium`
- `high`

## 8. Two-pass Review Procedure

### Pass A: Blinded Structural Review

Pass A is the primary manual judgment.

1. Open the fixed chart window ending at the confirmation candle.
2. Show the next-bar open only as an entry-price marker.
3. Do not render the entry candle high, low, close, volume, or completed
   indicator values.
4. Hide sample bucket, accepted-control status, source `review_id`, absolute
   confirmation timestamp, accepted/rejected status, failure reasons, target R,
   prominence values, and all post-confirmation candles except the entry-open
   marker.
5. Inspect visible left-side structure only.
6. Choose one `chosen_classification`.
7. If `chosen_classification` is `current_rank1`, set `chosen_target_rank` to
   `1`.
8. If `chosen_classification` is `later_rank`, choose one rank from `2` to `5`.
9. If no target should be selected, leave `chosen_target_rank` blank.
10. Record `structural_reason`, optional `secondary_reasons`, `confidence`, and
   notes.
11. Lock the Pass A answer before revealing any R values, acceptance, failure
   reasons, or outcomes.

Do not revise Pass A after Pass B.

### Pass B: Diagnostic Reveal

Pass B compares the blinded structural choice with mechanical diagnostics.

Reveal only after Pass A is locked:

- sample bucket
- source `review_id`
- pair
- absolute confirmation time
- accepted-control status
- target rank
- target R
- `simple_prominence_atr`
- accepted/rejected status
- existing failure reasons

Reveal repeat relationships only after all Pass A reviews, including repeated
items, are locked.

In Pass B:

1. Compare the Pass A target choice with current Strategy B rank 1.
2. Record whether the structural choice agrees with rank 1, chooses a later
   rank, chooses no valid target, or rejects the setup as no-trade structure.
3. Record whether target R and prominence support or conflict with the Pass A
   structural choice.
4. Do not alter the original Pass A answer.
5. Do not inspect post-confirmation candles, trade outcome, or profitability
   metrics.

## 9. Repeatability Controls

Review candidates in the deterministic hash-based presentation order from
section 5. The reviewer-facing order must be independent of pair, sample bucket,
target R, accepted-control status, and confirmation time.

Include blinded repeats:

- Repeat every tenth selected candidate.
- Give repeated cases separate opaque `presentation_id` values from the same
  `R0001` sequence.
- Do not append `_repeat` or any other repeat marker to a reviewer-visible ID.
- Keep repeat relationships in hidden local metadata.
- The repeat must be shown without indicating the prior answer or that the item
  is a repeat.
- Record whether the repeated classification agrees with the first
  classification only after all Pass A answers are locked.
- Do not reveal that an item is a repeat until blinded review is complete.

Disagreement handling:

- Do not resolve disagreement by looking at trade outcome.
- Mark disagreement as `classification_disagreement`, `target_rank_disagreement`,
  `reason_disagreement`, or `confidence_disagreement` in the local worksheet.
- Keep both answers for aggregate reliability review.

## 10. Interpretation Rules

After the local review is complete, summarize aggregate evidence into one of
these categories:

- `supports_current_rank1`
- `supports_later_rank_hypothesis`
- `supports_no_trade_structure_filter`
- `mixed`
- `inconclusive`

Interpretation guidance:

- Use `supports_current_rank1` only if blinded reviews usually choose rank 1
  with medium or high confidence.
- Use `supports_later_rank_hypothesis` only if blinded reviews frequently
  choose ranks 2-5 for structural reasons, not merely because later ranks are
  farther away.
- Use `supports_no_trade_structure_filter` if many candidates are classified as
  `no_valid_target` or `no_trade_structure`.
- Use `mixed` when pair, bucket, or reviewer-repeat results conflict.
- Use `inconclusive` when confidence is mostly low or repeatability is poor.

Do not derive a new trading rule directly from individual examples. Do not set
a numeric Strategy B2 threshold in this protocol.

## 11. Local Artifacts

The following artifacts must remain local and ignored unless a separate
decision is made:

- chart images generated from market data
- filled review worksheets
- hidden source-to-presentation mapping files
- repeat relationship mapping files
- raw or filled review CSVs
- candidate CSVs
- TP-candidate CSVs
- runner outputs under `results/`

Only aggregate summarized findings should be considered for Git in a later
task. Those summarized findings must avoid raw market rows and must not claim
profitability.

## 12. Exit Criteria

After this protocol is approved:

1. Run the review locally as a separate task.
2. Keep charts, worksheets, candidate CSVs, and review result CSVs local and
   ignored.
3. Produce only an aggregate summarized report for Git.
4. Do not create Strategy B2 until both conditions are met:
   - manual review results exist, and
   - the separate channel-wide corpus analysis is available for alignment.

The channel-wide corpus work must remain separate until an explicit alignment
task is requested.

## 13. Non-action Decision

No Strategy B change is approved by this protocol.

Specifically:

- no TP1 minimum RR change
- no TP2 minimum RR change
- no target-rank change
- no rank 2 switch
- no stop-width change
- no swing parameter change
- no Strategy B2 implementation
- no Strategy C implementation

This protocol only defines how to collect better manual evidence before any
future design decision.

## 14. Validation

This is a docs-only protocol. No code, tests, strategy parameters, runner logic,
or generated outputs are changed.

Validation requirement for this PR:

```powershell
git diff --check
```

Full tests are not required unless code changes are introduced.
