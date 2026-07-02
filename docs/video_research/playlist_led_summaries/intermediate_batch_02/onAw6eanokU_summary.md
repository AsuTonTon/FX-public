# Playlist-Led Intermediate Batch 02 Summary: onAw6eanokU

Task: `channel_playlist_led_intermediate_batch_02_downsub_summary`

## 1. Metadata

| field | value |
| --- | --- |
| video ID | `onAw6eanokU` |
| playlist label | `FX中級者のための勝率UP講座` |
| playlist order | 13 |
| compact title | 【神回】勝率20％以下のトレーダーが勝てるようになる方法 |
| source classification | `codex_accessed_downsub_third_party_subtitle_source`; `downsub_accessed_by_codex_for_caption_derivative_review` |
| access status | `caption_body_available` |
| raw subtitle text | not included |

The compact title and source performance-style wording are retained only as source metadata. This summary does not validate, adopt, or make any profitability claim.

## 2. Compact Paraphrased Lesson Summary

This lesson argues that win rate alone is not the main evaluation target. Monthly P&L is treated as the practical measure: a very low win-rate trader and a high win-rate trader are both failing if monthly results remain negative. The video uses low win rate as a diagnostic sign, not as a reason for despair.

The first half frames extremely low win rate as evidence that the trader's discretion is repeatedly making trades worse than a simple neutral baseline. Instead of reacting emotionally, the trader should identify the recurring behavior or view that is reducing expected results. The recommended tool is serious journaling: record the reasons, feelings, and assumptions for each trade, then review them until repeated mistakes become visible.

The speaker gives an example of believing that line-break judgment was already correct, then discovering through journal review that break confirmation was being judged on a shorter timeframe than the monitored chart. The second half discusses the difference between becoming monthly positive and making materially larger profits. The source says that after basic consistency, the trader needs different risk allocation, clear specialty patterns, and the ability to verbalize where larger risk is justified.

## 3. Trading Concept Notes

- Monthly P&L matters more than win rate in isolation.
- Very low win rate should trigger diagnosis of repeated behavior, not emotional self-judgment.
- A trader can be wrong about what they think they already do correctly.
- Journal review should search for hidden repeated mistakes, such as inconsistent timeframe use for line breaks.
- Moving from "not losing monthly" to "earning meaningfully more" may require a different risk posture.
- Larger risk is framed as belonging only to high-confidence, well-understood specialty patterns.
- The source does not provide a numeric lot-sizing model or an implementation-ready scaling policy.

## 4. Mechanical-Rule Candidate Observations

| candidate ID | setup context | condition | action | invalidation or risk note | automation readiness | uncertainty notes |
| --- | --- | --- | --- | --- | --- | --- |
| `I02_onAw6eanokU_C01_low_winrate_error_inventory` | Performance review. | Win rate is extremely low or monthly P&L is persistently negative. | Build an inventory of repeated mistakes from journaled reasons, emotions, stops, sizing, and timeframe decisions. | Emotional review without pattern identification is treated as low value. | `mechanical_candidate` | Requires a maintained trade log schema. |
| `I02_onAw6eanokU_C02_timeframe_consistent_break_check` | Line-break confirmation. | A setup is monitored on one timeframe but break confirmation is judged on a shorter timeframe. | Flag the trade for review or block the entry until the monitored timeframe confirms. | Timeframe mismatch can create false break entries. | `mechanical_candidate` | Needs a formal monitored-timeframe field and break-confirmation rule. |
| `I02_onAw6eanokU_C03_monthly_positive_vs_growth_mode_split` | Trader development planning. | A trader has achieved basic monthly positivity but is not growing capital meaningfully. | Separate "stability mode" from "growth mode" and define different risk limits before increasing size. | Larger risk can destroy consistency if it is not tied to a specialty pattern. | `not_automation_ready` | Requires personal account policy and risk tolerance. |
| `I02_onAw6eanokU_C04_specialty_pattern_verbalization` | Larger-risk candidate review. | A trader wants to risk more on selected opportunities. | Require a named specialty pattern and verbalized reason before considering larger exposure. | Vague confidence can become overbetting. | `doctrine_only` | Specialty patterns are not enumerated in the caption. |
| `I02_onAw6eanokU_C05_negative_result_reframe` | Review psychology. | A trader reacts to low win rate with vague frustration. | Reframe the problem into observable actions that can be changed. | Motivation without diagnosis does not improve the system. | `doctrine_only` | Process doctrine only. |

No candidate is implementation-ready. The most actionable material is a review schema for repeated mistakes and timeframe-consistent confirmation.

## 5. Strategy Boundary

This summary authorizes no Strategy A/B change, no Strategy B change, no Strategy B2/C creation, no backtest, no optimization, no market-data access, no broker/live execution, no Doctrine Map update, and no profitability claim.
