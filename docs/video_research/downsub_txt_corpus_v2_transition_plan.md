# DownSub TXT Corpus v2 Transition Plan

Task: `downsub_txt_corpus_v2_transition_plan`

## 1. Objective and scope

This document defines a docs-only transition plan for a Corpus v2 workflow that
can use user-provided DownSub TXT files as local comparison and source material
where available.

This plan does not access DownSub, YouTube, captions, audio, video, ASR, market
data, broker systems, or Strategy A/B code. It does not commit raw TXT files,
subtitle full text, caption URLs, CSV, JSON, database, data, or result files.

The goal is to create a safe workflow boundary before any user-provided local
TXT material is used.

## 2. Why this is not a full reset

Corpus v2 is not a reset of the existing channel research line.

Existing Batch 01 through Batch 07 outputs remain useful because they already
contain Git-safe, paraphrased lightweight summaries, aggregate reports, and
quality reviews. They preserve a structured record of what had been reviewed
under the prior caption-supported workflow.

Channel Doctrine Map v1 remains a provisional planning reference. It is not
treated as final doctrine and it is not implementation guidance, but it remains
valuable as a first map of repeated themes and known evidence gaps.

User-provided DownSub TXT material should be used to audit, correct, enrich,
and route the existing corpus work. It should not erase prior work, silently
replace prior source classification, or automatically upgrade any doctrine
claim.

The transition principle is:

```text
keep prior Git-safe summaries -> audit against local TXT where available ->
write paraphrased correction notes -> update doctrine only after review
```

## 3. Source classification

User-provided DownSub TXT files must be classified as:

`user_provided_downsub_txt_local_source`

This source class means:

- The user supplied the TXT files locally.
- Codex did not access DownSub.
- Codex did not access YouTube.
- Codex did not fetch captions.
- Codex did not download audio or video.
- The TXT files are local input material for review, not files to commit.

This source class must not be classified as:

- `official_youtube_caption_evidence`
- `caption_supported_evidence`
- `remote_caption_fetch`
- `asr_generated_by_codex`
- `raw_material_safe_to_commit`

DownSub TXT may reflect YouTube captions or auto-captions, but once provided as
local TXT it should be treated as local user-provided material unless a separate
future policy proves and documents a stronger source classification.

Policy boundary:

- raw TXT files must remain local and uncommitted;
- subtitle full text must not be copied into Git;
- long subtitle quotes must not be added to docs;
- caption URLs must not be added;
- any derived notes must be paraphrased, compact, and Git-safe.

## 4. Corpus v2 workflow

### 4.1 Local TXT inventory

The first Corpus v2 step is a local inventory of user-provided TXT files.

The inventory should record only Git-safe metadata in a future docs-only note,
such as:

- local filename;
- inferred or mapped video ID;
- whether the file is readable;
- whether the file appears to match the expected video;
- whether it is suitable for comparison;
- source class: `user_provided_downsub_txt_local_source`;
- do-not-commit status.

The inventory must not commit:

- TXT file contents;
- subtitle full text;
- long quotes;
- caption URLs;
- CSV, JSON, database, data, or result exports.

### 4.2 Map TXT filenames to video IDs

Before any comparison, each local TXT file should be mapped to a stable
`video_id`.

Preferred mapping signals:

- video ID embedded in filename;
- title plus existing Git-safe metadata match;
- user-provided filename convention;
- manual user confirmation if filename mapping is ambiguous.

Ambiguous mapping should be recorded as `mapping_uncertain` and excluded from
correction work until resolved.

### 4.3 Compare existing completed summaries first

Corpus v2 should start with the already completed Batch 01 through Batch 07
summaries before processing new videos.

Reason:

- completed summaries already have a stable Git-safe structure;
- correction work can reveal whether DownSub TXT quality is sufficient;
- Doctrine Map v1 can remain stable while source quality is tested;
- the workflow can detect systematic summary drift before expanding scope.

Comparison should ask:

- Does the completed summary preserve the core setup context?
- Are entry, stop, TP, RR, timeframe, indicator, and management fields accurate?
- Are missing fields truly unstated, or did the prior summary omit them?
- Are any existing claims too strong relative to the local TXT?
- Are any doctrine-map references affected?

### 4.4 Produce Git-safe paraphrased correction notes

The output of a comparison should be a paraphrased correction note, not raw
subtitle material.

Allowed Git-safe output:

- compact paraphrases;
- timestamp labels when available, without long quoted text;
- correction category;
- affected existing summary path;
- affected doctrine candidate, if any;
- confidence and uncertainty notes;
- source class label.

Disallowed output:

- raw TXT;
- full subtitle text;
- long transcript excerpts;
- caption URLs;
- bulk extracted subtitle tables;
- CSV, JSON, database, data, or result files.

### 4.5 Process unsummarized high-priority videos after audit

Only after the completed-summary audit proves reliable should Corpus v2 process
remaining high-priority unsummarized videos.

The unsummarized workflow should still be conservative:

1. map local TXT to video ID;
2. confirm source classification;
3. create a Git-safe lightweight summary;
4. label the summary as based on `user_provided_downsub_txt_local_source`;
5. avoid raw text, long quotes, caption URLs, and generated data artifacts;
6. run a quality review before using the summary for doctrine updates.

Batch labels may need a separate naming decision so Corpus v2 does not confuse
new local-TXT summaries with prior official-caption-supported batches.

### 4.6 Expand to the full channel corpus later

