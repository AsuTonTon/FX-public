# Strategy A Result Diagnostics

## 0. Scope and Guardrails

- Source outputs: `results/strategy_a_readonly/summary.md`, `metrics/metrics_comparison.csv`, `trades/*.csv`, `events/*.csv`, and `docs/video_research/vkaA9MCRlx4/xm_csv_normalization_report.md`.
- This report analyzes the already generated local CSV outputs only.
- No market-data API, broker API, auto-trading, order placement, real-money handling, or Strategy B/C implementation is included.
- The figures below are mechanical Strategy A validation outputs on the provided XM CSVs. They are not evidence of profitability or live-trading viability.
- `2026` is partial data ending at `2026-06-24T04:00:00`; period and recent-year comparisons should be read with that limitation.

## 1. Normalized Data Check

| pair | data_start | data_end | normalized rows | excluded rows | 4h intervals | gap candidates | duplicates | OHLC issues | missing values |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 1999-01-04T08:00:00 | 2026-06-24T04:00:00 | 42,780 | 7,161 + 1 = 7,162 | 41,323 | 1,456 | False | False | False |
| USDJPY | 1999-01-04T04:00:00 | 2026-06-24T04:00:00 | 42,769 | 7,164 + 1 = 7,165 | 41,311 | 1,457 | False | False | False |

- EURUSD and USDJPY both have 4h as the dominant interval.
- Gap candidates are treated as weekend or market-closure intervals, not as normal 4h candles.
- Adopted price type is XM MT4/MT5 export broker OHLC, with timestamps kept in XM server time.

## 2. RR Result Comparison

| pair | RR | trade_count | win_rate | average_r | median_r | total_r | profit_factor | max_drawdown_r | max_consecutive_losses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 1.0 | 178 | 53.93% | 0.0787 | 1.0000 | 14.0000 | 1.1707 | -7.0000 | 5 |
| EURUSD | 1.5 | 178 | 42.70% | 0.0674 | -1.0000 | 12.0000 | 1.1176 | -9.5000 | 6 |
| EURUSD | 2.0 | 174 | 34.48% | 0.0345 | -1.0000 | 6.0000 | 1.0526 | -19.0000 | 9 |
| EURUSD | 3.0 | 171 | 28.07% | 0.1228 | -1.0000 | 21.0000 | 1.1707 | -25.0000 | 9 |
| USDJPY | 1.0 | 195 | 50.26% | 0.0051 | 1.0000 | 1.0000 | 1.0103 | -10.0000 | 7 |
| USDJPY | 1.5 | 195 | 42.05% | 0.0513 | -1.0000 | 10.0000 | 1.0885 | -14.0000 | 7 |
| USDJPY | 2.0 | 195 | 35.38% | 0.0615 | -1.0000 | 12.0000 | 1.0952 | -12.0000 | 7 |
| USDJPY | 3.0 | 192 | 30.73% | 0.2292 | -1.0000 | 44.0000 | 1.3308 | -24.0000 | 18 |

Observations:
- EURUSD total R is positive in all tested RR settings, but RR2.0 has the weakest total R and larger drawdown than RR1.0/RR1.5.
- USDJPY RR3.0 has the largest total R, but also the largest consecutive loss count and one of the largest drawdowns.
- Profit factor values are close to 1.0 in several settings; this is a thin edge at the R-multiple level and should not be treated as robust without more validation.

## 3. Yearly Performance

### Yearly R Tables

### EURUSD

