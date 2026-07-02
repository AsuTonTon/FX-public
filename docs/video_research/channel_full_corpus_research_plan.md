# Full-Channel Video Corpus Research Plan

Status: planning only. This document designs the channel-level research phase before any Strategy A/B change.

## 1. Research objective

The current Strategy A/B work is based on a single source video. That is a useful starting point, but it should be treated as a verification hypothesis rather than the full doctrine of the channel.

The objective of the full-channel corpus review is to inventory the channel, summarize each relevant video lightly, classify recurring themes, and extract stable doctrine across videos. The goal is not to import every video rule into the strategy. The goal is to identify which ideas are repeated enough to be considered durable, which ideas were episode-specific, and where the current Strategy A/B interpretation may have misunderstood or oversimplified the channel's intent.

The output of this phase should support later decisions about diagnostics, documentation, or a separate Strategy B2 candidate specification. It must not directly modify Strategy B.

## 2. Why one video is insufficient

One video can explain a coherent setup, but it can still be incomplete as the foundation for a mechanical strategy.

- The explanation may be episode-specific. The video may focus on one setup, market condition, or chart example while assuming prior channel knowledge.
- Some assumptions may be missing. The video may rely on previously explained ideas about wave structure, trend context, range avoidance, or trade management.
- Exit and target interpretation may be incomplete. Terms such as left-side highs/lows, half profit, break-even movement, and final target can depend on examples shown elsewhere.
- Range avoidance may be underdefined. A single video may say to avoid ranges without fully defining mechanical detection rules.
- Discretionary wording can be mistaken for mechanical rules. Phrases such as "noticeable level", "clean wave", or "enough room" need cross-video evidence before being converted into code.

## 3. Why full-channel review is useful

Manual review would realistically focus on 10 to 20 representative videos. Codex-assisted processing makes it practical to consider the full channel, while still preserving a staged review process.

Full-channel review is useful because:

- Repeated claims reveal doctrine. Ideas that appear across many videos are more likely to be part of the channel's stable method.
- Contradictions can be identified. Different videos may define entry, stop, or target behavior differently, and those conflicts should be recorded rather than averaged away.
- Rare but important caveats can be found. Loss patterns, range warnings, and invalidation cases may appear in only a few videos but matter heavily for automation.
- TP, stop, and range concepts may be distributed. Target selection, half profit, break-even handling, and left-side levels may be explained across multiple videos rather than in the Strategy A/B source video alone.

## 4. Why not directly modify Strategy B

Full-channel findings must not be injected directly into Strategy B.

- It avoids overfitting. The full corpus will contain many examples, caveats, and discretionary statements that can become rule bloat if translated too quickly.
- It keeps the Strategy A/B baseline stable. A/B results remain interpretable only if the original hypothesis is preserved.
- It preserves causal traceability. Each future change should cite the claim, supporting videos, and reason for conversion into a mechanical rule.
- It separates diagnosis from implementation. Channel doctrine can explain why Strategy B behaves poorly without immediately changing parameters.
- It keeps a future Strategy B2 separate. If the evidence justifies a revised video-like strategy, it should be specified as B2 and compared against A/B rather than silently replacing B.

## 5. Full video inventory design

Create an inventory from channel metadata without committing raw metadata dumps. Store raw collection output only in ignored local paths, then commit derived summaries or reports.

Inventory schema:

| Field | Purpose |
| --- | --- |
| `video_id` | YouTube video ID. |
| `title` | Video title. |
| `url` | Canonical YouTube URL. |
| `published_at` | Published timestamp or date if available. |
| `duration` | Runtime, preferably ISO 8601 duration or seconds. |
| `transcript_available` | Boolean indicating whether transcript/subtitle text can be retrieved. |
| `transcript_source` | Source type such as YouTube auto captions, manual captions, local transcript, or unavailable. |
| `detected_theme` | Initial theme label or labels from title/transcript screening. |
| `priority` | `high`, `medium`, or `low` based on relevance to Strategy A/B gaps. |
| `notes` | Short derived notes only. Do not store raw transcript text here. |
| `processing_status` | `not_started`, `metadata_only`, `summarized`, `classified`, `reviewed`, or `blocked`. |

Priority rules:

- High: videos about TP, targets, half profit, break-even, left-side highs/lows, 3-wave completion, range avoidance, EMA, or losing patterns.
- Medium: videos about trend context, multiple timeframes, wave structure, risk management, or trade management.
- Low: general mindset, platform usage, news, or videos with no clear relation to Strategy A/B mechanics.

## 6. Lightweight per-video summary format

