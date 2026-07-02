# Strategy B Stop-Anchor Diagnostic Protocol Guardrails

## 1. Objective and scope

This report defines docs-only guardrails for a future Strategy B stop-anchor
diagnostic protocol based on the preserved backlog item
`B-TP1-FU-06 - Stop-anchor diagnostic path`.

Scope:

- define fixed stop-anchor labels for a future diagnostic protocol;
- define Pass A / Pass B separation before any stop distance, RR, TP result, or
  outcome-like field is considered;
- define reviewer blindness and leakage controls;
- define what future local-only artifacts may be needed outside Git;
- define what evidence would only justify reopening a future design review;
- confirm that no Strategy B rule, code, parameter, test, runner, or backtest
  change is authorized.

Out of scope:

- no Strategy A/B/B2/C rule, code, parameter, config, test, runner, or backtest
  change;
- no Strategy B2 or Strategy C creation;
- no new strategy variant design;
- no parameter optimization;
- no new diagnostics run;
- no new backtest;
- no chart packet, manual-review sheet, mapping, sample row, label set output,
  candidate row, or local artifact committed to Git;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, ASR, or external
  source access;
- no raw market data, normalized CSV, generated candidate/result/trade/event
  CSV, raw transcript, subtitle text, raw TXT/SRT/VTT, caption URL, downloaded
  media, `data/`, or `results/` content;
- no profitability claim or trading recommendation.

## 2. Source files and docs used

Committed docs inspected:

- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_backlog_issue_47_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_selection_issue_45_review.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_stop_anchor_followup_diagnostic_backlog.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_closure_note.md`
- `docs/video_research/vkaA9MCRlx4/strategy_b_tp1_decision_memo.md`

Committed code inspected read-only:

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`

No uncommitted local files, raw data artifacts, generated outputs, market data,
broker/live systems, video sources, captions, transcripts, or external sources
were used.

## 3. Why B-TP1-FU-06 was preserved

Issue #47 preserved `B-TP1-FU-06 - Stop-anchor diagnostic path` because the
committed evidence separates stop quality from TP1 RR convenience. The Issue
#45 review found that stop-to-TP geometry materially interacts with the current
TP1 minimum RR gate, but the same review also found that the evidence is
insufficient for changing stop anchors, stop buffers, stop limits, RR gates, or
TP1 ranking.

The committed decision memo and closure note keep Strategy B unchanged. They
freeze current rank-1 TP1 selection, TP1 minimum RR, TP2 minimum RR, TP1-only
minimum RR, stop-anchor logic, stop-buffer logic, stop sanity limits, ADX,
management structure, and Strategy B2 status until stronger evidence justifies
a separate design review.

The backlog frames stop-anchor quality as its own diagnostic path. It asks
whether structurally valid stops, questionable stops, and visually
uninterpretable stops can be separated before changing stop logic. That framing
is intentionally narrower than a rule proposal: it preserves a future research
question while blocking any immediate Strategy B behavior change.

## 4. Proposed fixed stop-anchor labels

A future diagnostic protocol should use a fixed label set before any review
begins. The minimum label set should be:

| Label | Meaning | Required reviewer basis | Forbidden reviewer basis |
| --- | --- | --- | --- |
| `structurally_valid_stop_anchor` | The current stop anchor is a defensible premise/invalidation point for the setup visible at confirmation time. | Visible pre-confirmation structure, reference candle, eligible left-side swing context, and whether the stop point plausibly invalidates the setup premise. | Later TP/SL outcome, trade result, final R, target distance, or whether the stop improves RR. |
| `questionable_stop_anchor` | The stop anchor may be defensible but has material ambiguity, such as weak structure, crowded local swings, unclear reference-candle fallback, or competing nearby invalidation points. | Visible ambiguity in pre-confirmation structure that can be stated without outcome data. | Reclassifying merely because the stop is wide, narrow, losing, or inconvenient for TP1 RR. |
| `visually_uninterpretable_stop_anchor` | The chart window or available context is not sufficient for a reviewer to judge stop-anchor structure. | Missing or unclear chart context, unreadable structure, insufficient left-side context, or inability to identify a premise/invalidation point. | Guessing from exported numeric fields, later candles, candidate success, or outcome-like diagnostics. |
| `insufficient_context_no_decision` | The case should not receive a structural label because the protocol inputs are incomplete or the setup itself cannot be evaluated cleanly. | Explicit protocol failure, missing required display fields, missing chart window, or setup context that prevents a clean stop-anchor read. | Filling gaps from raw CSV rows, hidden mappings, later outcome fields, or reviewer memory. |

