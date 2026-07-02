# Strategy B Low-R Structural TP Authorization Issue Skeleton

## 1. Objective and scope

This document provides a reusable GitHub Issue skeleton for a future
low-R-but-structural TP diagnostic authorization.

The skeleton can later authorize planning for a bounded local-only diagnostic,
but it does not authorize any diagnostic run by itself. It is intended to make a
future issue precise enough that automation can tell whether the requested work
is routine, blocked, or requires executive decision before any local access.

Scope:

- use committed repository Markdown reports only;
- define the future issue title and body shape;
- require explicit diagnostic question, source classes, fixed local-only root,
  sample buckets, Pass A / Pass B handling, Git-safe aggregate output, and
  hard-stop conditions;
- keep low-R-but-structural TP review separate from no-valid-target,
  no-trade-structure, stop width, stop validity, fallback availability,
  accepted status, and outcomes;
- preserve the current Strategy B behavior freeze;
- recommend one bounded next docs-only task.

Out of scope:

- no diagnostic run;
- no local OHLC data or generated Strategy B artifact access;
- no chart packet, worksheet, mapping, reveal table, sample row, CSV, JSON,
  image, `data/`, or `results/` creation;
- no market-data API, broker API, live system, order placement, auto-trading, or
  live-trading access;
- no Strategy A/B/B2/C behavior, code, parameter, config, test, runner, or
  backtest behavior change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no profitability, live-readiness, money-making, or trading-recommendation
  claim.

## 2. Source docs used

Committed repository docs used:

- `docs/video_research/vkaA9MCRlx4/strategy_b_diagnostic_authorization_template.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_design_review_evidence_gap_ledger.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_width_vs_stop_validity_evidence_matrix.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_contextual_rr_requirements_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_no_valid_target_no_trade_structure_taxonomy_preservation.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

No local OHLC files, generated Strategy B outputs, chart packets, worksheets,
hidden mappings, reveal tables, raw rows, market-data APIs, broker/live systems,
YouTube sources, DownSub, captions, subtitles, transcript bodies, caption URLs,
comments, live chat, community posts, downloaded media, ASR, or external sources
were used for this skeleton.

## 3. Future issue title template

Use this title shape:

`[codex] Authorize bounded Strategy B low-R structural TP diagnostic`

If the issue narrows the sample further, append the bounded class in plain
language, for example:

`[codex] Authorize bounded Strategy B low-R structural TP diagnostic for approved aggregate bucket`

The title must not imply implementation, RR threshold changes, TP target-rule
changes, Strategy B2, Strategy C, optimization, live readiness, or expected
profitability.

## 4. Future issue body skeleton

```markdown
## Objective

Authorize, but do not run unless this issue explicitly says so, a bounded
local-only Strategy B diagnostic for low-R-but-structural TP cases.

The diagnostic question is:

- `<exact question here>`

The output must be Git-safe aggregate Markdown only. The diagnostic must not
change Strategy B behavior, code, parameters, configs, tests, runner behavior,
or backtest behavior.

## Context

Use committed repository docs only before any local access, especially:

- `docs/video_research/vkaA9MCRlx4/strategy_b_diagnostic_authorization_template.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_design_review_evidence_gap_ledger.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_width_vs_stop_validity_evidence_matrix.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_contextual_rr_requirements_checklist.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_no_valid_target_no_trade_structure_taxonomy_preservation.md`
- `docs/operations/strategy_b_local_diagnostics_runbook.md`

Preserve the current Strategy B behavior freeze.

## Authorized source classes

Local-only root, redacted for Git-safe docs:

- `<USER_HOME>\FX-local-data\FX-public`

Allowed local source classes:

- `<approved OHLC input class, if authorized>`
- `<approved read-only Strategy B output class, if authorized>`
- `<approved diagnostic packet or worksheet class, if authorized>`
- `<approved aggregate local summary class, if authorized>`

Forbidden source classes:

- unrestricted local files;
- raw/generated artifacts not named above;
- external sources;
- market-data APIs;
- broker/live systems;
- YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, or ASR.

## Sample buckets

Predeclared buckets:

| Bucket | Target count | Source class | Replacement allowed? | Shortfall rule |
| --- | ---: | --- | --- | --- |
| `<bucket name>` | `<n>` | `<source class>` | `<yes/no>` | `<stop or report shortfall>` |

Do not select samples using accepted status, result, profit, loss, later
movement, or any performance-like outcome.

## Pass A hidden fields

Hide during Pass A:

- stop distance;
- RR;
- target rank;
- accepted status;
- rejection reason;
- outcome-like fields;
- row-level pair, time, price, candle, or later movement detail unless the
  issue explicitly authorizes a narrower non-biasing field set.

Pass A labels to lock before Pass B:

