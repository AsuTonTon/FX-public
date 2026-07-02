# Channel Full-Corpus Playlist-Led Remaining Input Status Review

Task: `channel_full_corpus_playlist_led_remaining_input_status_review`

Review date: 2026-07-01

## 1. Objective and scope

This is a docs-only review of remaining full-channel corpus input work.

This review:

- Uses existing committed inventory, availability, priority, and completed-summary docs as the source of truth.
- Records the project-owner-observed current count of 607 videos as a reconciliation item against the committed 601 baseline.
- Introduces playlist-led intake as the preferred future research order.
- Treats the previous title-priority route as useful routing history, not the default next intake method.
- Recommends a docs-only next planning PR before any new summaries are created.

This review does not:

- Access YouTube or DownSub.
- Fetch captions.
- Download video or audio.
- Run ASR.
- Use proxies, VPN rotation, IP rotation, cookies, credentials, rate-limit bypass, or downloader workarounds.
- Summarize new videos.
- Commit raw transcripts, subtitle text, raw TXT, SRT, VTT, caption URLs, CSV, JSON, database, `data/`, `results/`, videos, audio, or raw candidate rows.
- Modify Strategy A/B code, parameters, configs, or tests.
- Modify Strategy B.
- Create Strategy B2 or Strategy C.
- Run backtests or optimization.
- Access or fetch market data.
- Use broker APIs or add broker, live trading, order execution, or execution logic.
- Make profitability claims.
- Update `docs/video_research/channel_doctrine_map_v1.md`.
- Create or update `docs/video_research/channel_doctrine_map_v2.md`.
- Treat the Doctrine Map v2 draft proposal as final or accepted doctrine.
- Mark Batch 08 as completed.

## 2. Existing committed corpus baseline

The committed baseline remains 601 rows. The project-owner-observed current count of 607 is recorded only as an external reconciliation item in this PR.

| baseline item | committed count | source |
| --- | ---: | --- |
| full deduplicated corpus | 601 | `channel_transcript_availability_report.md`; `channel_lightweight_summary_batch_08_selection_report.md` |
| regular-video tab unique count | 509 | `channel_transcript_availability_report.md` |
| Shorts count | 92 | `channel_transcript_availability_report.md` |
| streams count | 0 | `channel_transcript_availability_report.md` |
| full-union manual-caption rows | 0 | `channel_high_priority_availability_completion_report.md` |
| full-union auto-caption rows | 500 | `channel_high_priority_availability_completion_report.md` |
| full-union unavailable rows | 4 | `channel_high_priority_availability_completion_report.md` |
| full-union blocked rows | 1 | `channel_high_priority_availability_completion_report.md` |
| full-union unknown rows | 96 | `channel_high_priority_availability_completion_report.md` |
| high-priority rows | 115 | `channel_transcript_availability_report.md`; `channel_high_priority_relevance_triage_report.md` |
| medium-priority rows | 186 | `channel_transcript_availability_report.md` |
| low-priority rows | 300 | `channel_transcript_availability_report.md` |
| high-priority regular videos | 100 | `channel_high_priority_availability_completion_report.md` |
| high-priority Shorts | 15 | `channel_high_priority_availability_completion_report.md` |
| high-priority streams | 0 | `channel_transcript_availability_report.md` |
| high-priority caption-available rows | 112 | `channel_high_priority_availability_completion_report.md`; `channel_lightweight_summary_batch_08_selection_report.md` |
| high-priority unavailable rows | 3 | `channel_high_priority_availability_completion_report.md`; `channel_lightweight_summary_batch_08_selection_report.md` |
| high-priority blocked rows | 0 | `channel_high_priority_availability_completion_report.md` |
| high-priority unknown rows | 0 | `channel_high_priority_availability_completion_report.md` |
| completed lightweight-summary batches before Batch 08 | 7 | `channel_lightweight_summary_batch_08_selection_report.md` |
| completed lightweight summaries before Batch 08 | 56 | `channel_lightweight_summary_batch_08_selection_report.md`; `corpus_v2_batch_01_07_audit_synthesis.md` |
| unique summarized IDs before Batch 08 | 56 | `channel_lightweight_summary_batch_08_selection_report.md` |
| high-priority caption-available unsummarized rows before Batch 08 reservation | 56 | `channel_lightweight_summary_batch_08_selection_report.md` |
| completed-summary audit batches synthesized | 7 | `corpus_v2_batch_01_07_audit_synthesis.md` |
| total videos audited in Batch 01-07 completed-summary audits | 56 | `corpus_v2_batch_01_07_audit_synthesis.md` |
| total mechanical-rule candidates audited in Batch 01-07 | 233 | `corpus_v2_batch_01_07_audit_synthesis.md` |

