# Playlist-Led Intermediate Batch 02 Summary: 5yjtVnTy_54

Task: `channel_playlist_led_intermediate_batch_02_downsub_summary`

## 1. Metadata

| field | value |
| --- | --- |
| video ID | `5yjtVnTy_54` |
| playlist label | `FX中級者のための勝率UP講座` |
| playlist order | 10 |
| compact title | 【超有料級】誰でも勝てるスキャルピング手法を教えます。 |
| source classification | `codex_accessed_downsub_third_party_subtitle_source`; `downsub_accessed_by_codex_for_caption_derivative_review` |
| access status | `caption_body_available` |
| raw subtitle text | not included |

The compact title and source performance-style wording are retained only as source metadata. This summary does not validate, adopt, or make any profitability claim.

## 2. Compact Paraphrased Lesson Summary

This lesson describes a short-term scalping framework built around the 15-minute chart, a 20 EMA, and a 200 MA/EMA-style long moving average. The source presents it as a creator-tested method, but this summary treats that as source context only, not verified project performance.

The sequence is: wait for the fast moving average and long moving average to cross, wait for price to touch the long moving average after the cross, draw both a diagonal neckline and a horizontal neckline, require both line breaks, then wait for a proper return move and price-action confirmation before entry. The lesson repeatedly emphasizes that diagonal-line quality matters. A steep or poorly reacted line should be rejected, while a line that reacts to visible swing points is preferred.

The exit discussion keeps the default target conservative at the recent high or low. Larger targets, such as a first-wave projection, are presented as optional only when the trader has additional context. The stop is placed at a point where the setup's assumed wave or return-move structure would be invalidated.

## 3. Trading Concept Notes

- The method is anchored to the 15-minute chart and two moving averages.
- The setup begins only after a moving-average cross and later touch of the long moving average.
- A diagonal line alone is considered weaker than a diagonal line plus horizontal neckline.
- Immediate one- or two-candle retests after a break are treated as lower quality than a clearer break-and-return sequence.
- Entry requires price action after the return move, not simply the first line touch.
- Default target is the nearby high or low because the method intentionally avoids heavier higher-timeframe analysis.
- Optional extension targets require additional context and should not be assumed.
- The setup remains visually discretionary because line quality, return-move quality, and price-action confirmation are chart-read decisions.

## 4. Mechanical-Rule Candidate Observations

| candidate ID | setup context | condition | action | invalidation or risk note | automation readiness | uncertainty notes |
| --- | --- | --- | --- | --- | --- | --- |
| `I02_5yjtVnTy54_C01_15m_cross_then_long_ma_touch` | 15-minute scalping setup. | The fast moving average crosses the long moving average, then price later touches the long moving average. | Begin setup review; do not enter from the cross alone. | Moving-average labels need local normalization before testing. | `mechanical_candidate` | Source wording mixes 200MA/EMA-style references; project definition is needed. |
| `I02_5yjtVnTy54_C02_functional_diagonal_line_filter` | Diagonal neckline drawing. | A proposed diagonal line is too steep or does not react cleanly to visible swings. | Reject the line and wait for a cleaner diagonal structure. | Bad line placement can create false timing. | `needs_visual_discretion` | "Clean reaction" is visual and not defined numerically. |
| `I02_5yjtVnTy54_C03_dual_neckline_break_gate` | Breakout qualification. | Both a functional diagonal line and a nearby horizontal neckline are defined. | Require break confirmation of both line concepts before considering entry. | Diagonal-only entries are described as more fragile. | `needs_visual_discretion` | Horizontal neckline selection remains chart-dependent. |
| `I02_5yjtVnTy54_C04_return_move_price_action_entry` | Entry timing. | Price breaks the line structure, makes a non-immediate return move, and then shows confirming price action. | Enter only after confirmation on the return-move leg. | Very fast one- or two-candle returns are lower quality in the source logic. | `needs_visual_discretion` | Price-action confirmation is not formalized. |
| `I02_5yjtVnTy54_C05_default_recent_swing_target` | Exit planning. | A qualified scalp entry is taken without deeper higher-timeframe support. | Use the nearest recent high/low as default target rather than assuming extension. | Stretching the target without context can change expectancy. | `mechanical_candidate` | Recent high/low selection and stop distance need formal definitions. |

No candidate is implementation-ready. The setup has mechanical shape, but line quality, return-move quality, price action, and MA definitions remain unresolved.

## 5. Strategy Boundary

This summary authorizes no Strategy A/B change, no Strategy B change, no Strategy B2/C creation, no backtest, no optimization, no market-data access, no broker/live execution, no Doctrine Map update, and no profitability claim.
