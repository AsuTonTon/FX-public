# Strategy B TP1 Local Artifact Preparation Checklist

Generated: 2026-06-26

This is a docs-only preparation checklist for the future Strategy B TP1 manual
chart review. It documents which existing commands, local-only outputs, and
documented fields are needed before the manual review can be retried.

## 1. Objective and scope

Objective: define a Git-safe checklist for preparing the local-only artifacts
required by the future Strategy B TP1 manual review.

Scope:

- docs-only preparation checklist;
- no command execution;
- no data generation;
- no market data fetching;
- no manual review execution;
- no candidate sampling execution;
- no raw candidate row inspection;
- no chart image generation;
- no reviewer packet generation;
- no hidden mapping generation;
- no filled worksheet rows;
- no Strategy B behavior changes;
- no Strategy A/B code changes;
- no parameter, config, or test changes;
- no backtests;
- no optimization;
- no profitability evaluation.

This checklist prepares the artifact boundary only. It does not authorize a
Strategy B rule change, Strategy B2, Strategy C, broker/API work, or live
trading.

## 2. Why this checklist exists

PR #38 recorded a blocker for the local-only Strategy B TP1 manual review. The
review could not execute because the required local-only source artifacts were
unavailable in ignored local paths.

The blocker matters because Codex must not:

- fabricate candidate rows;
- infer candidate rows from aggregate reports;
- fetch or download market data to fill the gap;
- call market-data or broker APIs;
- create chart packets without real local source inputs;
- expose hidden diagnostic fields during Pass A.

This checklist defines what must already exist, or what can be generated later
from already available local inputs, before the manual review execution task is
retried.

## 3. Existing command reference

The existing Strategy B read-only runner command is documented as:

```powershell
python -m src.backtest.strategy_b_runner `
  --input-dir data/strategy_a_ohlc `
  --pair-settings config/strategy_a_pairs.example.json `
  --output-dir results/strategy_b_readonly `
  --pairs USDJPY EURUSD
```

This PR does not run the command.

Command boundaries:

- The command requires local OHLC CSV input under `data/strategy_a_ohlc/`.
- The command must only be run when the local input data already exists.
- Running it must not fetch market data or call external APIs.
- Running it must not call broker APIs or perform live-trading work.
- Outputs must remain local-only and uncommitted under ignored `results/`.
- The command is a diagnostics/read-only artifact source, not a profitability
  proof or trading recommendation.

## 4. Required local source inputs

The following local-only source inputs must exist before retrying review
execution:

| input | purpose | Git status |
| --- | --- | --- |
| `data/strategy_a_ohlc/` | Local OHLC input directory for the read-only runner. | Must stay uncommitted. |
| Local OHLC CSVs for requested pairs | Candle source for runner outputs and chart-window preparation. Expected names include `{PAIR}_4h.csv`, `{PAIR}.csv`, `{pair}_4h.csv`, or `{pair}.csv`. | Must stay uncommitted. |
| `config/strategy_a_pairs.example.json` | Pair settings reference used by the documented read-only command. | Already tracked config reference; do not modify in this PR. |
| Existing local Strategy B candidate diagnostics, if already generated | May avoid rerunning the runner when valid local outputs already exist. | Must stay uncommitted. |

Required OHLC CSV columns are documented by the loader code as a timestamp
column alias (`timestamp`, `time`, `datetime`, or `date`) plus `open`, `high`,
`low`, and `close`.

Do not add raw or normalized market data to Git. Do not fetch, download, or
regenerate market data as part of this checklist.

## 5. Expected runner outputs

The read-only runner is expected to write local outputs under
`results/strategy_b_readonly/`:

