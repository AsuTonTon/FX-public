# YouTube Corpus Fallback Coverage Map

Task: `youtube_corpus_fallback_coverage_map`

## 1. Objective

This coverage map identifies which committed fallback documents currently cover
the YouTube channel-wide corpus fallback policy, status, checklist, review,
source-class alignment, registry boundary, and wait-gated probe-planning
surfaces.

It is docs-only. It uses committed public repository Markdown only and does not
authorize source access, caption probes, access-ledger population, doctrine
updates, or Strategy A/B/B2/C behavior changes.

## 2. Source documents mapped

Committed public repository docs mapped:

- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_fallback_only_backlog_review.md`
- `docs/video_research/youtube_corpus_source_alignment_cleanup.md`
- `docs/video_research/youtube_corpus_fallback_routing_checklist.md`
- `docs/video_research/youtube_corpus_fallback_checklist_review.md`
- `docs/video_research/youtube_corpus_fallback_review_index.md`
- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_intermediate_batch_03_continuation_blocked_status.md`
- `docs/video_research/channel_evidence_registry_batch_03_blocked_status_post_review_plan.md`

No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
live chat, community post, downloaded media, ASR, external source, private
repository content, local OHLC data, generated Strategy B artifact, market-data
API, broker API, or live system was accessed.

## 3. Coverage matrix

| coverage area | primary committed docs | current coverage | notes |
| --- | --- | --- | --- |
| Access policy | `youtube_corpus_access_learning_loop_policy.md` | covered | Defines outcome labels, cadence, cooldown, fallback routing, and Git-safe output boundaries. |
| Ledger template | `youtube_corpus_access_attempt_ledger_template.md` | covered as template only | Provides future Git-safe ledger fields but does not authorize population or add attempt facts. |
| Current status | `youtube_corpus_access_cooldown_status.md` | covered | Records `cooldown_or_uncertain_fallback_only` and `fallback_only` because the latest blocked timestamp and next allowed probe are not proven from committed docs. |
| Fallback backlog | `youtube_corpus_fallback_only_backlog_review.md` | covered | Classifies ready, blocked, duplicate, and deferred fallback-only work while cooldown expiry is not proven. |
| Source-class alignment | `youtube_corpus_source_alignment_cleanup.md` | covered | Aligns `blocked_status`, `metadata_only`, `summary_derived`, audit/synthesis/doctrine-derived, and Strategy-boundary lanes. |
| Routing checklist | `youtube_corpus_fallback_routing_checklist.md` | covered | Gives future issues and PR reviews a first-pass fallback-routing gate. |
| Checklist review | `youtube_corpus_fallback_checklist_review.md` | covered | Reviews and passes the routing checklist against current policy, status, alignment, and registry docs. |
| Review index | `youtube_corpus_fallback_review_index.md` | covered | Indexes the current fallback operating set and points to this coverage-map task. |
| Registry boundary | `channel_evidence_registry_design.md` | covered | Defines the future registry as claim-level, Git-safe, source-doc traceable, and separate from Strategy A/B implementation. |
| Blocked-status row boundary | `channel_evidence_registry_intermediate_batch_03_continuation_blocked_status.md` | covered for rows `21..27` only | Records the seven Intermediate Batch 03 continuation rows as blocked-status evidence only, without content or Strategy claims. |
| Wait-gated probe planning | `channel_evidence_registry_batch_03_blocked_status_post_review_plan.md` | covered as planning only | Preserves wait-only handling and future small-probe constraints; it does not authorize a probe. |

Coverage decision:

`fallback_coverage_surfaces_currently_mapped`

Reason: the committed fallback documents cover the active policy, current
fallback-only status, source-class separation, checklist/review surface, registry
boundary, and wait-gated probe-planning boundary. No additional source access or
row population is needed for this map.

## 4. Source-class coverage

| source class | covered by | current treatment |
| --- | --- | --- |
| `blocked_status` | `youtube_corpus_source_alignment_cleanup.md`; `youtube_corpus_fallback_routing_checklist.md`; `channel_evidence_registry_design.md`; `channel_evidence_registry_intermediate_batch_03_continuation_blocked_status.md` | Access-state and blocker evidence only. It must not support content, doctrine, mechanical-rule, Strategy, performance, or profitability claims. |
| `metadata_only` | `youtube_corpus_source_alignment_cleanup.md`; `youtube_corpus_fallback_routing_checklist.md`; `channel_evidence_registry_design.md` | Video ID, row, title, duration, source order, and availability evidence only. It must not support claims about what a video teaches. |
| `summary_derived` | `youtube_corpus_source_alignment_cleanup.md`; `youtube_corpus_fallback_routing_checklist.md`; `youtube_corpus_fallback_review_index.md`; `channel_evidence_registry_design.md` | Requires committed compact paraphrased summaries or committed docs reviewing those summaries. |
| `audit_derived` | `youtube_corpus_source_alignment_cleanup.md`; `youtube_corpus_fallback_routing_checklist.md`; `channel_evidence_registry_design.md` | Supports quality-review and uncertainty tracking without strengthening findings beyond the audit. |
| `synthesis_derived` | `youtube_corpus_source_alignment_cleanup.md`; `youtube_corpus_fallback_routing_checklist.md`; `channel_evidence_registry_design.md` | Supports corpus-level theme review but not executable Strategy guidance. |
| `doctrine_derived` | `youtube_corpus_source_alignment_cleanup.md`; `youtube_corpus_fallback_routing_checklist.md`; `channel_evidence_registry_design.md` | Supports doctrine-line review only; it is not implementation approval. |
| `strategy_boundary_derived` | `youtube_corpus_source_alignment_cleanup.md`; `youtube_corpus_fallback_routing_checklist.md`; `channel_evidence_registry_design.md` | Supports boundary tracking and later review questions only. |

