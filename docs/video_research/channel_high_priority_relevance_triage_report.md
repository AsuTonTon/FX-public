# Channel High-Priority Relevance Triage Report

Task: `channel_high_priority_relevance_triage`

## 1. Objective

This update reframes the 115-row output as provisional routing triage plus a bounded evidence audit of 10 regular-video candidates. It avoids another mass rewrite of caption-derived evidence across all rows.

This is a research-design correction only. It does not summarize the full corpus, extract Strategy B rules, modify Strategy A/B, create Strategy C or Strategy B2, run backtests, add parameters, add market data, or make profitability claims.

## 2. Provisional Full-Set Triage

| metric | count |
| --- | --- |
| frozen high-priority rows | 115 |
| unique high-priority video IDs | 115 |
| regular videos | 100 |
| Shorts | 15 |
| caption-available rows | 112 |
| caption-unavailable rows | 3 |

Frozen target hash: `ad2eb82ee4d351fc41e1ceb79367a278779399d85e1e920ee66c42fd614948ed`

The 115-row ledger is routing metadata, not completed mechanical-rule evidence. For unaudited rows, `candidate_dimensions` are candidate topics inferred from title/caption topic signals and must not be read as confirmed level-2 evidence.

| routing_class | count |
| --- | --- |
| direct_mechanical_rule | 8 |
| partial_mechanical_rule | 2 |
| provisional_case_or_recap | 51 |
| provisional_doctrine_or_context | 6 |
| provisional_mechanical_candidate | 37 |
| provisional_partial_candidate | 7 |
| provisional_psychology_or_mindset | 1 |
| unavailable | 3 |

| evidence_audit_status | count |
| --- | --- |
| audited | 10 |
| not_audited | 102 |
| unavailable | 3 |

Limitations: unaudited rows do not claim exact entry, stop, TP, or RR procedures; contradiction counts are not reported as confirmed findings for unaudited rows; possible Short links remain provisional routing links only.

## 3. Detailed Evidence Audit

| audit metric | count |
| --- | --- |
| candidates selected | 10 |
| candidates completed | 10 |
| passed as direct mechanical | 8 |
| downgraded after audit | 2 |
| replacements made | 1 |

Replacement made: `U9xsvLmdIOw` was removed from the audit set to reduce horizontal-line near-duplication, and `Mg09uk9I9JM` was added for trade-management coverage.

| confirmed_strong_dimension | audited_count |
| --- | --- |
| entry_trigger | 7 |
| indicator_condition | 1 |
| risk_reward | 7 |
| setup_context | 8 |
| stop_invalidation | 5 |
| timeframe_session | 8 |
| tp_exit | 4 |
| trade_management | 3 |
| trend_range_filter | 8 |

## 4. Auditable Evidence Table