| path | TP1 manual review use |
| --- | --- |
| `results/strategy_b_readonly/candidates/*_strategy_b_candidates.csv` | Required. Source for sampling buckets, Pass B reveal fields, candidate timing, entry, stop, TP1/TP2, RR, acceptance, and failure diagnostics. |
| `results/strategy_b_readonly/tp_candidates/*_strategy_b_tp_candidates.csv` | Required. Source for TP rank markers, rank 1-5 target prices/R values, selected TP1/TP2 flags, and swing metadata. |
| `results/strategy_b_readonly/events/` | Optional diagnostic trace. Not required for Pass A chart review and must not be exposed to the reviewer unless a later local-only protocol explicitly uses it after blinding checks. |
| `results/strategy_b_readonly/trades/` | Not required for Pass A. May support hidden accepted-control checks only after Pass A lock, but must not be used for outcome selection or profitability review. |
| `results/strategy_b_readonly/metrics/` | Not required for manual chart labels. May verify run metadata locally, but must not be used as profitability evidence. |
| `results/strategy_b_readonly/summary.md` | Optional local run summary. Must remain uncommitted and must not replace raw local source checks. |

Candidate and TP-candidate CSVs are the required sources for the TP1 manual
review. Events, trades, metrics, and summaries are secondary local diagnostics
and are not reviewer-facing Pass A material.

## 6. Manual review artifact mapping

| manual-review artifact | source file or source fields | existing runner provides it | additional local-only assembly required | may be committed to Git |
| --- | --- | --- | --- | --- |
| Sampling bucket source | Candidate CSV fields: `accepted`, `first_fail_reason`, `all_failed_reasons`, `tp1_r`, `tp2_r`, `stop_distance_atr`, `left_side_tp1_available`; TP candidate CSV fields: `target_rank`, `target_r`, `selected_tp1`, `selected_tp2`. | Partly. Runner provides source fields. | Yes. Build bucket assignment locally without exposing it to Pass A. | No. |
| Pass B reveal fields | `first_fail_reason`, `all_failed_reasons`, `tp1_r`, `tp2_r`, `stop_distance_atr`, `accepted`, target ranks available. | Yes, across candidate and TP candidate CSVs. | Yes. Copy into hidden mapping or Pass B worksheet fields locally after Pass A lock. | No. |
| TP rank markers | TP candidate CSV: `target_rank`, `target_price`, `selected_tp1`, `selected_tp2`; candidate CSV: `tp1_price`, `tp2_price`. | Yes. | Yes. Convert to neutral chart markers labeled rank 1-5. | No. |
| Chart-window inputs | Local OHLC data, candidate `confirmation_time`, `entry_time`, `entry_price`, `stop_price`, rank target prices. | Partly. Runner outputs marker prices and timestamps; OHLC input remains separate. | Yes. Build pre-confirmation/setup-context chart windows locally. | No. |
| Reviewer-facing chart packet | Opaque `presentation_id`, chart image/context, neutral entry/stop/target markers, direction if permitted. | No dedicated packet output. | Yes. Must be locally assembled after source artifacts exist. | No. |
| Hidden mapping | Candidate source reference, bucket, diagnostics, target ranks, chart file, worksheet path. | No dedicated mapping output. | Yes. Assemble locally from candidate CSV, TP candidate CSV, sampling results, and chart packet paths. | No. |
| Filled worksheets | Approved worksheet template plus Pass A and Pass B fields. | No. | Yes. Fill locally only after artifacts exist and Pass A/Pass B sequencing is enforced. | No. |
| Aggregate scratch calculations | Local completed worksheets and hidden mapping. | No. | Yes. Calculate locally after review completion. | No. |
| Git-safe aggregate report | Aggregate counts, cross-tabs, ambiguity categories, second-review counts, correction counts, non-raw interpretations. | No. | Yes, in a later PR after local review completion. | Yes, only if raw rows, charts, hidden mappings, and filled worksheets are excluded. |

## 7. Candidate CSV field mapping

Use documented schema only. Do not inspect raw rows in this PR.

