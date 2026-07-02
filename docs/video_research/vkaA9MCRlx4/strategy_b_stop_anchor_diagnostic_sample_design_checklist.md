# Strategy B Stop-Anchor Diagnostic Sample Design Checklist

## 1. Objective and scope

This report defines a docs-only checklist for a future local-only Strategy B
stop-anchor diagnostic sample design. It builds on the committed stop-anchor
diagnostic protocol guardrails and keeps the current Strategy B closure note
controlling.

Scope:

- define future sample-design requirements for the Pass A / Pass B
  stop-anchor protocol;
- define required packet fields, hidden fields, case IDs, repeat checks,
  second-review triggers, and hard stops;
- define what must remain local-only and out of Git;
- define what a future diagnostic-run issue would need to authorize explicitly;
- confirm that no diagnostic is run and no Strategy B rule, code, parameter,
  test, runner, config, or backtest change is authorized.

Out of scope:

- no Strategy A/B/B2/C rule, code, parameter, config, test, runner, or backtest
  change;
- no Strategy B2 or Strategy C creation;
- no parameter optimization;
- no diagnostics run, backtest run, sample-row generation, chart-packet
  generation, mapping generation, or review-sheet generation;
- no chart packet, image, screenshot, hidden mapping, review worksheet, sample
  row, label output, CSV, JSON, `data/`, `results/`, credentials, tokens, or
  secrets committed;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, ASR, or external
  source access;
- no profitability claim or trading recommendation.

## 2. Source files and docs used

Committed docs inspected:

- `docs/video_research/vkaA9MCRlx4/strategy_b_stop_anchor_diagnostic_protocol_guardrails.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_backlog_issue_47_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`

