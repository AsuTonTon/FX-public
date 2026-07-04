# YouTube Corpus Transcript Runtime Provisioning Policy Decision

Task: `youtube_corpus_transcript_runtime_provisioning_policy_decision`

## 1. Objective

This decision draft records the safe policy boundary for making an approved
transcript/caption runtime available to future YouTube corpus threshold-discovery
runs.

It follows the PR #145 runtime blocker and the PR #147 readiness plan. It is a
docs-only policy decision draft. It does not install dependencies, touch
YouTube or caption sources, run transcript access, create summaries, update
doctrine, or change Strategy behavior.

## 2. Source Documents Reviewed

Committed repository docs reviewed:

- `docs/video_research/youtube_corpus_transcript_runtime_readiness_plan.md`
- `docs/video_research/youtube_corpus_post_batch_03_rows_29_35_threshold_discovery.md`
- `docs/video_research/youtube_corpus_access_cadence_failure_log_protocol.md`
- `docs/video_research/youtube_corpus_access_learning_loop_policy.md`
- `docs/video_research/youtube_corpus_access_attempt_ledger_template.md`

Live GitHub issue and PR state was used only for duplicate-prevention and task
scope checks. No YouTube, DownSub, caption, subtitle, transcript-body, caption
URL, request URL, comment, live chat, community post, downloaded media, ASR,
external source, private source, market data, broker API, or live system was
accessed.

## 3. Problem Statement

PR #145 stopped before source access because the automation environment did not
have an approved transcript/caption runtime available. PR #147 then established
that rows `29..35` should not be retried until a runtime route is approved and a
no-network preflight can identify it before the first source touch.

The unresolved policy question is not whether the corpus line may bypass source
limits. It may not. The question is how this repository may make a normal
transcript/caption runtime available without causing source access, raw-artifact
storage, dependency drift, or hidden operational behavior inside a future
source-touch issue.

## 4. Unresolved Runtime Route Questions

| question | decision status |
| --- | --- |
| Which exact runtime binary may recurring worktrees use for transcript/caption access? | `human_approval_required` |
| May dependencies be installed during a source-touch issue? | `no` |
| May dependencies be pre-provisioned outside a source-touch issue? | `human_approval_required` |
| May a bundled Codex runtime be used when already present and importable? | `allowed_after_no_network_preflight` |
| May a repository-vendored runtime package be added? | `human_approval_required` |
| May browser automation, direct caption endpoints, DownSub, ASR, or downloaded media be used as substitute runtime routes? | `disallowed` |
| May the rows `29..35` retry issue be opened now? | `no` |

## 5. Safe Runtime Provisioning Options

These options are safe to discuss or prepare without source access. They do not
authorize touching video, caption, or transcript bodies by themselves.

| option | status | conditions |
| --- | --- | --- |
| Use an already-present bundled Python runtime with an already-installed transcript package | `allowed_after_approval` | The future worker must prove the binary path and package import with no-network checks before source access. |
| Use an already-present bundled Node runtime with an already-installed transcript package | `allowed_after_approval` | The future worker must prove the binary path and package import with no-network checks before source access. |
| Pre-provision a runtime in the Codex automation environment | `human_approval_required` | Approval must define owner, path, package name, version policy, update process, and no-secret/no-raw-artifact rules. |
| Commit a small runtime-readiness note naming the approved local route | `allowed_after_human_decision` | The note must not contain credentials, request URLs, cookies, sessions, raw responses, or private machine details beyond an approved stable class. |
| Keep fallback-only mode until an approved route exists | `allowed_now` | This is the default if approval is absent, ambiguous, or not reproducible. |

## 6. Disallowed Runtime Routes

The following routes remain disallowed for this policy decision and for any
future retry unless a later explicit policy change says otherwise.

