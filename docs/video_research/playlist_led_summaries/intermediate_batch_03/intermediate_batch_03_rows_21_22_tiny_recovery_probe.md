# Intermediate Batch 03 Rows 21-22 Tiny Recovery Probe

Task: `intermediate_batch_03_rows_21_22_tiny_recovery_probe`

## 1. Objective

Record the Git-safe result of the human-authorized tiny recovery probe for
Intermediate Batch 03 rows `21..22`.

This note records outcome labels only. It does not include raw caption text,
subtitle full text, caption URLs, request URLs, downloaded media, CSV, JSON,
`data/`, `results/`, credentials, tokens, cookies, sessions, IP addresses, or
secrets.

## 2. Scope

The probe was limited to the first two unresolved source-order rows from the
committed Intermediate Batch 03 continuation target table:

| playlist order | video ID | probe scope |
| ---: | --- | --- |
| 21 | `bG3-_KfpskE` | attempted caption-body availability check |
| 22 | `-VNpaMQWGUE` | attempted caption-body availability check |

Rows `23..27` were not checked. No parallel work, retries at scale, DownSub
access, alternate caption route, browser automation, media download, ASR,
comments, live chat, community posts, unrelated videos, or broader channel
surface was used.

## 3. Required references reviewed

Committed repository guardrail docs reviewed before the probe:

- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/youtube_corpus_fallback_coverage_map_review.md`
- `docs/video_research/youtube_corpus_fallback_documentation_chain_closeout.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_target_table.md`

## 4. Probe outcome

Attempt timestamp:

`2026-07-03 15:31:14 JST`

| playlist order | video ID | caption-body attempted | outcome label | error category | stop decision |
| ---: | --- | --- | --- | --- | --- |
| 21 | `bG3-_KfpskE` | yes | `success_git_safe_summary_possible` | `none` | continue to row 22 |
| 22 | `-VNpaMQWGUE` | yes | `success_git_safe_summary_possible` | `none` | stop at authorized slice boundary |

No `rate_limited_429`, `ip_limited`, `caption_body_empty`,
`caption_body_unavailable`, ambiguous-access, bypass-like, or raw-artifact
condition occurred in the authorized two-row slice.

## 5. Result interpretation

Rows `21..22` are no longer blocked by the prior `caption_access_blocked_http_429`
state for this probe window. The correct Git-safe status is:

`rows_21_22_caption_body_available_for_future_compact_summary_work`

This status means only that a future tightly scoped task may create compact
paraphrased summaries for rows `21..22` from the available caption bodies. This
probe note does not create those summaries, does not quote or reconstruct raw
source text, and does not treat compact titles as content evidence.

Rows `23..27` remain unprobed in this run and should retain their prior blocked
or unresolved accounting until separately authorized.

## 6. Next recommendation

Recommended next task:

`[codex] Intermediate Batch 03 rows 21-22 compact summary recovery`

Recommended scope:

- create compact paraphrased summaries for rows `21..22` only;
- preserve source order;
- keep raw caption text, subtitle full text, caption URLs, request URLs,
  downloaded media, CSV, JSON, `data/`, and `results/` out of Git;
- do not use the two recovered rows to update Doctrine or Strategy behavior
  without a separate review issue;
- leave rows `23..27` untouched unless a later issue explicitly authorizes
  another tiny probe.

## 7. Guardrail confirmation

This is a Git-safe Markdown status note.

No raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, exact
request URL, raw response body, downloaded video/audio, ASR output, CSV, JSON,
`data/`, `results/`, credential, token, cookie, session, IP address, or secret
is committed.

No Strategy A/B/B2/C behavior, code, parameter, config, test, runner, backtest,
or conclusion is changed. No Strategy B2 or Strategy C is created. No parameter
optimization is performed. No Doctrine conclusion, market-data handling,
broker/live behavior, trading-readiness claim, trading recommendation, win-rate
claim, or profitability claim is added.

The YouTube channel-wide corpus line remains separate from Strategy A/B
verification.

## 8. Status decision

Status decision:

`intermediate_batch_03_rows_21_22_tiny_recovery_probe_ready_for_review`

Reason: the human-authorized source-order probe checked only rows `21..22`,
returned `success_git_safe_summary_possible` for both rows, stopped at the
authorized slice boundary, and recorded only Git-safe status labels without raw
artifacts, Strategy changes, doctrine updates, market-data or broker/live
access, parameter optimization, or profitability claims.