Each video should receive a derived summary. The summary must be concise and must not include raw transcript, subtitle blocks, or full video text.

Recommended format:

```yaml
video_id:
title:
url:
published_at:
duration:
summary_status: draft | reviewed
primary_themes:
entry_rules:
exit_target_rules:
stop_rules:
range_avoidance:
risk_management:
invalidation:
examples_shown:
mechanical_rule_candidates:
discretionary_only_elements:
relation_to_current_strategy_ab:
confidence_level: low | medium | high
review_notes:
```

Field guidance:

- `entry_rules`: only describe what the video explicitly supports.
- `exit_target_rules`: separate TP1, TP2, half profit, full close, and break-even movement if present.
- `stop_rules`: record anchor, buffer, and discretionary adjustment separately.
- `range_avoidance`: distinguish structural chart warnings from indicator proxies such as ADX.
- `mechanical_rule_candidates`: include only rules that could plausibly be implemented without future-looking information.
- `discretionary_only_elements`: preserve judgment-based ideas without forcing them into code.
- `relation_to_current_strategy_ab`: use `supports`, `contradicts`, `extends`, `unclear`, or `not_relevant`.
- `confidence_level`: based on transcript quality, specificity, and whether the rule is supported by examples.

## 7. Theme taxonomy

Initial broad taxonomy:

- Trend continuation
- Reversal
- Breakout
- Pullback
- Support/resistance
- Liquidity/sweep
- Stop placement
- TP selection
- Risk/reward
- Time-frame alignment
- Session/time-of-day
- Indicator usage
- ADX/trend strength
- Candlestick/price action
- Range/filter logic
- Psychology/mindset
- Trade management
- Invalidation logic
- Discretionary judgment

Channel-specific subthemes and wording examples:

- EMA / moving average
- 20EMA touch
- 200EMA trend filter
- EMA cross condition
- 3-wave / wave structure
- 押し目 / 戻り目
- 利確 / target
- 左側高値安値
- 半利
- 建値
- 損切り
- レンジ回避
- 負けパターン
- 環境認識
- 複数時間足
- トレード管理
- メンタル or discretionary discussion

The broad taxonomy categories are used to prevent narrow cherry-picking around
Strategy B and to keep the corpus review open to channel doctrine outside the
current implementation hypothesis. The channel-specific subthemes preserve the
actual wording used in videos, especially when Japanese terms carry more nuance
than a generic English category. Title-detected themes and transcript-confirmed
themes must remain separate throughout processing. Discretionary, psychology,
and mindset themes are not mechanical evidence unless they define repeatable
rules that can be tested without future-looking information.

Theme assignment rules:

- Allow multiple themes per video.
- Keep title-detected themes separate from transcript-confirmed themes.
- Mark a theme as `weak` if it is inferred from the title only.
- Mark a theme as `strong` only when the video summary includes explicit claims or examples.
- Do not treat motivational or discretionary discussion as mechanical evidence unless it defines a repeatable rule.

## 8. Doctrine extraction method

After lightweight summaries exist, aggregate claims into a doctrine map. A claim should be small enough to evaluate, cite, and compare against current Strategy A/B logic.

Doctrine claim schema:

| Field | Purpose |
| --- | --- |
| `claim_text` | Short paraphrase of the channel claim. |
| `theme` | Taxonomy theme. |
| `supporting_videos` | Video IDs and titles that support the claim. |
| `frequency` | Number of supporting videos. |
| `consistency` | `consistent`, `mixed`, `contradicted`, or `unclear`. |
| `contradictions` | Video IDs or claim IDs that conflict with this claim. |
| `mechanical_feasibility` | `high`, `medium`, or `low`. |
| `risk_of_discretion` | `high`, `medium`, or `low`. |
| `relevance_to_strategy_ab` | Strategy A/B component affected. |
| `suggested_action` | `ignore`, `document`, `diagnose`, or `candidate_for_b2`. |

Extraction workflow:

1. Group per-video claims by theme.
2. Merge duplicate claims only when their meaning matches.
3. Preserve contradictions as first-class findings.
4. Rate mechanical feasibility before discussing implementation.
5. Rate discretion risk before suggesting any Strategy B2 candidate.
6. Assign suggested action without changing strategy code.

Suggested actions:

- `ignore`: unrelated to A/B, too vague, or unsupported.
- `document`: useful context but not suitable for code.
- `diagnose`: useful for explaining current Strategy A/B behavior or failure modes.
- `candidate_for_b2`: repeated, consistent, mechanically feasible, and relevant enough for a future separate spec.

