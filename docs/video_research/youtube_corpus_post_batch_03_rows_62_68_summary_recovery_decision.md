# YouTube Corpus Post-Batch-03 Rows 62-68 Summary Recovery Decision

Task: `youtube_corpus_post_batch_03_rows_62_68_summary_recovery_decision`

## 1. Objective

This note decides whether the YouTube corpus line may open a later compact
paraphrased summary-recovery issue for post-Batch-03 rows `62`, `63`, `64`,
`65`, `67`, and `68`.

It is the committed-docs-only deliverable for Issue #212.

It is a docs-only decision gate. It does not perform source access, transcript
or caption-body access, summary recovery, doctrine updates, or Strategy changes.

## 2. Source Documents Reviewed

Committed public repository docs reviewed:

- `docs/video_research/youtube_corpus_post_batch_03_rows_62_68_threshold_discovery.md`
- `docs/video_research/youtube_corpus_post_batch_03_next_target_slice.md`
- `docs/video_research/youtube_corpus_bundled_transcript_runtime_preflight_readiness.md`
- `docs/video_research/youtube_corpus_access_cadence_failure_log_protocol.md`
- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/youtube_corpus_post_batch_03_rows_54_61_summary_recovery_decision.md`

Live GitHub state was used only for duplicate-prevention and task-scope checks.
No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, request
URL, raw response body, comment, live chat, community post, downloaded media,
ASR, external source, private source, market data, broker API, or live system
was accessed.

## 3. PR #211 Threshold-discovery Result

The merged threshold-discovery report records this status for the target rows:

| field | PR #211 result |
| --- | --- |
| controlling issue | `#210` |
| approved runtime route | `bundled_python_youtube_transcript_api_1_2_4` |
| target rows | `62`, `63`, `64`, `65`, `67`, and `68` |
| completed-skip row | `66` |
| current reportable source-touch count | `6` |
| successful access-state count in current reportable run | `6` |
| unavailable or empty count | `0` |
| 429 or IP-limit count | `0` |
| retry count in current reportable run | `0` |
| stop reason | `source_order_slice_complete` |
| summary recovery performed | `no` |
| raw transcript, subtitle text, caption URL, request URL, raw response, CSV, JSON, `data/`, or `results` committed | `no` |

Each reportable target row received the access-state label:

`success_git_safe_summary_possible`

That label means a later issue may decide to recover compact paraphrased
summaries. It is not itself a summary, doctrine conclusion, Strategy finding,
trading rule, or performance result.

## 4. Eligibility Decision

Decision:

`summary_recovery_issue_authorized_after_clean_threshold_discovery_without_retry`

Rows `62`, `63`, `64`, `65`, `67`, and `68` are eligible for a later compact
paraphrased summary-recovery issue because:

1. the target rows are committed and bounded by the post-row-61 target-slice
   and metadata-resolution record;
2. PR #211 records a successful access-state label for all six reportable
   target rows;
3. PR #211 observed no 429, IP-limit, empty-body, unavailable-body,
   ambiguous-source-state, raw-artifact, retry, or bypass-like stop condition;
4. PR #211 did not perform summary recovery and did not commit raw artifacts;
5. the approved bundled Python transcript runtime route is documented and must
   be rechecked before any future source access;
6. the future output can be restricted to compact paraphrased Markdown summaries
   and Git-safe status fields;
7. row `66` is already completed/audited prior corpus work and is excluded from
   recovery scope;
8. this decision does not rely on prior retry disclosures or the clean no-retry
   Issue #200 recovery run as precedent for later source-access retries.

Eligible target rows:

| source-order row | public video ID | next recovery eligibility |
| ---: | --- | --- |
| 62 | `kljZef5IXLc` | `eligible_for_later_compact_summary_recovery_issue` |
| 63 | `PBxdWeI43Ic` | `eligible_for_later_compact_summary_recovery_issue` |
| 64 | `XnznwDuVQ08` | `eligible_for_later_compact_summary_recovery_issue` |
| 65 | `rvJ2QpQUY-E` | `eligible_for_later_compact_summary_recovery_issue` |
| 67 | `ABjvvCfYYXY` | `eligible_for_later_compact_summary_recovery_issue` |
| 68 | `d5Xfn_wNw0g` | `eligible_for_later_compact_summary_recovery_issue` |

Human approval is not still required to open the next summary-recovery issue.
The next issue itself remains the controlling authorization for any future
source access and summary recovery. If that issue is not open, active, and
explicit, no summary recovery may run.

## 5. Completed-skip Handling

| row | public video ID | status | decision use |
| ---: | --- | --- | --- |
| `66` | `GIHwOx6iwiw` | `already_summarized_audited_prior_corpus_work` | Carry forward as completed-skip. Do not touch, re-fetch, or re-summarize in the next recovery issue. |

Row `66` does not expand the next recovery issue. It is referenced only so later
source-order accounting does not lose the known completed-skip marker.

## 6. Allowed Summary-recovery Boundaries

A future summary-recovery issue may authorize only this scope:

- rows `62`, `63`, `64`, `65`, `67`, and `68` only;
- carry row `66` forward as a completed-skip row, with no source touch or
  re-summarization;
- source order from row `62`, skipping completed rows only as explicitly
  carried forward;
- at most six source touches;
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

## 7. Retry and Precedent Boundary

PR #211 records a clean current reportable run with no retry and no lost-status
event. This decision therefore does not rely on any retry exception.

Prior retry disclosures from earlier row windows remain specific to their own
controlling issues and PR discussions. They are not precedent for later
source-access retries. If any future summary-recovery source touch loses status,
fails, or needs a retry, the worker must stop and require explicit retry
authorization in the controlling GitHub issue or PR discussion before any
additional source touch.

## 8. Disallowed Artifacts and Interpretations

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

## 9. Next Issue Gate

Exact next issue title to use:

`[codex] Recover compact summaries for post-Batch-03 rows 62-68 with approved transcript runtime`

That future issue should reference:

- this decision note;
- the PR #211 threshold-discovery report;
- the post-row-61 target-slice and metadata-resolution record;
- the bundled transcript runtime preflight readiness note;
- the cadence and learning-loop protocol;
- the access-attempt ledger template.

The future issue should explicitly restate all source-access, artifact,
retry-record, and Strategy/corpus separation guardrails before any source touch.

## 10. Guardrail Statement

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

## 11. Decision

Decision:

`post_batch_03_rows_62_68_summary_recovery_decision_ready`

Reason: PR #211 records successful Git-safe access-state labels for all six
reportable target rows without retries, stop signals, or raw artifacts. Row
`66` remains completed-skip. Summary recovery must remain separate from this
decision note and must repeat all active checks before source access.
