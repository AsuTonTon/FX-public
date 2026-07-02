# Playlist-Led Intermediate Batch 03 Summary: fbTWY8U4h9A

Task: `channel_playlist_led_intermediate_batch_03_youtube_caption_summary`

## 1. Metadata

| field | value |
| --- | --- |
| video ID | `fbTWY8U4h9A` |
| playlist label | `FX中級者のための勝率UP講座` |
| playlist order | 18 |
| compact title | 【完全版】ダウ理論を使ってFXで稼ぐための方法を教える。 |
| source classification | `official_youtube_caption_evidence`; `remote_caption_fetch` |
| access status | `caption_body_available` |
| raw subtitle text | not included |

The compact title is retained only as source metadata from the bounded playlist check and is not a project claim.

## 2. Compact paraphrased lesson summary

This lesson narrows Dow theory to one practical principle: trend is assumed to continue until a clear reversal signal appears. The lecture spends most of its time translating that idea into chart-state management rather than treating Dow theory as a magical entry system.

The first step is defining the actual trend. Higher highs and higher lows confirm an uptrend, while lower highs and lower lows confirm a downtrend. The speaker then says the important reversal signal is the break of the last meaningful swing low in an uptrend or the last meaningful swing high in a downtrend.

A major caution is that not every small fluctuation should be counted as a real swing. The lesson warns that traders often promote small noise movement into full trend structure, then declare a reversal too early. Even after the last important swing breaks, the new state is described first as trendless, not automatically a fully confirmed opposite trend.

The lecture also argues that Dow theory gives direction more reliably than timing. A break entry or pullback entry still needs other strong reasons, because knowing the directional bias alone does not guarantee a clean trigger, stop, or target.

## 3. Trading concept notes

- Dow theory is reduced to a single trade-relevant continuity principle.
- Trend confirmation uses meaningful swing highs and lows, not every small fluctuation.
- Breaking the last important swing marks the end of the prior trend, not instant confirmation of the new opposite trend.
- Trendless transition is a separate state that should not be mislabeled.
- Dow-theory direction is treated as a filter that must be paired with better timing logic.
- Countertrend trades are not forbidden, but the lecture says they need extra strength to overcome the trend bias.

## 4. Mechanical-rule candidate observations

| candidate ID | setup context | condition | action | invalidation or risk note | automation readiness | uncertainty notes |
| --- | --- | --- | --- | --- | --- | --- |
| `I03_fbTWY8U4h9A_C01_last_meaningful_swing_reversal_test` | An established trend is under review. | The last meaningful swing low or swing high is clearly broken. | Mark the prior trend as ended and shift to reversal-state review. | Small internal wiggles should not be promoted into the main swing structure. | `mechanical_candidate` | Requires a consistent definition of "meaningful" swing. |
| `I03_fbTWY8U4h9A_C02_noise_swing_ignore_rule` | The timeframe contains both major waves and small fluctuations. | A local wiggle does not materially define the chart's larger wave. | Ignore the small fluctuation when labeling the main trend. | Mislabeling noise creates false reversal calls. | `needs_visual_discretion` | The principle is clear, but the exact scale threshold is visual. |
| `I03_fbTWY8U4h9A_C03_trendless_transition_state` | A prior trend has just lost its last key swing. | Opposite-direction lower high/lower low or higher low/higher high is not confirmed yet. | Classify the market as trendless instead of forcing the opposite trend label. | Premature reversal labeling is presented as a common mistake. | `mechanical_candidate` | Still needs a local state model for trendless handling. |
| `I03_fbTWY8U4h9A_C04_dow_bias_plus_extra_trigger` | A Dow-theory directional bias exists. | The trader wants to enter on break or pullback. | Require separate timing, stop, and target logic instead of treating the bias alone as sufficient. | The lesson says many hindsight examples hide this missing step. | `doctrine_only` | Helpful as a review guardrail rather than a full rule set. |

The lecture offers a strong state-management framework, but it does not by itself solve timing, stop, or target translation.

## 5. Strategy boundary

This summary does not authorize any Strategy A/B change, Strategy B change, Strategy B2/C creation, backtest, optimization, market-data access, broker/live execution, Doctrine Map update, or profitability claim.
