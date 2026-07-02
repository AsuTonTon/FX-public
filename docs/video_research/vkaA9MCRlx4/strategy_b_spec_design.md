# Strategy B Spec Design

## 0. Scope

This document starts the specification work for **Strategy B: Video-like Mechanical**.

It does not implement Strategy B. It only defines the additional rule components that should be fixed before coding.

Inputs reviewed:

- `docs/video_research/vkaA9MCRlx4/backtest_spec_v1.md`
- `docs/video_research/vkaA9MCRlx4/strategy_a_result_diagnostics.md`
- `docs/video_research/vkaA9MCRlx4/strategy_a_realdata_readonly_validation_report.md`

Guardrails:

- No market-data API.
- No broker API.
- No auto-trading.
- No order placement.
- No real-money handling.
- No Strategy C implementation.
- No profitability claim.

Strategy B should be treated as a research specification, not as a trading recommendation.

## 1. Strategy A Baseline Findings

Strategy A intentionally used only the mechanical core:

1. EMA20 / EMA200 cross.
2. First 20EMA touch after the cross.
3. Body-close break of the reference candle.
4. Fixed RR exit.

The real-data diagnostics suggest the following design lessons for Strategy B:

- Strategy A is useful as a baseline and should not be discarded yet.
- Several Profit Factor values are close to `1.0`, so any Strategy B improvement must be tested for robustness, not just headline total R.
- Higher RR settings can improve total R in some samples but increase drawdown and losing streak risk.
- RR3.0 especially needs concentration checks because some results depend heavily on specific years or regimes.
- Strategy B should therefore focus on trade-quality filtering, target realism, and risk-shape improvement rather than simply optimizing RR.

## 2. Elements Added From Strategy A

| Element | Strategy A | Strategy B Design Goal |
| --- | --- | --- |
| Take profit | Fixed RR full exit | Left-side swing targets |
| Minimum RR | None except tested RR scenario | Pre-entry quality gate |
| Stop buffer | Pair buffer | ATR-aware buffer |
| Position exit | Full TP or SL | Partial TP, final TP, break-even movement |
| Range filter | None | ADX or EMA-slope based no-trade condition |
| Diagnostics | RR comparison | Component-level comparison versus Strategy A |

Strategy B must keep the Strategy A setup logic unchanged unless a rule below explicitly changes trade management or filtering.

Unchanged from Strategy A:

- Timeframe: 4H.
- EMA calculation: close-based EMA20 and EMA200.
- Cross detection:
  - Long setup after EMA20 crosses above EMA200.
  - Short setup after EMA20 crosses below EMA200.
- First 20EMA touch after cross becomes the reference candle.
- Body-close break confirms the setup.
- Entry is the next candle open after confirmation.
- One position per pair.
- EMA warmup remains active.
- Strategy B/C discretionary judgment is not mixed into Strategy A results.

## 3. Left-Side Swing Take Profit

### Purpose

Replace fixed RR take profit with mechanical targets that approximate the video's left-side liquidity or prior-wave target idea.

### Swing Definition

Use only candles available before the confirmation candle. No future candles may be used.

Initial fixed definition:

- Swing high: candle high is greater than the highs of `2` candles to the left and `2` candles to the right.
- Swing low: candle low is lower than the lows of `2` candles to the left and `2` candles to the right.
- A swing candidate is valid only if its right-side confirmation candles are already closed before the Strategy B confirmation candle.

This avoids future leakage while still using a simple fractal-style swing definition.

### Target Selection

Long:

- TP1 is the nearest valid left-side swing high above entry.
- TP2 is the next valid left-side swing high above TP1.

Short:

- TP1 is the nearest valid left-side swing low below entry.
- TP2 is the next valid left-side swing low below TP1.

Lookback window:

- Initial fixed value: `100` closed 4H candles before the confirmation candle.
- If no valid TP1 exists in the window, skip the trade.
- If TP1 exists but TP2 does not, use the fallback rule in Section 6.

### Price Handling

The target price is the swing high or swing low itself.

Execution assumption for backtest:

- Long TP is hit when candle high reaches the target.
- Short TP is hit when candle low reaches the target.
- Same-candle ambiguity must be handled conservatively, with stop-loss priority unless explicitly changed before implementation.

## 4. Minimum RR Gate

### Purpose

Avoid trades where the left-side target is too close relative to risk.

Risk per unit:

- Long risk = `entry_price - stop_price`.
- Short risk = `stop_price - entry_price`.
- If risk is `<= 0`, skip.

Initial fixed thresholds:

- TP1 minimum RR: `1.0R`.
- TP2 minimum RR: `1.5R` when TP2 exists.
- If TP2 does not exist, TP1 must be at least `1.5R` and the trade exits fully at TP1.

No optimization rule:

- Do not tune these thresholds per pair.
- Do not choose thresholds after inspecting the Strategy B results.
- If sensitivity is needed later, compare a small predefined set such as `TP1 >= 0.8R / 1.0R / 1.2R`, but keep the first implementation at `1.0R`.

## 5. ATR Buffer

### Purpose

