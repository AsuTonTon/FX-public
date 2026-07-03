# YouTube Corpus Access Learning Loop Policy

Task: `youtube_corpus_access_learning_loop_policy`

## 1. Objective

This policy defines a Git-safe operating loop for learning from YouTube, caption, and transcript access outcomes during the YouTube channel-wide corpus research line.

The objective is to reduce access pressure, preserve reproducibility, and route blocked work into safe fallback documentation. This policy is for load reduction and reproducible research operations. It is not a bypass policy and does not authorize broader source access.

## 2. Non-goals

This policy does not:

- authorize YouTube, DownSub, caption, subtitle, transcript-body, comment, live chat, community-post, downloaded-media, ASR, market-data, broker, live-system, or private-source access;
- authorize caption probes by itself;
- authorize a crawler, downloader, scraper, or browser automation workflow;
- create or update Strategy A/B/B2/C rules, code, parameters, configs, tests, runners, backtests, or conclusions;
- create Strategy B2 or Strategy C;
- authorize parameter optimization;
- make or support profitability, trading-readiness, or trading-recommendation claims.

## 3. Prohibited Bypass Behavior

The corpus workflow must not use access-control or rate-limit bypass tactics.

Prohibited behavior includes:

- VPN rotation;
- proxy rotation;
- IP rotation;
- cookie or session swapping;
- CAPTCHA workarounds;
- browser automation for source access;
- parallel scraping;
- immediate repeated retries after blocked responses;
- hidden request URL, credential, token, or session capture;
- downloading audio or video to work around caption limits.

Blocked responses must be treated as access states, not implementation failures. A blocked access state is evidence for cadence and routing decisions only; it is not permission to widen access methods.

## 4. Access Outcome Taxonomy

Use these outcome labels in future Git-safe ledgers or retrospective notes:

| result | use |
| --- | --- |
| `success_git_safe_summary_possible` | Caption/body access was explicitly authorized for the target and a compact paraphrased summary can be prepared without raw text commits. |
| `metadata_only_available` | Metadata such as ID, title, duration, playlist position, or availability is visible, but no content evidence is available. |
| `caption_body_not_attempted` | The loop intentionally did not attempt caption-body access because the task was docs-only, the daily cap was reached, or cooldown was active. |
| `caption_body_empty` | A permitted caption-body attempt returned no usable body content. |
| `caption_body_unavailable` | Caption/body access was unavailable under the approved method. |
| `rate_limited_429` | A 429 or equivalent platform rate-limit response occurred. |
| `ip_limited` | The response indicates IP-based access limiting. |
| `blocked_by_policy` | The requested action was not allowed by repository guardrails or the controlling issue. |
| `deferred_to_fallback` | Work moved to a safe docs-only fallback task without further source access. |

Do not reinterpret title language, blocked status, or metadata-only availability as transcript-derived evidence.

## 5. Access Attempt Ledger Schema

A future access-attempt ledger, when explicitly authorized by an issue, must remain Git-safe and aggregate-friendly. It may use Markdown tables or compact per-attempt entries.

Allowed fields:

| field | description |
| --- | --- |
| `attempt_date_jst` | Calendar date or timestamp in JST. |
| `run_type` | Example values: `scheduled_loop`, `manual_probe_window`, `fallback_only`. |
| `worker_cadence` | Planned cadence, such as `15_minutes` or `30_minutes`. |
| `target_batch` | Batch or slice name approved for the attempt. |
| `video_id` | Public video ID only. |
| `video_duration_minutes` | Approximate duration if already available from approved metadata. |
| `wait_since_previous_attempt_minutes` | Elapsed wait before this attempt. |
| `caption_body_attempted` | `yes` or `no`. |
| `result` | One taxonomy value from this policy. |
| `error_category` | Controlled category such as `none`, `429`, `ip_limit`, `empty_body`, `unavailable_body`, or `policy_blocked`. |
| `cooldown_started` | `yes` or `no`. |
| `next_allowed_probe_after_jst` | Earliest next probe window when a cooldown applies. |
| `fallback_task_used` | Safe fallback task selected for the loop, if any. |
| `notes` | Short claim-level note; no raw source text or sensitive access details. |

Forbidden ledger content:

- raw caption URLs;
- exact request URLs;
- raw transcript text;
- subtitle full text;
- raw TXT, SRT, or VTT content;
- cookies, sessions, IP addresses, credentials, tokens, or secrets;
- downloaded media;
- CSV, JSON, `data/`, `results/`, generated candidates, generated results, or market-data artifacts.