Per-batch completed-summary audit coverage:

| batch | videos audited | mechanical-rule candidates audited | completed-summary audit decision |
| --- | ---: | ---: | --- |
| Batch 01 | 8 | 37 | `batch_01_completed_summaries_audit_passed` |
| Batch 02 | 8 | 49 | `batch_02_completed_summaries_audit_passed` |
| Batch 03 | 8 | 28 | `batch_03_completed_summaries_audit_passed` |
| Batch 04 | 8 | 35 | `batch_04_completed_summaries_audit_passed` |
| Batch 05 | 8 | 30 | `batch_05_completed_summaries_audit_passed` |
| Batch 06 | 8 | 32 | `batch_06_completed_summaries_audit_passed` |
| Batch 07 | 8 | 22 | `batch_07_completed_summaries_audit_passed` |

Known committed blocked, unavailable, and unknown counts:

- Full-union blocked rows: 1.
- Full-union unavailable rows: 4.
- Full-union unknown rows: 96.
- High-priority blocked rows: 0.
- High-priority unavailable rows: 3.
- High-priority unknown rows: 0.
- Batch 08 selection attempt: blocked, with no final target set frozen.

## 3. Current count reconciliation

| item | count | status |
| --- | ---: | --- |
| committed baseline count | 601 | verified only from committed docs |
| project-owner-observed current count | 607 | recorded as owner-observed, not independently regenerated in this PR |
| implied delta | +6 | requires reconciliation |
| committed docs identify the +6 videos | unknown from committed docs | no committed playlist/current-count mapping identifies them |

This PR does not access YouTube and does not regenerate the full inventory. The +6 delta could reflect new uploads, changed tab availability, playlist-specific rows, previously hidden rows, or counting differences, but the committed docs do not identify the video IDs.

Future reconciliation would require a bounded docs-only planning task that:

- compares the owner-observed 607 count against the committed 601 baseline;
- maps the owner-supplied playlist order to existing committed video IDs where possible;
- records which playlist entries are already in the committed corpus;
- identifies missing IDs without committing raw metadata dumps;
- decides whether a narrow metadata refresh is needed;
- avoids regenerating the whole inventory unless a specific gap is found and approved.

## 4. Playlist-led intake rationale

Playlist-led intake should supersede title-priority-only routing by default.

Rationale:

- The channel owner appears to prescribe a learning order through playlists.
- Beginner, intermediate, and advanced sequencing can reveal doctrine dependencies that title priority alone may miss.
- Playlist order reduces the risk of overfitting Strategy A/B to isolated videos selected only by obvious title terms.
- It can help distinguish foundational doctrine from advanced discretionary management.
- It can show whether Shorts are standalone lessons, promotional fragments, or compressed pointers to longer videos.
- It should remain separate from Strategy A/B changes until a playlist-led synthesis is complete and reviewed.

Project-owner supplied playlist learning order:

| order | playlist label |
| ---: | --- |
| 1 | `完全初心者向けFX講座｜ゼロから月100万円稼ぐロードマップ` |
| 2 | `FX中級者のための勝率UP講座` |
| 3 | `本物のトレーダーになるためのFX上級講座` |

These labels are project-owner-supplied and should be preserved exactly as UTF-8 text. This PR does not access those playlists or verify their membership.