Make stop placement less fragile than a fixed spread-plus-tick buffer.

ATR definition:

- ATR period: `14`.
- Timeframe: 4H.
- True Range:
  - `high - low`
  - `abs(high - previous_close)`
  - `abs(low - previous_close)`
- ATR calculation should use only current and past closed candles.

Initial buffer:

```text
buffer = max(pair_buffer, 0.10 * ATR(14), tick_size)
```

Stop placement:

- Long stop = reference swing low or reference candle low minus buffer.
- Short stop = reference swing high or reference candle high plus buffer.

Initial minimum Strategy B should choose one stop anchor before implementation. Recommended first anchor:

- Long: min(reference candle low, nearest valid left-side swing low below reference candle) minus buffer.
- Short: max(reference candle high, nearest valid left-side swing high above reference candle) plus buffer.
- If no stop-side swing exists in the lookback window, use the reference candle high/low with ATR buffer.

Stop-width sanity check:

- Skip if stop distance is less than `0.25 * ATR(14)`.
- Skip if stop distance is greater than `3.0 * ATR(14)`.

These thresholds are inherited from `backtest_spec_v1.md` and must be frozen before implementation.

## 6. Partial TP / Final TP

### Purpose

Approximate the video's more flexible target handling without using manual chart judgment.

Initial fixed split:

- TP1: close `50%`.
- TP2: close remaining `50%`.

If TP2 exists:

- Trade outcome is a weighted R result:
  - First half gets TP1 R.
  - Second half exits at TP2, break-even, or stop according to the management rules.

If TP2 does not exist:

- If TP1 RR is at least `1.5R`, exit `100%` at TP1.
- If TP1 RR is below `1.5R`, skip the trade.

Same-candle rules to freeze:

- If TP1 and stop are both reached in the same candle before TP1 was previously hit, stop-loss is prioritized.
- If TP1 and TP2 are both reached in the same candle, assume TP1 is hit first, then TP2, only if the candle did not also hit the original stop.
- If TP1 and original stop are both touched in the same candle, use stop-loss priority.

These are conservative assumptions and should be documented in test cases during implementation.

## 7. Break-Even Movement After TP1

### Purpose

Reduce tail risk after partial profit while keeping the rule mechanical.

Initial fixed rule:

- After TP1 is reached, move the stop on the remaining `50%` to break-even.
- Break-even price is the original entry price.

Cost-aware option for later sensitivity:

- Long break-even stop = entry price plus one tick.
- Short break-even stop = entry price minus one tick.

Do not implement both variants in the first pass. Use original entry price first to keep Strategy B minimal.

Event outcomes after TP1:

- `tp2`: remaining half exits at TP2.
- `breakeven`: remaining half exits at entry price after TP1.
- `end_of_data`: remaining half exits at final available close if still open.

The first implementation should record these as separate exit details, because Strategy A did not have partial exits.

## 8. Range Exclusion

### Purpose

Strategy A allowed all valid mechanical setups, including likely range conditions. Strategy B should add one predefined range filter.

Initial filter choice:

- Use ADX(14) first.
- Do not combine ADX and EMA slope in the first implementation.

ADX rule:

- Skip entry if ADX(14) at the confirmation candle is below `18`.
- ADX is computed from 4H candles using only closed candles.

EMA slope alternative for later comparison:

- EMA200 slope window: `20` bars.
- Slope unit: ATR-normalized EMA200 change per bar.
- Skip if absolute slope is below `0.03 ATR/bar`.

Why ADX first:

- It is a direct range/trend-strength proxy.
- It has a single threshold.
- It is easier to compare as an on/off filter against Strategy A.

Overfitting guard:

- Do not tune ADX thresholds after looking at pair-level Strategy B performance.
- If sensitivity is later needed, use a predefined set: `16`, `18`, `20`.
- Report all tested thresholds, including bad ones.

## 9. Over-Optimization Risk by Element

| Element | Risk | Why It Can Overfit | Guardrail |
| --- | --- | --- | --- |
| Left-side swing targets | Medium | Different swing widths and lookbacks can select convenient historical targets | Fix fractal width `2` and lookback `100` before testing |
| Minimum RR | Medium | Threshold can be tuned to remove losing trades | Start with TP1 `1.0R`, TP2 `1.5R`; compare only predefined alternatives later |
| ATR buffer | Medium | Buffer multiplier changes stop-out frequency | Start with `0.10 * ATR(14)` and do not tune by pair |
| Partial TP | Medium | Split ratio can reshape results | Start with fixed `50% / 50%` only |
| Break-even movement | Medium | Can improve drawdown while cutting winners depending on sample | Use entry-price break-even first; test cost-aware BE later |
| ADX filter | High | Threshold can easily remove bad historical regimes | Use ADX(14) < `18` as first fixed rule |
| EMA slope filter | High | Slope window and ATR normalization can be tuned | Keep as comparison-only, not first-pass default |

## 10. Comparison Method Against Strategy A

Strategy B should be evaluated against Strategy A, not in isolation.

Required comparison controls:

- Same input CSV files.
- Same pair settings.
- Same EMA warmup.
- Same 4H validation rules.
- Same pair universe.
- Same date ranges.
- Same one-position-per-pair constraint.

Primary metrics:

- trade_count
- win_rate
- average_r
- median_r
- total_r
- profit_factor
- max_drawdown_r
- max_consecutive_losses
- yearly_r
- end_of_data count

Strategy B additional metrics:

- TP1 hit count and rate.
- TP2 hit count and rate.
- break-even count and rate.
- full TP1-only exit count.
- no-trade count by reason:
  - no left-side TP1
  - TP1 below minimum RR
  - TP2 below minimum RR
  - ATR stop too narrow
  - ATR stop too wide
  - ADX range filter
  - overlap open position
- average initial risk in ATR units.
- average TP1 RR.
- average TP2 RR.

Recommended comparison sequence:

1. Re-run Strategy A as baseline on the same local CSVs.
2. Run minimal Strategy B with all parameters fixed.
3. Compare full-period results.
4. Compare yearly results.
5. Compare 1999-2008, 2009-2018, and 2019-2026 blocks.
6. Compare drawdown conversion at `1R = 0.5%`, `1.0%`, and `2.0%`.
7. Run ablation only after the first Strategy B result:
   - B without ADX filter.
   - B without break-even movement.
   - B with fixed RR disabled is not allowed, because B's purpose is swing-target exits.

Important:

- Strategy B should not be declared better just because total R improves.
- It should reduce fragile behavior, improve risk shape, or maintain results across periods.

## 11. Parameters To Freeze Before Implementation

These must be fixed before writing code:

| Parameter | Initial Fixed Value |
| --- | --- |
| timeframe | 4H |
| EMA periods | 20 / 200 |
| EMA warmup | 200 bars |
| ATR period | 14 |
| ATR buffer multiplier | 0.10 |
| swing fractal width | 2 left / 2 right |
| swing lookback | 100 closed bars |
| TP1 minimum RR | 1.0 |
| TP2 minimum RR | 1.5 |
| TP1-only full-exit minimum RR | 1.5 |
| partial close ratio | 50% at TP1, 50% at TP2/BE |
| break-even stop | original entry price |
| ADX period | 14 |
| ADX no-trade threshold | below 18 |
| min stop distance | 0.25 * ATR(14) |
| max stop distance | 3.0 * ATR(14) |
| same-bar TP/SL priority before TP1 | stop-loss first |
| one pair simultaneous positions | one open position per pair |

Do not tune these values after seeing Strategy B results. Any later sensitivity run must be documented as a separate experiment.

## 12. Minimal Strategy B For First Implementation

The first implementation should be the smallest version that is meaningfully closer to the video than Strategy A.

Include:

1. Strategy A setup and entry unchanged.
2. Left-side swing TP1 and TP2.
3. Minimum RR gate.
4. ATR-aware stop buffer.
5. 50% TP1 and 50% final management.
6. Break-even movement after TP1.
7. ADX(14) range exclusion with threshold `18`.
8. New event and no-trade reason logging.

Do not include:

- EMA slope filter in the first pass.
- Regression-slope filter.
- Double top / double bottom detection.
- Manual liquidity-zone scoring.
- Manual support/resistance strength scoring.
- News, session, or weekday filters.
- Parameter search or optimizer.
- Broker integration.
- Automatic order handling.

This makes the first Strategy B implementation testable while avoiding a pile-up of discretionary proxies.

## 13. Discretionary Elements Not Implemented

The following video-like or human-chart-reading elements should remain out of Strategy B first implementation:

- "Clean chart" visual judgment.
- Hand-drawn support/resistance quality.
- Manual wave count.
- Double bottom / double top visual recognition.
- Liquidity sweep interpretation.
- Waiting for a better-looking candle after the signal unless specified as a fixed delay rule.
- Manual target adjustment around round numbers.
- Avoidance based on economic news.
- Session-based discretion.
- Pair-specific parameter tuning.

These belong to later Strategy C-style approximation, if ever tested.

## 14. Implementation Acceptance Criteria

Before Strategy B code is accepted, it should have tests for:

- Swing high / swing low detection using only closed candles.
- No future swing usage.
- TP1 / TP2 selection for long and short.
- Minimum RR pass/fail.
- ATR calculation and ATR buffer.
- Stop-width too narrow / too wide no-trade.
- TP1 partial exit.
- Break-even movement after TP1.
- TP2 final exit.
- Break-even exit after TP1.
- Same-bar ambiguity with conservative stop priority.
- ADX below threshold no-trade.
- Strategy A setup logic unchanged.
- Event/no-trade reason counts.

## 15. Temporary Judgment

Strategy B is worth specifying and testing because Strategy A's results suggest that the core entry logic alone may be thin and regime-sensitive. The next question is whether video-like mechanical additions improve robustness and risk shape without simply overfitting EURUSD and USDJPY.

The correct first Strategy B goal is:

- not to prove profitability,
- not to maximize total R,
- not to find the best ADX or ATR setting,
- but to test whether fixed, video-like mechanics improve the Strategy A baseline in a repeatable way.

