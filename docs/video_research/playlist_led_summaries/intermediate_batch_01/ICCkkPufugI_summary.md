# Playlist-Led Intermediate Batch 01 Summary: ICCkkPufugI

Task: `channel_playlist_led_intermediate_batch_01_downsub_summary`

## 1. Metadata

| field | value |
| --- | --- |
| video ID | `ICCkkPufugI` |
| playlist label | `FX中級者のための勝率UP講座` |
| playlist order | 5 |
| compact title | 【完全版】FXで超重要の波形の正しい見方とは？ |
| source classification | `codex_accessed_downsub_third_party_subtitle_source`; `downsub_accessed_by_codex_for_caption_derivative_review` |
| access status | `caption_body_available` |
| raw subtitle text | not included |

The compact title is retained only as source metadata from committed playlist docs and is not a profitability claim.

## 2. Compact paraphrased lesson summary

This lesson argues that many traders know the names of Dow theory, chart patterns, and Elliott waves, but still lose because they read the surrounding wave form incorrectly. Two setups may satisfy the same named pattern, yet differ sharply in quality once recent flow, trapped positions, horizontal buildup, and location are considered.

The first major lens is "fuel." The lesson asks traders to think about where long and short positions are likely held, where stops or liquidation points may sit, and whether price has enough opposing-position fuel to continue in the expected direction. It also explains why price often moves opposite first, collects liquidity, and then continues in the environment's original direction.

The second lens is horizontal development. A pattern with more sideways buildup is treated as more meaningful because it can accumulate more fuel. The lesson applies this to double bottoms, head-and-shoulders shapes, and Elliott second-wave behavior, where sideways correction can replace a clean textbook pullback.

The third lens is pattern environment. A pattern should be judged by where it appears in the larger wave. Double bottoms and inverse head-and-shoulders patterns are not equivalent wherever they appear, and a pattern near the wrong part of the current wave may have too little room or too much opposing context to be easy.

## 3. Trading concept notes

- Wave-form reading is treated as the context layer beneath named setups.
- Fuel means likely pending pressure from profit-taking, stops, liquidations, and new entries.
- A move can need an opposite shakeout or horizontal base before continuation has enough fuel.
- Horizontal buildup can improve pattern quality because it accumulates more participants and clearer invalidation.
- Counting touch points alone is insufficient for chart-pattern identification.
- Pattern location matters: reversal patterns should be interpreted differently at bottoms, tops, and mid-wave areas.
- The lesson strongly depends on visual judgment and does not provide exact swing, stop-cluster, or pattern-quality measurements.

## 4. Mechanical-rule candidate observations

| candidate ID | setup context | condition | action | invalidation or risk note | automation readiness | uncertainty notes |
| --- | --- | --- | --- | --- | --- | --- |
| `I01_ICCkkPufugI_C01_fuel_before_continuation` | Continuation entry review. | Price is expected to continue, but recent structure has not created enough opposing-position fuel or horizontal buildup. | Delay entry or reduce confidence until fuel is created. | Entering before fuel builds can lead to shakeout losses. | `needs_visual_discretion` | Fuel is described conceptually, not with measurable order-flow data. |
| `I01_ICCkkPufugI_C02_horizontal_base_quality` | Pattern-quality review. | A double bottom, head-and-shoulders, or second-wave structure includes meaningful sideways development. | Treat the pattern as higher quality than a quick touch-count pattern. | Sideways buildup can still fail or become a range trap. | `needs_visual_discretion` | Requires definitions for duration, range, and breakout confirmation. |
| `I01_ICCkkPufugI_C03_touch_count_not_enough` | Chart-pattern validation. | A pattern is identified only because price touched two lows, two highs, or three peaks. | Reject pattern classification until wave location and fuel context are checked. | Over-filtering can skip valid simple structures. | `mechanical_candidate` | The checklist shape is mechanical, but the follow-up checks remain visual. |
| `I01_ICCkkPufugI_C04_pattern_location_filter` | Reversal-pattern entry review. | A bottom-pattern candidate is not near a plausible bottom zone, or a top-pattern candidate is not near a plausible top zone. | Downgrade or skip the setup for less experienced trading. | Advanced contexts can intentionally use non-textbook patterns. | `needs_visual_discretion` | Location and "plausible zone" are not formally defined. |

No candidate is implementation-ready. The lesson is valuable for manual review protocols, but automation would need formal definitions for wave location, horizontal buildup, and fuel.

## 5. Strategy boundary

This summary does not authorize any Strategy A/B change, Strategy B change, Strategy B2/C creation, backtest, optimization, market-data access, broker/live execution, Doctrine Map update, or profitability claim.