- low-R-but-structural TP candidate;
- not low-R-but-structural TP;
- no-valid-target / no-left-side-target;
- no-trade-structure;
- stop-width-only concern;
- stop-validity concern;
- ambiguous / needs second review;
- shortfall / unusable packet.

## Pass B revealed fields

Reveal only after Pass A labels are locked:

- `<field 1>`
- `<field 2>`
- `<field 3>`

Pass B may interpret aggregate relationships only. It must not revise Pass A
labels unless the issue predeclares a specific adjudication rule.

## Review handling

Reviewer handling:

- `<single review / independent second review / adjudication required>`

Ambiguity handling:

- ambiguous labels must be reported as aggregate ambiguity;
- ambiguous labels must not be counted as implementation support;
- second-review disagreement must remain separate from low-R-but-structural TP
  counts.

## Git-safe output

Allowed Git output:

- one compact aggregate Markdown report;
- aggregate bucket counts;
- aggregate Pass A labels;
- aggregate Pass B interpretation;
- shortfall and ambiguity summaries;
- blocker notes;
- next-task recommendation.

Forbidden Git output:

- raw rows;
- row-level pair, time, price, candle, chart, or outcome detail;
- chart packets, screenshots, worksheets, mappings, reveal tables, images,
  CSV/JSON, `data/`, or `results/`;
- raw market data or normalized market CSV;
- raw transcripts, subtitle full text, raw TXT/SRT/VTT, caption URLs, or
  downloaded media;
- credentials, tokens, or secrets.

## Hard-stop conditions

Stop before local access if:

- any required authorization field is missing;
- the local-only root is absent, ambiguous, or outside the stated boundary;
- the issue asks for Strategy behavior, code, parameter, config, test, runner,
  or backtest changes;
- the issue asks for Strategy B2, Strategy C, optimization, live readiness, or
  broker/live behavior;
- sample buckets are selected using outcomes or performance-like fields;
- Pass A hidden fields cannot be hidden because of filenames, paths, packet
  ordering, or surrounding metadata;
- Git-safe aggregate output cannot support the conclusion;
- raw/generated artifacts would need to be committed;
- low-R-but-structural TP is merged with no-valid-target, no-trade-structure,
  stop width, stop validity, fallback availability, accepted status, or
  outcomes;
- YouTube corpus findings would be mixed into executable Strategy B behavior.

## Routine versus executive-decision boundary

Routine automation is allowed only if all fields above are complete, the work is
bounded local-only diagnostic work, and the output is Git-safe aggregate
Markdown.

Executive decision is required for any Strategy A/B/B2/C behavior, code,
parameter, config, test, runner, or backtest change; Strategy B2 or Strategy C
creation; optimization; broader source universes; taxonomy merges into
implementation behavior; market-data API, broker API, live system, order
placement, auto-trading, live-trading, or live-readiness work; or profitability
or trading-recommendation claims.

## No Strategy behavior change confirmation

This issue authorizes no Strategy A/B/B2/C behavior change, no code change, no
parameter change, no config change, no test change, no runner change, and no
backtest behavior change.

## Validation required

- `git diff --check`
- `git diff --cached --check`
- `git diff --check HEAD~1..HEAD`
- `git status --short`
- changed-file sanity check limited to intended Markdown output
- required-section check
- mojibake/encoding sanity check over changed Markdown
- forbidden path/artifact/claim scan
- confirm no raw/generated artifacts are staged or committed
- repository guardrail workflow through the PR

## Human decision required?

