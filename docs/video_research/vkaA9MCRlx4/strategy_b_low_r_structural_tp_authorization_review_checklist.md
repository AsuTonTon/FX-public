# Strategy B Low-R Structural TP Authorization Review Checklist

## 1. Objective and scope

This checklist reviews whether a future Strategy B low-R-but-structural TP
diagnostic authorization issue is complete enough for automation to classify it
before any local-only diagnostic proceeds.

Scope:

- use committed repository Markdown reports only;
- define review checks for required authorization fields;
- classify a future issue as routine, blocked, PM-decide, or
  executive-escalation;
- preserve the current Strategy B behavior freeze;
- keep low-R-but-structural TP separate from no-valid-target,
  no-trade-structure, stop width, stop validity, fallback availability,
  accepted status, and outcomes;
- recommend one bounded docs-only next task.

Out of scope:

- no diagnostic run;
- no local OHLC data or generated Strategy B artifact access;
- no chart packet, worksheet, mapping, reveal table, sample row, CSV, JSON,
  image, `data/`, or `results/` creation;
- no market-data API, broker API, live system, order placement, auto-trading,
  or live-trading access;
- no Strategy A/B/B2/C behavior, code, parameter, config, test, runner, or
  backtest behavior change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no profitability, live-readiness, money-making, or trading-recommendation
  claim.

## 2. Source docs used

Committed repository docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_low_r_structural_tp_authorization_issue_skeleton.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_diagnostic_authorization_template.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_design_review_evidence_gap_ledger.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_width_vs_stop_validity_evidence_matrix.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_contextual_rr_requirements_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_no_valid_target_no_trade_structure_taxonomy_preservation.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market-data APIs, broker/live
systems, YouTube sources, DownSub, captions, subtitles, transcript bodies,
caption URLs, comments, live chat, community posts, downloaded media, ASR, or
external sources were used for this checklist.

## 3. Checklist use boundary

Use this checklist only to decide whether a future authorization issue is
complete and safely classifiable before local-only work starts.

Allowed review results:

- routine, when every required field is present and the requested output is
  Git-safe aggregate Markdown only;
- blocked, when required fields are missing, contradictory, or impossible to
  verify without unauthorized access;
- PM-decide, when the issue is bounded but leaves reviewer discretion or
  prioritization unresolved;
- executive-escalation, when the issue asks for Strategy behavior changes,
  optimization, broader source universes, live/broker behavior, or claims that
  exceed research documentation.

This checklist does not authorize local reads, diagnostic runs, implementation
work, or Strategy B design changes.

## 4. Required field checklist

| Field | Complete when | Classify as blocked when |
| --- | --- | --- |
| Exact diagnostic question | The issue asks one bounded low-R-but-structural TP question. | The question is broad exploration, rule design, implementation, or threshold review. |
| Allowed source classes | The issue names committed docs plus exact local-only artifact classes. | Source classes are unrestricted, external, or require unnamed local files. |
| Fixed local-only root | The root is stated in Git-safe redacted form, normally `<USER_HOME>\FX-local-data\FX-public`. | The root is absent, ambiguous, outside the boundary, or requires committing exact local paths. |
| Sample buckets and target counts | Bucket names, target counts, replacement rules, and shortfall rules are predeclared. | Buckets are chosen after accepted status, result, profit, loss, later movement, or performance-like fields are known. |
| Replacement and shortfall rules | Replacement is explicitly allowed or forbidden, and shortfall handling is stated. | The issue encourages filling gaps from adjacent taxonomy classes without a rule. |
| Hidden fields for Pass A | Stop distance, RR, target rank, accepted status, rejection reason, and outcome-like fields are hidden unless narrowly authorized. | Hidden fields are visible in filenames, paths, packet order, worksheet columns, or surrounding metadata. |
| Revealed fields for Pass B | Pass B fields are named and used only after Pass A labels are locked. | Pass B fields revise Pass A labels without a predeclared adjudication rule. |
| Locked Pass A labels | Labels include low-R-but-structural TP, adjacent taxonomy classes, ambiguity, and unusable/shortfall states. | Labels collapse low-R-but-structural TP into no-valid-target, no-trade-structure, stop width, stop validity, accepted status, or outcomes. |
| Ambiguity and second review | Ambiguity, disagreement, and adjudication handling are predeclared. | Ambiguous labels are counted as implementation support. |
| Git-safe output | Output is compact aggregate Markdown only. | The conclusion needs raw rows, pair/time/price/candle detail, charts, worksheets, mappings, CSV/JSON, `data/`, or `results/` in Git. |
| Hard-stop conditions | The issue names stops before local access, during sample selection, during Pass A, during Pass B, and before PR creation. | Stop conditions are missing or discretionary. |
| No Strategy behavior change | The issue explicitly confirms no Strategy behavior, code, parameter, config, test, runner, or backtest change. | The issue requests or implies implementation, tuning, or behavior changes. |