| video_id | source_title | content_type | caption_status | evidence_audit_status | timestamp_reference | atomic_paraphrased_claim | setup/context condition | entry condition | stop/invalidation condition | TP/exit condition | trend/range filter | time-frame/session condition | indicator condition | risk/reward condition | trade-management condition | discretionary_or_undefined_elements | contradictions_or_conditional_scope | audited_relevance_class | audited_confidence | summary_eligibility |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16Kb39TFFek | 【負けを激減】FX専業も使う水平線の抜け判断の見極め方 | regular_video | auto_caption | audited | 02:24-03:32; 03:32-04:26 | 02:24-03:32: horizontal-line breakout validity depends on the line's higher-timeframe context, not only the small chart reaction. | 02:24-03:32: treat daily/weekly-level horizontal lines as stronger context than a 15-minute break alone. | 03:18-03:32: use higher-timeframe close/confirmation before treating the break as actionable. | not stated | not stated | 01:32-02:28: if a lower-timeframe break conflicts with the higher-timeframe line, treat it as likely damashi/routing risk. | 02:24-03:32: align the break judgment with the timeframe that created the horizontal line. | not stated | 03:32-04:26: waiting for confirmation can widen stop distance and hurt RR, so entry timing must account for that trade-off. | not stated | Stop and TP placement are not defined in this audited passage. | 02:24-03:32: Conditional scope is the line's originating timeframe; contradiction not identified. | direct_mechanical_rule | high | first_batch_candidate |
| CES2xzjeOTk | 【勝率爆上げ】本物のブレイクアウトを見極めるコツ | regular_video | auto_caption | audited | 00:10-00:33; 01:39-02:16; 08:32-09:33; 10:42-11:03 | 08:32-09:33: a break of a higher-timeframe line should wait for at least 1H and ideally 4H candle confirmation. | 00:10-00:21: breakout setup is defined as price breaking a recent high/low line and then extending in that direction. | 08:32-09:33: wait for higher-timeframe body confirmation before judging the breakout usable. | 10:42-11:03: stop placement is adjusted narrower when the TP/stop ratio would otherwise be poor. | 06:01-06:14: TP location must be decided explicitly because breakout exits are not automatically determined by wave structure. | 01:39-02:16: skip breaks when wave shape suggests damashi rather than continuation. | 08:32-09:33: line-break judgment is anchored to 1H/4H confirmation. | not stated | 10:42-11:03: compare stop and TP ratio and narrow the stop if RR would otherwise be unacceptable. | not stated | Exact TP anchor is discussed as needing separate decision; the audited passage does not give a universal TP formula. | 08:32-11:03: Conditional scope is higher-timeframe confirmation plus acceptable RR; contradiction not identified. | direct_mechanical_rule | high | first_batch_candidate |
| CPKh323IyO8 | 【リスクリワードの嘘】勝率と報酬の「最適なバランス」を見つけて聖杯を作る方法 | regular_video | auto_caption | audited | 00:01-00:29; 02:18-02:34; 03:12-04:36 | 00:01-00:29: RR should be adjusted to the market-provided price room rather than fixed at a universal 1:2 target. | not stated | not stated | 02:18-02:34: example uses the 3-wave origin as the stop anchor, but this is illustrative rather than a full setup rule. | 02:23-02:34: forcing a 100-pip target is criticized when the market room does not support it. | not stated | 01:34-01:48: longer timeframe posture is discussed as a beginner constraint, not a specific entry rule. | not stated | 03:12-04:36: win rate, RR, and position scaling are treated as variables to balance rather than a fixed RR command. | 04:26-04:36: adding positions is discussed as a way to increase reward without changing initial risk, but no complete procedure is specified. | No repeatable entry trigger or universal TP/stop procedure is defined. | 00:01-04:36: Conditional scope is market room, win rate, and trader level; contradiction not identified. | partial_mechanical_rule | medium | later_summary_candidate |
| HuNeo8FfBO8 | 【完全版】エリオット波動1波.2波.3波の見極め方とトレード方法を完全解説 | regular_video | auto_caption | audited | 01:06-01:58; 02:40-03:32; 09:53-10:44 | 09:53-10:44: align the monitored chart's wave with the higher-timeframe wave before targeting the move. | 01:06-01:29: identify wave stage by whether the final pullback high/low is cleanly broken. | 01:38-01:58: avoid first-wave entries and prefer later wave structure after the pattern is more identifiable. | 03:42-03:57: place stop around the relevant wave/timeframe pivot or RR becomes poor. | 02:40-03:32: use the next pullback low/high or defined wave target as the exit area. | 09:53-10:44: only target where monitored and higher-timeframe Elliott waves overlap. | 09:53-10:44: daily/higher-timeframe wave direction must support the monitored timeframe. | not stated | 03:43-04:03: stop must be near the relevant pivot because otherwise RR deteriorates. | not stated | Requires visual wave interpretation; exact quantitative threshold is not defined. | 09:53-10:44: Conditional scope is overlap between higher-timeframe and monitored-timeframe waves; contradiction not identified. | direct_mechanical_rule | high | first_batch_candidate |
| SrWVDh_BpVs | 【流動性の罠】 なぜ「完璧なエントリー」ほど損切りに遭うのか？大口が仕掛けるストップ狩りの全貌 | regular_video | auto_caption | audited | 00:52-02:12; 03:20-05:13 | 03:39-05:13: avoid entering during the sweep; wait for higher-timeframe target context and a confirmed recovery beyond the reference foot. | 00:52-02:12: clustered stops below a textbook pattern can become fuel for a large participant's intended move. | 04:48-05:13: only consider entry after the reference foot closes back beyond the level following the sweep. | not stated | not stated | 04:10-04:52: distinguish a quick stop sweep that returns by wick from a real break that builds sideways below the line. | 03:39-04:10: first identify the higher-timeframe target line before judging the local sweep. | not stated | not stated | not stated | It explains liquidity/sweep behavior and entry avoidance, but does not define TP or own-stop placement. | 03:39-05:13: Conditional scope is a clustered stop area quickly reclaimed after a sweep; contradiction not identified. | direct_mechanical_rule | high | first_batch_candidate |
| V8DoVtiE-0Y | 【完全版】損切り・利確とリスクリワードの決め方 | regular_video | auto_caption | audited | 01:08-02:30; 02:56-03:53 | 01:08-02:30: do not enter unless stop and TP can be defined from the pattern or wave structure. | 01:08-01:26: avoid entries where the stop cannot be clearly decided in advance. | not stated | 01:26-01:54: for wave/pattern entries, use the wave origin or pattern-defined line as the stop anchor. | 01:54-02:30: use the pattern/wave-defined target, such as the 1-wave measured move for a 3-wave entry. | not stated | not stated | not stated | 03:28-03:53: compare the stop/TP plan with RR expectations before accepting the trade. | 02:56-03:14: if later price action suggests a larger wave, discretionary earlier or extended exit may be considered. | Entry trigger itself is not defined; exit adjustment includes discretionary reading of price action. | 01:26-02:30: Conditional scope is whether the setup is wave-based or chart-pattern-based; contradiction not identified. | direct_mechanical_rule | high | first_batch_candidate |
| e4N22IkeOs4 | 【超簡単】レンジ相場を簡単に攻略する裏技 | regular_video | auto_caption | audited | 01:36-03:37; 03:31-04:00 | 02:32-03:23: define a range after upper/lower boundaries have three touches, then prefer the fourth touch rather than late fifth/sixth entries. | 02:32-03:23: range is identified after three upper/lower boundary touches. | 02:55-03:23: target the fourth touch; avoid entering after the pattern is already mature. | not stated | not stated | 01:56-02:27: treat 1H/4H ranges as tradable and very short timeframe ranges as noise. | 01:56-02:27: use 1H/4H for entry and daily/weekly/monthly for environment. | not stated | not stated | not stated | Stop, TP, and invalidation are not defined in the audited passage. | 02:32-03:37: Conditional scope is early range formation before late fifth/sixth touches; contradiction not identified. | direct_mechanical_rule | high | first_batch_candidate |
| iZuUWHc5bcI | 【これで負けない】FX専業が使うエントリー前の最終チェックリストを公開します。 | regular_video | auto_caption | audited | 00:17-02:10; 03:27-04:39; 04:55-05:23 | 00:32-02:10: before entry, require candle close confirmation or compensate with multiple stronger reasons. | 03:27-04:39: require the trade reason's strength to be verbalized, not just the presence of a pattern. | 00:32-02:10: entry should wait for the relevant timeframe's candle close unless other strong reasons exist. | not stated | not stated | 04:05-04:39: compare pattern quality with horizontal time, price action, wave shape, and higher-timeframe resistance. | 00:52-02:10: use the watched timeframe's close as a pre-entry checklist item. | not stated | 04:55-05:23: expectancy check is framed through lot, RR, and win-rate components. | not stated | Checklist contains judgment-heavy items and does not define stop or TP rules. | 01:36-02:10: Conditional scope is waiting for candle close unless stronger multiple reasons exist; contradiction not identified. | direct_mechanical_rule | medium | first_batch_candidate |
| vkaA9MCRlx4 | 【聖杯級】4時間足3波を確実に取るためのEMA戦略 | regular_video | auto_caption | audited | 00:57-03:14; 03:29-06:46 | 02:51-03:14: after an EMA-related setup, skip the trade if the cross flips against the intended direction before confirmation. | 00:57-01:10: the setup is a 4H third-wave attempt using moving-average context. | 02:51-03:14: wait for the reference high to be exceeded and confirmed; skip if the opposite cross appears first. | 03:29-03:54: use the recent pullback low/high as the basic stop anchor. | 05:20-05:44: use visible left-side swing levels as staged TP targets. | 02:12-03:14: avoid immediate touch entries and require confirmation to reduce damashi. | 00:57-01:10: method is scoped to a 4H wave strategy. | 00:57-03:14: moving-average/EMA relationship is part of the setup and skip condition. | 06:08-06:46: RR near half/full TP is checked before deciding whether to widen the stop. | 05:20-06:17: split exits are considered between first and second visible swing targets. | TP/stop still require visual swing judgment; the transcript says some discretion remains. | 02:51-03:14: Conditional scope is confirmation before entry and skip on opposite cross; contradiction not identified. | direct_mechanical_rule | high | first_batch_candidate |
| Mg09uk9I9JM | 【FX必須スキル】ポジションを持ってる時の途中利確・損切りのやり方 | regular_video | auto_caption | audited | 01:03-01:18; 03:45-04:05; 05:23-05:45; 06:44-07:16 | 01:03-01:18: mid-trade discretion is organized into three criteria rather than treated as ad hoc reaction. | 03:45-04:05: manage position when the original reason is breaking down rather than holding as a gamble. | not stated | 03:45-04:05: exit or reduce when the initial trade premise breaks. | 00:34-01:11: mid-trade partial profit/stop decisions are the topic, but a universal TP level is not defined. | 05:23-05:45: judge whether the post-entry path still matches the intended reversal/pattern premise. | 06:44-07:16: 1H and especially 4H candle close can change the flow and inform management. | not stated | not stated | 01:03-01:18: use horizontal time, premise strength, and candle confirmation as mid-trade management criteria. | The video is management-focused and explicitly leaves some strength/path reading to judgment. | 03:45-04:05: Conditional scope is reducing/exiting when the original premise weakens; contradiction not identified. | partial_mechanical_rule | medium | later_summary_candidate |

