# Playlist-Led Intermediate Batch 03 Summary: UnRs896Utnc

Task: `channel_playlist_led_intermediate_batch_03_youtube_caption_summary`

## 1. Metadata

| field | value |
| --- | --- |
| video ID | `UnRs896Utnc` |
| playlist label | `FX中級者のための勝率UP講座` |
| playlist order | 17 |
| compact title | 【永久保存版】チャートパターンの全てがわかる完全講義 |
| source classification | `codex_accessed_youtube_auto_caption_source`; `youtube_auto_caption_accessed_by_codex_for_caption_derivative_review` |
| access status | `caption_body_available` |
| raw subtitle text | not included |

The compact title is retained only as source metadata and is not a project completeness claim.

## 2. Compact Paraphrased Lesson Summary

This lesson narrows the topic to the chart patterns the speaker says are actually used in practice, then ties each pattern to entry timing, stop placement, and context. The early examples focus on double tops and bottoms, where the entry is not just the pattern label itself but the neckline break, one-bar confirmation, or a return-move confirmation after the break. The stop is anchored around the second swing point, while profit handling depends on structure strength and may be shortened if the broader evidence is weak.

The later emphasis is that pattern naming is not enough. Neckline selection can be ambiguous, diagonal and horizontal candidates can coexist, and a trader may need to wait for a return move when multiple reasonable necklines are visible. The video also argues that pattern location matters more than pattern presence. A triangle or similar continuation pattern can deserve different treatment depending on whether it appears inside a strong uptrend, in weak context, or in a structurally messy area.

## 3. Trading Concept Notes

- Double-top and double-bottom entries are tied to neckline logic, not to touching the second pivot alone.
- Return-move confirmation is presented as an important fallback when neckline choice is unclear.
- Stop placement is tied to the second pivot rather than arbitrary distance.
- Entry timing is treated as a sequence: identify the relevant break, then judge whether the post-break structure is usable.
- Pattern location and surrounding market state matter more than memorizing many pattern names.
- Horizontal and diagonal candidate lines can coexist, so ambiguity handling matters.

## 4. Mechanical-Rule Candidate Observations

| candidate ID | setup context | condition | action | invalidation or risk note | automation readiness | uncertainty notes |
| --- | --- | --- | --- | --- | --- | --- |
| `I03_UnRs896Utnc_C01_double_pattern_second_pivot_stop` | Double bottom or double top. | The pattern is accepted and the neckline logic is valid. | Place the default stop slightly beyond the second pivot. | Poor pattern quality can still make the stop placement insufficient. | `mechanical_candidate` | The stop anchor is clear, but buffer size remains undefined. |
| `I03_UnRs896Utnc_C02_neckline_break_or_return_move_gate` | Pattern breakout entry. | A valid neckline break appears. | Enter on confirmed break or on the return move if that is the cleaner confirmation. | Jumping before confirmation can worsen reward/risk or increase false breaks. | `needs_visual_discretion` | The caption supports the logic, but not a precise candle rule for every case. |
| `I03_UnRs896Utnc_C03_ambiguous_neckline_wait_filter` | Multiple plausible necklines. | Horizontal and diagonal neckline candidates both look usable. | Delay entry and wait for the return move or clearer structure rather than guessing which neckline is primary. | Early entry can make reward/risk worse and raise false-break risk. | `needs_visual_discretion` | Ambiguity still depends on chart interpretation. |
| `I03_UnRs896Utnc_C04_pattern_location_context_priority` | Any named chart pattern. | A pattern appears in the market. | Judge the surrounding trend and location before using the pattern as an entry trigger. | A pattern in weak context can fail even if the shape itself looks correct. | `mechanical_candidate` | The context rule is clear, but the location taxonomy still needs formal definitions. |

No candidate is implementation-ready. The pattern family is materially visual and still depends on chart-object definitions.

## 5. Strategy Boundary

This summary authorizes no Strategy A/B change, no Strategy B change, no Strategy B2/C creation, no backtest, no optimization, no market-data access, no broker/live execution, no Doctrine Map update, and no profitability claim.
