# YouTube Corpus Post-Batch-03 Rows 36-45 Summary Recovery Decision

Task: `youtube_corpus_post_batch_03_rows_36_45_summary_recovery_decision`

## 1. Objective

This note decides whether the YouTube corpus line may open a later compact
paraphrased summary-recovery issue for post-Batch-03 rows `36`, `37`, `38`,
`41`, `42`, `43`, and `45`.

It is a docs-only decision gate. It does not perform source access, transcript
or caption-body access, summary recovery, doctrine updates, or Strategy changes.

## 2. Source Documents Reviewed

Committed public repository docs reviewed:

- `docs/video_research/youtube_corpus_post_batch_03_rows_36_45_threshold_discovery.md`
- `docs/video_research/youtube_corpus_post_batch_03_next_target_slice.md`
- `docs/video_research/youtube_corpus_bundled_transcript_runtime_preflight_readiness.md`
- `docs/video_research/youtube_corpus_access_cadence_failure_log_protocol.md`
- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`

PR discussion reviewed:

- PR #168 PM review note accepting the status-only threshold-discovery PR on
  the disclosed one-off row-36 retry basis, with the future boundary that
  lost-status or retry authorization must be recorded in the controlling issue
  or PR discussion before any retry source touch.

Live GitHub state was used only for duplicate-prevention and task scope checks.
No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, request
URL, raw response body, comment, live chat, community post, downloaded media,
ASR, external source, private source, market data, broker API, or live system
was accessed.

## 3. PR #168 Threshold-discovery Result

The merged threshold-discovery report records this status for the target rows:

| field | PR #168 result |
| --- | --- |
| controlling issue | `#167` |
| approved runtime route | `bundled_python_youtube_transcript_api_1_2_4` |
| target rows | `36`, `37`, `38`, `41`, `42`, `43`, and `45` |
| completed-skip rows | `39`, `40`, and `44` |
| current reportable source-touch count | `7` |
| known Issue #167 source-touch events | `8`, consisting of one prior row-36 lost-status event plus seven current reportable touches |
| successful access-state count in current reportable run | `7` |
| unavailable or empty count | `0` |
| 429 or IP-limit count | `0` |
| stop reason | `source_order_slice_complete` |
| summary recovery performed | `no` |
| raw transcript, subtitle text, caption URL, request URL, raw response, CSV, JSON, `data/`, or `results` committed | `no` |

Each reportable target row received the access-state label:

`success_git_safe_summary_possible`

That label means a later issue may decide to recover compact paraphrased
summaries. It is not itself a summary, doctrine conclusion, Strategy finding,
trading rule, or performance result.

## 4. Row 36 Retry and PM Boundary

PR #168 discloses that row `36` had one earlier source-touch event whose
Git-safe status output was lost after the source touch. The merged report does
not use that lost-status event as access-state evidence.

The current reportable run in PR #168 is the basis for this decision. In that
run, row `36` and the other six target rows returned
`success_git_safe_summary_possible` under the approved route.

The PM review note accepted PR #168 on that disclosed one-off basis. It also
sets a future operating boundary: if any later source-touch run loses status or
needs a retry, the retry authorization must be recorded in the controlling
GitHub issue or PR discussion before the retry source touch. This decision note
does not weaken that requirement.

## 5. Eligibility Decision

Decision:

`summary_recovery_issue_authorized_after_successful_threshold_discovery_with_retry_boundary`

Rows `36`, `37`, `38`, `41`, `42`, `43`, and `45` are eligible for a later
compact paraphrased summary-recovery issue because:

1. the target rows are committed and bounded by the post-row-35 target-slice
   and metadata-resolution record;
2. PR #168 records a successful access-state label for all seven reportable
   target rows;
3. PR #168 observed no 429, IP-limit, empty-body, unavailable-body,
   ambiguous-source-state, raw-artifact, or bypass-like stop condition;
4. PR #168 did not perform summary recovery and did not commit raw artifacts;
5. the approved bundled Python transcript runtime route is documented and must
   be rechecked before any future source access;
6. the future output can be restricted to compact paraphrased Markdown summaries
   and Git-safe status fields;
