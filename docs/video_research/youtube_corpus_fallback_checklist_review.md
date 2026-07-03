# YouTube Corpus Fallback Checklist Review

Task: `youtube_corpus_fallback_checklist_review`

## 1. Objective

This note reviews `youtube_corpus_fallback_routing_checklist.md` against the
current committed corpus access policy, cooldown status, source-alignment, and
registry design documents.

The review is docs-only. It uses committed public repository Markdown only and
does not authorize source access, caption probes, access-ledger population,
doctrine updates, or Strategy A/B/B2/C behavior changes.

## 2. Source documents reviewed

Committed public repository docs reviewed:

- `docs/video_research/youtube_corpus_fallback_routing_checklist.md`
- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_fallback_only_backlog_review.md`
- `docs/video_research/youtube_corpus_source_alignment_cleanup.md`
- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_batch_03_blocked_status_post_review_plan.md`

No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
live chat, community post, downloaded media, ASR, external source, private
repository content, local OHLC data, generated Strategy B artifact, market-data
API, broker API, or live system was accessed.

## 3. Review criteria

The checklist should remain acceptable only if it:

- routes fallback-only corpus work to committed public Markdown unless a future
  issue explicitly authorizes another source class;
- keeps `blocked_status`, `metadata_only`, `summary_derived`,
  `audit_derived`, `synthesis_derived`, `doctrine_derived`, and
  `strategy_boundary_derived` source classes separate;
- preserves the current `fallback_only` status while cooldown expiry and the
  next allowed probe window are not proven from committed Git-safe docs;
- rejects title-only or blocked-status rows as support for content, doctrine,
  mechanical-rule, Strategy, performance, or profitability claims;
- keeps channel-wide corpus work separate from Strategy A/B verification;
- does not authorize source probes, access-ledger population, doctrine updates,
  Strategy changes, parameter optimization, or profitability claims.

## 4. Findings

| checklist area | review finding | decision |
| --- | --- | --- |
| First-pass routing | The checklist defaults to `fallback_only_unless_probe_is_explicitly_authorized_and_git_safe`, which matches the cooldown status note and access policy. | pass |
| Source-class separation | The checklist carries forward the same source classes used by the registry design and source-alignment cleanup. | pass |
| Blocked-status handling | Blocked rows remain access-state evidence only and are not promoted into content, doctrine, Strategy, or performance evidence. | pass |
| Metadata-only handling | Video IDs, titles, duration, source order, and availability stay limited to inventory and routing evidence. | pass |
| Summary-derived evidence | The checklist requires committed paraphrased summaries, audits, syntheses, or doctrine docs before a content claim can be treated as summary-derived. | pass |
| Probe boundary | Probe work is blocked unless a future issue explicitly authorizes it and Git-safe preconditions pass. | pass |
| Registry compatibility | The checklist aligns with the registry design's evidence-type, source-granularity, title-only, and Strategy/corpus boundary rules. | pass |
| Strategy boundary | The checklist does not change Strategy A/B/B2/C behavior and does not route corpus evidence into implementation without a separate Strategy-line review. | pass |

## 5. Residual limits

The checklist is review-ready, but it remains a routing and PR-review aid only.
It does not prove that cooldown has expired, create a `next_allowed_probe_after_jst`
value, populate an access ledger, repair registry rows, or authorize any source
access.

If future work needs caption/body access, the controlling issue must separately
authorize the exact source-access scope, repeat the stop conditions, preserve
raw-artifact guardrails, and pass duplicate checks before work begins.

If future work needs doctrine or Strategy-line use, it must stay separate from
this corpus fallback checklist and require a separate design decision.

## 6. Guardrail confirmation

This review is docs-only and uses committed public repository Markdown only.

It performs no YouTube, DownSub, caption, subtitle, transcript-body, caption
URL, comment, live chat, community post, downloaded media, ASR, external source,
private repository, local OHLC, generated Strategy B artifact, market-data API,
broker API, or live-system access.

It does not run caption probes, create a recovery-probe issue, populate an
access ledger, infer cooldown expiry, download video/audio, add raw transcript
or subtitle text, add caption URLs, add CSV/JSON/data/results artifacts, change
Strategy A/B/B2/C behavior, create Strategy B2/C, propose parameter values or
trading-rule changes, perform parameter optimization, update doctrine
conclusions, or make profitability, trading-readiness, or trading-recommendation
claims.

## 7. Review decision

Review decision:

`youtube_corpus_fallback_routing_checklist_review_passed`

Reason: the checklist is consistent with the current corpus access policy,
cooldown status, fallback-only backlog review, source-alignment cleanup, and
registry design. It preserves blocked-status / metadata-only / summary-derived
separation, keeps corpus work separate from Strategy A/B, and routes unsafe or
ambiguous work to no-op, blocker reporting, or a future separately authorized
issue.

## 8. Recommended next docs-only task

Recommended next issue:

`[codex] Corpus fallback review index from committed docs`

Recommended scope:

- use committed public repository Markdown only;
- add a compact index of current corpus fallback policy, status, checklist, and
  review notes;
- keep blocked-status rows, metadata-only rows, and summary-derived evidence
  separate;
- do not run source probes, populate ledgers, revise Strategy A/B/B2/C, update
  doctrine conclusions, access market data, use broker/live systems, optimize
  parameters, or make profitability claims.
