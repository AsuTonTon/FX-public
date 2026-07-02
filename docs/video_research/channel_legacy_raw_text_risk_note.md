# Channel Legacy Raw Text Risk Note

Task: `channel_local_asr_evidence_policy_and_legacy_raw_text_risk_note`

## 1. Objective and scope

This note documents legacy tracked transcript/subtitle-like files observed during the local ASR evidence policy work.

Scope limits:

- Docs-only risk note.
- The legacy files are documented by path only.
- Their contents are not opened, quoted, summarized, copied, deleted, or modified here.
- No raw transcript, subtitle, ASR, caption URL, audio, video, CSV, JSON, data, result, screenshot, worksheet, hidden mapping, credential, or secret file is added.
- No Strategy A/B code, parameter, test, or configuration is modified.
- No Strategy B2 or Strategy C is created.
- No backtest, optimization, broker/API action, live trading, or profitability claim is made.

## 2. Legacy files observed

The following tracked transcript/subtitle-like files were observed by filename/path only:

- `docs/video_research/vkaA9MCRlx4/raw_transcript.srt`
- `docs/video_research/vkaA9MCRlx4/vkaA9MCRlx4.ja.vtt`
- `docs/video_research/vkaA9MCRlx4/cleaned_transcript.md`

These files predate this policy note. They were not added or modified by the Batch 08 ASR quality gate and are not changed in this PR.

## 3. Why this is a risk under current guardrails

Current corpus-research guardrails prohibit committing raw transcript text, subtitle full text, raw subtitle files, caption URLs, downloaded audio, and downloaded video.

The observed legacy files are risk-relevant because their paths and extensions indicate transcript/subtitle-like content. They may be inconsistent with the current Git-safe evidence practice, which prefers compact derived summaries and timestamp-supported paraphrases rather than raw text artifacts.

This note does not determine whether those files must be removed. It only records that they should be handled explicitly rather than ignored or silently expanded.

## 4. Why this PR does not delete them

This PR does not delete or modify the legacy files because:

- deletion is a separate repository-history and research-continuity decision;
- other existing docs may reference the `vkaA9MCRlx4` evidence package;
- this task is limited to policy documentation, not cleanup;
- changing or deleting legacy artifacts could create review risk outside the ASR policy scope;
- a cleanup decision should identify any replacement Git-safe derived notes before removing legacy evidence files.

## 5. Recommended future cleanup decision

A separate future cleanup PR or policy decision should decide whether to:

- keep the legacy files with an explicit exception note;
- remove the legacy raw transcript/subtitle-like files;
- replace them with Git-safe derived summaries;
- add repository checks that prevent future raw transcript/subtitle additions;
- clarify whether historical exceptions are allowed and under what conditions;
- document any affected downstream references before deletion.

That future decision should not quote or re-commit raw transcript or subtitle text.

## 6. Guardrails

This note preserves the following guardrails:

- no raw transcript text is opened, quoted, copied, added, or modified;
- no ASR full text is opened, quoted, copied, added, or modified;
- no subtitle full text is opened, quoted, copied, added, or modified;
- no raw subtitle file is added;
- no caption URL is added;
- no downloaded audio or video is added;
- no CSV, JSON, data, or result file is added;
- no `data/` or `results/` path is added;
- no screenshot, worksheet, hidden mapping, credential, or secret is added;
- no remote caption fetch is performed;
- no audio or video download is performed;
- no new transcription is run;
- no Batch 08 summary, quality review, or final target set is created;
- no later-batch selection is created;
- no Strategy A/B modification is made;
- no Strategy B2 or Strategy C is created;
- no backtest or optimization is run;
- no profitability claim is made.

## 7. Readiness decision

`ready_for_asr_policy_and_legacy_risk_review`

Reason: the legacy raw transcript/subtitle-like files are documented as a separate cleanup risk without opening, quoting, modifying, deleting, or expanding them in this PR.
