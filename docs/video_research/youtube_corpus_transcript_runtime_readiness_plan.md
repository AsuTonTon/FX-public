# YouTube Corpus Transcript Runtime Readiness Plan

Task: `youtube_corpus_transcript_runtime_readiness_plan`

## 1. Objective

This plan resolves the readiness question raised by PR #145 before any retry of
post-Batch-03 rows `29..35`.

PR #145 recorded that the bounded threshold-discovery retry stopped before
source access because the automation environment did not have an approved
transcript/caption runtime available. This document defines the safe route
criteria for a later retry. It does not run a source touch, install a
dependency, create summaries, update doctrine, or change Strategy behavior.

## 2. Source Documents Reviewed

Committed repository docs reviewed:

- `docs/video_research/youtube_corpus_post_batch_03_rows_29_35_threshold_discovery.md`
- `docs/video_research/youtube_corpus_post_batch_03_next_target_slice.md`
- `docs/video_research/youtube_corpus_access_cadence_failure_log_protocol.md`
- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`
- `docs/video_research/youtube_corpus_access_cooldown_status.md`
- `docs/video_research/youtube_corpus_threshold_discovery_stage_1.md`

Issue #146 and PR #145 metadata were used only to confirm the task scope,
duplicate state, and the runtime blocker that the merged PR body records. No
YouTube, DownSub, caption, subtitle, transcript-body, caption URL, request URL,
comment, live chat, community post, downloaded media, ASR, external source,
private source, market data, broker API, or live system was accessed.

## 3. Blocker from PR #145

PR #145 stopped before source access with:

`stop_before_source_access_no_approved_runtime`

The committed blocker report records these runtime facts for that run:

| runtime or route | PR #145 status |
| --- | --- |
| `python` / `python3` | resolved to WindowsApps stubs, not usable runtimes |
| `py` | unavailable |
| bundled local Codex `python.exe` | not found |
| `node` / `npm` on `PATH` | unavailable |
| Node REPL transcript packages | unavailable |
| `uv`, `uvx`, `pip`, `pipx` | unavailable |
| `yt-dlp`, `youtube-dl` | unavailable and not used |
| direct caption endpoint | not attempted |
| browser source access | not used |
| alternate source route | not attempted |

This was an environment-capability blocker, not a YouTube access result. It did
not prove caption availability, transcript availability, rate limiting, empty
body state, unavailable body state, row content, doctrine, Strategy evidence, or
trading relevance.

## 4. Approved Runtime Requirements

The committed docs allow a future source-touch run only when all controlling
requirements are satisfied.

| requirement | current rule from committed docs |
| --- | --- |
| controlling issue | Must explicitly authorize the exact source class, batch or row range, and maximum touch count. |
| active recheck | Must recheck the controlling issue and live duplicate state immediately before the first source touch. |
| target slice | Rows `29..35` must come from the committed target-slice document and remain unresolved. |
| runtime route | Must be a normal approved transcript/caption mechanism available before source access starts. |
| dependency state | No committed doc currently authorizes installing a new dependency inside the source-touch run. |
| output type | Markdown status fields only unless a later issue separately authorizes summary recovery. |
| source-touch count | At most one touch per target row, preserving source order and stopping on the first protocol stop signal. |
| cadence | No parallel source access, no immediate retries after failure, and all timing/count fields recorded in JST. |
| cooldown handling | Latest relevant failure timing must be proven from committed Git-safe docs or explicitly recorded as unknown. |
| forbidden artifacts | No raw transcript text, subtitle full text, caption URLs, request URLs, raw responses, media, CSV, JSON, `data/`, or `results/`. |
| research boundary | Corpus source-access status must not change Strategy A/B/B2/C behavior, doctrine conclusions, or trading conclusions. |

The stage-1 report proves that a normal installed transcript API route was used
successfully for a prior authorized run. It does not by itself make a specific
runtime available in every later automation worktree.

## 5. Runtime Route Classification

Allowed now:

| route | status | condition |
| --- | --- | --- |
| docs-only readiness planning | `allowed` | Uses committed Markdown and PR metadata only. |
| no-network runtime preflight | `allowed` | May check whether an already-present runtime binary and transcript package can be imported without touching video, caption, transcript, or request sources. |
| future normal transcript/caption runtime | `allowed_after_approval` | Requires an open controlling issue, the active recheck, duplicate clearance, and a runtime already available before the first source touch. |
| status-only blocker report | `allowed` | Use if the approved runtime route remains unavailable or ambiguous. |

Disallowed for this readiness task and for any retry unless a later committed
policy explicitly changes the rule:

| route | status | reason |
| --- | --- | --- |
| YouTube, caption, subtitle, or transcript-body access in this issue | `disallowed` | Issue #146 is readiness-only and no-source-access. |
| DownSub route | `disallowed` | Not authorized by the reviewed docs for this retry path. |
| browser automation for source access | `disallowed` | The learning-loop policy prohibits browser automation as a source-access route. |
| direct caption endpoint or captured request URL | `disallowed` | Would risk caption URL or request URL handling outside the approved method. |
| audio/video download or ASR | `disallowed` | Repository and policy guardrails forbid this route unless a future issue explicitly authorizes ASR. |
| VPN, proxy, IP rotation, cookie/session swap, CAPTCHA workaround, or parallel scraping | `disallowed` | These are bypass-like behaviors under the learning-loop policy. |
| dependency installation during a source-touch run | `disallowed_here` | Issue #146 forbids dependency installation unless already explicitly allowed by committed project docs. |

Unresolved:

| question | current state |
| --- | --- |
| Which exact runtime binary and package are approved for recurring automation worktrees? | Not established by committed docs. |
| Whether a dependency may be installed, cached, vendored, or pre-provisioned for transcript access? | Requires explicit committed authorization before use. |
| Whether bundled Python, Node, or another local runtime will be consistently available in future worktrees? | Not proven by PR #145. |
| How to prove runtime readiness without source access? | Use only local no-network binary/package checks until a source-touch issue is opened. |
| Whether rows `29..35` may be retried immediately after readiness is solved? | Requires a new controlling issue and the active source-touch recheck. |

## 6. Minimum Safe Preflight Before Retrying Rows 29-35

A later retry must complete this preflight before the first source touch:

1. Confirm the controlling issue is open and explicitly authorizes rows
   `29..35`, the transcript/caption source class, and a maximum of seven
   touches.
2. Confirm no open PR, merged PR, deterministic branch, or recently closed
   duplicate already covers the same rows or deliverable path.
3. Confirm the target rows still come from
   `docs/video_research/youtube_corpus_post_batch_03_next_target_slice.md` and
   have no newer committed completion evidence.
4. Identify the exact runtime binary and transcript/caption package before any
   source touch.
5. Run only no-network runtime checks during preflight, such as binary version
   and package import checks. Do not pass video IDs to the runtime during
   preflight.
6. Confirm no dependency install is required unless a committed policy or the
   controlling issue explicitly authorizes that installation route.
7. Confirm the output document will use only Git-safe status fields from the
   cadence protocol and ledger template.
8. Confirm stop rules are repeated: 429, IP-limit, empty body, unavailable body,
   ambiguous source state, raw-artifact need, bypass-like access need, duplicate
   coverage, Strategy drift, doctrine drift, market-data drift, broker/live
   drift, and profitability drift.
9. Re-run the active controlling-issue check immediately before the first
   source-touch command.
10. If any item fails, stop before source access and produce either no PR or a
    docs-only blocker using committed public Markdown only.

## 7. Next Issue Gate

Do not open a retry issue merely because rows `29..35` remain unresolved. Open
the retry only after an approved runtime route is available and the no-network
preflight can identify it.

Exact next issue to open after the runtime route is available:

`[codex] Retry YouTube threshold discovery over post-Batch-03 rows 29-35 with approved transcript runtime`

Required next-issue scope:

- use `docs/video_research/youtube_corpus_post_batch_03_next_target_slice.md`;
- reference this readiness plan, the cadence protocol, the learning-loop
  policy, the ledger template, the cooldown status note, and the PR #145
  blocker report;
- preserve source order from row `29`;
- limit source touches to rows `29..35`, maximum seven touches;
- use only the approved transcript/caption runtime identified before source
  access starts;
- record only Git-safe status fields unless a later issue separately authorizes
  compact summary recovery;
- stop immediately on the first protocol stop signal;
- keep the YouTube corpus line separate from Strategy A/B verification.

If choosing or provisioning the runtime requires a new policy decision, the
retry issue must wait. The policy decision should be handled separately before
the retry issue exists.

## 8. Guardrail Statement

Docs-only readiness plan. No source access was run. No YouTube, DownSub,
caption, subtitle, transcript-body, caption URL, request URL, comment, live
chat, community post, downloaded media, ASR, external source, private source,
local OHLC data, generated Strategy artifact, market-data API, broker API, or
live system was accessed.

No raw transcript text, subtitle full text, raw TXT/SRT/VTT, caption URL,
request URL, raw response body, CSV, JSON, `data/`, `results`, downloaded
media, credential, token, cookie, session, IP address, or secret was added.

No Strategy A/B/B2/C behavior, code, parameters, configs, tests, runners,
backtests, market-data handling, broker/live behavior, doctrine conclusion, or
trading conclusion was changed. No Strategy B2 or Strategy C was created. No
parameter optimization was performed. No profitability, trading-readiness,
win-rate, money-making, or trading-recommendation claim was made. The YouTube
channel-wide corpus line remains separate from Strategy A/B verification.

## 9. Decision

Decision:

`youtube_corpus_transcript_runtime_readiness_plan_ready`

Reason: the blocker in PR #145 was a missing approved runtime before source
access. The safe next step is not another immediate source-touch issue, but a
runtime-gated retry only after an already-approved transcript/caption route is
available and no-network preflight checks pass.
