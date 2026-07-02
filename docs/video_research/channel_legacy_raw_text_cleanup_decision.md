# Channel Legacy Raw Text Cleanup Decision

Task: `channel_legacy_raw_text_cleanup_decision`

## 1. Objective and scope

This document records a docs-only cleanup decision for legacy tracked transcript/subtitle-like files identified during the local ASR evidence policy work.

Scope limits:

- No legacy raw transcript/subtitle-like file is opened, quoted, copied, summarized, modified, or deleted in this PR.
- No caption, subtitle, ASR, audio, or video access is performed.
- No raw transcript, ASR full text, subtitle full text, raw subtitle file, caption URL, audio file, video file, CSV, JSON, data file, result file, screenshot, worksheet, hidden mapping, credential, or secret is added.
- No Batch 08 summary, Batch 08 quality review, Batch 09 selection, Strategy A/B change, Strategy B2, Strategy C, backtest, optimization, or profitability claim is created.

This decision prepares a future cleanup path. It does not execute cleanup.

## 2. Legacy files under review

The legacy tracked transcript/subtitle-like files under review are:

- `docs/video_research/vkaA9MCRlx4/raw_transcript.srt`
- `docs/video_research/vkaA9MCRlx4/vkaA9MCRlx4.ja.vtt`
- `docs/video_research/vkaA9MCRlx4/cleaned_transcript.md`

These files predate this PR. They are documented by path only here.

## 3. Current guardrail conflict

Current channel research guardrails prohibit adding or expanding raw transcript text, ASR full text, subtitle full text, raw subtitle files, caption URLs, downloaded audio, downloaded video, CSV/JSON/data/result artifacts, screenshots, worksheets, hidden mappings, credentials, or secrets.

The legacy files are risk-relevant because their names and extensions indicate raw transcript/subtitle-like artifacts. That does not mean this PR has inspected their contents. It means the repository should make an explicit cleanup decision instead of letting historical exceptions become a precedent for new raw-text commits.

## 4. Why immediate deletion is not done in this PR

Immediate deletion is not done here because:

- this task is a docs-only decision, not a cleanup execution PR;
- downstream references should be mapped by filename/path before deletion;
- replacement Git-safe derived notes may be needed before removing historical files;
- deleting evidence artifacts without a separate review could disrupt existing research docs;
- cleanup should be staged so reviewers can separate policy agreement from file removal.

## 5. Cleanup options

Available cleanup options:

| option | description | main tradeoff |
| --- | --- | --- |
| Keep legacy files with explicit historical exception | Preserve the existing files and document that they are a non-repeatable historical exception. | Avoids disruption but leaves raw-text-like artifacts in Git history and weakens guardrail clarity. |
| Delete legacy raw transcript/subtitle-like files | Remove the tracked legacy files in a cleanup PR. | Aligns with current guardrails but requires reference mapping and replacement notes if docs depend on them. |
| Replace legacy raw text with Git-safe derived summaries | Create compact derived notes, then delete raw-text-like files. | Preserves research continuity while reducing raw-text exposure, but requires careful non-quoting replacement work. |
| Add checks to prevent future raw transcript/subtitle additions | Add or update repository guardrails or review checks. | Helps prevent recurrence, but should not silently rewrite historical files. |
| Defer cleanup until downstream references are mapped | Wait until all filename/path dependencies are clear. | Lowest immediate risk, but leaves the known issue unresolved. |

## 6. Recommended cleanup path

Recommended conservative future cleanup path:

1. Audit references to the legacy paths by filename/path only.
2. Confirm whether existing docs or metadata depend on those files.
3. Prepare Git-safe replacement notes if needed, without quoting raw transcript/subtitle content.
4. Delete legacy raw transcript/subtitle-like files in a separate cleanup PR.
5. Add or update guardrails/checks to prevent reintroduction.

This PR performs only the first decision step. It does not delete files.

## 7. Replacement evidence policy

If replacement evidence notes are needed, they should follow these rules:

- use compact derived summaries only;
- avoid raw transcript or subtitle text;
- avoid ASR full text;
- avoid caption URLs;
- avoid raw subtitle files;
- identify source type and confidence level;
- distinguish official caption-supported evidence from local ASR-derived text;
- mark ASR-derived material as low-confidence if it is used under a separately approved policy;
- preserve enough path-level provenance for audit without reintroducing raw text.

Replacement notes should not be used to create Strategy A/B changes, Strategy B2, Strategy C, backtests, optimization, or profitability claims.

## 8. Future cleanup PR requirements

A future cleanup PR should report:

- exact legacy files removed or retained;
- downstream references found by filename/path;
- whether replacement Git-safe notes were added;
- whether raw content was opened;
- whether raw transcript/subtitle/caption/ASR/audio/video files were added or modified;
- whether repository guardrails or checks were updated;
- confirmation that no Batch 08 target set, Batch 08 summaries, Batch 09 selection, or Strategy A/B changes were created;
- confirmation that `git diff --check` passed.

If deletion is chosen, the PR should delete only the reviewed legacy files and any directly necessary path-only references. It should not broaden into corpus selection, summarization, or strategy work.

## 9. Guardrails

This decision preserves these guardrails:

- no raw transcript content opened, quoted, copied, summarized, added, modified, or deleted;
- no ASR full text opened, quoted, copied, summarized, added, or modified;
- no subtitle full text opened, quoted, copied, summarized, added, modified, or deleted;
- no raw subtitle file added or modified;
- no caption URL added;
- no downloaded audio or video added;
- no CSV, JSON, data, or result file added;
- no `data/` or `results/` addition;
- no screenshot, worksheet, hidden mapping, credential, or secret added;
- no remote caption fetch;
- no YouTube call;
- no audio/video download;
- no new transcription;
- no user manual video-observation requirement;
- no platform rate-limit or IP-block bypass;
- no Batch 08 summaries or quality review;
- no later-batch selection;
- no Strategy A/B modification;
- no Strategy B2 or Strategy C;
- no backtest or optimization;
- no profitability claim.

## 10. Readiness decision

`ready_for_legacy_raw_text_cleanup_review`

Reason: the cleanup options and conservative future path are documented without opening, quoting, modifying, deleting, or expanding the legacy raw transcript/subtitle-like files.
