# YouTube Corpus Access Cadence and Failure-log Protocol

Task: `youtube_corpus_access_cadence_failure_log_protocol`

## 1. Objective

This protocol defines the operating cadence and failure-log rules for future
YouTube channel-wide corpus source-access work.

It is docs-only. It uses committed public repository Markdown only and does not
authorize source access, caption probes, access-ledger population, bypass
methods, doctrine updates, or Strategy A/B/B2/C behavior changes.

Purpose:

- avoid repeated access pressure;
- estimate a practical access threshold from controlled evidence instead of
  assuming a low fixed cap;
- make future source touches auditable;
- preserve Git-safe failure logging;
- keep fallback-only work available when source state is blocked, fragile, or
  unclear;
- keep the YouTube channel-wide corpus line separate from Strategy A/B
  verification.

## 2. Source documents reviewed

Committed public repository docs reviewed:

- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_fallback_documentation_chain_closeout.md`
- `docs/video_research/youtube_corpus_fallback_routing_checklist.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_22_tiny_recovery_probe.md`

No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
live chat, community post, downloaded media, ASR, external source, private
repository content, local OHLC data, generated Strategy B artifact, market-data
API, broker API, or live system was accessed.

## 3. Current source-state context

The committed access learning-loop policy already defines conservative source
cadence, outcome labels, daily caps, cooldown rules, fallback routing, and
Git-safe output restrictions.

The committed cooldown status previously defaulted the corpus line to
`fallback_only` because the latest blocked timestamp and next allowed probe
window could not be proven from committed Git-safe docs.

The committed rows `21..22` tiny recovery probe later recorded a human-authorized
two-row source-order probe at `2026-07-03 15:31:14 JST` with outcome label
`success_git_safe_summary_possible` for both rows. That probe note does not
authorize broader probing, rows `23..27`, summary creation, doctrine updates, or
Strategy changes.

Operational decision:

`source_access_threshold_discovery_protocol_required`

Reason: recent committed docs show both prior blocked access and a later tiny
successful probe. Future work must therefore discover the practical access
threshold with staged, timestamped, immediately stoppable source touches instead
of guessing a permanently low daily cap or expanding without a stop protocol.

## 4. Cadence decisions

Use these defaults for any future issue that explicitly authorizes source
touches.

| decision | required value |
| --- | --- |
| Discovery goal | Estimate the practical threshold where limit signals begin. |
| Discovery stage 1 cap | Up to `10` source touches in one JST day. |
| Discovery stage 2 cap | Up to `20` source touches in one JST day, only if stage 1 has no blocker. |
| Discovery stage 3 cap | Up to `30` source touches in one JST day, only if stage 2 has no blocker. |
| Discovery stage 4 cap | Up to `50` source touches in one JST day, only if stage 3 has no blocker. |
| Minimum spacing between touches | Record and keep consistent inside each discovery stage. |
| Parallel source access | prohibited. |
| Immediate retry after a failure | prohibited. |
| Expansion after a successful stage | allowed only by a later issue that explicitly authorizes the next discovery stage. |
| Default mode when authorization or wait proof is missing | `fallback_only`. |

Rationale: the older policy used conservative fixed caps, and this protocol
previously tightened them further while the recovery state was fragile. The
human direction for the corpus line is now to discover a practical non-bypass
threshold rather than assume a low cap for hundreds of videos.

The stage cap is a maximum, not a quota. Use fewer touches or no touches when
the task can be completed from committed public Markdown. Successful completion
of one stage does not authorize bypass methods, raw artifact commits, or
unauthorized expansion beyond the next explicitly authorized stage.

## 5. Timestamp requirements

Every future source touch must record a Git-safe JST timestamp.

Required fields:

| event | required timestamp field | rule |
| --- | --- | --- |
| Authorized source touch starts | `touch_started_at_jst` | Record the local JST start time before the source touch. |
| Authorized source touch completes | `touch_completed_at_jst` | Record the local JST completion time after the outcome is known. |
| Discovery stage | `discovery_stage` | Record the authorized stage number before the source touch. |
| In-stage spacing | `spacing_minutes` | Record the spacing used consistently inside the stage. |
| Daily cumulative count | `source_touch_count_this_jst_day` | Record the cumulative source-touch count for the JST day after each touch. |
| Failure occurs | `failure_observed_at_jst` | Record when the failure category was observed. |
| Cooldown starts | `cooldown_started_at_jst` | Record the same time as the first cooldown-triggering failure unless a later approved source proves a different time. |
| Next allowed consideration | `next_allowed_attempt_not_before_jst` | Record the earliest future time at which a new issue may consider a source touch. |
| Daily cap accounting | `jst_day` | Use the JST calendar date for daily cap tracking. |

Do not fill timestamp fields from memory, browser history, local untracked logs,
raw request output, private notes, or external sources unless a future
controlling issue explicitly authorizes that source class and the committed
output remains Git-safe.

## 6. Failure categories and waits

Use controlled failure categories only.

| failure category | immediate action | minimum wait before next allowed consideration |
| --- | --- | --- |
| `rate_limited_429` | Stop all source touches for the run and start cooldown. | `48_hours` from `failure_observed_at_jst`. |
| `ip_limited` | Stop all source touches for the run and start cooldown. | `72_hours` from `failure_observed_at_jst`. |
| `caption_body_empty` | Stop the current video and do not retry it in the same run. | `24_hours` before the same video or same batch slice may be reconsidered. |
| `caption_body_unavailable` | Stop the current video and do not retry it in the same run. | `24_hours` before the same video or same batch slice may be reconsidered. |
| `ambiguous_source_state` | Stop and route to fallback-only docs or blocker reporting. | Until a future issue clarifies authorization and source-state handling. |
| `raw_artifact_needed` | Stop; do not create raw artifacts. | Until a future issue changes scope, subject to repository guardrails. |
| `bypass_like_access_needed` | Stop; do not use the method. | Indefinite unless repository policy changes. |

When a stop occurs, record the failure time, discovery stage, cumulative JST-day
count, spacing, affected row or video, outcome label, and next allowed attempt
time. The first failure point is the observed upper-bound signal. The
recommended operating cap after a failure should be below the last known clean
stage unless a later human decision changes it.

If any 429 or IP-limit repeats after a cooldown, the next wait must be at least
`72_hours`, and fallback work should remain the default until a docs-only
retrospective reviews the pattern.

Empty or unavailable body states do not create content evidence. They may only
support blocked-status, cadence, cooldown, or fallback-routing decisions.

## 7. Restart conditions

A future source-touch issue may be considered only when all restart conditions
are satisfied:

1. The issue explicitly authorizes the exact source class, batch, row range, and
   maximum touch count.
2. The issue references this protocol, the learning-loop policy, the cooldown
   status note, and the access-attempt ledger template.
3. The latest relevant `failure_observed_at_jst` and
   `next_allowed_attempt_not_before_jst` are either proven from committed
   Git-safe docs or explicitly recorded as unknown.
4. The required wait has elapsed or the issue explicitly stays fallback-only.
5. Duplicate checks confirm no open issue, open PR, deterministic branch, or
   recently merged PR already covers the same probe, summary, or status output.
6. The expected output is Markdown status, compact paraphrase, or aggregate
   retrospective only.
7. Stop rules for 429, IP-limit, empty body, unavailable body, ambiguous state,
   raw-artifact need, bypass-like access, Strategy drift, and doctrine drift are
   repeated in the controlling issue.

If any condition is missing, the correct action is no-op, fallback-only docs, or
blocker reporting.

## 8. Batch expansion stop rules

Stop expanding a batch when any of these occurs:

- the authorized discovery stage cap has been reached;
- any 429 or IP-limit response occurs;
- two empty-body or unavailable-body outcomes occur in the same batch window;
- source state is ambiguous;
- the next row would require a method not authorized by the issue;
- compact paraphrase cannot be produced without raw or near-raw text;
- the work would update doctrine, Strategy behavior, backtests, parameters,
  market-data handling, broker/live behavior, or profitability conclusions;
- duplicate checks find an existing open issue, open PR, deterministic branch,
  or recently merged PR for the same deliverable.

Successful access for one row, one tiny slice, or one discovery stage must not
be treated as permission to continue through the rest of a batch or into the
next discovery stage without explicit authorization.

## 9. Git-safe status-only output

Future source-touch status notes or ledgers may commit only Git-safe fields:

| field | allowed value style |
| --- | --- |
| `controlling_issue` | issue number and title |
| `jst_day` | `YYYY-MM-DD` |
| `touch_started_at_jst` | `YYYY-MM-DD HH:MM JST` |
| `touch_completed_at_jst` | `YYYY-MM-DD HH:MM JST` |
| `failure_observed_at_jst` | `YYYY-MM-DD HH:MM JST`, `none`, or `unknown_in_committed_git_safe_docs` |
| `next_allowed_attempt_not_before_jst` | `YYYY-MM-DD HH:MM JST`, `not_applicable`, or `not_proven_from_committed_docs` |
| `discovery_stage` | `stage_1`, `stage_2`, `stage_3`, `stage_4`, or `not_applicable` |
| `spacing_minutes` | integer minutes or `not_applicable` |
| `target_slice` | approved batch and row range only |
| `public_video_id` | public video ID only |
| `source_touch_count_this_run` | integer |
| `source_touch_count_this_jst_day` | integer or `unknown_in_committed_git_safe_docs` |
| `outcome_label` | learning-loop taxonomy value |
| `failure_category` | controlled category from this protocol |
| `observed_upper_bound_signal` | compact label such as `none`, `stage_2_count_14_429`, or `unknown` |
| `stop_decision` | compact status label |
| `fallback_task` | safe docs-only task or `none` |
| `notes` | compact claim-level note only |

Forbidden output remains:

- raw transcripts;
- subtitle full text;
- raw TXT, SRT, or VTT files;
- caption URLs;
- exact request URLs;
- raw response bodies;
- downloaded video or audio;
- ASR output;
- CSV or JSON dumps;
- `data/` or `results/` files;
- generated candidate, event, trade, metric, or result artifacts;
- cookies, sessions, IP addresses, credentials, tokens, or secrets.

## 10. Fallback mode

Use `fallback_only` when source access is unauthorized, cooldown state is
unclear, a wait period has not elapsed, daily cap is reached, duplicate checks
find existing coverage, or a stop rule fires.

Allowed fallback tasks:

- inventory reconciliation;
- coverage-map updates;
- blocked-status cleanup;
- metadata-only classification cleanup;
- evidence-registry cleanup;
- source-class alignment cleanup;
- cadence retrospective templates;
- doctrine-map gap tracking that does not create new doctrine claims.

Fallback mode must use committed public repository Markdown only unless a
future controlling issue explicitly authorizes another source class.

## 11. Strategy and doctrine boundary

This protocol belongs to the YouTube channel-wide corpus line only.

Source-touch status, blocked-status rows, metadata-only rows, cadence logs, and
failure categories must not change:

- Strategy A/B/B2/C behavior;
- strategy code;
- tests;
- parameters;
- configs;
- runners;
- backtests;
- market-data handling;
- broker/live behavior;
- doctrine conclusions;
- profitability, win-rate, trading-readiness, money-making, or
  trading-recommendation claims.

If a future corpus finding appears relevant to Strategy A/B, it must be routed
to a separate Strategy-line review before any integration.

## 12. Guardrail confirmation

This protocol is docs-only and uses committed public repository Markdown only.

It performs no YouTube, DownSub, caption, subtitle, transcript-body, caption
URL, comment, live chat, community post, downloaded media, ASR, external source,
private repository, local OHLC, generated Strategy B artifact, market-data API,
broker API, or live-system access.

It does not run caption probes, populate an access ledger, infer cooldown expiry
from non-committed sources, download video/audio, add raw transcript or subtitle
text, add caption URLs, add CSV/JSON/data/results artifacts, change Strategy
A/B/B2/C behavior, create Strategy B2/C, propose parameter values or
trading-rule changes, perform parameter optimization, update doctrine
conclusions, or make profitability, trading-readiness, win-rate,
money-making, or trading-recommendation claims.

## 13. Protocol decision

Protocol decision:

`youtube_corpus_access_cadence_failure_log_protocol_ready`

Reason: this protocol reframes future fragile recovery work around staged
threshold discovery, explicit timing and count logging, conservative cooldown
waits, hard stop rules, and Git-safe status-only output. It preserves
corpus/Strategy separation and does not authorize any new source access by
itself.

## 14. Recommended next task

Recommended next task:

`[codex] Intermediate Batch 03 row 21 compact summary recovery`

Recommended scope:

- use only the separately authorized row `21` recovery scope;
- create a compact paraphrased summary only if the controlling issue explicitly
  authorizes summary recovery and the source state supports it;
- do not touch row `22` or rows `23..27`;
- do not run broader probes or threshold-discovery stages under a summary issue;
- do not update doctrine or Strategy behavior.