Timestamps are navigation references only. Claims are paraphrased and intentionally omit transcript quotations, subtitle blocks, and caption URLs.

## 5. Proposed First Summary Batch

Only audited rows that passed the evidence standard are eligible for `first_batch_candidate`.

| video_id | source_title | audited_class | confirmed_strong_dimensions | timestamp-supported inclusion reason |
| --- | --- | --- | --- | --- |
| 16Kb39TFFek | 【負けを激減】FX専業も使う水平線の抜け判断の見極め方 | direct_mechanical_rule | setup_context;entry_trigger;trend_range_filter;timeframe_session;risk_reward | 02:24-03:32: horizontal-line breakout validity depends on the line's higher-timeframe context, not only the small chart reaction. |
| CES2xzjeOTk | 【勝率爆上げ】本物のブレイクアウトを見極めるコツ | direct_mechanical_rule | setup_context;entry_trigger;stop_invalidation;tp_exit;trend_range_filter;timeframe_session;risk_reward | 08:32-09:33: a break of a higher-timeframe line should wait for at least 1H and ideally 4H candle confirmation. |
| HuNeo8FfBO8 | 【完全版】エリオット波動1波.2波.3波の見極め方とトレード方法を完全解説 | direct_mechanical_rule | setup_context;entry_trigger;stop_invalidation;tp_exit;trend_range_filter;timeframe_session;risk_reward | 09:53-10:44: align the monitored chart's wave with the higher-timeframe wave before targeting the move. |
| SrWVDh_BpVs | 【流動性の罠】 なぜ「完璧なエントリー」ほど損切りに遭うのか？大口が仕掛けるストップ狩りの全貌 | direct_mechanical_rule | setup_context;entry_trigger;trend_range_filter;timeframe_session | 03:39-05:13: avoid entering during the sweep; wait for higher-timeframe target context and a confirmed recovery beyond the reference foot. |
| V8DoVtiE-0Y | 【完全版】損切り・利確とリスクリワードの決め方 | direct_mechanical_rule | setup_context;stop_invalidation;tp_exit;risk_reward;trade_management | 01:08-02:30: do not enter unless stop and TP can be defined from the pattern or wave structure. |
| e4N22IkeOs4 | 【超簡単】レンジ相場を簡単に攻略する裏技 | direct_mechanical_rule | setup_context;entry_trigger;trend_range_filter;timeframe_session | 02:32-03:23: define a range after upper/lower boundaries have three touches, then prefer the fourth touch rather than late fifth/sixth entries. |
| iZuUWHc5bcI | 【これで負けない】FX専業が使うエントリー前の最終チェックリストを公開します。 | direct_mechanical_rule | setup_context;entry_trigger;trend_range_filter;timeframe_session;risk_reward | 00:32-02:10: before entry, require candle close confirmation or compensate with multiple stronger reasons. |
| vkaA9MCRlx4 | 【聖杯級】4時間足3波を確実に取るためのEMA戦略 | direct_mechanical_rule | setup_context;entry_trigger;stop_invalidation;tp_exit;trend_range_filter;timeframe_session;indicator_condition;risk_reward;trade_management | 02:51-03:14: after an EMA-related setup, skip the trade if the cross flips against the intended direction before confirmation. |

