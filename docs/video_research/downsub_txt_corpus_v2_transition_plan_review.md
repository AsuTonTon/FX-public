# DownSub TXT Corpus v2 Transition Plan Review

Task: `downsub_txt_corpus_v2_transition_plan_review`

## 1. Objective and scope

This review verifies the docs-only DownSub TXT Corpus v2 transition-plan PR.

Reviewed file:

- `docs/video_research/downsub_txt_corpus_v2_transition_plan.md`

This review does not inspect or use any raw DownSub TXT files. It does not
access DownSub, YouTube, captions, audio, video, ASR, market data, broker
systems, or Strategy A/B code.

## 2. Files added by this PR

This PR adds exactly two Markdown planning/review files:

- `docs/video_research/downsub_txt_corpus_v2_transition_plan.md`
- `docs/video_research/downsub_txt_corpus_v2_transition_plan_review.md`

No raw local source file is added.

## 3. Required-content review

| Requirement | Review result |
| --- | --- |
| Explains why Corpus v2 is not a full reset | pass |
| Preserves Batch 01-07 usefulness | pass |
| Keeps Doctrine Map v1 as provisional reference | pass |
| States DownSub TXT audits/enriches rather than erases prior work | pass |
| Defines `user_provided_downsub_txt_local_source` | pass |
| States this is not official YouTube caption evidence | pass |
| States raw TXT must not be committed | pass |
| Defines local TXT inventory step | pass |
| Defines filename-to-video-ID mapping step | pass |
| Compares completed summaries first | pass |
| Requires Git-safe paraphrased correction notes | pass |
| Processes unsummarized high-priority videos only later | pass |
| Expands to full channel corpus only later | pass |
| Defines P0 through P4 priority order | pass |
| Includes restart/readiness criteria | pass |
| Confirms guardrails | pass |

## 4. Prohibited-artifact verification

| Prohibited item | Added? | Review note |
| --- | --- | --- |
| raw TXT files | no | No `.txt` files are added. |
| subtitle full text | no | The docs contain policy language only. |
| long subtitle quotes | no | No subtitle passages are quoted. |
| caption URLs | no | No caption URLs are added. |
| video files | no | No media files are added. |
| audio files | no | No media files are added. |
| screenshots | no | No image files are added. |
| CSV files | no | No CSV files are added. |
| JSON files | no | No JSON files are added. |
| database files | no | No database files are added. |
| data files | no | No `data/` material is added. |
| result files | no | No `results/` material is added. |
| credentials or secrets | no | No credential-bearing file is added. |

## 5. Workflow-action verification

| Prohibited action | Performed? | Review note |
| --- | --- | --- |
| DownSub access | no | The plan was written without accessing DownSub. |
| YouTube access | no | No YouTube access was performed. |
| caption fetch | no | No captions were fetched. |
| caption access probe | no | No probe was run. |
| proxy / VPN / IP rotation / bypass | no | No platform workaround was used. |
| video download | no | No video was downloaded. |
| audio download | no | No audio was downloaded. |
| ASR run | no | No transcription or ASR was run. |
| automated bulk downloading | no | No download workflow was created or run. |
| market-data fetch | no | No market data was fetched. |
| broker/API/live trading | no | No trading integration was touched. |
| backtest | no | No backtest was run. |
| optimization | no | No parameter optimization was run. |

## 6. Strategy A/B boundary verification

| Strategy boundary | Changed? | Review note |
| --- | --- | --- |
| Strategy A code | no | No `src/` Strategy A file changed. |
| Strategy B code | no | No `src/` Strategy B file changed. |
| parameters | no | No parameter file or value changed. |
| configs | no | No config file changed. |
| tests | no | No test file changed. |
| Strategy B2 | no | No Strategy B2 was created. |
| Strategy C | no | No Strategy C was created. |
| profitability claim | no | The plan does not claim profitability. |

## 7. Source-classification review

The plan correctly classifies user-provided DownSub TXT as:

`user_provided_downsub_txt_local_source`

The plan explicitly says this class is not:

- `official_youtube_caption_evidence`
- `caption_supported_evidence`
- `remote_caption_fetch`
- `asr_generated_by_codex`
- `raw_material_safe_to_commit`

This preserves separation between local user-provided material and the prior
caption-supported evidence model.

## 8. Readiness review

The plan does not declare Corpus v2 operational immediately. It requires:

- sufficient local TXT inventory;
- filename-to-video-ID mapping;
- a `vkaA9MCRlx4` pilot;
- readable local source quality;
- paraphrased Git-safe correction notes;
- recorded source classification;
- raw TXT remaining local and uncommitted;
- no Codex access to DownSub, YouTube, captions, audio, video, ASR, or platform
  workarounds.

This is an appropriate readiness gate.

## 9. Review conclusion

`review_passed_for_downsub_txt_corpus_v2_transition_plan`

Reason: the added transition plan is docs-only, keeps raw local TXT and subtitle
text out of Git, preserves the existing Batch 01 through Batch 07 and Doctrine
Map v1 work, defines a conservative source classification, and does not modify
Strategy A/B or create any trading, data-generation, transcript, caption, media,
backtest, optimization, or profitability artifact.
