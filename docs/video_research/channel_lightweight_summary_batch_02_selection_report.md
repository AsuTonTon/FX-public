# Channel Lightweight Summary Batch 02 Selection Report

## 1. Objective

This document selects the next bounded lightweight-summary batch through caption-derived evidence audit. It is selection and audit only: it does not generate Batch 02 per-video summaries, establish channel doctrine, modify Strategy A/B, create Strategy C or B2, run backtests, optimize parameters, or make profitability claims.

Raw captions were used only as local working material under ignored paths. This report records timestamped paraphrases and selection decisions, not raw transcript or subtitle text.

## 2. Source-pool validation

Authoritative source: `docs/video_research/channel_high_priority_relevance_triage_ledger.md`.

| check | result |
| --- | --- |
| merged ledger rows | 115 |
| unique video IDs | 115 |
| Batch 01 IDs excluded | 8 |
| caption-unavailable rows excluded | 3 |
| previously audited non-Batch-01 rows excluded by `evidence_audit_status != not_audited` | 2 |
| eligible source pool | 102 |
| eligible regular videos | 90 |
| eligible Shorts | 12 |
| preferred provisional mechanical rows in eligible pool | 37 |
| preferred provisional partial rows in eligible pool | 7 |
| preferred mechanical/partial routing pool | 44 |

Eligible rows were required to have `evidence_audit_status = not_audited`, `caption_status = auto_caption`, a unique ID, and no Batch 01 membership. Provisional routing was used only to form a candidate pool; no provisional topic or class was treated as confirmed evidence.

Caption-unavailable rows excluded from the pool: `6SUZWdAUd6c`, `qNcZIRfNueg`, `qTrZJQiT5OE`.

Batch 01 rows excluded from re-audit: `16Kb39TFFek`, `CES2xzjeOTk`, `HuNeo8FfBO8`, `SrWVDh_BpVs`, `V8DoVtiE-0Y`, `e4N22IkeOs4`, `iZuUWHc5bcI`, `vkaA9MCRlx4`.

## 3. Audit shortlist

Shortlist size: 12 videos. All 12 are regular videos; no Short was selected for the audit shortlist.

Hash method: sort the 12 video IDs lexicographically, join with LF (`\n`), do not append a trailing LF, then calculate SHA-256.

Shortlist hash: `1d08bdd0446ea398ce243364332d52f40d03d6428b743321ba04cb06bb9f5fab`

Lexicographically sorted shortlist IDs:

```text
6bZ-OG-133s
6vGtLPFfWYQ
8OpVGAO8_2Y
BxQyDLIWE0U
FnX9995OSYQ
G3OTGwKAip4
GIGLYCFBH9Q
KEE4Dk8LM1A
QTXMzTbGH5U
_sx3dCvPXac
rG3ELeTim8U
tw9gxJ7KXUs
```

| video_id | source_title | content_type | shortlist reason |
| --- | --- | --- | --- |
| G3OTGwKAip4 | 【利確の教科書】利益を最大化するための最強の考え方 | regular_video | TP/exit gap candidate; title routing suggested a broad profit-taking lesson, and audit was needed to test whether it contained operational target anchors rather than TP claims only. |
| 8OpVGAO8_2Y | FXで資金を守りながら利益を増やす利確の絶対ルール【ゆっくり実況】 | regular_video | TP/exit and trade-management gap candidate; selected to test whether protective exit conditions were repeatable. |
| FnX9995OSYQ | 【必須知識】負けトレードでも利益を残して勝ちで終わる方法/第150話 | regular_video | Partial-exit and early-exit case candidate; selected to test whether the recap yielded repeatable management rules. |
| 6bZ-OG-133s | 【完全版】FXの損切りの正しい決め方・考え方を全て教える。 | regular_video | Stop/invalidation gap candidate; selected because the routing ledger indicated stop, wave, and structure topics. |
| GIGLYCFBH9Q | 【今日から変わる】FXの損切り貧乏を改善する方法を解説 | regular_video | Stop, RR, and time-axis candidate; selected to test whether the video gave operational conditions beyond mindset. |
| 6vGtLPFfWYQ | 【トレード厳禁】お金が減る負けやすい相場とは？ | regular_video | Range/regime, stop-distance, and RR candidate; selected to test market-condition rejection rules. |
| rG3ELeTim8U | 【危険な罠】FX初心者がよく負ける騙しポイントとは？ | regular_video | False-break, timeframe confirmation, and indicator-use candidate; selected to test Batch 01 damashi and filter observations. |
| tw9gxJ7KXUs | 【完全攻略】こうやって環境認識をしたらFXは負けないよね。/第90話 | regular_video | MTF environment-recognition case candidate; selected to test whether a trade recap provides generalizable environment rules. |
| BxQyDLIWE0U | 【ゆっくり実況】ブレイク手法はこうすれば勝てる/FX.XM10万円チャレンジ/第23話 | regular_video | Breakout, wave target, and RR candidate; selected to test whether the breakout method narrows Batch 01 entry-confirmation observations. |
| KEE4Dk8LM1A | 【負けを激減】押し戻りの「待ち方」について必勝法を伝授する | regular_video | Pullback/waiting, MTF, and RR candidate; selected to test explicit entry delay rules. |
| _sx3dCvPXac | 【FXの負け方】この行動を取れば確実に負けます。 | regular_video | Psychology and trade-management-warning candidate; selected as a negative-control row for discretionary or mindset content. |
| QTXMzTbGH5U | 【月収爆増】ローソク足レンジを攻略して稼ぎまくる方法。（プライスアクション第4弾） | regular_video | Range/filter, price-action, stop, and exit candidate; selected despite promotional title wording to test timestamped mechanics only. |