Full-channel expansion should happen only after:

- the pilot succeeds;
- Batch 01 through Batch 07 audit is complete or materially advanced;
- high-priority unsummarized processing is stable;
- source labels remain consistent;
- raw material boundaries are proven safe;
- project-owner review agrees that Corpus v2 outputs are reliable enough for
  broader doctrine work.

Full-channel expansion must remain separate from Strategy A/B implementation.

## 5. Priority order

### P0: `vkaA9MCRlx4` pilot refinement

Start with the original Strategy A/B source video.

Pilot goals:

- test local DownSub TXT readability;
- verify video ID mapping;
- compare the existing source-video summary and Strategy A/B interpretation;
- identify whether Strategy A/B source assumptions need paraphrased correction
  notes;
- keep all Strategy A/B code and parameters unchanged.

P0 should produce a Git-safe pilot comparison note only after local TXT exists
and can be mapped.

### P1: Batch 01-07 completed-summary audit

Audit completed summaries before adding new corpus scope.

Goals:

- preserve useful existing work;
- identify summary drift;
- correct overstated or understated claims;
- tag corrections by source class;
- keep Doctrine Map v1 provisional until audit findings accumulate.

### P2: Remaining high-priority unsummarized videos

After the completed-summary audit proves the workflow, process remaining
high-priority unsummarized videos where user-provided TXT exists.

Goals:

- fill high-priority evidence gaps;
- avoid Batch 08 remote caption probes;
- avoid title-only, ASR-only, or raw-text-only doctrine claims;
- create Git-safe summaries with explicit local-source classification.

### P3: Doctrine Map v2 candidate update after audit

Doctrine Map v2 should be considered only after enough Corpus v2 audit and
summary work exists.

Doctrine Map v2 candidate updates should:

- preserve Doctrine Map v1 as a historical provisional reference;
- identify which claims are confirmed, weakened, corrected, or split;
- separate official-caption-supported prior evidence from
  `user_provided_downsub_txt_local_source`;
- avoid treating local TXT as implementation guidance.

### P4: Strategy A/B mismatch re-check after Doctrine Map v2, not before

Strategy A/B mismatch should be re-checked only after a reviewed Doctrine Map v2
candidate exists.

This prevents Strategy A/B from changing based on partial pilot findings or
single-video corrections. Any future Strategy A/B review must remain docs-only
unless a separate design memo explicitly authorizes implementation work.

## 6. Guardrails

Confirmed guardrails for Corpus v2 transition:

- no raw TXT commits;
- no full subtitle text commits;
- no long subtitle quotes;
- no caption URLs;
- no DownSub access from Codex;
- no YouTube access from Codex;
- no caption fetches;
- no caption access probes;
- no proxy, VPN rotation, IP rotation, or platform-rate-limit bypass;
- no automated bulk downloading;
- no video downloads;
- no audio downloads;
- no ASR runs;
- no CSV, JSON, database, data, or result files;
- no Strategy A/B code changes;
- no Strategy A/B parameter changes;
- no Strategy A/B config changes;
- no Strategy A/B test changes;
- no Strategy B2;
- no Strategy C;
- no backtests;
- no optimization;
- no broker/API/live-trading/execution work;
- no profitability claims.

## 7. Restart / readiness criteria

Corpus v2 may start only when all of the following are true:

1. A sufficient local TXT inventory exists.
2. TXT filenames can be mapped to video IDs.
3. The first pilot target, `vkaA9MCRlx4`, has a clear local TXT source.
4. The pilot comparison confirms the local TXT is readable enough for review.
5. Correction notes can be written as paraphrased, Git-safe observations.
6. Source classification is recorded as
   `user_provided_downsub_txt_local_source`.
7. Raw TXT files remain local and uncommitted.
8. No workflow step requires Codex to access DownSub, YouTube, captions, audio,
   video, ASR, or platform workarounds.

If these criteria are not met, Corpus v2 should remain in planning status.

## 8. Relationship to Batch 08 blocked status

This plan does not restart Batch 08 under the old remote caption-access model.

The current blocked Batch 08 state remains relevant historical context:

- no final Batch 08 target set is frozen by this plan;
- no Batch 08 summaries are created by this plan;
- no Batch 08 quality review is created by this plan;
- no Batch 09 selection is created by this plan;
- no caption access probe is run by this plan.

Corpus v2 is a separate transition path based on user-provided local TXT files.
It should not be mixed with remote caption recovery probes.

## 9. Git-safe output model

Future Corpus v2 PRs should prefer small, reviewable Markdown outputs:

- transition plans;
- source-classification policy notes;
- pilot comparison notes;
- paraphrased correction notes;
- summary audit notes;
- quality reviews;
- doctrine-map candidate deltas.

Future Corpus v2 PRs should not include:

- raw local TXT;
- copied subtitle full text;
- caption URL dumps;
- generated CSV or JSON ledgers;
- databases;
- local data folders;
- result folders;
- screenshots;
- audio or video.

## 10. Readiness decision

`ready_for_project_owner_review_of_downsub_txt_corpus_v2_transition`

Reason: the workflow has been defined as a non-reset transition that preserves
existing Batch 01 through Batch 07 work, keeps Doctrine Map v1 as a provisional
reference, classifies user-provided DownSub TXT as local uncommitted source
material, and requires Git-safe paraphrased correction notes before any Corpus
v2 expansion or Strategy A/B re-check.
