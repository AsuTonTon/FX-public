# YouTube Corpus Access Cooldown Status

Task: `youtube_corpus_access_cooldown_status`

## 1. Objective

This note records the current Git-safe cooldown/status checkpoint for the YouTube channel-wide corpus access line before any future caption, transcript, DownSub, YouTube, or recovery-probe issue is considered.

It is status documentation only. It does not authorize source access, caption probing, browser automation, downloads, ASR, transcript-body access, or any Strategy A/B/B2/C behavior change.

## 2. Source documents reviewed

Committed public repository docs reviewed:

- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_03_continuation_blocked_status.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_03_continuation_blocked_status_review.md`
- `docs/video_research/channel_evidence_registry_batch_03_blocked_status_post_review_plan.md`

No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment, live chat, community post, downloaded media, ASR, external source, private repository content, local OHLC data, generated Strategy B artifact, market-data API, broker API, or live system was accessed.

## 3. Current authoritative cooldown state from committed docs

Committed docs establish a blocked caption-access state for Intermediate Batch 03 continuation rows `21..27`.

The recovery plan records all seven target rows as `caption_access_blocked_http_429` and states that the run stopped without retries at scale, alternate caption routes, DownSub access, media download, ASR, comments, live chat, community posts, unrelated videos, or broader channel surfaces.

The learning-loop policy requires a 24 to 48 hour caption-access cooldown after a first 429 or IP-limit response, and fallback-only corpus work while cooldown is active.

However, the committed docs reviewed here do not provide a precise timestamp for the latest blocked / 429 / empty-body event. Because the latest timestamp is not provable from committed Git-safe docs, the current operational status defaults to:

`cooldown_or_uncertain_fallback_only`

## 4. Known information gaps

Known gaps:

- latest HTTP 429 timestamp is not present in the reviewed committed docs;
- latest failed recovery-probe timestamp is not present in the reviewed committed docs;
- no committed ledger row currently proves a `next_allowed_probe_after_jst` value;
- no committed document proves that the required wait period has elapsed from the latest blocked event;
- no future probe issue is currently authorized by this status note.

These gaps must not be filled from memory, browser state, local untracked files, raw logs, captions, request output, or external sources unless a future controlling issue explicitly authorizes that source class.

## 5. Last blocked / 429 timestamp handling

If the latest blocked / 429 / empty-body timestamp is not available in committed Git-safe docs, do not invent it.

For the current status, the last blocked timestamp is:

`unknown_in_committed_git_safe_docs`

This means the cooldown cannot be marked expired. A future operator may update this status only from an approved Git-safe source that records the timestamp without raw response bodies, request URLs, IP addresses, cookies, sessions, credentials, tokens, or caption URLs.

## 6. Next allowed probe handling

The next allowed probe cannot be proven from the reviewed committed docs.

Current value:

`not_proven_from_committed_docs`

Do not create or recommend an immediate caption probe unless committed docs prove that the required wait period has elapsed and a future issue explicitly authorizes the exact small probe. A future probe issue must first reference this status note, `youtube_corpus_access_learning_loop_policy.md`, and `youtube_corpus_access_attempt_ledger_template.md`.

## 7. Fallback-only status

Because the current cooldown state cannot be proven from committed docs, the active mode is:

`fallback_only`

Allowed fallback work must use committed public repository docs only unless a controlling issue explicitly authorizes another source class. Fallback work may update inventory, coverage maps, blocked-status ledgers, metadata-only classifications, existing-summary claim extraction, evidence-registry cleanup, source-alignment cleanup, or doctrine-map gap tracking.

Fallback work must not treat blocked status, title language, or metadata-only availability as content evidence, doctrine evidence, mechanical-rule evidence, Strategy evidence, performance evidence, or profitability evidence.

## 8. Rules before any future probe issue can be created

Before any future source-access probe issue is created, all of the following must be true:

1. The future issue explicitly authorizes the exact caption-access recovery probe.
2. This status note is referenced.
3. The access learning-loop policy is referenced.
4. The access-attempt ledger template is referenced.
5. Committed Git-safe docs prove the latest blocked / 429 / empty-body timestamp or explicitly state that the timestamp remains unknown.
6. Committed Git-safe docs prove whether the required wait period has elapsed.
7. The probe is tiny, non-parallel, and source-order preserving.
8. The issue repeats immediate stop conditions for 429, IP-limit, empty-body, unavailable, ambiguous, bypass-like access, raw-artifact needs, or Strategy/Doctrine/backtest/market-data/broker/live/profitability drift.
9. Duplicate checks confirm no open issue, open PR, deterministic branch, or recently merged PR already covers the same probe.
10. The expected output remains Git-safe Markdown only.

If any item is not satisfied, the safe action is fallback-only documentation or no-op.

## 9. Git-safe fields for future ledger population

If a future issue authorizes ledger population, use only Git-safe fields such as:

| field | current value or rule |
| --- | --- |
| `attempt_date_jst` | Use only an approved timestamp from the future controlling issue or approved Git-safe run record. |
| `run_type` | `fallback_only` for this status note. |
| `worker_cadence` | `fallback_only` until probe authorization and wait proof exist. |
| `target_batch` | Intermediate Batch 03 continuation rows `21..27` only when a future issue authorizes that target. |
| `caption_body_attempted` | `no` for this status note. |
| `result` | `deferred_to_fallback` for this status note. |
| `error_category` | `429_known_for_rows_21_27_timestamp_unknown` from committed docs. |
| `cooldown_started` | `unknown_timestamp_from_committed_docs`. |
| `next_allowed_probe_after_jst` | `not_proven_from_committed_docs`. |
| `fallback_task_used` | cooldown/status documentation. |
| `notes` | Keep compact, claim-level, and Git-safe. |

Do not include raw captions, transcript text, subtitle full text, raw TXT/SRT/VTT, caption URLs, request URLs, downloaded media, ASR output, CSV/JSON dumps, `data/`, `results/`, cookies, sessions, IP addresses, credentials, tokens, or secrets.

## 10. Safe fallback tasks while cooldown / uncertainty remains

Safe fallback tasks include:

- inventory reconciliation;
- coverage map updates;
- metadata-only classification;
- existing-summary claim extraction;
- evidence-registry cleanup;
- source-alignment cleanup;
- doctrine-map gap tracking;
- blocked-status documentation cleanup;
- cadence retrospective template drafting without source access.

These tasks must preserve the channel-wide corpus line as separate from Strategy A/B verification. They must not change Strategy A/B/B2/C behavior, parameters, code, configs, tests, runners, backtests, or conclusions.

## 11. Guardrail confirmation

This note is docs-only and uses committed public repository docs only.

It performs no YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment, live chat, community post, downloaded media, ASR, external source, private repository, local OHLC, generated Strategy B artifact, market-data API, broker API, or live-system access.

It does not run caption probes, create a recovery-probe issue, download video/audio, add raw transcript/subtitle/full caption text, add caption URLs, add CSV/JSON/data/results artifacts, infer exact timestamps absent from committed docs, change Strategy A/B/B2/C behavior, create Strategy B2/C, propose parameter values or trading-rule changes, perform parameter optimization, or make profitability or trading-recommendation claims.

## 12. Next safe task

Recommended next safe task:

`[codex] Review YouTube corpus fallback-only task backlog while cooldown is uncertain`

Reason: the current cooldown expiry cannot be proven from committed Git-safe docs, so the safest next work is fallback-only backlog review using committed public repository docs. Do not run a caption probe, create a recovery-probe issue, or widen source access until a future issue satisfies the rules in Section 8.

## 13. Status decision

Status decision:

`youtube_corpus_access_cooldown_status_fallback_only_ready_for_review`

Reason: committed docs establish 429-blocked caption access for Intermediate Batch 03 rows `21..27`, but do not prove the latest blocked timestamp or a next allowed probe window. This note therefore defaults to `cooldown_or_uncertain_fallback_only`, preserves Git-safe fallback routing, and does not authorize source access.