## 4. Audit coverage

| audit outcome | count |
| --- | ---: |
| attempted | 12 |
| completed | 12 |
| processing_failure | 0 |
| direct_mechanical_rule | 9 |
| partial_mechanical_rule | 1 |
| doctrine_context | 0 |
| case_study_or_trade_recap | 1 |
| psychology_or_mindset | 1 |
| promotional_or_generic | 0 |

All 12 audited rows have usable `auto_caption` captions. The direct-mechanical count is larger than the final selected count because the final batch is capped at 8 and prioritizes coverage diversity; the extra direct row remains useful for later breakout work.

## 5. Gap coverage

| gap area | audited evidence suppliers |
| --- | --- |
| TP/exit | `G3OTGwKAip4`, `8OpVGAO8_2Y`, `FnX9995OSYQ`, `BxQyDLIWE0U`, `QTXMzTbGH5U`, `tw9gxJ7KXUs` |
| stop/invalidation | `6bZ-OG-133s`, `6vGtLPFfWYQ`, `GIGLYCFBH9Q`, `QTXMzTbGH5U`, `FnX9995OSYQ`, `tw9gxJ7KXUs` |
| trade management | `G3OTGwKAip4`, `8OpVGAO8_2Y`, `GIGLYCFBH9Q`, `QTXMzTbGH5U`, `FnX9995OSYQ`, `tw9gxJ7KXUs`, `_sx3dCvPXac` |
| range/filter or regime | `6vGtLPFfWYQ`, `rG3ELeTim8U`, `QTXMzTbGH5U`, `KEE4Dk8LM1A`, `tw9gxJ7KXUs` |
| timeframe/session or MTF | `6bZ-OG-133s`, `GIGLYCFBH9Q`, `rG3ELeTim8U`, `tw9gxJ7KXUs`, `KEE4Dk8LM1A`, `QTXMzTbGH5U`, `8OpVGAO8_2Y` |
| indicator usage | `rG3ELeTim8U` |
| risk/reward | `G3OTGwKAip4`, `GIGLYCFBH9Q`, `6vGtLPFfWYQ`, `BxQyDLIWE0U`, `KEE4Dk8LM1A`, `6bZ-OG-133s` |

ADX or explicit trend-strength-indicator usage was not found in this 12-video audit. The only indicator-specific confirmed row is `rG3ELeTim8U`, where RSI is treated as a secondary check after chart evidence, not as the primary entry basis.

## 6. Batch 01 observation tests

These counts are observation tests only. They do not convert Batch 01 observations or Batch 02 findings into channel doctrine.

| Batch 01 observation | supports | narrows | conditional_difference | potentially_contradicts | not_relevant | insufficient_evidence |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| O1 Higher-timeframe context or confirmation matters before treating a local signal as actionable. | 8 | 0 | 0 | 0 | 3 | 1 |
| O2 Entry is commonly delayed for confirmation rather than taken on first touch or first break. | 7 | 0 | 0 | 0 | 5 | 0 |
| O3 Structural context is required before the trigger is interpreted. | 11 | 0 | 0 | 0 | 1 | 0 |
| O4 Stop and TP should be definable from structure where the video covers exits. | 9 | 0 | 0 | 0 | 3 | 0 |
| O5 RR is contextual and tied to stop/target placement rather than established as a universal fixed ratio in this batch. | 5 | 0 | 1 | 0 | 6 | 0 |
| O6 Discretion remains in level, wave, pattern, or swing-quality selection. | 12 | 0 | 0 | 0 | 0 | 0 |
| O7 False-break, damashi, sweep, or range-maturity handling appears as a recurring filter family. | 5 | 1 | 0 | 0 | 6 | 0 |

No actual contradiction was found. The matrix-aligned row notes are:

- `rG3ELeTim8U` supports O1, O2, O3, O6, and O7; O5 is `conditional_difference`; O4 is `not_relevant`.
- `6vGtLPFfWYQ` supports O1 through O7. It is not counted as narrowing O3 or O5.
- `QTXMzTbGH5U` supports O1, O2, O3, O4, O6, and O7; O5 is `not_relevant`. It is not counted as narrowing O7.
- `GIGLYCFBH9Q` supports O1, O3, O4, O5, and O6; O2 and O7 are `not_relevant`. It is not a `conditional_difference` row for O5.
- `BxQyDLIWE0U` is the single row classified as `narrows`, and that narrowing is for O7.

## 7. Final Batch 02 selection

Final selected count: 8. All selected rows are audited `direct_mechanical_rule` rows with usable captions, medium or high confidence, timestamp-supported confirmed dimensions, and no unresolved near-duplicate issue.

Hash method: sort the 8 selected video IDs lexicographically, join with LF (`\n`), do not append a trailing LF, then calculate SHA-256.

Final Batch 02 hash: `8fbcaa23d3c85949e5ca7e06d412097989020f549b9dcf52e0ec140fc6d4d3fd`

Lexicographically sorted final selected IDs:

```text
6bZ-OG-133s
6vGtLPFfWYQ
8OpVGAO8_2Y
G3OTGwKAip4
GIGLYCFBH9Q
KEE4Dk8LM1A
QTXMzTbGH5U
rG3ELeTim8U
```

| video_id | source_title | content_type | audited class | confirmed dimensions | key timestamp-supported reason | gap filled | Batch 01 relation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G3OTGwKAip4 | 【利確の教科書】利益を最大化するための最強の考え方 | regular_video | direct_mechanical_rule | `tp_exit`; `risk_reward`; `trade_management`; `setup_context` | 02:34-05:38 gives repeatable initial TP anchors from wave-3 measured move and chart-pattern measured width; 06:04-06:54 adds a management rule to exit earlier when price action rejects the expected move. | TP/exit; trade management | Supports O3/O4/O5/O6. |
| 8OpVGAO8_2Y | FXで資金を守りながら利益を増やす利確の絶対ルール【ゆっくり実況】 | regular_video | direct_mechanical_rule | `tp_exit`; `trend_range_filter`; `timeframe_session`; `trade_management` | 02:03-02:34 defines protective exit after Dow breakdown or short-term uptrend against a sell; 02:46-03:03 defines exit after important-line rebound and range upside break; 03:51-04:25 anchors initial TP to wave completion or daily/weekly levels. | TP/exit; range exit; MTF target | Supports O1/O3/O4/O6/O7. |
| 6bZ-OG-133s | 【完全版】FXの損切りの正しい決め方・考え方を全て教える。 | regular_video | direct_mechanical_rule | `stop_invalidation`; `setup_context`; `timeframe_session`; `risk_reward` | 03:55-06:35 states stop placement should be where entry grounds fail, prioritizing textbook chart-pattern stops or Elliott wave invalidation; 07:31-09:39 warns against using lower-timeframe stops for higher-timeframe targets unless deliberately accepting lower win rate for RR. | Stop/invalidation; timeframe-stop alignment | Supports O1/O3/O4/O6. |
| GIGLYCFBH9Q | 【今日から変わる】FXの損切り貧乏を改善する方法を解説 | regular_video | direct_mechanical_rule | `stop_invalidation`; `tp_exit`; `risk_reward`; `timeframe_session`; `trade_management` | 04:18-05:12 requires imagining the losing scenario when TP/SL are set; 05:32-06:36 rejects changing a 1H exit plan into a 4H/daily target without new grounds and advises taking the originally planned shorter target or re-entering later. | RR; time-axis alignment; management discipline | Supports O1/O3/O4/O5/O6; O2/O7 not relevant. |
| 6vGtLPFfWYQ | 【トレード厳禁】お金が減る負けやすい相場とは？ | regular_video | direct_mechanical_rule | `setup_context`; `entry_trigger`; `stop_invalidation`; `trend_range_filter`; `risk_reward` | 01:06-03:52 defines weak entries as places with only one "back" to the stop and stronger entries as places with two or more structural backs; 04:07-07:29 rejects far-stop breakout or mid-trend entries and prefers clean breakout/pullback or close-stop alternatives. | Regime filter; stop distance; RR | Supports O1/O2/O3/O4/O5/O6/O7. |
| rG3ELeTim8U | 【危険な罠】FX初心者がよく負ける騙しポイントとは？ | regular_video | direct_mechanical_rule | `entry_trigger`; `trend_range_filter`; `timeframe_session`; `indicator_condition`; `risk_reward` | 01:33-02:43 requires line-break confirmation on the timeframe where the line/pattern was drawn; 03:10-04:17 treats RSI as valid only after chart evidence; 05:41-06:48 explains return-move waiting but admits momentum assessment remains discretionary. | False-break filter; indicator discipline; MTF confirmation | Supports O1/O2/O3/O6/O7; conditional difference on O5. |
| KEE4Dk8LM1A | 【負けを激減】押し戻りの「待ち方」について必勝法を伝授する | regular_video | direct_mechanical_rule | `setup_context`; `entry_trigger`; `trend_range_filter`; `timeframe_session`; `risk_reward` | 02:03-02:11 gives the sequence environment recognition -> scenario construction -> alert -> entry; 02:44-04:57 narrows pullback candidates from wave structure and then requires one of three entry triggers; 06:16-06:50 applies the same candle-confirmation logic to return selling and notes RR improvement from waiting. | Entry delay; MTF/pullback; RR | Supports O1/O2/O3/O5/O6/O7. |
| QTXMzTbGH5U | 【月収爆増】ローソク足レンジを攻略して稼ぎまくる方法。（プライスアクション第4弾） | regular_video | direct_mechanical_rule | `setup_context`; `entry_trigger`; `stop_invalidation`; `tp_exit`; `trend_range_filter`; `timeframe_session`; `trade_management` | 00:47-01:28 defines candle-body range and break-confirmed direction; 02:03-02:24 warns against short-timeframe range-break judgment; 02:49-04:25 gives entry, temporary stop below range, nearby structural TP, and exit/hold management after the price action appears. | Range filter; stop/TP; trade management | Supports O1/O2/O3/O4/O6/O7. |

