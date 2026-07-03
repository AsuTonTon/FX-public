# YouTube Corpus Source-Alignment Cleanup

Task: `youtube_corpus_source_alignment_cleanup`

## 1. Objective

This note records a docs-only source-alignment cleanup for the YouTube channel-wide corpus line.

The objective is to align current committed corpus-access, cooldown, registry, and blocked-status wording so future work keeps these source classes separate:

- blocked-status rows;
- metadata-only rows;
- summary-derived evidence;
- audit, synthesis, or doctrine-derived evidence;
- Strategy-boundary notes.

This cleanup uses committed public repository Markdown only. It does not authorize source access, caption probes, recovery probes, ledger population, doctrine updates, or Strategy A/B/B2/C behavior changes.

## 2. Source documents reviewed

Committed public repository docs reviewed:

- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_fallback_only_backlog_review.md`
- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_next_slice_after_batch_02_plan.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_03_continuation_blocked_status.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_03_continuation_blocked_status_review.md`
- `docs/video_research/channel_evidence_registry_batch_03_blocked_status_post_review_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_continuation_review.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_03/intermediate_batch_03_rows_21_27_caption_access_recovery_plan.md`

No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment, live chat, community post, downloaded media, ASR, external source, private repository content, local OHLC data, generated Strategy B artifact, market-data API, broker API, or live system was accessed.

## 3. Current source-class alignment

Current committed docs already define a conservative source-class structure:

| source class | current meaning | allowed use |
| --- | --- | --- |
| `blocked_status` | Caption/body evidence is unavailable, blocked, ambiguous, or intentionally not attempted under current guardrails. | Access-state tracking, cooldown routing, fallback-task routing, and review of missing evidence. |
| `metadata_only` | Video ID, playlist row, title, duration, availability, or source-order metadata without content evidence. | Inventory, coverage, row identity, prioritization, and source routing. |
| `summary_derived` | A claim is derived from a committed compact paraphrased summary. | Corpus claim review when the summary exists and stays Git-safe. |
| `audit_derived` | A claim or blocker is derived from a committed quality review or completed-summary audit. | Review of summary quality, uncertainty, and boundaries. |
| `synthesis_derived` | A claim is derived from a committed batch, playlist, or cross-batch synthesis. | Corpus-level theme review without becoming executable Strategy guidance. |
| `doctrine_derived` | A claim is derived from a committed doctrine map, evidence index, review, or proposal. | Doctrine-line review only, subject to title/source and Strategy-boundary limits. |
| `strategy_boundary_derived` | A note is derived from committed Strategy/corpus separation or mismatch documentation. | Boundary tracking and later review questions, not implementation approval. |

Alignment decision:

`source_classes_aligned_with_current_registry_taxonomy`

Reason: the access policy, cooldown status, fallback backlog review, registry design, and blocked-status registry docs use compatible source lanes. No existing committed document reviewed here needs an immediate wording repair before the next docs-only fallback task.

## 4. Blocked-status rows

Blocked-status rows should remain access-state evidence only.

Use blocked-status wording when a row records:

- HTTP 429, IP-limit, empty-body, unavailable-body, ambiguous source access, or policy-blocked status;
- intentionally not attempted caption/body access;
- wait-gated recovery state;
- source-access blocker documentation;
- fallback-only routing while cooldown expiry is not proven.

Blocked-status rows may support:

- source-access caution;
- cooldown or fallback-only routing;
- duplicate-prevention context for future probes;
- row identity and unresolved-source accounting.

Blocked-status rows must not support:

- per-video content claims;
- doctrine claims;
- mechanical-rule candidates;
- Strategy A/B/B2/C review inputs;
- performance, win-rate, trading-readiness, or profitability conclusions.

For current Intermediate Batch 03 continuation rows `21..27`, the aligned wording is:

`target_resolved_but_caption_body_evidence_unavailable`

The reviewed docs should continue to treat compact titles as metadata only and `caption_access_blocked_http_429` as a blocker, not as content evidence.

## 5. Metadata-only rows

Metadata-only rows should remain navigation and source-status evidence only.

Use metadata-only wording when a row uses:

- video ID;
- playlist order;
- compact title;
- duration;
- availability or target-resolution state;
- source grouping or batch membership.

Metadata-only rows may support:

- inventory reconciliation;
- coverage maps;
- target-table checks;
- source-order preservation;
- future audit prioritization.

Metadata-only rows must not support:

- claims about what a video teaches;
- doctrine conclusions;
- Strategy rule changes;
- parameter values;
- profitability or trading-readiness claims.