The protocol may later add sublabels only after a docs-only design review. It
should not add labels during execution, because mid-review label creation makes
aggregate counts harder to audit and invites post-hoc sorting.

## 5. Pass A / Pass B separation

Future stop-anchor diagnostics should separate structural labeling from
distance, RR, and outcome-like interpretation.

### Pass A: structural stop-anchor label lock

Pass A should show only information needed to judge stop-anchor structure at
confirmation time:

- direction;
- setup, touch, and confirmation context;
- entry marker if needed to orient the stop side;
- current stop-anchor marker and stop side;
- enough pre-confirmation bars to evaluate left-side structure;
- no future bars beyond the confirmation context unless a future docs-only
  protocol defines a stricter display rule that still excludes outcome data.

Pass A must hide:

- stop distance in price, ATR, or R units;
- TP1 and TP2 prices;
- TP rank information;
- TP1 R, TP2 R, RR pass/fail fields, and stop sanity pass/fail fields;
- accepted/rejected status;
- first-fail and all-failed reasons;
- exit, TP hit, stop hit, final R, win/loss, or profitability-like fields;
- pair/time identifiers if the future protocol decides that pair/time leakage
  could bias reviewers.

The Pass A output is a locked structural label plus a short ambiguity note. It
must be completed before any Pass B fields are revealed.

### Pass B: diagnostic interpretation after label lock

Pass B may reveal stop distance, ATR multiple, TP1 RR, TP candidate rank
context, and rejection reasons only after the Pass A label is locked. Pass B is
for aggregate interpretation, not label revision.

Allowed Pass B questions:

- how many `structurally_valid_stop_anchor` cases are wide by the existing stop
  sanity fields;
- how often questionable or uninterpretable stop labels overlap with TP1 RR
  failures;
- whether stop distance and TP1 RR failures cluster in a way that justifies a
  future design-review reopen;
- which cases require no decision because the protocol inputs were
  insufficient.

Forbidden Pass B actions:

- changing Pass A labels after seeing RR or outcomes;
- treating width alone as proof of stop invalidity;
- treating a shallow alternative stop as valid merely because it improves RR;
- proposing a stop-rule change;
- proposing parameter changes;
- approving Strategy B2 or Strategy C work.

## 6. Leakage risks and reviewer blindness requirements

Primary leakage risks:

- outcome leakage from later bars, TP/SL hits, final R, win/loss, or accepted
  status;
- RR leakage from TP1 R, stop distance, ATR multiple, or rejection reason fields;
- target leakage from TP1/TP2 prices or rank information when the reviewer is
  meant to judge only stop structure;
- pair/time leakage if reviewers remember specific cases or market episodes;
- selection leakage if sample rows are chosen because they are known to support
  a preferred rule change;
- source-line leakage if corpus doctrine is used to override the Strategy B
  verification line without a separate design decision.

Reviewer blindness requirements:

- Pass A labels must be completed without TP/RR/outcome fields.
- Review packets should use stable anonymized case IDs rather than pair/time
  identifiers when feasible.
- Any repeat or second-review subset should be defined before outcome-like
  fields are revealed.
- Reviewers should record ambiguity rather than force a structural label when
  the chart context is insufficient.
- Reviewers must not infer validity from whether a stop is wide, narrow, passed
  a sanity gate, failed TP1 RR, or would have improved a result.
- Any later adjudication should preserve the original Pass A label and document
  the reason for a revision separately if a future protocol allows revisions.

## 7. Local-only artifact policy