Final selected regular/Short breakdown: 8 regular videos, 0 Shorts.

## 8. Rejected or deferred candidates

| video_id | audited class | reason not selected | future disposition |
| --- | --- | --- | --- |
| FnX9995OSYQ | partial_mechanical_rule | The caption supports a case-specific early-exit decision from a live trade, but the repeatable procedure is less complete than the selected TP and management videos. | Useful later as a trade-recap example for early exit, horizontal-axis mismatch, and avoiding false double-bottom interpretation. |
| BxQyDLIWE0U | direct_mechanical_rule | The breakout method is timestamped and repeatable, but the final set was capped at 8 and this row lacks a timestamped stop/invalidation condition while also noting poor RR tendency. | Useful later for a breakout or Elliott-wave target summary; not a near-duplicate of Batch 01, but lower coverage value for this batch. |
| tw9gxJ7KXUs | case_study_or_trade_recap | Strong MTF environment evidence appears inside a specific trade recap with case-bound chart conditions; selected set already covers MTF entry and range filters through more direct teaching videos. | Useful later as a case study for weekly/daily/4H alignment and staged exit behavior. |
| _sx3dCvPXac | psychology_or_mindset | The useful evidence is mostly behavioral warning: do not copy advanced management tools without understanding them and verbalize entry grounds. It does not define a mechanical entry/exit rule. | Useful later for mindset, review discipline, and discretionary-risk notes; not suitable for Batch 02 summary target. |

## 9. Final target validation

| validation item | result |
| --- | --- |
| selected count | 8 |
| unique selected IDs | 8 |
| selected regular videos | 8 |
| selected Shorts | 0 |
| final hash | `8fbcaa23d3c85949e5ca7e06d412097989020f549b9dcf52e0ec140fc6d4d3fd` |
| duplicate status | No unresolved near-duplicate issue. `KEE4Dk8LM1A` has a likely related Short (`GB7wgE3GZtc`) in the triage ledger, but the selected row is the regular full video and the Short was not selected. |
| readiness decision | `ready_for_batch_02_summary` |

The selected set covers TP/exit, stop/invalidation, trade management, range/filter, timeframe/MTF, indicator usage, and RR. It includes multiple candidates that narrow or conditionally differ from Batch 01 observations without claiming contradiction.

## 10. Guardrail validation

Confirmed:

- only two Markdown files are added for this task;
- no Batch 02 per-video summaries were written;
- no raw transcript or subtitle text is committed;
- no subtitle files, caption URLs, or raw subtitle metadata are committed;
- no video or audio is downloaded or committed;
- no data, results, CSV, JSON, or processing log is committed;
- no Strategy A/B code or parameter files are changed;
- no backtests were run;
- no Strategy C or Strategy B2 is created;
- no profitability claim is made;
- the PR branch was created from latest `main`, and the intended PR base is `main`.

## Assumptions and blockers

Assumptions:

- `auto_caption` rows are usable for selection audit when the timestamped evidence is clear enough to paraphrase conservatively.
- Sensational or promotional title wording was ignored during final selection unless timestamped captions established operational conditions.

Unresolved blockers: none.
