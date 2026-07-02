# Channel Playlist-Led Intermediate Batch 03 Caption Access Plan

Task: `channel_playlist_led_intermediate_batch_03_caption_access_plan`

## 1. Objective and scope

This docs-only planning document defines the proposed scope for playlist-led Intermediate Batch 03 in:

`FX中級者のための勝率UP講座`

This plan uses committed repository docs only. It does not perform new source access and does not identify exact Batch 03 video IDs from live playlist metadata.

This PR does not:

- access YouTube;
- access DownSub;
- fetch captions, subtitles, transcript bodies, caption URLs, comments, live chat, community posts, or unrelated channel surfaces;
- download video or audio;
- run ASR;
- add or revise per-video summaries;
- add raw transcript or subtitle text;
- update `docs/video_research/channel_doctrine_map_v1.md`;
- create, update, finalize, or accept a final Doctrine Map v2;
- modify Strategy A/B code, parameters, configs, tests, or conclusions;
- modify Strategy B or create Strategy B2/C;
- run backtests or optimization;
- access market data;
- use broker APIs or add broker/live execution logic;
- make profitability claims.

This is a planning-only corpus-line document. It defines the next Intermediate Batch 03 boundary and future guardrails, but it does not authorize source access by itself.

## 2. Committed source documents used

This plan relies on these committed repository docs:

- `docs/video_research/channel_playlist_metadata_reconciliation_report.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_01_caption_access_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_01/intermediate_batch_01_synthesis.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02_caption_access_plan.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_completed_summary_audit.md`
- `docs/video_research/playlist_led_summaries/intermediate_batch_02/intermediate_batch_02_synthesis.md`

These sources establish the intermediate-playlist order already covered by prior batch work, the known later skip rows that already have completed summaries from older corpus work, and the guardrail posture that Batch 03 should preserve.

## 3. Proposed Intermediate Batch 03 boundary

Committed docs support the following source-order picture for the intermediate playlist:

- playlist order 2 is a known earlier summarized/audited skip row;
- Intermediate Batch 01 covers playlist orders 1 and 3 through 7;
- Intermediate Batch 02 covers playlist orders 8 through 14;
- later known already summarized/audited intermediate rows exist at playlist orders 28, 39, 40, 44, 48, 57, and 66.

Based on that committed evidence, the safest Batch 03 planning boundary is:

- start immediately after completed Batch 02;
- stay within the intermediate playlist only;
- draw from the first unresolved source-order segment after playlist order 14;
- stop before the first later known already summarized/audited skip row at playlist order 28;
- preserve playlist order and skip any row that committed docs later prove was already summarized/audited.

That means Batch 03 should be selected from the unresolved intermediate source-order window bounded by playlist orders 15 through 27, with the exact target rows to be confirmed only in a future explicitly authorized execution step.

This plan intentionally does not claim exact video IDs, compact titles, or caption availability for playlist orders 15 through 27 because those details are not established in committed docs.

## 4. Planned Batch 03 task shape

The future Batch 03 execution task should remain modest and source-order driven.

Recommended shape:

- target 5 to 8 videos;
- prefer the first unresolved rows in playlist order within the 15 through 27 window;
- prefer a 6- or 7-video slice unless committed skip evidence or access blockers justify a different count;
- do not jump ahead to later rows while unresolved earlier rows in the same window remain in scope;
- do not cross the known later skip marker at playlist order 28 in the same task.

If a future authorized execution step discovers that one or more candidate rows in this window already have committed summaries or audits, those rows should be skipped and the next unresolved rows in the same 15 through 27 window should be used instead.

## 5. Planned deliverables for the future Batch 03 task

The next Batch 03 execution task should produce only Git-safe, paraphrased docs outputs.

Expected deliverables:

- one bounded Batch 03 target table recording only the exact selected playlist rows, video IDs, and compact titles needed for that task;
- one paraphrased Markdown summary per approved selected video if caption access is explicitly authorized and succeeds;
- one Batch 03 aggregate report;
- one Batch 03 review document;
- one access-status note for any selected row that is unavailable, blocked, or skipped due to guardrails;
- one recommended next corpus-line step after Batch 03 completion.