| year | RR1.0 | RR1.5 | RR2.0 | RR3.0 |
| --- | --- | --- | --- | --- |
| 1999 | -3.00 | -5.00 | -5.00 | -5.00 |
| 2000 | 1.00 | 3.00 | 5.00 | 9.00 |
| 2001 | 3.00 | 2.50 | 4.00 | 7.00 |
| 2002 | -5.00 | -4.00 | -6.00 | -5.00 |
| 2003 | 3.00 | 2.50 | 1.00 | 3.00 |
| 2004 | 0.00 | -0.50 | 1.00 | 4.00 |
| 2005 | -1.00 | -1.50 | 0.00 | 3.00 |
| 2006 | 3.00 | 5.00 | 1.00 | -1.00 |
| 2007 | -3.00 | -3.00 | -3.00 | -3.00 |
| 2008 | 5.00 | 4.00 | 1.00 | 1.00 |
| 2009 | 3.00 | 2.50 | 4.00 | 3.00 |
| 2010 | 2.00 | 1.00 | 2.00 | 4.00 |
| 2011 | 0.00 | -0.50 | -2.00 | 0.00 |
| 2012 | -1.00 | -2.50 | -2.00 | -1.00 |
| 2013 | -1.00 | -1.50 | -6.00 | -6.00 |
| 2014 | 0.00 | 1.00 | -1.00 | 1.00 |
| 2015 | -1.00 | -2.00 | -1.00 | -5.00 |
| 2016 | 1.00 | 0.50 | 2.00 | -3.00 |
| 2017 | 4.00 | 2.00 | -1.00 | -3.00 |
| 2018 | 1.00 | 0.00 | -2.00 | -1.00 |
| 2019 | 1.00 | -1.00 | -2.00 | 1.00 |
| 2020 | 0.00 | 1.00 | 2.00 | 4.00 |
| 2021 | 1.00 | 0.50 | -1.00 | 1.00 |
| 2022 | 1.00 | 3.00 | 5.00 | 5.00 |
| 2023 | 0.00 | 1.50 | 3.00 | 2.00 |
| 2024 | -1.00 | 0.00 | 1.00 | 3.00 |
| 2025 | -1.00 | 0.00 | 1.00 | -1.00 |
| 2026 | 2.00 | 3.50 | 5.00 | 4.00 |
### USDJPY

| year | RR1.0 | RR1.5 | RR2.0 | RR3.0 |
| --- | --- | --- | --- | --- |
| 1999 | -3.00 | -1.50 | 0.00 | 3.00 |
| 2000 | 4.00 | 4.00 | 6.00 | 10.00 |
| 2001 | -6.00 | -5.00 | -4.00 | -2.00 |
| 2002 | 2.00 | 2.00 | -2.00 | 0.00 |
| 2003 | 0.00 | -0.50 | -2.00 | 0.00 |
| 2004 | 3.00 | 5.50 | 5.00 | 9.00 |
| 2005 | 0.00 | -0.00 | 2.00 | 6.00 |
| 2006 | 0.00 | 1.00 | 0.00 | 3.00 |
| 2007 | -2.00 | 0.50 | 2.00 | 5.00 |
| 2008 | 2.00 | 3.50 | 2.00 | 0.00 |
| 2009 | 0.00 | -1.00 | 0.00 | -1.00 |
| 2010 | 2.00 | 1.50 | 0.00 | 2.00 |
| 2011 | -4.00 | -3.50 | -3.00 | -2.00 |
| 2012 | 1.00 | 1.00 | 3.00 | 7.00 |
| 2013 | 0.00 | -1.00 | 0.00 | 0.00 |
| 2014 | -3.00 | -6.50 | -6.00 | -5.00 |
| 2015 | -1.00 | 0.50 | -1.00 | 1.00 |
| 2016 | 0.00 | 1.50 | 0.00 | 2.00 |
| 2017 | 0.00 | 1.50 | 3.00 | 6.00 |
| 2018 | -2.00 | 0.00 | 0.00 | -1.00 |
| 2019 | 2.00 | -1.00 | -1.00 | -3.00 |
| 2020 | -1.00 | -1.00 | -2.00 | -6.00 |
| 2021 | 1.00 | 1.00 | -3.00 | -10.00 |
| 2022 | 0.00 | 0.50 | 1.00 | -2.00 |
| 2023 | 0.00 | -1.50 | -1.00 | 0.00 |
| 2024 | 4.00 | 6.00 | 8.00 | 12.00 |
| 2025 | 3.00 | 3.00 | 5.00 | 9.00 |
| 2026 | -1.00 | -0.50 | 0.00 | 1.00 |

### Year Counts and Extremes

| pair | RR | winning years | losing years | flat years | max winning year | max losing year | recent 5 years 2022-2026 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 1.0 | 14 | 9 | 5 | 2008 / 5.00R | 2002 / -5.00R | 1.00R |
| EURUSD | 1.5 | 17 | 10 | 3 | 2006 / 5.00R | 1999 / -5.00R | 8.00R |
| EURUSD | 2.0 | 15 | 12 | 1 | 2000 / 5.00R | 2002 / -6.00R | 15.00R |
| EURUSD | 3.0 | 16 | 11 | 1 | 2000 / 9.00R | 2013 / -6.00R | 13.00R |
| USDJPY | 1.0 | 10 | 9 | 9 | 2000 / 4.00R | 2001 / -6.00R | 6.00R |
| USDJPY | 1.5 | 16 | 12 | 2 | 2024 / 6.00R | 2014 / -6.50R | 7.50R |
| USDJPY | 2.0 | 10 | 10 | 8 | 2024 / 8.00R | 2014 / -6.00R | 13.00R |
| USDJPY | 3.0 | 14 | 9 | 5 | 2024 / 12.00R | 2021 / -10.00R | 20.00R |