## 9. Strategy A/B gap analysis design

Future analysis should compare channel doctrine with the current Strategy A/B design. The comparison should not change code; it should produce a gap report.

Gap analysis schema:

| Field | Purpose |
| --- | --- |
| `strategy_component` | Strategy A/B component under review. |
| `current_behavior` | Current documented or implemented behavior. |
| `channel_doctrine` | Aggregated channel claim. |
| `supporting_claims` | Doctrine claim IDs and supporting videos. |
| `gap_type` | `aligned`, `missing`, `over_mechanical`, `under_specified`, `contradicted`, or `not_enough_evidence`. |
| `impact_hypothesis` | How the gap may affect entries, exits, risk, or skipped trades. |
| `recommended_next_step` | `no_action`, `document`, `diagnose`, or `spec_b2`. |

Components to compare:

- Strategy A entry logic.
- Strategy B TP1/TP2 logic.
- Stop anchor logic.
- Break-even logic.
- ADX/range proxy.
- First-touch rule.
- EMA cross condition.
- Left-side target interpretation.

Rules for gap interpretation:

- A/B can be simpler than the channel by design. Simplicity is not automatically a defect.
- A gap matters only when the channel doctrine is repeated, relevant, and specific enough to test.
- If the channel uses discretionary language, the gap report should separate "human discretion missing" from "mechanical rule missing".
- If a doctrine claim would require parameter tuning, defer it to B2 design rather than changing Strategy B.

## 10. TP1 selection priority

Current Strategy B diagnostics identify TP1 selection as the main bottleneck. Therefore, videos about target selection should receive the first deep-review pass after inventory creation.

Priority keywords:

- 利確
- 目標値
- 左側高値安値
- 半利
- 建値
- 3波の到達点
- 伸びる波 / 伸びない波

TP1 workflow:

1. Filter inventory for titles and transcript summaries matching priority keywords.
2. Summarize these videos before lower-priority themes.
3. Extract all claims about first target selection, half profit, and break-even movement.
4. Separate left-side level doctrine from RR threshold doctrine.
5. Identify whether target selection depends on wave structure, prior liquidity, support/resistance, or market context.
6. Compare doctrine against current Strategy B TP1/TP2 logic.
7. Produce a TP1-specific gap report before any Strategy B2 specification.

The TP1 pass must avoid parameter optimization. It should explain whether current TP1 interpretation is likely incomplete or misaligned, not search for the most profitable parameter set.

## 11. Storage policy

Raw and large generated materials must remain local-only and ignored.

Local-only paths:

- `data/video_research/channel_inventory_raw/`
- `data/video_research/transcripts_raw/`
- `results/video_research/channel_corpus/`

Allowed in Git:

- Research plans.
- Summary formats.
- Theme taxonomy design.
- Doctrine extraction design.
- Strategy A/B gap analysis design.
- Derived summary reports that do not contain raw transcript, raw subtitle, full video text, or large metadata dumps.

Not allowed in Git:

- Raw transcript text.
- Raw subtitles.
- Full video text.
- Downloaded videos.
- Generated candidate CSVs.
- Market data.
- Result outputs from scans/backtests.
- Large raw metadata dumps.

Operational rules:

- Do not create raw data directories in a PR unless the ignore policy is already active.
- Do not commit files from local-only paths.
- Do not paste transcript blocks into derived reports.
- If a report needs evidence, cite video ID, title, timestamp if available, and a short paraphrase.
- If transcript quality is poor, lower confidence rather than preserving raw text.

## 12. Planned PR sequence

Recommended follow-up PR sequence:

1. Channel video inventory design / plan.
2. Metadata inventory generation.
3. Transcript availability report.
4. Lightweight summary batch process.
5. Theme taxonomy report.
6. Channel doctrine map.
7. Strategy A/B gap analysis against channel doctrine.
8. Strategy B2 candidate spec, only if justified.

Each PR should keep raw collection output local-only. Strategy changes should not appear until after the doctrine map and gap analysis have been reviewed.

## 13. Guardrails

This research phase must obey the following guardrails:

- No market-data API.
- No broker API.
- No auto-trading.
- No order placement.
- No real-money handling.
- No Strategy C.
- No parameter optimization.
- No profitability claims.
- No Strategy A/B code changes.
- No Strategy B parameter changes.
- No raw transcript commits.
- No raw subtitle commits.
- No full video text commits.
- No downloaded video commits.
- No large raw data commits.

The only acceptable output of this phase is planning and derived research design. Any later Strategy B2 work must be proposed as a separate specification with traceable evidence.