| route | decision | reason |
| --- | --- | --- |
| Installing dependencies inside a source-touch issue | `disallowed` | It mixes environment mutation with source access and makes the run harder to audit. |
| Ad hoc `pip`, `npm`, `npx`, `uv`, or downloaded package use during source access | `disallowed` | It creates unreviewed dependency and reproducibility drift. |
| Browser automation for source access | `disallowed` | The learning-loop policy classifies this as a prohibited source-access route. |
| Direct caption endpoint or captured request URL use | `disallowed` | It risks handling request URLs or hidden source details outside the approved method. |
| DownSub route | `disallowed` | It is not authorized by the readiness plan for this retry path. |
| Audio/video download or ASR | `disallowed` | Repository guardrails forbid downloaded media and ASR unless a future issue explicitly authorizes ASR. |
| VPN, proxy, IP rotation, cookie/session swap, CAPTCHA workaround, or parallel scraping | `disallowed` | These are bypass-like behaviors under the learning-loop policy. |
| Committing raw transcript, subtitle text, caption URLs, request URLs, CSV, JSON, `data/`, or `results/` artifacts | `disallowed` | These are forbidden repository artifacts. |

## 7. Recommended Policy Decision

Recommended decision:

`human_approval_required_before_runtime_provisioning`

Rationale:

- PR #145 and PR #147 establish that the blocker is runtime availability before
  source access, not a caption availability result.
- Current committed docs do not name a stable approved runtime path, package,
  version policy, provisioning owner, or update process.
- Choosing or provisioning that route changes project operations beyond a normal
  docs-only issue.
- The safe default is fallback-only until the user or project owner approves a
  runtime route.

Minimum human approval should answer:

1. Which runtime family is approved: bundled Python, bundled Node, a
   pre-provisioned local runtime, or another explicitly named route.
2. Which package name and version policy are approved.
3. Whether the route may be pre-provisioned outside source-touch issues.
4. Who owns updates when the package or platform behavior changes.
5. How future workers should prove readiness without network access.
6. Whether any repository documentation should record the approved route class.

Until those answers exist, future automation must not open the rows `29..35`
retry issue and must not install or improvise a runtime during a source-touch
run.

## 8. Minimum No-network Preflight Requirements

After human approval exists, a future source-touch issue must still complete
these checks before the first source touch:

1. Confirm the controlling issue is open and explicitly authorizes rows
   `29..35`, the transcript/caption source class, and a maximum of seven
   touches.
2. Confirm no open PR, merged PR, deterministic branch, or recently closed
   duplicate already covers the same rows or deliverable path.
3. Confirm the approved runtime route matches the route named by the policy
   decision or controlling issue.
4. Print or record only the runtime class, binary availability, package import
   availability, and package/version identity when safe. Do not pass video IDs,
   caption IDs, URLs, cookies, sessions, or request details during preflight.
5. Confirm no dependency installation is required in the source-touch run.
6. Confirm the output document will record only Git-safe status fields from the
   cadence protocol and ledger template.
7. Re-run the active controlling-issue check immediately before the first source
   touch.
8. Stop before source access if any preflight item fails.

## 9. Next Issue Gate

Do not open the rows `29..35` retry issue yet.

Open the retry issue only after the runtime route is approved and the no-network
preflight can identify it.

Exact next issue title to use after approval:

`[codex] Retry YouTube threshold discovery over post-Batch-03 rows 29-35 with approved transcript runtime`

That future issue should:

- reference this decision draft, the readiness plan, the PR #145 blocker report,
  the cadence protocol, the learning-loop policy, and the ledger template;
- name the approved runtime route;
- limit source touches to rows `29..35`, maximum seven touches, in source order;
- require no-network preflight before source access;
- record only Git-safe status fields unless a separate issue authorizes compact
  summary recovery;
- stop on the first protocol stop signal;
- keep YouTube corpus findings separate from Strategy A/B verification.

## 10. Guardrail Statement

Docs-only policy decision draft. No source access was run. No dependency was
installed. No YouTube, DownSub, caption, subtitle, transcript-body, caption URL,
request URL, comment, live chat, community post, downloaded media, ASR,
external source, private source, local OHLC data, generated Strategy artifact,
market-data API, broker API, or live system was accessed.

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

`youtube_corpus_transcript_runtime_provisioning_policy_decision_draft_ready`

Reason: committed docs prove that the next safe action is a human-approved
runtime provisioning policy decision, not another source-touch retry. Until the
runtime route is approved and no-network preflight can identify it, the corpus
line should stay in fallback-only mode for rows `29..35`.