`<No, if all fields are complete and bounded. Yes, if any executive-decision
trigger appears.>`
```

## 5. Required authorization fields

A future issue must predeclare every field below before automation may proceed.

| Field | Required content | Routine only when | Hard-stop condition |
| --- | --- | --- | --- |
| Diagnostic question | Exact low-R-but-structural TP question. | The question is bounded and diagnostic-only. | The issue asks for general exploration, rule design, or implementation. |
| Source classes | Committed docs plus named local-only artifact classes. | Every class is named before local access. | The issue requires unrestricted local files or external sources. |
| Fixed local-only root | Redacted root, expected under `<USER_HOME>\FX-local-data\FX-public` unless explicitly narrowed. | The root is fixed and Git-safe. | The root is missing, ambiguous, or outside boundary. |
| Sample buckets | Bucket names, target counts, replacement rules, and shortfall handling. | Buckets are chosen before outcome-like fields are seen. | Buckets are selected after accepted status, result, profit, loss, or later movement is known. |
| Hidden fields | Fields hidden during Pass A. | Biasing fields are hidden in filenames, paths, packets, worksheets, and ordering. | Hidden fields are inferable before labels are locked. |
| Revealed fields | Fields revealed only during Pass B. | Pass B fields support aggregate interpretation only. | Pass B is used to revise labels without a predeclared adjudication rule. |
| Pass A label set | Allowed structural and taxonomy labels. | Low-R-but-structural TP remains separate from adjacent categories. | Labels collapse no-valid-target, no-trade-structure, stop width, stop validity, or outcomes. |
| Review handling | Single review, second review, adjudication, and ambiguity handling. | Ambiguity is tracked as a result or blocker. | Ambiguity is counted as implementation support. |
| Git-safe output | Allowed aggregate Markdown tables and summaries. | No row-identifying detail enters Git. | Raw/generated artifacts or row-level details are needed in Git. |
| Hard-stop list | Stops before local access, during review, and before PR creation. | Stops are explicit and enforceable. | Stop conditions are missing or discretionary. |
| No behavior change | Explicit no-change confirmation. | Diagnostic output cannot change Strategy behavior. | The issue requests code, parameter, config, tests, runner, or backtest changes. |

## 6. Pass A / Pass B requirements

Pass A must lock labels before any RR, stop distance, target rank, accepted
status, rejection reason, or outcome-like field can bias classification.

Pass A must:

- use only the fields authorized by the future issue;
- label low-R-but-structural TP separately from no-valid-target,
  no-trade-structure, stop width, stop validity, fallback availability,
  accepted status, and outcomes;
- record ambiguous and unusable samples as diagnostic states;
- stop if hidden fields are inferable from packet names, paths, ordering, or
  surrounding metadata.

Pass B must:

- start only after Pass A labels are locked;
- reveal only fields named by the issue;
- summarize relationships in aggregate Markdown only;
- keep row-level pair, time, price, candle, chart, worksheet, mapping, reveal
  table, and generated artifact details out of Git;
- treat ambiguity, shortfall, or mixed evidence as blockers for design review,
  not as support for a rule change.

## 7. Git-safe output requirements

Allowed Git output:

- compact aggregate Markdown authorization or diagnostic reports;
- aggregate bucket counts;
- aggregate Pass A label counts;
- aggregate Pass B interpretation;
- shortfall summaries;
- ambiguity summaries;
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

## 8. Hard-stop conditions

Stop without local access or file changes when:

- the future issue does not explicitly authorize the local read or diagnostic
  run being attempted;
- any required authorization field is missing;
- the low-R-but-structural TP question is not exact and bounded;
- source classes, sample buckets, Pass A / Pass B handling, output shape, or
  stop conditions are ambiguous;
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

## 9. Routine versus executive-decision boundary

Routine bounded authorization is allowed only when:

- the issue is diagnostic-only;
- all required authorization fields are complete;
- source classes are bounded and local-only;
- sample buckets are predeclared;
- Pass A / Pass B separation is enforceable;
- output is aggregate Markdown only;
- no Strategy behavior change is requested or implied.

Executive decision is required before automation proceeds on:

- Strategy A/B/B2/C behavior, code, parameter, config, test, runner, or backtest
  changes;
- Strategy B2 or Strategy C creation;
- parameter optimization or performance-tuned threshold search;
- broader source universes not named by the issue;
- merging rejection taxonomy categories into implementation behavior;
- direct integration of YouTube channel-wide corpus findings into executable
  Strategy A/B behavior;
- market-data API, broker API, order-placement, auto-trading, live-trading, or
  live-readiness work;
- committing raw/generated artifacts, row-level details, images, worksheets,
  mappings, CSV/JSON, `data/`, or `results/`;
- making or relying on profitability, money-making, live-readiness, or trading
  recommendation claims.

## 10. No Strategy behavior change confirmation

Confirmed:

- no Strategy A/B/B2/C behavior changed;
- no Strategy B TP1, TP2, RR, contextual RR, stop-anchor, stop-buffer, stop
  sanity, ADX, ATR, swing-width, lookback, pair-setting, management, runner,
  config, test, or backtest behavior changed;
- no Strategy B2 or Strategy C was created;
- no diagnostic was run;
- no local data or generated artifact was accessed;
- no stop, RR, target, ADX, ATR, lookback, pair, timeframe, or management rule
  is proposed;
- no implementation proposal is authorized by this skeleton;
- no YouTube channel-wide corpus findings are mixed into Strategy B executable
  behavior.

## 11. Guardrail confirmation

Confirmed:

- docs-only authorization issue skeleton;
- committed repository docs only;
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

`[codex] Strategy B low-R structural TP authorization skeleton review checklist`

Suggested scope:

- docs-only;
- use committed Strategy B authorization, evidence-gap, taxonomy, matrix, and
  runbook docs only;
- create a compact review checklist for deciding whether a future
  low-R-but-structural TP diagnostic issue has all required fields;
- do not run diagnostics;
- do not access local data or generated artifacts;
- do not change Strategy B behavior, code, parameters, configs, tests, runner
  behavior, or backtest behavior.
