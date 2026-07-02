# Channel Legacy Raw Text Reference Audit

Task: `channel_legacy_raw_text_cleanup_decision`

## 1. Objective and scope

This document audits references to legacy tracked transcript/subtitle-like files by filename/path only.

Scope limits:

- Search is limited to exact legacy filenames and paths.
- Legacy raw transcript/subtitle-like file contents are not opened, quoted, summarized, copied, modified, or deleted.
- This audit does not fetch captions, call YouTube, download audio/video, run transcription, create Batch 08 summaries, create Batch 09 selection, modify Strategy A/B, create Strategy B2 or Strategy C, run backtests, optimize, or make profitability claims.

## 2. Search method

The repository was searched for exact legacy filenames and paths:

- `docs/video_research/vkaA9MCRlx4/raw_transcript.srt`
- `docs/video_research/vkaA9MCRlx4/vkaA9MCRlx4.ja.vtt`
- `docs/video_research/vkaA9MCRlx4/cleaned_transcript.md`
- `raw_transcript.srt`
- `vkaA9MCRlx4.ja.vtt`
- `cleaned_transcript.md`

The search explicitly excluded the three legacy files themselves so their raw contents were not opened.

## 3. Legacy path references found

| referencing file | referenced legacy item | reference type | apparent dependency |
| --- | --- | --- | --- |
| `docs/video_research/channel_legacy_raw_text_risk_note.md` | `docs/video_research/vkaA9MCRlx4/raw_transcript.srt` | path-only risk documentation | Documents the legacy risk; does not appear to require raw content. |
| `docs/video_research/channel_legacy_raw_text_risk_note.md` | `docs/video_research/vkaA9MCRlx4/vkaA9MCRlx4.ja.vtt` | path-only risk documentation | Documents the legacy risk; does not appear to require raw content. |
| `docs/video_research/channel_legacy_raw_text_risk_note.md` | `docs/video_research/vkaA9MCRlx4/cleaned_transcript.md` | path-only risk documentation | Documents the legacy risk; does not appear to require raw content. |
| `docs/video_research/vkaA9MCRlx4/source_metadata.json` | `vkaA9MCRlx4.ja.vtt` | filename metadata | Records a stored subtitle filename; may need path-only update if the legacy file is deleted. |
| `docs/video_research/vkaA9MCRlx4/source_metadata.json` | `raw_transcript.srt` | filename metadata | Records a derived SRT filename; may need path-only update if the legacy file is deleted. |

No separate reference to `cleaned_transcript.md` was found outside the legacy risk note during this path-only audit.

## 4. Downstream dependency assessment

The references found are path-only or filename-only. This audit did not find a Git-safe doc that appears to require the raw transcript/subtitle contents themselves.

Known dependency considerations:

- `channel_legacy_raw_text_risk_note.md` depends only on documenting the existence of legacy risk paths.
- `source_metadata.json` appears to record source-package filenames and may need an update or replacement metadata policy if the legacy files are deleted later.
- Deleting the legacy files without touching `source_metadata.json` could leave stale metadata references.
- A future cleanup PR should decide whether to update metadata, add a path-only historical note, or replace raw-file references with Git-safe derived-source labels.

## 5. Cleanup risk assessment

Cleanup risk is moderate, not because content dependency was found, but because one metadata file records legacy filenames.

Risks to handle in a future cleanup PR:

- stale filename metadata after deletion;
- accidental raw-content inspection while preparing replacement notes;
- accidentally treating historical raw files as a precedent for future raw transcript/subtitle commits;
- mixing cleanup work with Batch 08 selection or Strategy A/B work;
- deleting files before reviewers agree on replacement evidence policy.

## 6. Recommended future cleanup PR

Recommended future cleanup PR scope:

- delete the three reviewed legacy raw transcript/subtitle-like files, if cleanup is approved;
- update or annotate filename metadata references without adding raw text;
- add Git-safe derived replacement notes only if existing docs need them;
- keep any replacement note compact and paraphrased;
- update guardrails/checks to prevent future raw transcript/subtitle additions;
- report that no Batch 08 target set, Batch 08 summaries, Batch 09 selection, Strategy A/B changes, Strategy B2, Strategy C, backtests, optimization, or profitability claims were created.

This PR should remain separate from that future cleanup PR.

## 7. Guardrails

This audit preserves these guardrails:

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

## 8. Readiness decision

`ready_for_legacy_raw_text_cleanup_review`

Reason: legacy references have been audited by filename/path only, downstream risk is identified, and the future cleanup PR scope is defined without opening, quoting, modifying, or deleting legacy raw transcript/subtitle-like files.