A future diagnostic run may require local-only artifacts outside Git, such as:

- chart packets;
- hidden case mappings;
- blinded reviewer packets;
- sample selection tables;
- unfilled and filled worksheets;
- candidate, event, TP-candidate, or trade rows;
- generated CSV/JSON diagnostics;
- local chart images or screenshots;
- raw or normalized market data.

Those artifacts must remain outside Git. This PR does not create or commit any
of them.

Git-safe outputs from a future run may include only aggregate Markdown reports,
diagnostic taxonomies, decision memos, and blocker notes that exclude raw rows,
pair/time/price details, chart images, hidden mappings, filled worksheet rows,
caption/transcript content, downloaded media, and outcome/profitability claims.

## 8. Evidence sufficient only to reopen a design review

Future stop-anchor diagnostic evidence may justify reopening a docs-only design
review only if it shows repeated, low-ambiguity patterns after Pass A labels are
locked.

Minimum reopen evidence should include:

- a predeclared sample design;
- fixed labels used before review execution;
- Pass A labels locked before Pass B reveal;
- enough independent cases to show repeated patterns rather than isolated
  anecdotes;
- low ambiguity after second review or adjudication;
- clear separation between structural validity, stop width, TP1 RR, and
  outcome-like fields;
- no parameter sweep, performance-tuned threshold, pair-specific tuning, or
  future-bar logic;
- a proposed mechanical question that uses only information available at
  confirmation time;
- continued separation of Strategy A/B verification from the YouTube
  channel-wide corpus line unless a separate design decision authorizes
  integration.

Even if those conditions are met, the evidence would only justify a later
docs-only design review. It would not automatically authorize a Strategy B rule
change, parameter change, implementation PR, Strategy B2, Strategy C, or
live-trading behavior.

## 9. Why no Strategy B change is authorized

No Strategy B rule, code, parameter, runner, test, or backtest change is
authorized because:

- this report defines protocol guardrails only;
- no diagnostic run was executed;
- no chart packet, sample, worksheet, mapping, label output, CSV, JSON, or
  generated artifact was created;
- no replacement stop-anchor rule is specified;
- no evidence has been produced under the proposed Pass A / Pass B protocol;
- the existing closure note remains controlling;
- the current implementation remains aligned with the committed Strategy B
  documentation;
- changing stop anchors to improve RR would risk fitting the denominator rather
  than preserving premise/invalidation structure.

Current Strategy B behavior therefore remains unchanged.

## 10. Guardrail confirmation

Confirmed:

- docs-only protocol guardrail report;
- committed repository docs and code only;
- one Markdown report added;
- no Strategy A/B/B2/C behavior change;
- no Strategy B rules, parameters, configs, tests, runner behavior, or backtest
  behavior changed;
- no Strategy B2 or Strategy C created;
- no parameter optimization;
- no new diagnostics or backtests run;
- no chart packets, manual-review sheets, mappings, sample rows, labels, or
  generated artifacts committed;
- no market-data API, broker API, live trading, auto-trading, or order
  execution behavior;
- no YouTube, DownSub, captions, subtitles, transcript bodies, caption URLs,
  comments, live chat, community posts, downloaded media, ASR, or external
  sources accessed;
- no raw market data, normalized CSV, generated candidate/result/trade/event
  CSV, raw transcript, subtitle text, raw TXT/SRT/VTT, caption URL, downloaded
  media, `data/`, `results/`, credentials, tokens, or secrets committed;
- no profitability claim or trading recommendation.

## 11. Recommended next bounded docs-only task

Recommended next task:

`[codex] Strategy B stop-anchor diagnostic sample design checklist`

Scope:

- docs-only;
- define the future local-only sample design needed for the Pass A / Pass B
  protocol;
- define required packet fields, hidden fields, case IDs, repeat checks,
  second-review triggers, and hard stops;
- keep all rows, charts, mappings, worksheets, CSV/JSON outputs, and market
  data local-only and out of Git;
- do not run diagnostics;
- do not change Strategy B behavior;
- keep the Issue #45 closure note controlling.
