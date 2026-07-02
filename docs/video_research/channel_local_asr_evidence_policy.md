# Channel Local ASR Evidence Policy

Task: `channel_local_asr_evidence_policy_and_legacy_raw_text_risk_note`

## 1. Objective and scope

This note defines how local ASR-derived text discovered during the Batch 08 caption-block investigation may be classified and, if separately approved later, used.

Scope limits:

- Docs-only policy note.
- No raw ASR text is read, quoted, copied, committed, or modified here.
- No raw transcript, subtitle, caption URL, audio, video, CSV, JSON, data, result, screenshot, worksheet, hidden mapping, credential, or secret file is added.
- No remote captions are fetched.
- No audio or video is downloaded.
- No new transcription is run.
- No Batch 08 target set is frozen.
- No Batch 08 summaries or quality review are created.
- No later-batch selection is created.
- No Strategy A/B code, parameter, test, or configuration is modified.
- No Strategy B2 or Strategy C is created.
- No backtest, optimization, broker/API action, live trading, or profitability claim is made.

## 2. Current Batch 08 caption-block status

Remote caption body access remains blocked in the current environment. Metadata-level subtitle availability may be visible, but body retrieval is not currently reliable enough for caption-supported audit.

Current Batch 08 boundary:

| item | status |
| --- | --- |
| remaining high-priority caption-available unsummarized IDs | 56 |
| final Batch 08 target set frozen | no |
| Batch 08 summaries created | no |
| Batch 08 quality review created | no |
| Strategy A/B changed | no |

The merged Batch 08 selection rework remains a blocked selection attempt. A proper Batch 08 selection still requires official caption-supported audit evidence or another separately approved evidence policy.

## 3. Local ASR cache finding

A read-only local ASR cache quality gate found filename matches for 47 of the 56 remaining high-priority caption-available unsummarized IDs.

The local material appears to be ASR-derived from audio transcription. It is not official YouTube caption evidence. It must not be silently mixed with official caption evidence or previously merged timestamp-supported caption summaries.

The quality gate classified the local ASR material as:

`usable_for_low_confidence_topic_routing`

The same gate found ASR usability for Batch 08 selection:

`no`

## 4. Evidence classification

Local ASR-derived text must be classified as:

`local_asr_derived_text_low_confidence`

It must not be classified as:

`caption_supported_evidence`

Policy statements:

- Local ASR-derived text is not official caption evidence.
- Local ASR-derived text is not caption-supported evidence.
- Local ASR-derived text may contain recognition errors, speaker-intent distortion, missing terms, or misleading segmentation.
- Timestamp presence in ASR output does not make the text equivalent to official captions.
- Recognizable FX terms in ASR output do not by themselves establish entry, stop, TP, RR, trade-management, or doctrine evidence.

## 5. Permitted uses

Low-confidence ASR may be used only if a future docs-only policy decision explicitly allows it.

Potentially permitted future uses:

- topic-routing support;
- planning which videos to prioritize after official caption access recovers;
- identifying candidate themes that still require caption-supported confirmation;
- marking a row as worth later audit, without claiming doctrine or mechanical evidence.

Any future use must label the source as `local_asr_derived_text_low_confidence` and keep it separate from `caption_supported_evidence`.

## 6. Disallowed uses

ASR-derived text alone must not be used to:

- freeze a Batch 08 target set;
- create Batch 08 summaries;
- create Batch 08 quality review findings;
- create later-batch selection;
- create doctrine claims;
- create mechanical-rule candidates;
- upgrade confidence above low;
- substitute for official caption-supported audit;
- modify Strategy A/B;
- create Strategy B2 or Strategy C;
- run or justify backtests;
- optimize parameters;
- make profitability claims.

The following must not be committed:

- ASR full text;
- raw transcript text;
- subtitle full text;
- raw subtitle files;
- caption URLs;
- downloaded audio;
- downloaded video;
- CSV, JSON, data, or result artifacts derived from raw ASR text.

## 7. Batch 08 implications

ASR alone does not unblock Batch 08 selection.

Batch 08 remains blocked for final target selection until one of the following happens:

- official caption body access recovers enough to support a proper timestamp-supported audit;
- a separate docs-only policy decision approves a limited ASR-derived triage workflow that does not freeze targets or create summaries;
- another approved Git-safe evidence source becomes available and is explicitly documented before use.

Even if ASR is readable, it cannot make a final Batch 08 target set summary-ready by itself.

## 8. Future decision criteria

Before ASR-derived evidence is used for anything beyond local planning, a separate policy or cleanup PR should decide:

- whether ASR may be used at all in the corpus workflow;
- whether use is limited to topic-routing only;
- what minimum timestamp quality is required;
- how to label ASR-derived observations in ledgers;
- how to prevent ASR from being mixed with official captions;
- how to record uncertainty without quoting raw ASR text;
- how to handle cases where ASR conflicts with official captions after caption access recovers;
- whether any legacy raw text artifacts should be removed or replaced with Git-safe derived notes.

No future policy should authorize ASR as a direct substitute for official caption-supported evidence without explicit review.

## 9. Guardrails

This policy preserves the following guardrails:

- no raw transcript commits;
- no ASR full-text commits;
- no subtitle full-text commits;
- no raw subtitle files;
- no caption URLs;
- no downloaded video or audio;
- no CSV, JSON, data, or result files;
- no `data/` or `results/` additions;
- no screenshots, worksheets, hidden mappings, credentials, or secrets;
- no remote caption fetches;
- no audio or video downloads;
- no new transcription;
- no platform rate-limit or IP-block bypass;
- no requirement for user manual video observation;
- no Batch 08 summaries;
- no Batch 08 quality review;
- no later-batch selection;
- no Strategy A/B modification;
- no Strategy B2 or Strategy C;
- no backtests or optimization;
- no profitability claims.

## 10. Readiness decision

`ready_for_asr_policy_and_legacy_risk_review`

Reason: the ASR cache has been classified as low-confidence local ASR-derived text, its use has been limited to possible future topic-routing or planning only after a separate docs-only decision, and Batch 08 selection remains blocked from ASR alone.