Committed code inspected read-only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`

No uncommitted local files, raw data artifacts, generated outputs, market data,
broker/live systems, video sources, captions, transcripts, or external sources
were used.

## 3. Protocol guardrail recap

The committed protocol guardrail report defines a future diagnostic path for
`B-TP1-FU-06 - Stop-anchor diagnostic path`. Its central rule is that
structural stop-anchor labels must be locked before reviewers see stop
distance, TP prices, TP ranks, RR fields, acceptance status, rejection reasons,
or outcome-like information.

The fixed Pass A label set is:

- `structurally_valid_stop_anchor`;
- `questionable_stop_anchor`;
- `visually_uninterpretable_stop_anchor`;
- `insufficient_context_no_decision`.

Pass A may inspect only confirmation-time structure needed to judge the stop
anchor. Pass B may reveal distance, RR, TP-rank context, and rejection reasons
only after the Pass A label is locked. Pass B is for aggregate interpretation,
not label revision or rule approval.

The current Strategy B closure note remains controlling. Current rank-1 TP1
selection, RR gates, stop-anchor logic, stop-buffer logic, stop sanity logic,
ADX, management structure, and Strategy B2 status remain frozen.

## 4. Future local-only sample design checklist

A future sample design should be approved before any local diagnostic run
starts. The design should answer each item below.

Sample frame:

- [ ] State the exact future issue number authorizing the diagnostic run.
- [ ] State the diagnostic question as stop-anchor structure, not strategy
  performance.
- [ ] State that the sample is local-only and no row-level artifact will be
  committed.
- [ ] State which committed docs define the fixed labels and Pass A / Pass B
  separation.
- [ ] State the candidate universe using existing local artifacts only, if a
  future issue explicitly authorizes those local artifacts.
- [ ] State inclusion buckets before reviewing any chart packet.
- [ ] State exclusion rules before reviewing any chart packet.
- [ ] State the planned sample size or shortfall rule.
- [ ] State how repeats will be inserted without revealing that they are
  repeats.
- [ ] State how second-review cases will be selected before Pass B reveal.

Bucket requirements:

- [ ] Include cases where current stop logic has an eligible stop anchor.
- [ ] Include cases where current stop logic falls back to the reference candle.
- [ ] Include cases later known locally as stop-width concerns only after Pass A
  labels are locked.
- [ ] Keep no-left-side/no-valid-target and no-trade-structure cases separate
  from low-RR cases.
- [ ] Do not choose rows because they are known winners, losers, accepted
  candidates, or convenient examples for a desired rule.

Shortfall requirements:

- [ ] If a bucket has too few cases, record the shortfall rather than borrowing
  from an outcome-selected bucket.
- [ ] If chart context is unreadable or incomplete, allow
  `insufficient_context_no_decision`.
- [ ] If the sample cannot preserve Pass A blindness, stop the run.

## 5. Pass A packet field checklist

Each future Pass A packet should show only the fields needed to judge
confirmation-time stop structure.

Allowed Pass A packet fields:

- [ ] anonymized case ID;
- [ ] direction;
- [ ] setup marker or setup window;
- [ ] touch marker or touch window;
- [ ] confirmation marker or confirmation candle;
- [ ] entry-side orientation when needed to interpret stop side;
- [ ] current stop-anchor marker;
- [ ] stop side;
- [ ] reference-candle high or low marker when needed to judge fallback logic;
- [ ] enough pre-confirmation left-side bars to judge swing context;
- [ ] a packet-completeness flag;
- [ ] reviewer label field using only the fixed Pass A label set;
- [ ] short ambiguity note field.

Pass A packet construction checks:

- [ ] Do not show future bars beyond the approved confirmation-context display
  rule.
- [ ] Do not show TP1 or TP2 markers.
- [ ] Do not show TP ranks or target-candidate diagnostics.
- [ ] Do not show stop distance, ATR multiple, risk, RR, accepted status,
  first-fail reason, all-failed reasons, exit reason, final R, or trade
  outcome.
- [ ] Do not show pair/time identifiers unless the future issue explicitly
  accepts pair/time leakage risk and explains why anonymization is not feasible.
- [ ] Do not include raw CSV rows or generated row dumps in any Git-tracked
  artifact.

## 6. Hidden-field / leakage-control checklist

The following fields must remain hidden until Pass A labels are locked:

- [ ] pair;
- [ ] setup time;
- [ ] touch time;
- [ ] confirmation time;
- [ ] entry time;
- [ ] entry price;
- [ ] ATR;
- [ ] ADX and ADX pass/fail;
- [ ] stop price;
- [ ] buffer;
- [ ] risk;
- [ ] stop distance in ATR or price terms;
- [ ] stop-too-narrow and stop-too-wide pass/fail;
- [ ] TP1 and TP2 prices;
- [ ] TP1 R and TP2 R;
- [ ] left-side TP1 availability;
- [ ] TP1, TP1-only, and TP2 RR pass/fail;
- [ ] accepted status;
- [ ] first-fail reason;
- [ ] all-failed reasons;
- [ ] target rank diagnostics;
- [ ] trade exit, TP hit, stop hit, final R, win/loss, or any outcome-like
  field.

Leakage controls:

- [ ] Store hidden mappings outside Git.
- [ ] Use stable anonymized case IDs in packets.
- [ ] Keep the case-ID-to-row mapping local-only.
- [ ] Keep reviewer packets separate from hidden Pass B reveal tables.
- [ ] Lock Pass A labels before opening any hidden-field table.
- [ ] Preserve original Pass A labels even if later adjudication records a
  revision note.
- [ ] Stop if reviewers can infer outcomes, RR failures, or accepted status
  from packet naming, ordering, file paths, image names, or bucket labels.

## 7. Pass B reveal checklist

Pass B may start only after all Pass A labels and ambiguity notes are locked.

Before Pass B:

- [ ] Confirm every Pass A case has exactly one fixed label or an explicit
  no-decision label.
- [ ] Confirm repeat cases have been identified locally but not used to alter
  original labels.
- [ ] Confirm second-review candidates are selected by predeclared triggers.
- [ ] Confirm the Pass A label file remains local-only if it contains row-level
  mappings, pair/time details, prices, images, or generated rows.

Allowed Pass B reveal fields:

- [ ] stop distance;
- [ ] stop distance ATR multiple;
- [ ] TP1 RR;
- [ ] TP2 RR if relevant to aggregate interpretation;
- [ ] current stop sanity pass/fail;
- [ ] current TP1/TP2 RR pass/fail;
- [ ] first-fail and all-failed reasons;
- [ ] target-rank context.

Pass B aggregate questions:

- [ ] Count label distribution by fixed Pass A label.
- [ ] Count overlap between `questionable_stop_anchor` and stop-width concerns.
- [ ] Count overlap between `structurally_valid_stop_anchor` and TP1 RR
  failures.
- [ ] Count cases where chart context prevented a decision.
- [ ] Identify whether repeated, low-ambiguity structural patterns exist.
- [ ] Record ambiguity and shortfalls without converting them into rule
  changes.

Forbidden Pass B actions:

- [ ] Do not change Pass A labels merely because Pass B fields are inconvenient.
- [ ] Do not treat width alone as stop invalidity.
- [ ] Do not accept a shallower stop merely because it improves RR.
- [ ] Do not propose a stop-rule change.
- [ ] Do not propose parameter changes.
- [ ] Do not authorize Strategy B2, Strategy C, or live-trading behavior.

## 8. Repeat-check and second-review trigger checklist

Repeat checks should measure label stability, not reviewer performance or trade
outcomes.

Repeat checks:

- [ ] Predeclare the repeat percentage or repeat count.
- [ ] Insert repeat packets under different anonymized case IDs.
- [ ] Keep repeat identity hidden until Pass A is locked.
- [ ] Compare original and repeat labels after Pass A lock.
- [ ] Record disagreement as an ambiguity signal.
- [ ] Do not resolve repeat disagreement by looking at RR, acceptance, or
  outcome fields.

Second-review triggers:

- [ ] `questionable_stop_anchor` with a high-impact ambiguity note.
- [ ] `visually_uninterpretable_stop_anchor` where missing context may be a
  packet construction issue.
- [ ] repeat-case disagreement.
- [ ] reviewer note says the stop anchor depends on a competing nearby swing.
- [ ] reviewer note says reference-candle fallback may be driving the label.
- [ ] reviewer note uses language that implies RR, outcome, or later-candle
  leakage.
- [ ] packet-completeness flag is false.

Second-review boundaries:

- [ ] The second reviewer must see only Pass A material.
- [ ] Adjudication must preserve original labels and add a separate
  adjudication note.
- [ ] No second review may use Pass B fields to decide stop-anchor validity.
- [ ] If ambiguity remains high, the only Git-safe conclusion is a blocker or
  no-decision aggregate.

## 9. Hard-stop conditions

A future diagnostic run should stop immediately if any condition below occurs.

- [ ] The future issue does not explicitly authorize a diagnostic run.
- [ ] The sample design is not fixed before packet review starts.
- [ ] Label definitions change during review.
- [ ] Sample selection uses outcome, profitability, accepted status, or a
  desired rule conclusion.
- [ ] Pass A packets reveal stop distance, RR, TP rank, rejection reason,
  accepted status, or outcome-like fields.
- [ ] Reviewers can infer pair/time identity where the protocol required
  anonymization.
- [ ] Raw market data, normalized CSVs, candidate rows, generated CSV/JSON,
  chart images, worksheets, mappings, or row-level packets are staged for Git.
- [ ] A reviewer proposes a stop-anchor rule change during the diagnostic run.
- [ ] The diagnostic starts optimizing thresholds, stop buffers, ATR multiples,
  RR gates, swing widths, lookbacks, ADX, or pair-specific settings.
- [ ] The work starts mixing YouTube channel-wide corpus findings into Strategy
  B behavior without a separate design decision.
- [ ] Any output makes profitability, live-readiness, or money-making claims.

## 10. Local-only artifact policy

The following artifacts must remain local-only and out of Git:

- chart packets;
- chart images and screenshots;
- hidden case mappings;
- case-ID-to-row mappings;
- raw CSVs;
- normalized OHLC CSVs;
- candidate rows;
- event rows;
- trade rows;
- TP-candidate rows;
- generated CSV or JSON diagnostics;
- review worksheets;
- filled label sheets;
- Pass A row-level label tables;
- Pass B reveal tables with row-level fields;
- raw market data;
- downloaded media;
- credentials, tokens, and secrets.

Git-safe outputs may include only compact aggregate Markdown reports,
diagnostic taxonomies, protocol notes, blocker notes, and design-decision memos
that exclude row-level market data, pair/time/price details, chart images,
hidden mappings, filled worksheet rows, transcript or subtitle content, and
outcome/profitability claims.

## 11. Future diagnostic-run authorization requirements

A future diagnostic-run issue would need to authorize all of the following
explicitly before any run starts:

- the exact diagnostic question;
- the local-only artifact classes allowed for the run;
- the local-only source artifacts allowed for sample construction;
- the fixed sample buckets and shortfall rules;
- the fixed Pass A packet contents;
- the fixed hidden-field list;
- the repeat-check design;
- the second-review triggers;
- the Pass B reveal fields;
- the Git-safe aggregate output format;
- the hard-stop rules;
- confirmation that no Strategy B code, parameter, config, test, runner,
  backtest, or behavior change is authorized by the run itself.

Without that authorization, future work should remain docs-only planning.

## 12. Why no Strategy B rule/code/parameter change is authorized

No Strategy B rule, code, parameter, config, test, runner, or backtest change is
authorized because:

- this report is a checklist only;
- no diagnostic run was executed;
- no sample rows, chart packets, mappings, labels, review sheets, CSV, JSON, or
  generated artifacts were created;
- no Pass A labels were collected;
- no Pass B aggregate was produced;
- no replacement stop-anchor rule is specified;
- no evidence has been produced under the future local-only protocol;
- the committed closure note still freezes TP1, stop-anchor, RR, filter,
  management, and Strategy B2 decisions;
- changing stops to improve RR would risk fitting the denominator rather than
  preserving premise/invalidation structure.

Current Strategy B behavior remains unchanged.

## 13. Guardrail confirmation

Confirmed:

- docs-only sample design checklist;
- committed repository docs and code only;
- one Markdown report added;
- no Strategy A/B/B2/C behavior change;
- no Strategy B rules, parameters, configs, tests, runner behavior, or backtest
  behavior changed;
- no Strategy B2 or Strategy C created;
- no parameter optimization;
- no diagnostics or backtests run;
- no chart packets, review sheets, mappings, sample rows, labels, CSV, JSON,
  `data/`, `results/`, or generated artifacts committed;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, ASR, or external
  sources accessed;
- no raw market data, normalized CSV, generated candidate/result/trade/event
  CSV, raw transcript, subtitle text, raw TXT/SRT/VTT, caption URL, downloaded
  media, credentials, tokens, or secrets committed;
- no profitability claim or trading recommendation.

## 14. Recommended next bounded docs-only task

Recommended next task:

`[codex] Strategy B stop-anchor diagnostic run authorization review`

Scope:

- docs-only;
- decide whether a future local-only diagnostic run is warranted;
- if warranted, specify the exact local-only source artifacts, sample buckets,
  packet fields, hidden fields, repeat checks, second-review triggers, Pass B
  reveal fields, hard stops, and Git-safe aggregate output;
- do not run the diagnostic;
- do not create local artifacts in Git;
- do not change Strategy B behavior;
- keep the current Strategy B closure note controlling.