| future review need | candidate CSV field or derivation | visibility |
| --- | --- | --- |
| Stable reference or candidate identifier | No single stored ID is documented. Assemble locally from `pair`, `direction`, `setup_time`, `touch_time`, `confirmation_time`, and `entry_time`; the protocol also recommends a compact review ID from pair, direction, and confirmation time, with entry time added on collision. | Hidden until Pass B. |
| Pair | `pair` | Hidden in Pass A where feasible; Pass B only. |
| Timeframe | Not a candidate CSV field. Derive from the runner setting, default `--timeframe-hours 4`, and record in hidden mapping. | Hidden in Pass A where feasible; Pass B only. |
| Direction | `direction` | May be visible in Pass A if needed to interpret entry/stop/targets. |
| Setup/touch context | `setup_time`, `touch_time` | Hidden source context; not Pass A visible unless converted into chart context without absolute source metadata. |
| Confirmation time | `confirmation_time` | Hidden in Pass A; used to cut chart window and reveal in Pass B. |
| Entry | `entry_time`, `entry_price` | Entry price marker may be visible; entry time remains hidden in Pass A. |
| Stop | `stop_anchor`, `stop_price`, `risk`, `buffer` | Stop marker may be visible; anchor diagnostics remain hidden unless later Pass B interpretation requires them. |
| Stop distance | `stop_distance_atr` | Hidden in Pass A; reveal in Pass B. |
| ADX context | `adx`, `adx_pass` | Hidden in Pass A; may support ADX-first-fail bucket after reveal. |
| Stop gates | `stop_too_narrow_pass`, `stop_too_wide_pass` | Hidden in Pass A; may support Pass B interpretation. |
| TP1 | `tp1_price` | Rank 1 marker may be visible as neutral chart marker. |
| TP1 R | `tp1_r` | Hidden in Pass A; reveal in Pass B. |
| TP2 | `tp2_price` | Rank 2 marker may be visible as neutral chart marker if available. |
| TP2 R | `tp2_r` | Hidden in Pass A; reveal in Pass B. |
| Target availability | `left_side_tp1_available`, plus TP candidate rows for rank availability | Hidden in Pass A except visible neutral target markers. |
| RR pass/fail gates | `tp1_min_rr_pass`, `tp1_only_min_rr_pass`, `tp2_min_rr_pass` | Hidden in Pass A; reveal only after lock if needed. |
| Accepted/rejected status | `accepted` | Hidden in Pass A; reveal in Pass B if needed for controls. |
| First failure reason | `first_fail_reason` | Hidden in Pass A; reveal in Pass B. |
| Full failure set | `all_failed_reasons` | Hidden in Pass A; reveal in Pass B. |

## 8. TP candidate CSV field mapping

Use documented schema only. Do not inspect raw rows in this PR.

| future review need | TP candidate CSV field or derivation | visibility |
| --- | --- | --- |
| Candidate reference | No single stored ID is documented. Join locally to candidate CSV by `pair`, `direction`, `setup_time`, `touch_time`, `confirmation_time`, and `entry_time`. | Hidden until Pass B. |
| Direction and timing | `pair`, `direction`, `setup_time`, `touch_time`, `confirmation_time`, `entry_time` | Hidden in Pass A except direction if needed. |
| Entry marker | `entry_price` | Visible in Pass A as neutral entry marker. |
| Stop marker | `stop_price` | Visible in Pass A as neutral stop marker. |
| Risk and ATR | `risk`, `atr` | Hidden in Pass A; use only for Pass B diagnostics. |
| Target rank | `target_rank` | Visible in Pass A only as neutral rank label. |
| Target price | `target_price` | Visible in Pass A as neutral rank marker. |
| Target R | `target_r` | Hidden in Pass A; reveal in Pass B. |
| Target source swing | `swing_index`, `swing_kind`, `swing_time` | Hidden metadata; may support local chart marker construction. |
| Target distance diagnostics | `swing_bar_distance_from_confirmation`, `swing_price_distance_from_entry`, `swing_price_distance_atr` | Hidden in Pass A; optional Pass B diagnostics. |
| Prominence proxy | `simple_prominence`, `simple_prominence_atr` | Hidden in Pass A; optional Pass B diagnostics. |
| Current TP flags | `selected_tp1`, `selected_tp2` | Hidden in Pass A; used locally to identify rank 1/2 and Pass B comparison. |
| Accepted status | `accepted` | Hidden in Pass A; reveal in Pass B if needed for controls. |
| First failure reason | `first_fail_reason` | Hidden in Pass A; reveal in Pass B. |

## 9. Sampling bucket preparation checklist

Future local sampling can be built from documented fields only. Do not compute
counts in this PR.

Before bucket assignment:

- Confirm candidate CSV exists locally.
- Confirm TP candidate CSV exists locally.
- Confirm each sampled source candidate can be identified deterministically.
- Sort or otherwise order candidates deterministically, such as by export order
  or `confirmation_time`.