Missing required fields should stop automation before local access or file
changes.

## 5. Pass A / Pass B checklist

Before Pass A:

- confirm the issue explicitly authorizes the local read or diagnostic run;
- confirm the source classes and fixed local-only root are complete;
- confirm sample buckets were selected without accepted status, results,
  profit, loss, later movement, or performance-like fields;
- confirm filenames, paths, ordering, and packet metadata do not reveal hidden
  fields.

During Pass A:

- use only fields authorized by the future issue;
- lock labels before RR, stop distance, target rank, accepted status, rejection
  reason, or outcome-like fields are revealed;
- keep low-R-but-structural TP separate from no-valid-target,
  no-trade-structure, stop width, stop validity, fallback availability,
  accepted status, and outcomes;
- record ambiguous, disagreement, shortfall, and unusable states separately.

During Pass B:

- reveal only fields named by the issue;
- interpret relationships in aggregate only;
- do not revise Pass A labels unless a specific adjudication rule was
  predeclared;
- treat shortfall, ambiguity, or mixed evidence as blockers for design review,
  not as support for rule changes.

## 6. Git-safe output checklist

Allowed Git output:

- compact aggregate Markdown reports;
- aggregate bucket counts;
- aggregate Pass A label counts;
- aggregate Pass B interpretation;
- shortfall summaries;
- ambiguity and disagreement summaries;
- blocker notes;
- docs-only next-task recommendations.

Forbidden Git output:

- `data/` or `results/`;
- raw market data or normalized market CSV;
- candidate, event, trade, TP-candidate, result, worksheet, mapping, packet, or
  diagnostic CSV/JSON files;
- chart packets, chart images, screenshots, or contact sheets;
- row-level pair, time, price, candle, chart, or outcome detail;
- hidden mappings or reveal tables;
- raw transcripts, subtitle full text, raw TXT/SRT/VTT files, caption URLs, or
  downloaded media;
- credentials, tokens, or secrets.

If Git-safe aggregate Markdown cannot support the conclusion, the future issue
is blocked rather than broadened.

## 7. Taxonomy-separation checklist

The future issue must preserve these separations:

| Category | Must remain separate from |
| --- | --- |
| Low-R-but-structural TP | No-valid-target, no-trade-structure, stop-width-only concern, stop-validity concern, accepted status, and outcomes. |
| No-valid-target / no-left-side-target | Low-RR TP availability, stop-width, stop-validity, fallback availability, and outcome. |
| No-trade-structure | Target absence, low-RR TP availability, stop-width, fallback availability, and implementation evidence. |
| Stop width | Structural stop validity, RR failure, accepted status, and outcomes. |
| Stop validity | Stop width, RR, target rank, fallback availability, accepted status, and outcomes. |
| Fallback availability | Stop validity, stop width, target absence, no-trade-structure, and broader source-universe conclusions. |

Any issue that merges these categories into implementation behavior requires
executive escalation.

## 8. Hard-stop checklist

Stop before local access or file changes when:

- the future issue does not explicitly authorize the local read or diagnostic
  run being attempted;
