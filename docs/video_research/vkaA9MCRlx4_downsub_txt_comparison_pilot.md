# vkaA9MCRlx4 DownSub TXT Comparison Pilot

Task: `vkaA9MCRlx4_downsub_txt_comparison_pilot`

## 1. Objective and scope

This is the P0 pilot comparison for Corpus v2.

Pilot target:

- video_id: `vkaA9MCRlx4`
- source title: `【聖杯級】4時間足3波を確実に取るためのEMA戦略`
- existing summary: `docs/video_research/lightweight_summaries/batch_01/vkaA9MCRlx4.md`

The pilot compares the existing Git-safe Batch 01 summary against a
user-provided local DownSub TXT file. The comparison is used only to refine the
existing summary and test the Corpus v2 workflow.

This note is paraphrased only. It does not commit raw TXT, copy subtitle full
text, quote long subtitle passages, add caption URLs, access DownSub, access
YouTube, fetch captions, run ASR, download audio, download video, create data
artifacts, update Doctrine Map v1, modify Strategy A/B code, or make
profitability claims.

## 2. Source classification

The local TXT is classified as:

`user_provided_downsub_txt_local_source`

It is not classified as:

- `official_youtube_caption_evidence`
- `caption_supported_evidence`
- `remote_caption_fetch`
- `raw_material_safe_to_commit`

The local TXT was used only for comparison. It remains local input material and
is not committed to the repository.

## 3. Comparison method

The pilot used the following Git-safe comparison method:

1. Read the existing lightweight summary.
2. Read the user-provided local TXT as local source material.
3. Compare only the method-relevant topics: EMA setup, first-touch scope,
   entry confirmation, skip conditions, stop logic, TP / exit logic, and
   unresolved discretionary elements.
4. Update the existing summary only where the local TXT clearly clarified or
   corrected the current summary.
5. Write this note as paraphrased evidence handling, without raw subtitle text.

No remote collection or platform access was used.

## 4. What the existing summary already captured correctly

The existing summary already captured the main shape of the method:

- The setup is a 4H third-wave attempt.
- EMA or moving-average context is part of the setup.
- Immediate touch entries are avoided.
- Confirmation is required before entry.
- Opposite cross before confirmation is a no-entry condition.
- Stop placement relates to a recent pullback high or low.
- TP uses visible left-side swing levels.
- Split exits can be considered between visible targets.
- RR is assessed contextually rather than as a universal fixed threshold.
- TP and stop choices retain visual judgment.

The pilot did not overturn those points.

## 5. What the local TXT clarified

The local TXT clarified several points that were either compressed or
under-specified in the existing summary:

- The EMA setup is explicitly a 4H chart with 20EMA and 200EMA.
- The method waits for a golden cross or dead cross before looking for the
  pullback setup.
- Only the first valid 20EMA-touch setup after that cross belongs to this
  method.
- Later 20EMA touches after the same cross are not valid method entries.
- The 20EMA touch may be made by the candle body or by the wick.
- The touch candle becomes the reference candle.
- Long entry requires a body-close break of the reference candle high.
- Short entry requires a body-close break of the reference candle low.
- A wick-only break is insufficient.
- Opposite EMA cross before confirmation means no-entry.
- Poor RR at the initial trigger can justify skipping that trigger.
- No realistic visible left-side TP target is a no-entry reason.
- Directionless range and low-volatility range are skip contexts.
- Double bottom or double top against the intended trade direction is a skip
  or caution context.
- Stop widening may be considered only when RR remains sufficiently favorable.
- Post-TP1 management remains discretionary.

## 6. What was corrected or enriched

The existing summary was enriched in these areas:

- Metadata now records the Corpus v2 pilot source class.
- Main claim now states 20EMA / 200EMA rather than generic EMA or moving
  average context.
- Setup/context now records first-touch-only scope after the EMA cross.
- Entry logic now separates touch, reference candle, body-close confirmation,
  wick-only insufficiency, and opposite-cross skip.
- Stop logic now distinguishes the basic pullback stop from discretionary
  stop widening.
- TP / exit logic now separates staged exits, full exit at one clear target,
  no-entry when no realistic target exists, and discretionary post-TP1
  management.
- Trend/range filters now include directionless range, low-volatility range,
  and double bottom / double top caution.
- Unresolved questions now remove the prior uncertainty around exact EMA
  parameters and keep the remaining visual-context blockers.

These changes are summary refinements only.

## 7. What remains discretionary

The local TXT does not make the following items fully mechanical:

- whether the current wave is a valid third-wave attempt;
- which visible left-side swing target is the correct first target;
- when a nearby target is realistic enough;
- how to classify directionless range;
- how to classify low-volatility range;
- how to mechanically detect a relevant double bottom or double top;
- how much stop widening is acceptable;
- when to hold after TP1 versus exit early;
- when a later confirmation candle offers acceptable RR after an initial poor
  RR trigger.

These remain visual or discretionary interpretation questions.

## 8. What remains not mechanical-ready

The pilot does not create a backtest-ready rule for:

- range definition;
- low-volatility definition;
- double bottom / double top detection;
- target realism scoring;
- swing-target priority;
- stop-widening tolerance;
- post-TP1 management;
- contextual RR thresholds.

Any future mechanical design would need a separate docs-only design memo before
implementation.

## 9. Why Channel Doctrine Map v1 is not updated from this pilot alone

Channel Doctrine Map v1 is a provisional corpus-level reference based on the
completed Git-safe summary set. A single local TXT pilot should not update a
corpus doctrine map by itself.

Reasons:

- This pilot covers one already summarized source video.
- The source class is local user-provided TXT, not official YouTube caption
  evidence.
- The pilot is meant to test the Corpus v2 correction workflow.
- Corpus-level claims should wait for a broader completed-summary audit and
  quality review.
- Doctrine Map v2 should only be considered after enough Corpus v2 audit
  evidence exists.

## 10. Why Strategy A/B is not modified from this pilot alone

Strategy A/B is not modified from this pilot.

Reasons:

- The pilot is docs-only.
- The local TXT clarifies the summary but does not authorize code changes.
- Strategy B TP1, stop-anchor, RR, ADX, and Strategy B2 status remain frozen by
  the existing decision cycle.
- Several clarified elements remain discretionary and not mechanical-ready.
- No backtest, optimization, or live-trading implication follows from this
  comparison.

Any future Strategy A/B change would require a separate design memo after
broader Corpus v2 review.

## 11. Guardrails confirmation

Confirmed:

- docs-only P0 comparison pilot;
- local TXT treated as `user_provided_downsub_txt_local_source`;
- local TXT used only for comparison;
- no TXT file added;
- no raw subtitle text added;
- no long subtitle quotes added;
- no caption URL added;
- no DownSub access;
- no YouTube access;
- no caption fetch or probe;
- no proxy, VPN rotation, IP rotation, or platform-rate-limit bypass;
- no audio or video download;
- no ASR run;
- no CSV, JSON, database, data, or result artifact added;
- no Doctrine Map v1 update;
- no Strategy A/B code, parameter, config, or test changes;
- no Strategy B2 or Strategy C;
- no backtest or optimization;
- no profitability claim.

## 12. Readiness decision

`ready_for_review_as_p0_downsub_txt_pilot_refinement`

Reason: the existing `vkaA9MCRlx4` summary was refined using only local
user-provided DownSub TXT material, with raw TXT kept out of Git and all
clarifications recorded as paraphrased Git-safe notes. The pilot is sufficient
to review the Corpus v2 workflow, but not sufficient to update Doctrine Map v1
or modify Strategy A/B.
