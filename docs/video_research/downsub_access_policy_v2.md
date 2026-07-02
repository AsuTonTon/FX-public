# DownSub Access Policy v2

## 1. Objective and Scope

This document defines the policy for bounded Codex-accessed DownSub use in the FX video-research workflow.

The policy exists to make any future DownSub use explicit, bounded, documented, and reviewable. It does not authorize unrestricted full-channel automated downloading, Strategy A/B changes, Doctrine Map updates by itself, Strategy B2 or Strategy C creation, backtests, optimization, or profitability claims.

This policy applies only to derived subtitle comparison and audit work where the project owner has approved a specific bounded batch or explicit video ID set.

## 2. Relationship to the Prior Corpus v2 Plan

PR #64 defined a local-only Corpus v2 transition plan. Under that plan, subtitle-derived work was expected to use local materials rather than Codex-initiated third-party subtitle access.

PR #66 introduced a documented source-handling exception: Codex accessed DownSub for a bounded Batch 01 completed-summary audit and documented that access in the audit report and PR body.

This v2 policy reconciles those two states. The default Corpus v2 posture remains local-only unless the project owner explicitly approves a bounded exception. When an exception is approved, DownSub access must be classified honestly, limited to the approved batch or video IDs, and reported in the PR and related report.

## 3. Source Classifications

| classification | applies when | reporting requirement |
| --- | --- | --- |
| `user_provided_downsub_txt_local_source` | The project owner provides local DownSub TXT material and Codex does not access DownSub for the task. | State that the material was user-provided and local-only for this task. |
| `codex_accessed_downsub_third_party_subtitle_source` | Codex directly accesses DownSub as a third-party subtitle source for approved bounded work. | State that Codex accessed DownSub and identify the approved batch or video IDs. |
| `downsub_accessed_by_codex_for_caption_derivative_review` | Codex uses DownSub-derived material only for subtitle-derived comparison, audit, correction, or review. | State that the output is paraphrased and Git-safe, and that raw subtitle material and caption URLs were not committed. |

Multiple classifications may be used together when appropriate. For example, a bounded audit may use both `codex_accessed_downsub_third_party_subtitle_source` and `downsub_accessed_by_codex_for_caption_derivative_review`.

## 4. Allowed Bounded Use

DownSub access is allowed only when all of the following are true:

- The project owner explicitly approves the bounded batch or exact video ID set.
- The work is limited to the approved batch or video IDs.
- The purpose is subtitle-derived comparison, completed-summary audit, quality review, or correction-note preparation.
- The committed output is limited to Git-safe paraphrased summaries, audits, correction notes, policy documents, or review documents.
- No raw TXT, SRT, VTT, subtitle full text, caption URLs, video, audio, generated datasets, or result artifacts are committed.
- No automated downloader is added to the repository.
- No Strategy A/B files are changed.
- No Doctrine Map update is made unless separately authorized after corpus-level review.

## 5. Disallowed Use

The following uses are not allowed under this policy:

- Unrestricted full-channel automation.
- Open-ended scraping.
- Proxy, VPN, IP rotation, platform-rate-limit bypass, or other platform bypass attempts.
- Committing an automated downloader to the repository.
- Committing raw TXT, SRT, VTT, subtitle full text, or caption URL dumps.
- Downloading video or audio.
- Running ASR.
- Producing or committing market data, broker data, live-trading artifacts, CSV, JSON, database, `data/`, or `results/` artifacts.
- Changing Strategy A/B code, parameters, configs, or tests.
- Creating Strategy B2 or Strategy C.
- Running backtests or optimization.
- Making profitability claims.
- Updating Channel Doctrine Map v1 from a DownSub-accessed batch alone.

## 6. Approval Model

Future DownSub access requires explicit project-owner approval per bounded batch.

Approval must name the batch or exact video ID set. The approval must be recorded in the PR body and in the related report. The evidence/source handling must describe whether Codex accessed DownSub and must use the applicable source classification.

If approval is ambiguous, absent, or broader than a bounded batch or exact video ID set, Codex must not access DownSub.

## 7. Required PR Reporting

Every future PR that involves Codex-accessed DownSub material must report:

- Whether Codex accessed DownSub.
- The exact source classification.
- The target batch or video IDs.
- Whether raw TXT, SRT, or VTT was committed.
- Whether subtitle full text was committed.
- Whether caption URLs were committed.
- Whether audio or video was downloaded.
- Whether ASR was run.
- Whether proxy, VPN, IP rotation, or platform-rate-limit bypass was used.
- Whether an automated downloader was committed.
- Whether Doctrine Map v1 was changed.
- Whether Strategy A/B code, parameters, configs, or tests were changed.
- Whether Strategy B2 or Strategy C was created.
- Whether backtests, optimization, or profitability analysis were performed.

## 8. Required Guardrails

The required guardrails for any future approved DownSub-accessed work are:

- Git-safe paraphrase only.
- No raw subtitle text commits.
- No caption URL commits.
- No video or audio downloads.
- No ASR.
- No proxy, VPN, IP rotation, or platform bypass.
- No committed downloader.
- No `data/`, `results/`, CSV, JSON, database, or generated artifact commits.
- No Strategy A/B change.
- No Doctrine Map change unless separately authorized after corpus-level review.
- No backtest, optimization, or profitability claim.

## 9. Future Workflow

Batch 02 can proceed only after this policy is merged.

Batch 02 should be a bounded audit similar to Batch 01. It should name its target batch or exact video ID set, use the required source classification, and keep the committed output limited to Git-safe paraphrased documentation.

Batch 02 should not update Doctrine Map v1 or Strategy A/B. Any later doctrine or strategy work must be separately authorized after broader corpus-level review.

## 10. Readiness Decision

`downsub_access_policy_v2_ready_for_review`

Reason: this policy documents how future Codex-accessed DownSub use must be approved, classified, bounded, and reported. It preserves the local-only Corpus v2 default while allowing explicit, project-owner-approved exceptions for bounded batch audits. It does not authorize unrestricted automation, raw subtitle commits, Doctrine Map updates, Strategy A/B changes, backtests, optimization, or profitability claims.