## 6. 15-minute Human-paced Cadence Rule

The default corpus access loop is human-paced:

- at most one video may be processed per 15-minute loop;
- caption-body access, if explicitly authorized, may be attempted for at most one video per loop;
- do not run parallel workers for caption/body access;
- do not queue immediate retries inside the same loop;
- if the current issue is docs-only, the loop must remain docs-only even if a candidate video is known.

If no safe source-access action is available, the loop should switch to fallback documentation or no-op cleanly.

## 7. Daily Caption-attempt Cap

Caption-body attempts need a daily cap even when explicitly authorized.

Initial cap:

- 8 to 10 caption-body attempts per JST day.

The cap is a maximum, not a quota. Use fewer attempts when:

- previous attempts produced empty-body or unavailable-body responses;
- 429 or IP-limit responses recently occurred;
- source-access evidence is not needed for the current task;
- safe docs-only fallback work is available.

The cap must not be bypassed by parallel runs, multiple sessions, alternate environments, cookie/session changes, or browser automation.

## 8. 429 and IP-limit Handling

If any 429 or IP-limit response occurs:

1. Stop caption-body attempts immediately for the current loop.
2. Record the result as `rate_limited_429` or `ip_limited`.
3. Start a 24 to 48 hour caption-access cooldown.
4. Route later loops to docs-only fallback work until the cooldown expires.
5. Do not try VPN, proxy, IP rotation, cookie/session swapping, CAPTCHA workarounds, browser automation, parallel scraping, or immediate retry.

If 429 or IP-limit responses recur after cooldown:

1. Extend the next cooldown to 48 to 72 hours.
2. Reduce the daily cap for the next attempt window.
3. Prefer fallback-only mode until a retrospective confirms that retry pressure can be safely lowered.

## 9. Empty-body and Unavailable Handling

If empty-body or unavailable-body failures occur:

- record the state as `caption_body_empty` or `caption_body_unavailable`;
- do not repeatedly retry the same video in the same loop;
- do not treat the response as a scraper or implementation failure by default;
- if the same failure repeats within a batch, stop retrying that batch until the next scheduled probe window;
- route the loop to fallback documentation or metadata-only status updates.

Empty-body and unavailable-body states do not create content evidence and must not be promoted into doctrine, mechanical-rule candidates, or Strategy behavior.

## 10. Cooldown Rules

Cooldowns apply to caption-body access, not to safe docs-only fallback work.

| trigger | minimum cooldown | next action |
| --- | --- | --- |
| first 429 or IP-limit response | 24 to 48 hours | fallback-only corpus work |
| repeated 429 or IP-limit after cooldown | 48 to 72 hours | reduce next daily cap and continue fallback-only work |
| repeated empty-body or unavailable-body responses within a batch | until next scheduled probe window | record blocked status and avoid same-batch retries |
| daily cap reached | until next JST day or next approved window | switch to fallback-only work |
| ambiguous source authorization | until human clarification | no source access; docs-only or no-op |

Cooldown records must not include IP addresses, session details, cookies, credentials, exact request URLs, or raw response bodies.

## 11. Fallback Task Routing While Blocked

Safe fallback tasks include:

- inventory reconciliation;
- coverage map updates;
- blocked-status ledger updates;
- metadata-only classification;
- existing-summary claim extraction;
- evidence-registry cleanup;
- source-alignment cleanup;
- doctrine-map gap tracking.

Fallback tasks must use committed public repository docs only unless a controlling issue explicitly authorizes another source. Fallback work must preserve the separation between the channel-wide corpus line and the Strategy A/B verification line.

## 12. Cadence Retrospective

Run a docs-only cadence retrospective after every 10 caption-body attempts or once per JST day when caption attempts occur.

The retrospective should summarize only aggregate, Git-safe information:

- number of attempted caption-body accesses;
- number of successful accesses;
- number of 429 or IP-limit responses;
- number of empty-body or unavailable-body responses;
- average wait interval;
- daily cap used;
- whether cooldown was triggered;
- whether the next window should keep 15 minutes, increase to 30 minutes, reduce the daily cap, or stay in fallback-only mode.

The retrospective must not include raw source text, caption URLs, request URLs, cookies, session details, IP addresses, downloaded media, or generated data artifacts.