### Three-Period Comparison

| pair | RR | 1999-2008 | 2009-2018 | 2019-2026 |
| --- | --- | --- | --- | --- |
| EURUSD | 1.0 | 3.00R | 8.00R | 3.00R |
| EURUSD | 1.5 | 3.00R | 0.50R | 8.50R |
| EURUSD | 2.0 | -1.00R | -7.00R | 14.00R |
| EURUSD | 3.0 | 13.00R | -11.00R | 19.00R |
| USDJPY | 1.0 | 0.00R | -7.00R | 8.00R |
| USDJPY | 1.5 | 9.50R | -6.00R | 6.50R |
| USDJPY | 2.0 | 9.00R | -4.00R | 7.00R |
| USDJPY | 3.0 | 34.00R | 9.00R | 1.00R |

Notes:
- EURUSD RR3.0 is negative in 2009-2018 and positive in 2019-2026, so the behavior is regime-dependent.
- USDJPY RR3.0 is strong in 1999-2018 but nearly flat in 2019-2026 after the 2021 loss offsets later gains.
- The 2022-2026 block includes partial 2026 and should not be interpreted as a completed five-year sample.

## 4. Exit Reason Analysis

`take_profit`, `stop_loss`, and `end_of_data` come from trade exit records. `no_trade`, `expired_setup`, and `ignored_touch` are event-log counts, because they are setup lifecycle events rather than trade exits.

| pair | RR | take_profit | stop_loss | end_of_data | no_trade events | expired_setup events | ignored_touch events |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 1.0 | 96 | 82 | 0 | 0 | 212 | 1104 |
| EURUSD | 1.5 | 76 | 102 | 0 | 0 | 212 | 1104 |
| EURUSD | 2.0 | 60 | 114 | 0 | 4 | 212 | 1104 |
| EURUSD | 3.0 | 48 | 123 | 0 | 7 | 212 | 1104 |
| USDJPY | 1.0 | 98 | 97 | 0 | 0 | 229 | 1213 |
| USDJPY | 1.5 | 82 | 113 | 0 | 0 | 229 | 1213 |
| USDJPY | 2.0 | 69 | 126 | 0 | 0 | 229 | 1213 |
| USDJPY | 3.0 | 59 | 133 | 0 | 3 | 229 | 1213 |

Observations:
- `end_of_data` is 0 in all tested combinations, so the current closed-trade set did not depend on forced end-of-data exits.
- Higher RR lowers TP count and increases SL count, which is mechanically expected for fixed-RR exits.
- `ignored_touch` is high because only the first 20EMA touch after a cross is valid; later touches are logged and ignored. This is noisy but consistent with the specification.

## 5. Event Log Check

| pair | RR | events_total | setup_started | reference_touch | expired_setup | no_trade | overlap_open_position | ignored_touch | entry | take_profit events | stop_loss events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 1.0 | 2427 | 390 | 365 | 212 | 0 | 0 | 1104 | 178 | 96 | 82 |
| EURUSD | 1.5 | 2427 | 390 | 365 | 212 | 0 | 0 | 1104 | 178 | 76 | 102 |
| EURUSD | 2.0 | 2423 | 390 | 365 | 212 | 4 | 4 | 1104 | 174 | 60 | 114 |
| EURUSD | 3.0 | 2420 | 390 | 365 | 212 | 7 | 7 | 1104 | 171 | 48 | 123 |
| USDJPY | 1.0 | 2655 | 424 | 399 | 229 | 0 | 0 | 1213 | 195 | 98 | 97 |
| USDJPY | 1.5 | 2655 | 424 | 399 | 229 | 0 | 0 | 1213 | 195 | 82 | 113 |
| USDJPY | 2.0 | 2655 | 424 | 399 | 229 | 0 | 0 | 1213 | 195 | 69 | 126 |
| USDJPY | 3.0 | 2652 | 424 | 399 | 229 | 3 | 3 | 1213 | 192 | 59 | 133 |

Event-log interpretation:
- `setup_started` and `reference_touch` counts are stable across RR for each pair, as expected, because setup discovery does not depend on RR.
- `entry`, `take_profit`, `stop_loss`, and `no_trade` vary with RR because open-position duration changes by target distance.
- `overlap_open_position` appears only where a valid signal occurred while an earlier position was still open; counts are low relative to total events.
- No obviously impossible event pattern was found. The high `ignored_touch` count is the main volume driver, and it is explainable by the first-touch rule.