Title language such as `勝率`, `神回`, `一攫千金`, `稼ぐ`, `勝ちやすい`, `profitable`, `win`, or similar promotional wording must remain metadata only unless a later committed Git-safe summary, audit, synthesis, or doctrine review supports a compact paraphrased claim separately.

## 6. Summary-derived evidence

Summary-derived evidence requires an existing committed paraphrased summary or a committed document that explicitly reviews such a summary.

Use summary-derived wording only when:

- the source document is a committed Git-safe Markdown summary, aggregate report, audit, synthesis, or doctrine document;
- the claim is a compact paraphrase, not raw or near-raw transcript text;
- the row distinguishes title metadata from the claim itself;
- the claim remains inside the channel-wide corpus line unless a separate Strategy-line review authorizes integration.

Do not promote blocked-status or metadata-only rows into `summary_derived` merely because:

- the title sounds specific;
- the title uses mechanical or performance language;
- a future recovery probe is planned;
- a video ID has been resolved;
- a playlist row has been selected.

## 7. Next-task routing cleanup

Current routing should use these lanes:

| next-task type | safe current routing |
| --- | --- |
| source-alignment cleanup | Safe docs-only fallback when scoped to committed Markdown only. |
| evidence-registry cleanup | Safe docs-only fallback when it does not add raw artifacts or promote blocked rows into claims. |
| inventory or coverage cleanup | Safe docs-only fallback when it uses committed docs only and keeps metadata as metadata. |
| access-attempt ledger population | Deferred until a future issue explicitly authorizes a specific Git-safe ledger population scope. |
| cadence retrospective | Deferred unless committed Git-safe docs provide aggregate attempt facts. |
| rows `21..27` recovery probe | Blocked unless a future issue explicitly authorizes a wait-gated small probe and duplicate checks pass. |
| doctrine-map gap tracking | Deferred to a narrow issue that preserves blocked-status and title-only limits. |
| Strategy-line use | Blocked until a separate Strategy-line review authorizes integration. |

Routing decision:

`fallback_docs_only_routing_preserved`

Reason: current committed docs support source-alignment, evidence-registry cleanup, inventory cleanup, and metadata-only classification as fallback work. They do not authorize source probes, ledger population, doctrine promotion, Strategy changes, or profitability conclusions.

## 8. Reviewer checklist for future corpus docs

Before future corpus docs reuse source-status language, reviewers should confirm:

- blocked rows use `blocked_status` and do not create content claims;
- metadata-only rows stay limited to row identity, inventory, coverage, or routing;
- summary-derived claims cite committed paraphrased summaries, audits, syntheses, or doctrine docs;
- compact titles are not treated as transcript-derived evidence;
- source-access blockers are not described as implementation failures;
- next-task language does not imply probe authorization unless the issue explicitly grants it;
- Strategy A/B/B2/C behavior, tests, parameters, configs, runners, backtests, and conclusions remain unchanged;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw DownSub output, downloaded media, CSV, JSON, `data/`, `results`, credential, token, cookie, session, IP address, or secret is added.

## 9. Guardrail confirmation

This cleanup is docs-only and uses committed public repository Markdown only.

It performs no YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment, live chat, community post, downloaded media, ASR, external source, private repository, local OHLC, generated Strategy B artifact, market-data API, broker API, or live-system access.

It does not run caption probes, create a recovery-probe issue, populate an access ledger, infer cooldown expiry, download video/audio, add raw transcript/subtitle/full caption text, add caption URLs, add CSV/JSON/data/results artifacts, change Strategy A/B/B2/C behavior, create Strategy B2/C, propose parameter values or trading-rule changes, perform parameter optimization, update doctrine conclusions, or make profitability, trading-readiness, or trading-recommendation claims.

## 10. Cleanup decision

Cleanup decision:

`youtube_corpus_source_alignment_cleanup_ready`

Reason: committed corpus docs already provide compatible source-class lanes. This note makes the alignment explicit, preserves blocked-status / metadata-only / summary-derived separation, keeps corpus work separate from Strategy A/B, and routes future work to docs-only fallback tasks unless a later issue explicitly authorizes a narrower source-access or Strategy-line path.

## 11. Recommended next docs-only task

Recommended next issue:

`[codex] Corpus fallback routing checklist from committed docs`

Recommended scope:

- use committed public repository Markdown only;
- turn the source-class alignment and fallback-only routing rules into a compact checklist for future corpus issues and PR reviews;
- keep blocked-status rows, metadata-only rows, and summary-derived evidence separate;
- do not run source probes, populate ledgers, revise Strategy A/B/B2/C, update doctrine conclusions, access market data, use broker/live systems, optimize parameters, or make profitability claims.