## 13. Adaptive Cadence Adjustment Rules

Use conservative cadence changes:

- keep `15_minutes` only when no rate-limit, IP-limit, repeated empty-body, or repeated unavailable-body pattern is present;
- increase to `30_minutes` after repeated empty-body or unavailable-body outcomes;
- reduce the daily cap after any repeated 429 or IP-limit outcome;
- use `fallback_only` while cooldown is active;
- require human review before increasing the daily cap above 10 attempts per JST day;
- require explicit issue authorization before changing source-access method or target scope.

Adaptive cadence is a risk-control mechanism. It must not be used to optimize around platform limits or access controls.

## 14. Manual Viewing Notes

Manual viewing notes are allowed only as claim-level notes when a future issue explicitly permits them.

Manual notes must:

- be compact paraphrases;
- identify uncertainty and source class;
- avoid reconstructing full transcript text;
- avoid timestamp-by-timestamp transcript substitutes;
- avoid raw subtitle, raw caption, or near-raw speech text;
- stay out of Strategy behavior unless a separate Strategy-line review authorizes integration.

Manual viewing notes must not be used to turn metadata-only or blocked-status rows into doctrine or Strategy claims.

## 15. Metadata-only Evidence Boundary

Metadata-only evidence must remain metadata-only.

Metadata-only rows may support:

- inventory status;
- playlist or batch routing;
- blocked-status documentation;
- future audit prioritization;
- source-availability notes.

Metadata-only rows must not support:

- doctrine claims;
- mechanical-rule candidates;
- Strategy A/B/B2/C behavior;
- parameter values;
- profitability or trading-readiness claims.

Promotion from metadata-only status requires later supporting evidence from approved Git-safe summaries, audits, syntheses, or doctrine review documents.

## 16. Git-safe Outputs

Allowed outputs under this policy:

- Markdown policy notes;
- Git-safe access-attempt ledger entries;
- aggregate cadence retrospectives;
- blocked-status reports;
- metadata-only classification notes;
- fallback task reports;
- evidence-registry cleanup notes;
- doctrine-map gap-tracking notes that do not create new doctrine claims from blocked or metadata-only evidence.

Forbidden outputs:

- raw transcripts;
- subtitle full text;
- raw TXT, SRT, or VTT files;
- caption URLs;
- exact request URLs;
- downloaded video or audio;
- ASR output;
- CSV or JSON dumps;
- `data/` or `results/` artifacts;
- generated candidates or generated result files;
- credentials, tokens, cookies, sessions, IP addresses, or secrets.

## 17. Guardrail Confirmation

This policy preserves the repository guardrails:

- no YouTube, DownSub, caption, subtitle, transcript-body, caption-URL, comment, live-chat, community-post, downloaded-media, ASR, external-source, private-repository, local-OHLC, generated Strategy B artifact, market-data API, broker API, or live-system access is authorized here;
- no caption probes are run or authorized by this document;
- no video or audio download is authorized;
- no raw transcript, subtitle full text, raw subtitle file, caption URL, CSV, JSON, `data/`, `results/`, credential, token, cookie, session, IP address, or secret is added;
- no Strategy A/B/B2/C behavior, code, parameter, config, test, runner, backtest, or conclusion is changed;
- no Strategy B2 or Strategy C is created;
- no parameter optimization is performed;
- no profitability, trading-readiness, or trading-recommendation claim is made;
- channel-wide corpus evidence remains separate from Strategy A/B unless a later Strategy-line review authorizes integration.

## 18. Next Safe Tasks

Recommended next safe tasks:

1. Add a narrow Git-safe access-attempt ledger template for future explicitly authorized probe windows.
2. Review existing blocked-status corpus docs and align their outcome labels to this taxonomy.
3. Add a docs-only cadence retrospective template for future aggregate reviews.
4. Continue evidence-registry cleanup using committed public repository docs only.
5. Track doctrine-map gaps without promoting metadata-only or blocked-status rows into doctrine claims.

## 19. Readiness Decision

`youtube_corpus_access_learning_loop_policy_ready_for_review`

Reason: this policy defines a conservative learning loop for access outcomes, caps, cooldowns, fallback routing, and aggregate retrospectives. It reduces access pressure and records blocked states safely without authorizing source-access widening, bypass behavior, raw artifact commits, Strategy changes, parameter optimization, or profitability claims.