## 6. Risk Evaluation

The following drawdown conversion is a linear R-based approximation. It does not model compounding, leverage limits, margin calls, or live execution differences.

| pair | RR | max DD if 1R=0.5% | max DD if 1R=1.0% | max DD if 1R=2.0% | max consecutive losses | loss streak if 1R=0.5% | loss streak if 1R=1.0% | loss streak if 1R=2.0% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 1.0 | -3.50% | -7.00% | -14.00% | 5 | -2.50% | -5.00% | -10.00% |
| EURUSD | 1.5 | -4.75% | -9.50% | -19.00% | 6 | -3.00% | -6.00% | -12.00% |
| EURUSD | 2.0 | -9.50% | -19.00% | -38.00% | 9 | -4.50% | -9.00% | -18.00% |
| EURUSD | 3.0 | -12.50% | -25.00% | -50.00% | 9 | -4.50% | -9.00% | -18.00% |
| USDJPY | 1.0 | -5.00% | -10.00% | -20.00% | 7 | -3.50% | -7.00% | -14.00% |
| USDJPY | 1.5 | -7.00% | -14.00% | -28.00% | 7 | -3.50% | -7.00% | -14.00% |
| USDJPY | 2.0 | -6.00% | -12.00% | -24.00% | 7 | -3.50% | -7.00% | -14.00% |
| USDJPY | 3.0 | -12.00% | -24.00% | -48.00% | 18 | -9.00% | -18.00% | -36.00% |

Mental-load notes:
- USDJPY RR3.0 has 18 maximum consecutive losses. Even at 1R=1.0%, that is about -18% from the loss streak alone under a linear approximation; at 2R risk it becomes about -36%.
- EURUSD RR2.0/RR3.0 and USDJPY RR3.0 all reach drawdown levels that would be psychologically difficult if risk per trade is too high.
- The risk table argues for keeping any later experimental risk sizing small during research; it does not justify live allocation.

### RR3.0 Concentration Check

| pair | RR3 total_r | largest winning year | largest year share of total | top 3 winning years sum | top 3 share of total | 1999-2018 total | 2019-2026 total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 21.00R | 2000 / 9.00R | 42.9% | 21.00R | 100.0% | 2.00R | 19.00R |
| USDJPY | 44.00R | 2024 / 12.00R | 27.3% | 31.00R | 70.5% | 43.00R | 1.00R |

RR3.0 read:
- EURUSD RR3.0 is meaningfully dependent on a few good years: the top three positive years sum to the same size as the full-period total, meaning other years mostly net out.
- USDJPY RR3.0 is not only one-year dependent, but it is period-dependent: most of the total comes from 1999-2018, while 2019-2026 is close to flat overall.
- RR3.0 therefore needs out-of-sample, pair expansion, and cost/slippage sensitivity before being treated as a stable rule choice.

## 7. Temporary Judgment

### Should Strategy A Be Discarded?

Do not discard it completely yet. Strategy A is useful as a mechanical baseline because it isolates the core EMA cross -> first 20EMA touch -> body-close break idea. However, the current results are not strong enough to treat Strategy A alone as an implementation candidate for live trading.

### Is Strategy B Worth Exploring?

Yes, with caution. Strategy B is worth specifying and testing because the video-like elements that Strategy A deliberately removed, such as range exclusion, left-side swing targets, ATR buffer, partial exits, and breakeven handling, may materially change both trade quality and drawdown shape. That said, Strategy B carries higher overfitting risk and should be tested against Strategy A as a baseline, not tuned until it merely looks better on these two CSVs.

### Additional Validation Needed

- Add more pairs only after keeping the current rules frozen.
- Split evaluation by training/validation/out-of-sample periods, or at minimum compare pre/post 2019 regimes.
- Run cost sensitivity on assumed spread, buffer, and slippage.
- Inspect trade distributions by holding period and year to see whether results are clustered in a few regimes.
- Compare Strategy B rules one component at a time against this Strategy A baseline.

### Bottom Line

Strategy A should be kept as the benchmark baseline, not promoted as a profitable method. Moving to Strategy B has research value, but only if the next test is explicitly framed as robustness testing rather than optimization for this EURUSD/USDJPY sample.

## Generated Artifacts

- Report generated: 2026-06-24 16:32:55 local time
- Output file: `docs/video_research/vkaA9MCRlx4/strategy_a_result_diagnostics.md`