## 5. Existing completed input status

| input line | committed status |
| --- | --- |
| Completed lightweight summaries | Batch 01 through Batch 07 are complete, covering 56 summaries. |
| Completed-summary audits | Batch 01 through Batch 07 completed-summary audits all passed. |
| Corpus v2 Batch 01-07 audit synthesis | Merged synthesis covers 56 audited videos and 233 audited mechanical-rule candidates. |
| Doctrine Map v2 candidate review | Ready for human review as candidate planning only; it does not create final Doctrine Map v2 or update Doctrine Map v1. |
| Strategy A/B mismatch review | Human-reviewed as conservative context; it authorizes no Strategy A/B implementation change. |
| Strategy B TP1 review | Closed with prior closure reaffirmed; Strategy B should not continue summary/review PRs by default. |
| Batch 08 | Blocked selection attempt only; no final target set, summaries, or quality review were created. |

## 6. Remaining input categories

| category | committed count/status | interpretation | missing committed doc if exact count is unavailable |
| --- | --- | --- | --- |
| Already summarized/audited | 56 summaries, 56 audited videos, 233 audited candidates | Batch 01-07 are complete and audited. | none |
| High-priority caption-available unsummarized | 56 | Remaining high-priority caption-available rows after Batch 01-07 and blocked Batch 08. | none |
| High-priority caption-unknown | 0 | High-priority availability accounting is complete. | none |
| High-priority blocked | 0 | No high-priority row remains blocked at availability-accounting level. | none |
| High-priority unavailable | 3 | These are accounted for and not eligible for caption-based summarization unless a separate approved non-caption method exists. | none |
| High-priority Shorts | 15 total; 12 auto-caption, 3 unavailable | Shorts remain a distinct input segment and need playlist-led handling. | exact playlist mapping and summary eligibility by Short |
| Medium-priority unsummarized | unknown from committed docs; 186 medium-priority rows exist | The committed docs give the medium-priority baseline, but not a full current summary-status map for medium rows. | committed row-level summary-status inventory or playlist mapping |
| Low-priority unsummarized | unknown from committed docs; 300 low-priority rows exist | The committed docs give the low-priority baseline, but not a full current summary-status map for low rows. | committed row-level summary-status inventory or playlist mapping |
| Playlist-mapped but not yet summarized | unknown from committed docs | No committed playlist-to-video-ID mapping exists for the three owner-supplied playlists. | playlist metadata reconciliation plan and mapping output |
| Not-yet-playlist-mapped | unknown from committed docs | The committed 601 baseline is not currently partitioned by the owner-supplied playlist order. | playlist metadata reconciliation plan and mapping output |
| Current-count delta requiring reconciliation | +6 owner-observed rows | The delta is not identified in committed docs. | current-count reconciliation or playlist metadata reconciliation output |

The table intentionally does not infer exact medium-priority, low-priority, playlist-mapped, or not-yet-playlist-mapped remaining counts beyond what committed docs prove.

## 7. Batch 08 status

Batch 08 status from committed docs:

| question | committed answer |
| --- | --- |
| Was the Batch 08 target set finalized? | No. The selection report says no final Batch 08 target set is frozen. |
| Were Batch 08 summaries completed? | No. The report says no Batch 08 per-video summaries should be created from that PR. |
| Was Batch 08 blocked? | Yes. It is recorded as a blocked caption-access recovery and selection rework attempt. |
| What was retained? | Two provisional carry-forward candidates, not a frozen target set. |
| Why blocked? | Caption body retrieval remained blocked in that environment, and local ignored caption cache coverage was insufficient for a proper eight-target selection. |
| Should Batch 08 resume as-is? | No. Under the new playlist-led direction, Batch 08 should be re-planned or replaced after playlist metadata reconciliation. |
| Should Batch 08 be marked completed? | No. Committed docs do not prove completion. |

Wait/probe policy:

- Do not probe YouTube or DownSub in this PR.
- Do not run immediate retry loops against blocked caption access.
- Future caption access should use a bounded, project-owner-approved batch.
- Future DownSub use should follow `docs/video_research/downsub_access_policy_v2.md`.
- If caption access remains blocked, the next step should remain planning/status documentation rather than summary generation.

## 8. DownSub usage strategy

Future DownSub use should be the preferred subtitle acquisition route for bounded input batches because prior direct access attempts encountered blocking or rate-limit issues. That preference does not authorize access in this PR.

Future DownSub use must be:

- bounded to a project-owner-approved batch or exact video ID set;
- low-rate;
- documented in the PR body and related report;
- classified honestly under `docs/video_research/downsub_access_policy_v2.md`;
- limited to subtitle-derived comparison, lightweight summaries, audits, correction notes, or review documents;
- committed only as Git-safe paraphrased documentation.

Future DownSub use must not include:

- raw subtitle commits;
- subtitle full text commits;
- raw TXT, SRT, or VTT commits;
- caption URL commits;
- downloaded video or audio;
- ASR;
- proxy, VPN, IP rotation, cookies, credentials, platform bypass, or rate-limit bypass;
- automated downloader commits;
- CSV, JSON, database, `data/`, or `results/` artifacts;
- Strategy A/B changes;
- Doctrine Map updates unless separately authorized after corpus-level review;
- Strategy B2 or Strategy C creation;
- backtests, optimization, or profitability claims.

If local raw material is needed for a future approved batch, it should remain local-only and uncommitted. The committed output should remain paraphrased lightweight summaries, audits, or correction notes only.

## 9. Recommended next PR

Recommended next docs-only PR:

`Channel playlist metadata reconciliation plan`

Reason:

- The corpus count has changed from committed 601 to project-owner-observed 607.
- The future intake order should follow the three owner-supplied playlists.
- Before summarizing more videos, the repo should map the playlist order to existing committed video IDs where possible and identify what is missing.
- The plan should use existing committed inventory, availability, priority, and completed-summary docs as the source of truth.
- It should identify the smallest safe reconciliation step for the +6 delta.
- It should not fetch subtitles or summarize videos yet.
- It should not regenerate the entire corpus unless the reconciliation plan later approves it.

This recommendation does not authorize YouTube access, DownSub access, caption fetching, raw transcript commits, Strategy A/B changes, Strategy B2/C, backtests, optimization, market data, or profitability claims.

## 10. Guardrails

Confirmed guardrails for this review:

- No raw transcript, subtitle text, raw TXT, SRT, VTT, or caption URL commits.
- No CSV, JSON, database, `data/`, or `results/` commits.
- No video or audio download.
- No ASR.
- No YouTube or DownSub access in this PR.
- No proxy, VPN, IP rotation, cookies, credentials, rate-limit bypass, platform bypass, or downloader workaround.
- No downloader added.
- No market data.
- No broker, live trading, order execution, or execution logic.
- No Strategy A/B code, parameter, config, or test changes.
- No Strategy B change.
- No Strategy B2 or Strategy C.
- No backtests.
- No optimization.
- No profitability claims.
- No Channel Doctrine Map v1 update.
- No final Channel Doctrine Map v2 creation or update.
- No Batch 08 completion claim.
- The 607-video observation is recorded only as a project-owner-observed current count requiring reconciliation.

## 11. Readiness decision

Decision:

`channel_full_corpus_playlist_led_remaining_input_status_review_ready_for_human_review`

Reason: this docs-only review uses committed inventory, availability, priority, and completed-summary docs to summarize the 601-row baseline, record the 607 owner-observed count as an unresolved reconciliation item, preserve Batch 08 as blocked rather than completed, introduce playlist-led intake as the preferred future direction, and recommend a docs-only `Channel playlist metadata reconciliation plan` before new summaries or subtitle access. It does not access YouTube or DownSub, fetch captions, generate inventory, commit raw artifacts, alter Strategy A/B, update Doctrine Map v1, create final Doctrine Map v2, create Strategy B2/C, run backtests or optimization, access market data, or make profitability claims.