- Apply de-duplication precedence so each source candidate belongs to only one
  hidden bucket.
- Keep bucket assignment hidden from Pass A material.
- Do not select or replace examples based on later outcome, profit, loss, TP
  hit, SL hit, or visually interesting charts.

Bucket preparation:

| bucket | required fields |
| --- | --- |
| Accepted candidates | Candidate CSV `accepted = True`; keep as hidden controls. |
| Very low TP1 R below 0.25R | Rank-1 `tp1_r` or selected rank-1 `target_r` below `0.25`. |
| TP1 R 0.25R-0.5R | Rank-1 `tp1_r` or selected rank-1 `target_r` from `0.25` inclusive to below `0.5`. |
| Near-miss 0.8R-1.0R | Rank-1 `tp1_r` or selected rank-1 `target_r` from `0.8` inclusive to below `1.0`. |
| `stop_too_wide` plus TP1 failure | Candidate CSV `first_fail_reason` or `all_failed_reasons` includes `stop_too_wide`, and `all_failed_reasons` includes `tp1_below_min_rr` when evaluable. |
| Later-rank-clears-1.0R | Rank 1 below `1.0R` and any available rank 2-5 `target_r >= 1.0`. |
| Rank 1-5 all fail 1.0R | Rank 1 below `1.0R`, at least one rank 2-5 available, and all available ranks 2-5 below `1.0R`. Keep separate from absent-later-rank cases. |
| `no_left_side_tp1` | Candidate CSV `first_fail_reason` or `all_failed_reasons` includes `no_left_side_tp1`, or `left_side_tp1_available = False`. |
| ADX-first-fail plus TP1 failure | Candidate CSV `first_fail_reason = adx_below_threshold` and `all_failed_reasons` includes `tp1_below_min_rr` when evaluable. |
| Deterministic controls | Deterministic controls selected without outcome or profitability criteria, replacing larger-bucket examples if needed. |

If a bucket has fewer available candidates than the target, record the shortfall
locally and do not pad with outcome-selected examples.

## 10. Chart-window preparation gap

No dedicated chart image or reviewer-facing chart packet generation command was
found in the existing inspected code. Existing code writes read-only runner
outputs, candidate CSVs, TP-candidate CSVs, events, trades, metrics, and
summaries; it does not create blinded chart images or review packets.

Future local chart-window preparation would need:

- local OHLC data already present under ignored paths;
- candidate timestamps, especially `confirmation_time` and `entry_time`;
- `entry_price`;
- `stop_price`;
- rank 1-5 `target_price` values from TP candidate diagnostics;
- the fixed pre-confirmation/setup-context window definition;
- EMA20 and EMA200 calculated only through the confirmation candle if rendered;
- neutral marker rendering for entry, stop, and target ranks;
- no post-confirmation outcome candles;
- no R values, failure reasons, selected bucket, accepted/rejected status, or
  outcome in Pass A material;
- local-only chart output paths such as `results/local_manual_review/charts/`.

Do not fetch market data to fill this gap. Do not implement chart rendering in
this PR.

## 11. Hidden mapping preparation checklist

A future local hidden mapping can be assembled only after candidate CSV, TP
candidate CSV, sampling decisions, and chart-window inputs exist locally.

Hidden mapping fields should include:

- `presentation_id`;
- `stable_reference`;
- `source_row_reference`;
- `pair`;
- `timeframe`;
- `direction`;
- `confirmation_time`;
- `selected_bucket`;
- `first_fail_reason`;
- `all_failed_reasons`;
- `tp1_r`;
- `tp2_r`;
- `stop_distance_atr`;
- `target_ranks_available`;
- `accepted_or_rejected_status`;
- `chart_window_id`;
- `worksheet_path_local`;
- `pass_a_locked_at`;
- `pass_b_revealed_at`;
- `second_review_required`;
- `correction_requested`.

Checklist:

- Build `stable_reference` deterministically from documented source fields.
- Assign `presentation_id` only after deterministic reviewer-facing ordering.
- Keep source pair/time/bucket/failure/R fields hidden from Pass A.
- Map each `presentation_id` to exactly one source candidate.
- Map each chart file or chart context to exactly one `presentation_id`.
- Store worksheet local path only in the hidden mapping.
- Keep hidden mapping local-only and uncommitted.
- Do not allow the hidden mapping keeper to influence Pass A labels.

## 12. Worksheet preparation checklist

The approved worksheet template should be copied and filled locally only after
the required artifacts exist.

Checklist:

- Copy `strategy_b_tp1_manual_review_worksheet_template.md` into a local-only
  review folder.
- Create either one worksheet per `presentation_id` or one combined local
  worksheet with one section per `presentation_id`.
- Fill Pass A visible fields first.
- Keep Pass B fields blank or inaccessible during Pass A.
- Record Pass A labels, reviewer notes, confidence, and second-review flag.
- Lock Pass A before revealing hidden diagnostics.
- Reveal Pass B fields only after Pass A lock.
- Preserve original Pass A labels if a correction is later needed.
- Use correction fields only for clerical mistakes or chart misreadings.
- Store filled worksheets under an ignored local path such as
  `results/local_manual_review/worksheets/`.
- Do not commit filled worksheets.

## 13. Preconditions before retrying execution

Before retrying the local manual review execution task, confirm all of the
following:

- Local OHLC input exists under ignored paths.
- The runner output exists or can be generated from already available local
  input without API calls, broker calls, data fetches, or downloads.
- Candidate CSV exists locally.
- TP candidate CSV exists locally.
- Required candidate CSV schema fields are present.
- Required TP candidate CSV schema fields are present.
- Chart-window input exists, including OHLC data and candidate marker fields.
- Local-only output folders exist or can be created under ignored paths:
  - `results/local_manual_review/`;
  - `results/local_manual_review/charts/`;
  - `results/local_manual_review/worksheets/`;
  - `results/local_manual_review/hidden_mappings/`.
- Reviewer-facing material can be prepared without revealing Pass B fields.
- `git status --short` shows no local artifacts staged.

Do not inspect raw candidate rows merely to satisfy this checklist in Git. Row
inspection belongs only to the later local-only execution task after artifacts
are available.

## 14. Hard stop conditions

Stop the execution task if any of these conditions occurs:

- Local OHLC input is missing.
- Candidate CSV is missing.
- TP candidate CSV is missing.
- Required schema fields are missing.
- Chart-window input is missing.
- Preparing charts would require fetching or downloading market data.
- Preparing charts would require calling external APIs.
- Preparing the sample would require fabricating candidates.
- Hidden mapping cannot be created without guessing source rows.
- Pass A material would expose failure reasons, R multiples, bucket names,
  accepted/rejected status, outcomes, or profitability.
- There is any risk of committing raw artifacts, generated CSV/JSON, charts,
  hidden mappings, filled worksheets, or market data.
- The task would require Strategy A/B code, parameter, config, or test changes.
- The task would require a backtest, optimization, Strategy B2, Strategy C,
  broker/API work, or live execution.

When a hard stop is reached, preserve the blocker state and report which local
artifact category is missing.

## 15. Recommended next step

Updated routing after the public diagnostic boundary:

Do not proceed next to making local-only inputs available for rerun, manual
review execution, packet creation, worksheet filling, or aggregate diagnostic
reporting. Next local-only diagnostic, packet, sample, Pass A / Pass B,
worksheet, mapping, reveal-table, chart-packet, or review-run work remains
paused under
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md` until
explicit human approval is given after corpus input, visual evidence review, and
doctrine synthesis dependencies are addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.

## 16. Guardrails

Confirmed guardrails for this PR:

- docs-only;
- exactly one Markdown file created;
- no command execution;
- no data fetch;
- no API call;
- no market data download;
- no raw candidate row inspection;
- no candidate CSV created;
- no TP candidate CSV created;
- no chart image created;
- no reviewer packet created;
- no hidden mapping created;
- no worksheet filled;
- no data, results, CSV, or JSON added;
- no Strategy A/B code change;
- no parameter, config, or test change;
- no backtest;
- no optimization;
- no Strategy C or Strategy B2;
- no broker, API, live-trading, or execution change;
- no profitability claims.