If exact target rows still cannot be derived from committed docs alone at execution time, a future task may use a separately authorized bounded metadata-only step to resolve only the minimum row, ID, and title data needed for the selected Batch 03 slice. That future step must not expand into caption, transcript, comment, or channel-wide access without explicit authorization.

## 6. Source-access guardrails for the future task

Any future Batch 03 access task must preserve these rules:

- access only the approved intermediate playlist scope;
- resolve only the exact Batch 03 target rows needed for the selected source-order slice;
- do not access beginner or advanced playlist entries as substitutes;
- do not access unrelated channel videos or other channel surfaces;
- do not access comments, live chat, community posts, or full transcript bodies unless a later issue explicitly authorizes them;
- do not access DownSub, captions, subtitles, transcript bodies, or caption URLs unless a later issue explicitly authorizes that exact route;
- if a future issue authorizes bounded caption access, keep it limited to the exact approved Batch 03 video set only;
- do not retry at scale, scrape broadly, or bypass access controls;
- do not download video or audio;
- do not run ASR;
- do not infer caption availability, content quality, or profitability from titles alone.

Any future source-access step should stop and report if access becomes blocked, unstable, or ambiguous under project guardrails.

## 7. Forbidden artifacts and repository hygiene

Any future Batch 03 execution must not commit:

- raw transcript text;
- subtitle full text;
- raw TXT, SRT, or VTT files;
- caption URLs;
- raw DownSub output;
- raw extractor output;
- downloaded video or audio;
- CSV, JSON, database dumps, `data/`, or `results/` artifacts;
- generated candidate rows or result files;
- credentials, tokens, or secrets.

Committed outputs should remain limited to paraphrased Markdown summaries, reports, reviews, and planning notes.

## 8. Strategy and corpus-line separation

Intermediate Batch 03 remains a YouTube channel-wide corpus-line task only.

It must not:

- update Strategy A/B;
- update Strategy B;
- create Strategy B2 or Strategy C;
- update Doctrine Map v1;
- finalize Doctrine Map v2;
- change backtests or backtest conclusions;
- change market-data handling;
- change broker/live behavior;
- change profitability conclusions.

Batch 03 findings must remain separate from executable strategy rules unless a separate strategy-line review explicitly authorizes integration.

## 9. Validation plan

This planning PR and any future Batch 03 execution PR should validate at minimum:

- `git diff --check`
- `git status --short`
- changed-file sanity check limited to intended docs outputs
- repository guardrail workflow through the PR
- confirmation that no forbidden raw/generated artifacts are committed

For a future source-access or summary task, validation should also confirm that access scope stayed limited to the exact approved Batch 03 rows and that any omitted or blocked rows are documented conservatively.

## 10. Recommended next task

Recommended next PR after this planning document:

`Channel playlist-led intermediate batch 03 bounded target resolution and caption-access execution`

That future task should:

- stay inside the committed Batch 03 boundary defined here;
- resolve the exact selected rows only for the first modest slice inside playlist orders 15 through 27;
- use bounded metadata access only if exact row, ID, and title resolution is still missing from committed docs;
- perform caption access only if that exact route is explicitly authorized by the controlling issue;
- produce paraphrased summaries, aggregate report, and review only for the exact approved Batch 03 set;
- preserve all raw-artifact, Strategy, Doctrine, market-data, broker/live, optimization, and profitability guardrails.

## 11. Readiness decision

Readiness decision:

`intermediate_batch_03_caption_access_plan_ready_for_review`

Reason: this plan defines a committed-docs-only Batch 03 boundary as the next unresolved intermediate source-order window after Batch 02 and before the known later skip row at order 28, records the future selection rules and expected deliverables, preserves source-access and raw-artifact guardrails, and does not authorize captions, subtitles, transcripts, Strategy changes, Doctrine changes, market-data access, broker/live execution, backtests, optimization, or profitability claims.