## 6. Short And Duplicate Handling

Shorts are outside this first bounded audit, not permanently excluded. The 8 possible Short relationships remain provisional routing links only, with no asserted parent-child relationship.

| short_video_id | possible_related_video_id | routing_basis |
| --- | --- | --- |
| GB7wgE3GZtc | KEE4Dk8LM1A | title/topic/method overlap only; not confirmed parent-child |
| HbnU3Ee3qic | DeRVQNJtq3s | title/topic/method overlap only; not confirmed parent-child |
| S3Z3W7bRdoM | HuNeo8FfBO8 | title/topic/method overlap only; not confirmed parent-child |
| SWDGYUMPvN8 | k2_pm_TPgh0 | title/topic/method overlap only; not confirmed parent-child |
| qNcZIRfNueg | SrWVDh_BpVs | title/topic/method overlap only; not confirmed parent-child |
| rj4lZBlUf8s | vkaA9MCRlx4 | title/topic/method overlap only; not confirmed parent-child |
| tx4h1_ZSvXA | HuNeo8FfBO8 | title/topic/method overlap only; not confirmed parent-child |
| wESvPcbu2CM | e4N22IkeOs4 | title/topic/method overlap only; not confirmed parent-child |

## 7. Validation

| validation item | status |
| --- | --- |
| frozen target count remains | 115 |
| frozen hash unchanged | ad2eb82ee4d351fc41e1ceb79367a278779399d85e1e920ee66c42fd614948ed |
| ledger rows | 115 |
| audited rows | 10 |
| caption-available not_audited rows | 102 |
| unavailable rows | 3 |
| every audited assertion has timestamp reference | passed |
| unaudited rows claim confirmed strong dimensions | no |
| every first_batch_candidate is audited | passed |
| raw transcript/subtitle committed | no |
| data/results/CSV/JSON/video/audio committed | no |
| Strategy A/B changes | no |
| backtests run | no |