7. the row-36 lost-status event is disclosed and quarantined from the
   access-state evidence, with a stricter future retry-record requirement.

Human approval is not still required to open the next summary-recovery issue.
The next issue itself remains the controlling authorization for any future
source access and summary recovery. If that issue is not open, active, and
explicit, no summary recovery may run.

## 6. Allowed Summary-recovery Boundaries

A future summary-recovery issue may authorize only this scope:

- rows `36`, `37`, `38`, `41`, `42`, `43`, and `45` only;
- carry rows `39`, `40`, and `44` forward as completed-skip rows, with no
  source touch or re-summarization for those rows;
- source order from row `36`, skipping completed rows only as explicitly
  carried forward;
- at most seven source touches;
- approved bundled Python transcript runtime route only;
- no-network runtime preflight before the first source touch;
- one compact paraphrased summary per successfully recovered target row;
- no raw or near-raw transcript reconstruction;
- no title-language promotion into project conclusions;
- no doctrine updates;
- no Strategy A/B/B2/C changes;
- no market-data, broker/live, backtest, parameter, optimization, or
  profitability work.

The future issue must stop before source access if the active issue recheck,
duplicate check, runtime preflight, source authorization, retry-record
requirement, or guardrail check fails.

## 7. Disallowed Artifacts and Interpretations

The future summary-recovery issue must not commit:

- raw transcript text;
- subtitle full text;
- raw TXT/SRT/VTT content;
- caption URLs;
- request URLs;
- raw response bodies;
- downloaded video or audio;
- ASR output;
- CSV or JSON dumps;
- `data/` or `results` artifacts;
- generated candidate, event, trade, metric, or result artifacts;
- credentials, tokens, cookies, sessions, IP addresses, or secrets.

The future issue must not infer:

- doctrine conclusions from metadata-only or title text;
- Strategy A/B/B2/C behavior;
- mechanical trading rules;
- backtest results;
- market-data conclusions;
- broker/live behavior;
- profitability, trading-readiness, win-rate, money-making, or trading
  recommendation claims.

## 8. Next Issue Gate

Exact next issue title to use:

`[codex] Recover compact summaries for post-Batch-03 rows 36-45 with approved transcript runtime`

That future issue should reference:

- this decision note;
- the PR #168 threshold-discovery report;
- the PR #168 PM review boundary for future lost-status or retry authorization;
- the post-row-35 target-slice and metadata-resolution record;
- the bundled transcript runtime preflight readiness note;
- the cadence and learning-loop protocol;
- the access-attempt ledger template.

The future issue should explicitly restate all source-access, artifact,
retry-record, and Strategy/corpus separation guardrails before any source touch.

## 9. Guardrail Statement

Docs-only decision note. No source access was run. No transcript or caption-body
access was run. No summary was created. No dependency was installed. No YouTube,
DownSub, caption, subtitle, transcript-body, caption URL, request URL, comment,
live chat, community post, downloaded media, ASR, external source, private
source, local OHLC data, generated Strategy artifact, market-data API, broker
API, or live system was accessed.

No raw transcript text, subtitle full text, raw TXT/SRT/VTT, caption URL,
request URL, raw response body, CSV, JSON, `data/`, `results`, downloaded
media, credential, token, cookie, session, IP address, or secret was added.

No Strategy A/B/B2/C behavior, code, parameters, configs, tests, runners,
backtests, market-data handling, broker/live behavior, doctrine conclusion, or
trading conclusion was changed. No Strategy B2 or Strategy C was created. No
parameter optimization was performed. No profitability, trading-readiness,
win-rate, money-making, or trading-recommendation claim was made. The YouTube
channel-wide corpus line remains separate from Strategy A/B verification.

## 10. Decision

Decision:

`post_batch_03_rows_36_45_summary_recovery_decision_ready`

Reason: PR #168 records successful Git-safe access-state labels for all seven
reportable target rows without stop signals or raw artifacts. The disclosed
row-36 lost-status event is quarantined from access-state evidence and creates
a stricter future retry-record boundary, but it does not block opening a later
compact paraphrased summary-recovery issue for the seven reportable successful
target rows. Summary recovery must remain separate from this decision note and
must repeat all active checks before source access.