If future work encounters a row or claim spanning multiple source classes, the
safe action is to split the row or choose the most conservative class.

## 5. Wait-gated probe and registry boundary map

Current wait-gated probe coverage:

- the cooldown/status note says cooldown expiry and the next allowed probe
  window are not proven from committed Git-safe docs;
- the fallback backlog review classifies recovery probes as blocked under the
  current fallback-only scope;
- the routing checklist blocks probe work unless a future issue explicitly
  authorizes the exact probe and Git-safe preconditions pass;
- the blocked-status post-review plan preserves wait-only handling until a
  separate future issue authorizes a small recovery probe;
- the blocked-status registry slice records rows `21..27` as blocked-status
  rows only.

Current registry boundary coverage:

- the registry design allows claim-level, Git-safe rows only;
- blocked-status rows may record unavailable or blocked source access, but they
  must not become content claims;
- metadata-only rows may support inventory, coverage, and routing only;
- future larger registry work should remain narrow and reviewable, not a raw
  artifact store or Strategy specification.

Boundary decision:

`registry_and_probe_boundaries_remain_wait_gated`

Reason: the current document set supports fallback documentation, coverage
mapping, and registry-boundary review. It does not support caption-access
recovery, ledger population with attempt facts, new summary creation, doctrine
updates, or Strategy-line integration.

## 6. Covered, deferred, and blocked surfaces

Covered now:

- fallback policy;
- Git-safe ledger-template structure;
- current fallback-only status;
- fallback-only backlog routing;
- source-class alignment;
- routing checklist and checklist review;
- review index;
- registry schema boundary;
- seven-row blocked-status boundary for Intermediate Batch 03 continuation rows
  `21..27`;
- wait-gated future-probe planning boundary.

Deferred until a future controlling issue:

- access-attempt ledger population;
- cadence retrospective from committed aggregate attempt facts;
- doctrine-map gap tracking that stays within title-only and blocked-status
  limits;
- a small wait-gated recovery probe after explicit authorization and duplicate
  checks;
- any Strategy-line review of future recovered summaries.

Blocked from this task:

- YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
  live chat, community post, downloaded media, ASR, external-source, or
  private-source access;
- source-access recovery probes;
- summary creation from titles or blocked rows;
- raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw DownSub
  output, downloaded media, CSV, JSON, `data/`, `results`, credential, token,
  cookie, session, IP address, or secret commits;
- Strategy A/B/B2/C behavior, code, test, parameter, config, runner, backtest,
  or conclusion changes;
- Strategy B2 or Strategy C creation;
- parameter optimization;
- trading-readiness, trading-recommendation, win-rate, or profitability claims.

## 7. Coverage gaps

Current gaps are intentional rather than defects:

| gap | reason it remains open | safe handling |
| --- | --- | --- |
| Latest blocked / 429 timestamp | Not proven from committed Git-safe docs. | Keep `fallback_only` unless a future issue cites an approved Git-safe source. |
| `next_allowed_probe_after_jst` | Not proven from committed Git-safe docs. | Do not infer from memory, browser state, local logs, or external sources. |
| Populated access-attempt ledger | No current issue authorizes ledger population with attempt facts. | Keep the template as planning-only. |
| New summaries for rows `21..27` | Caption/body evidence is blocked in committed docs. | Do not summarize from titles; wait for a separately authorized recovery path. |
| Strategy-line use | Corpus fallback docs do not authorize Strategy integration. | Require a separate Strategy-line review and design decision. |

## 8. Guardrail confirmation

This coverage map is docs-only and uses committed public repository Markdown
only.

It performs no YouTube, DownSub, caption, subtitle, transcript-body, caption
URL, comment, live chat, community post, downloaded media, ASR, external source,
private repository, local OHLC, generated Strategy B artifact, market-data API,
broker API, or live-system access.

It does not run caption probes, create a recovery-probe issue, populate an
access ledger, infer cooldown expiry, download video/audio, add raw transcript
or subtitle text, add caption URLs, add CSV/JSON/data/results artifacts, change
Strategy A/B/B2/C behavior, create Strategy B2/C, propose parameter values or
trading-rule changes, perform parameter optimization, update doctrine
conclusions, or make profitability, trading-readiness, win-rate, or
trading-recommendation claims.

## 9. Coverage-map decision

Coverage-map decision:

`youtube_corpus_fallback_coverage_map_ready`

Reason: the current committed corpus fallback document set has explicit coverage
for policy, status, checklist, review, source-class alignment, registry
boundary, and wait-gated probe planning. Remaining gaps are intentionally
blocked or deferred because this task does not authorize source access, ledger
population, doctrine promotion, or Strategy-line integration.

## 10. Recommended next docs-only task

Recommended next issue:

`[codex] Corpus fallback coverage map review from committed docs`

Recommended scope:

- use committed public repository Markdown only;
- review this coverage map against the current fallback policy, status, routing
  checklist, source-class alignment, review index, registry design, and
  wait-gated probe plan;
- confirm that blocked-status rows, metadata-only rows, and summary-derived
  evidence remain separated;
- do not run source probes, populate ledgers, revise Strategy A/B/B2/C, update
  doctrine conclusions, access market data, use broker/live systems, optimize
  parameters, or make profitability claims.