- any required authorization field is missing;
- the diagnostic question is not exact and bounded;
- source classes, local root, sample buckets, hidden fields, Pass A / Pass B
  handling, output shape, or stop conditions are ambiguous;
- sample buckets depend on accepted status, result, profit, loss, later
  movement, or performance-like outcomes;
- hidden fields cannot be hidden before Pass A labels are locked;
- raw/generated artifacts would need to be committed;
- row-level details would be needed in Git;
- low-R-but-structural TP is merged into no-valid-target, no-trade-structure,
  stop width, stop validity, fallback availability, accepted status, or
  outcomes;
- the issue asks for Strategy A/B/B2/C behavior, code, parameter, config, test,
  runner, or backtest changes;
- the issue asks for Strategy B2, Strategy C, parameter optimization, or
  performance-tuned threshold search;
- the issue asks for market-data API, broker API, live system, order placement,
  auto-trading, live-trading, or live-readiness work;
- YouTube corpus findings would be mixed into Strategy B behavior without a
  separate design decision;
- any output would imply profitability, money-making reliability,
  live-readiness, or trading advice.

## 9. Routine / blocked / PM-decide / executive-escalation decision table

| Outcome | Use when | Automation action |
| --- | --- | --- |
| Routine | The issue is diagnostic-only, all fields are complete, source classes are bounded, Pass A / Pass B separation is enforceable, and output is aggregate Markdown only. | Proceed only with the explicitly authorized bounded work. |
| Blocked | Required fields are missing, local boundaries are ambiguous, hidden fields cannot be hidden, or Git-safe output cannot support the conclusion. | Stop without local access or file changes; report the missing field or blocker. |
| PM-decide | The issue is bounded but leaves priority, reviewer count, ambiguity tolerance, replacement policy, or shortfall handling unresolved. | Stop and request a PM decision in the issue or controlling thread. |
| Executive-escalation | The issue asks for Strategy behavior changes, optimization, Strategy B2/C creation, broader source universes, live/broker behavior, taxonomy merges into implementation, or profitability/live-readiness claims. | Stop without changes; require explicit executive design decision. |

## 10. No Strategy behavior change confirmation

Confirmed:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B TP1, TP2, RR, contextual RR, stop-anchor, stop-buffer, stop
  sanity, ADX, ATR, swing-width, lookback, pair-setting, management, runner,
  config, test, or backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or generated artifact was accessed;
- no stop, RR, target, ADX, ATR, lookback, pair, timeframe, TP-ranking,
  fallback, diagnostic, or management rule is proposed;
- no implementation proposal is authorized by this checklist;
- no YouTube channel-wide corpus findings are mixed into Strategy B executable
  behavior.

## 11. Guardrail confirmation

Confirmed:

- docs-only authorization review checklist;
- committed repository Markdown reports only;
- exactly one Markdown file added;
- no diagnostic was run;
- no local OHLC data or generated Strategy B artifact was accessed;
- no chart packet, worksheet, mapping, reveal table, sample row, CSV, JSON,
  image, `data/`, or `results/` was created or committed;
- no raw market data or normalized market CSV is committed;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT caption file, caption
  URL, downloaded video, downloaded audio, raw DownSub output, or ASR output is
  committed;
- no credentials, tokens, or secrets are committed;
- no market-data API, broker API, order-placement, auto-trading, live-trading,
  or live-readiness behavior is added;
- no parameter optimization is performed;
- no profitability, money-making, live-readiness, or trading recommendation
  claim is made;
- Strategy A/B verification work remains separate from YouTube channel-wide
  corpus work.

## 12. Recommended next bounded task

Recommended next task:

`[codex] Strategy B low-R structural TP diagnostic authorization packet readiness note`

Suggested scope:

- docs-only;
- use committed Strategy B authorization, evidence-gap, taxonomy, matrix,
  checklist, and runbook docs only;
- define what a future local-only packet readiness note would need to confirm
  before any low-R-but-structural TP diagnostic run;
- do not run diagnostics;
- do not access local data or generated artifacts;
- do not change Strategy B behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior.
