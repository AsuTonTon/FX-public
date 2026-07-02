# vkaA9MCRlx4 DownSub TXT Comparison Pilot Review

Task: `vkaA9MCRlx4_downsub_txt_comparison_pilot_review`

## 1. Objective and scope

This review checks the P0 DownSub TXT comparison pilot for `vkaA9MCRlx4`.

Reviewed files:

- `docs/video_research/lightweight_summaries/batch_01/vkaA9MCRlx4.md`
- `docs/video_research/vkaA9MCRlx4_downsub_txt_comparison_pilot.md`
- `docs/video_research/vkaA9MCRlx4_downsub_txt_comparison_pilot_review.md`

The review verifies repository hygiene and guardrails. It does not inspect,
quote, commit, or reproduce raw TXT content.

## 2. Prohibited artifact check

| Item | Added? | Review note |
| --- | --- | --- |
| TXT file | no | No `.txt` file is added to Git. |
| raw subtitle text | no | Added docs contain paraphrased notes only. |
| long subtitle quotes | no | No long subtitle passage is quoted. |
| caption URL | no | No caption URL is added. |
| video file | no | No video file is added. |
| audio file | no | No audio file is added. |
| screenshot | no | No image or screenshot is added. |
| CSV file | no | No CSV file is added. |
| JSON file | no | No JSON file is added. |
| database file | no | No database file is added. |
| data artifact | no | No `data/` artifact is added to Git. |
| result artifact | no | No `results/` artifact is added to Git. |
| credential or secret | no | No credential-bearing file is added. |

## 3. Prohibited action check

| Action | Performed? | Review note |
| --- | --- | --- |
| DownSub access | no | No DownSub access was performed. |
| YouTube access | no | No YouTube access was performed. |
| caption fetch | no | No captions were fetched. |
| caption probe | no | No caption access probe was run. |
| proxy / VPN / IP rotation / bypass | no | No platform workaround was used. |
| video download | no | No video was downloaded. |
| audio download | no | No audio was downloaded. |
| ASR run | no | No transcription or ASR was run. |
| CSV/JSON/database generation | no | No generated data file was created. |
| backtest | no | No backtest was run. |
| optimization | no | No parameter optimization was run. |

## 4. Doctrine and Strategy boundary check

| Boundary | Changed? | Review note |
| --- | --- | --- |
| Channel Doctrine Map v1 | no | No doctrine map file is changed. |
| Strategy A code | no | No `src/` Strategy A file is changed. |
| Strategy B code | no | No `src/` Strategy B file is changed. |
| Strategy parameters | no | No parameter file or value is changed. |
| Strategy configs | no | No config file is changed. |
| Strategy tests | no | No test file is changed. |
| Strategy B2 | no | No Strategy B2 is created. |
| Strategy C | no | No Strategy C is created. |
| profitability claim | no | No profitability claim is made. |

## 5. Summary update review

The existing summary was updated only to clarify or correct method
interpretation from the local comparison:

- 4H 20EMA / 200EMA setup;
- first valid 20EMA-touch setup after the cross;
- touch may be wick or body;
- reference candle high/low body-close confirmation;
- wick-only break insufficiency;
- opposite EMA cross before confirmation as no-entry;
- skip conditions for poor RR, no visible left-side TP target, range, low
  volatility, and double bottom / double top against direction;
- basic pullback stop and discretionary stop widening;
- visible left-side TP targets, staged exits, full exit at one clear target,
  and discretionary post-TP1 management;
- unresolved questions around visual and discretionary elements.

The update does not create a mechanical implementation rule.

## 6. Source-classification review

The comparison note classifies the local source as:

`user_provided_downsub_txt_local_source`

It explicitly does not classify the source as:

- `official_youtube_caption_evidence`
- `caption_supported_evidence`
- `remote_caption_fetch`
- `raw_material_safe_to_commit`

This matches the Corpus v2 transition plan boundary.

## 7. Review conclusion

`review_passed_for_vkaA9MCRlx4_downsub_txt_comparison_pilot`

Reason: the pilot updates one existing Git-safe summary and adds two Git-safe
Markdown notes while keeping raw TXT, subtitle text, caption URLs, media,
generated data artifacts, Strategy A/B changes, Doctrine Map updates, backtests,
optimization, and profitability claims out of scope.
