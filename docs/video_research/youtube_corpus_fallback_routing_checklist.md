# YouTube Corpus Fallback Routing Checklist

Task: `youtube_corpus_fallback_routing_checklist`

## 1. Objective

This checklist gives future YouTube channel-wide corpus issues and PR reviews a
compact fallback-routing gate.

Use it when caption/body access is blocked, cooldown status is uncertain, or a
task must stay on committed public repository Markdown only.

This checklist does not authorize source access, caption probes, recovery
probes, access-ledger population, doctrine updates, or Strategy A/B/B2/C
behavior changes.

## 2. Source documents reviewed

Committed public repository docs reviewed:

- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_fallback_only_backlog_review.md`
- `docs/video_research/youtube_corpus_source_alignment_cleanup.md`
- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_next_slice_after_batch_02_plan.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_03_continuation_blocked_status.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_03_continuation_blocked_status_review.md`
- `docs/video_research/channel_evidence_registry_batch_03_blocked_status_post_review_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_review.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`

No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
live chat, community post, downloaded media, ASR, external source, private
repository content, local OHLC data, generated Strategy B artifact, market-data
API, broker API, or live system was accessed.

## 3. First-pass routing

Before starting a corpus task, classify it into exactly one current route.

| question | if yes | route |
| --- | --- | --- |
| Does the issue explicitly authorize a narrow source-access probe and repeat the stop conditions? | Continue only after cooldown proof, duplicate checks, and raw-artifact guardrails pass. | `separately_authorized_probe_review` |
| Does committed Git-safe documentation prove cooldown expiry and the next allowed probe window? | Continue only if the issue also authorizes the probe. | `probe_possible_but_not_self_authorizing` |
| Is cooldown expiry unknown or source access unauthorized? | Use committed docs only or no-op. | `fallback_only` |
| Is the task about blocked rows, metadata, registry cleanup, source labels, or coverage maps? | Keep the output docs-only and claim-safe. | `safe_fallback_docs_only` |
| Would the task require captions, transcripts, source bodies, browser source access, downloads, ASR, market data, broker/live access, or Strategy changes? | Stop unless a future issue explicitly and narrowly authorizes that exact source or action class. | `blocked_or_needs_human_decision` |

Default decision:

`fallback_only_unless_probe_is_explicitly_authorized_and_git_safe`

## 4. Source-class checklist

Use this checklist before writing or approving any corpus fallback document.

| source class | required treatment | reject if |
| --- | --- | --- |
| `blocked_status` | Use for unavailable, blocked, ambiguous, cooldown, or intentionally not attempted source access. | It creates content, doctrine, mechanical-rule, Strategy, performance, or profitability claims. |
| `metadata_only` | Use for video ID, playlist row, compact title, duration, source order, or availability. | It treats title wording as evidence for what the video teaches. |
| `summary_derived` | Use only for compact claims from committed paraphrased summaries or docs reviewing those summaries. | It is inferred from titles, blocked rows, unavailable captions, or raw text. |
| `audit_derived` | Use for committed quality reviews, completed-summary audits, or uncertainty notes. | It upgrades an audit caveat into a stronger conclusion than the audit supports. |
| `synthesis_derived` | Use for committed batch, playlist, or cross-batch synthesis observations. | It becomes executable Strategy guidance or final doctrine without a separate review. |
| `doctrine_derived` | Use for committed doctrine maps, evidence indexes, reviews, or proposals. | It treats candidate doctrine as accepted implementation guidance. |
| `strategy_boundary_derived` | Use for Strategy/corpus separation and mismatch-boundary notes. | It changes Strategy A/B/B2/C behavior, tests, parameters, configs, backtests, or conclusions. |

If a row or claim crosses two source classes, split it or choose the more
conservative class.

## 5. Allowed fallback tasks

Allowed fallback tasks are docs-only and must use committed public repository
Markdown only unless a controlling issue says otherwise.

Safe fallback tasks:

- inventory reconciliation;
- coverage-map updates;
- metadata-only classification cleanup;
- blocked-status documentation cleanup;
- evidence-registry cleanup for committed registry docs;
- source-label or source-class alignment cleanup;
- doctrine-map gap tracking that does not create new claims from blocked or
  metadata-only evidence;
- cadence or ledger templates that do not invent attempt facts.

Every allowed fallback task still needs duplicate checks before work starts.
If an open issue, open PR, deterministic branch, or recently merged PR already
covers the exact deliverable, the correct action is no-op.

## 6. Blocked or deferred tasks

Do not perform these actions from a fallback-only issue:

- YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
  live chat, community post, downloaded media, ASR, external-source, or
  private-source access;
- caption-access recovery probes;
- access-ledger population with new attempt facts;
- proof of cooldown expiry from memory, browser state, untracked logs, raw
  request output, local-only files, or external sources;
- summary creation from compact titles alone;
- doctrine updates from blocked-status or metadata-only rows;
- Strategy A/B/B2/C behavior, code, test, parameter, config, runner, backtest,
  or conclusion changes;
- Strategy B2 or Strategy C creation;
- parameter optimization;
- trading-readiness, trading-recommendation, or profitability claims.

Deferred does not mean authorized. Each deferred action needs a separate
controlling issue with exact scope, duplicate checks, raw-artifact guardrails,
and Strategy/corpus separation.

## 7. PR review checklist

For future corpus PRs, check:

- the PR body states whether the work is fallback-only, probe-authorized, or
  blocked/no-op;
- source access is either explicitly authorized by the issue or clearly not
  performed;
- blocked-status rows remain access-state evidence only;
- metadata-only rows remain inventory or routing evidence only;
- summary-derived claims cite committed paraphrased summaries, audits,
  syntheses, or doctrine docs;
- compact titles are not used as transcript-derived evidence;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw
  DownSub output, downloaded media, CSV, JSON, `data/`, `results`, credential,
  token, cookie, session, IP address, or secret is added;
- no source-probe output, access URL, raw response body, local-only log, or
  generated artifact is committed;
- no Strategy A/B/B2/C behavior, test, parameter, config, runner, backtest, or
  conclusion changed;
- no doctrine conclusion is updated from blocked or metadata-only evidence;
- no profitability, win-rate, trading-readiness, or trading-recommendation claim
  is made.

## 8. Routing examples

| candidate task | checklist result | safe action |
| --- | --- | --- |
| Clean up stale source-class labels in committed corpus docs. | `safe_fallback_docs_only` | Proceed if duplicate checks pass. |
| Add rows for caption-blocked videos using only video IDs and compact titles. | `metadata_only` or `blocked_status` only | Proceed only if no content or doctrine claims are created. |
| Create summaries for rows `21..27` from titles because captions are blocked. | blocked | No-op or document blocker. |
| Run a caption-access probe after a cooldown is believed to have elapsed. | blocked unless the issue explicitly authorizes the probe and Git-safe docs prove or handle the wait state. | Stop or wait for a controlling issue. |
| Populate an access ledger from committed aggregate attempt facts. | deferred unless explicitly scoped. | Use only Git-safe fields from the controlling issue or committed docs. |
| Use recovered corpus observations to change Strategy B behavior. | blocked Strategy-line action. | Requires a separate Strategy-line design decision and issue. |

## 9. Guardrail confirmation

This checklist is docs-only and uses committed public repository Markdown only.

It performs no YouTube, DownSub, caption, subtitle, transcript-body, caption
URL, comment, live chat, community post, downloaded media, ASR, external source,
private repository, local OHLC, generated Strategy B artifact, market-data API,
broker API, or live-system access.

It does not run caption probes, create a recovery-probe issue, populate an
access ledger, infer cooldown expiry, download video/audio, add raw
transcript/subtitle/full caption text, add caption URLs, add CSV/JSON/data/results
artifacts, change Strategy A/B/B2/C behavior, create Strategy B2/C, propose
parameter values or trading-rule changes, perform parameter optimization,
update doctrine conclusions, or make profitability, trading-readiness, or
trading-recommendation claims.

## 10. Checklist decision

Checklist decision:

`youtube_corpus_fallback_routing_checklist_ready`

Reason: current committed corpus docs support a conservative fallback-only route
when source access is blocked, cooldown proof is missing, or the issue is
docs-only. This checklist makes the routing gate explicit, preserves
blocked-status / metadata-only / summary-derived separation, keeps corpus work
separate from Strategy A/B, and routes unsafe or ambiguous work to no-op,
blocker reporting, or a future separately authorized issue.

## 11. Recommended next docs-only task

Recommended next issue:

`[codex] Corpus fallback checklist review from committed docs`

Recommended scope:

- use committed public repository Markdown only;
- review this checklist against the current access policy, cooldown status,
  fallback backlog review, source-alignment cleanup, and registry design;
- confirm that blocked-status rows, metadata-only rows, and summary-derived
  evidence remain separated;
- do not run source probes, populate ledgers, revise Strategy A/B/B2/C, update
  doctrine conclusions, access market data, use broker/live systems, optimize
  parameters, or make profitability claims.
