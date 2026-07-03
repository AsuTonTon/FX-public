# YouTube Corpus Fallback Review Index

Task: `youtube_corpus_fallback_review_index`

## 1. Objective

This index summarizes the current committed corpus fallback policy, status,
checklist, and review notes for the YouTube channel-wide corpus line.

It is docs-only. It uses committed public repository Markdown only and does not
authorize source access, caption probes, access-ledger population, doctrine
updates, or Strategy A/B/B2/C behavior changes.

## 2. Source documents indexed

Committed public repository docs indexed:

- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_fallback_only_backlog_review.md`
- `docs/video_research/youtube_corpus_source_alignment_cleanup.md`
- `docs/video_research/youtube_corpus_fallback_routing_checklist.md`
- `docs/video_research/youtube_corpus_fallback_checklist_review.md`
- `docs/video_research/channel_evidence_registry_design.md`
- `docs/video_research/channel_evidence_registry_batch_03_blocked_status_post_review_plan.md`

No YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
live chat, community post, downloaded media, ASR, external source, private
repository content, local OHLC data, generated Strategy B artifact, market-data
API, broker API, or live system was accessed.

## 3. Current fallback document map

| document | role | current decision |
| --- | --- | --- |
| `youtube_corpus_access_learning_loop_policy.md` | Defines access outcome labels, cadence, cooldown, fallback routing, and Git-safe output boundaries. | Source-access widening is not authorized; blocked outcomes route to fallback documentation. |
| `youtube_corpus_access_attempt_ledger_template.md` | Provides a future Git-safe ledger structure. | Template only; no attempt facts should be populated unless a future issue explicitly authorizes that scope. |
| `youtube_corpus_access_cooldown_status.md` | Records the current cooldown/status checkpoint from committed docs. | Current mode remains `cooldown_or_uncertain_fallback_only` and `fallback_only` because the latest blocked timestamp and next allowed probe are not proven from committed Git-safe docs. |
| `youtube_corpus_fallback_only_backlog_review.md` | Classifies fallback-only backlog items while cooldown expiry is not proven. | Docs-only cleanup from committed Markdown may proceed when narrowly scoped; source probes, ledger population, cadence claims, doctrine promotion, and Strategy-line use remain blocked or deferred. |
| `youtube_corpus_source_alignment_cleanup.md` | Aligns source classes across corpus access, cooldown, registry, and blocked-status docs. | `blocked_status`, `metadata_only`, `summary_derived`, audit/synthesis/doctrine-derived, and Strategy-boundary lanes are compatible and should remain separate. |
| `youtube_corpus_fallback_routing_checklist.md` | Gives future corpus issues and PR reviews a first-pass routing gate. | Default route is `fallback_only_unless_probe_is_explicitly_authorized_and_git_safe`. |
| `youtube_corpus_fallback_checklist_review.md` | Reviews the fallback routing checklist against current policy, status, source-alignment, and registry docs. | Review passed; the checklist is consistent with current fallback-only boundaries. |
| `channel_evidence_registry_design.md` | Defines the future claim-level registry schema and source-class taxonomy. | Registry rows must remain claim-level, Git-safe, source-doc traceable, and separate from Strategy A/B implementation. |
| `channel_evidence_registry_batch_03_blocked_status_post_review_plan.md` | Plans post-review handling for Intermediate Batch 03 rows `21..27`. | Wait-only handling remains the current path unless a separate issue explicitly authorizes a small wait-gated recovery probe. |

## 4. Source-class index

Use the following conservative lanes when reviewing or writing future corpus
fallback docs.

| source class | indexed meaning | allowed fallback use | must not support |
| --- | --- | --- | --- |
| `blocked_status` | Caption/body evidence is unavailable, blocked, ambiguous, wait-gated, or intentionally not attempted. | Access-state tracking, cooldown routing, fallback routing, and blocker review. | Content claims, doctrine claims, mechanical-rule candidates, Strategy evidence, performance evidence, or profitability conclusions. |
| `metadata_only` | Video ID, playlist row, compact title, duration, source order, or availability without content evidence. | Inventory, coverage, target resolution, source ordering, and audit prioritization. | Claims about what a video teaches, Strategy behavior, parameter values, or trading-readiness claims. |
| `summary_derived` | Claim derived from a committed compact paraphrased summary or a committed document reviewing that summary. | Corpus claim review when the source remains Git-safe and paraphrased. | Title-only promotion, raw or near-raw transcript reconstruction, or Strategy implementation approval. |
| `audit_derived` | Claim, caveat, or blocker from a committed audit or quality review. | Summary-quality review and uncertainty tracking. | Stronger conclusions than the audit supports. |
| `synthesis_derived` | Observation from a committed batch, playlist, or cross-batch synthesis. | Corpus-level theme review and doctrine-gap framing. | Executable Strategy guidance without a separate Strategy-line review. |
| `doctrine_derived` | Observation from a committed doctrine map, evidence index, review, or proposal. | Doctrine-line review subject to source and title-only limits. | Accepted implementation guidance or profitability claims. |
| `strategy_boundary_derived` | Boundary note from committed Strategy/corpus separation docs. | Boundary tracking and later review questions. | Strategy A/B/B2/C behavior, test, config, parameter, runner, backtest, or conclusion changes. |

If a future row or claim spans multiple lanes, split it or use the most
conservative lane.

## 5. Current safe routing summary

Current safe routing:

- fallback-only docs may use committed public repository Markdown only;
- inventory, coverage, metadata-only classification, blocked-status cleanup,
  evidence-registry cleanup, source-class alignment, and checklist/index work
  are safe only when they remain narrow and pass duplicate checks;
- compact titles remain metadata only;
- blocked rows remain access-state evidence only;
- summary-derived claims require committed paraphrased summaries, audits,
  syntheses, or doctrine docs;
- corpus fallback work remains separate from Strategy A/B verification unless a
  later Strategy-line review explicitly authorizes integration.

Current blocked or deferred routing:

- source-access recovery probes;
- YouTube, DownSub, caption, subtitle, transcript-body, caption URL, comment,
  live chat, community post, downloaded media, ASR, external-source, or
  private-source access;
- access-ledger population with new attempt facts;
- proof of cooldown expiry from memory, browser state, untracked logs, raw
  request output, local-only files, or external sources;
- doctrine updates from blocked-status or metadata-only rows;
- Strategy A/B/B2/C behavior, code, test, parameter, config, runner, backtest,
  or conclusion changes;
- Strategy B2 or Strategy C creation;
- parameter optimization;
- trading-readiness, trading-recommendation, or profitability claims.

## 6. Review checklist for future fallback PRs

Review future corpus fallback PRs against these index gates:

- PR body states whether the work is fallback-only, separately authorized, or
  blocked/no-op;
- source access is either explicitly authorized by the issue or clearly not
  performed;
- changed files are limited to the intended Git-safe Markdown scope;
- blocked-status and metadata-only rows are not promoted into content evidence;
- summary-derived claims cite committed paraphrased summaries or reviews;
- compact titles are not treated as transcript-derived evidence;
- no raw transcript, subtitle full text, raw TXT/SRT/VTT, caption URL, raw
  DownSub output, downloaded media, CSV, JSON, `data/`, `results`, credential,
  token, cookie, session, IP address, or secret is added;
- no Strategy A/B/B2/C behavior, test, parameter, config, runner, backtest, or
  conclusion changed;
- no doctrine conclusion is updated from blocked or metadata-only evidence;
- no profitability, win-rate, trading-readiness, or trading-recommendation claim
  is made.

## 7. Guardrail confirmation

This index is docs-only and uses committed public repository Markdown only.

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

## 8. Index decision

Index decision:

`youtube_corpus_fallback_review_index_ready`

Reason: the current committed corpus fallback documents form a consistent
fallback-only operating set. They preserve blocked-status / metadata-only /
summary-derived separation, keep the channel-wide corpus line separate from
Strategy A/B verification, and route unsafe or ambiguous work to no-op, blocker
reporting, or a future separately authorized issue.

## 9. Recommended next docs-only task

Recommended next issue:

`[codex] Corpus fallback coverage map from committed docs`

Recommended scope:

- use committed public repository Markdown only;
- map which fallback documents cover policy, status, checklist, review,
  source-class alignment, registry boundary, and wait-gated probe planning;
- keep blocked-status rows, metadata-only rows, and summary-derived evidence
  separate;
- do not run source probes, populate ledgers, revise Strategy A/B/B2/C, update
  doctrine conclusions, access market data, use broker/live systems, optimize
  parameters, or make profitability claims.
