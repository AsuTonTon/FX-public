# XM CSV Normalization Report

## Scope

This report documents read-only normalization of XM MT4/MT5 exported raw CSV files for Strategy A validation.

No raw CSV was modified. No market-data API, broker API, auto-trading, order placement, real-money handling, Strategy B/C logic, or profitability claim is included.

## Normalization Policy

- Input encoding: UTF-16 is accepted for XM raw exports.
- Headerless input is accepted.
- Input format: `YYYY.MM.DD HH:MM,open,high,low,close,volume,spread`.
- Output format: `timestamp,open,high,low,close,volume`.
- Output timestamp format: ISO 8601, for example `1999-01-04T04:00:00`.
- Rows before `1999-01-04T00:00:00` are excluded.
- Latest row is excluded as an unconfirmed-candle candidate.
- Adopted price type: XM MT4/MT5 export broker OHLC.
- Timezone: kept as XM server time.
- This data is not evidence of profitability.

## Summary

| Pair | Raw file | Raw rows | Normalized rows | Excluded before start | Excluded tail candidate | Start | End | Mode interval | 4h intervals | Gap candidates | Duplicates | OHLC issues | Missing values |
|---|---|---:|---:|---:|---:|---|---|---:|---:|---:|---|---|---|
| EURUSD | EURUSDH4.csv | 49942 | 42780 | 7161 | 1 | 1999-01-04T08:00:00 | 2026-06-24T04:00:00 | 4.0h (41323) | 41323 | 1456 | False | False | False |
| USDJPY | USDJPYH4.csv | 49934 | 42769 | 7164 | 1 | 1999-01-04T04:00:00 | 2026-06-24T04:00:00 | 4.0h (41311) | 41311 | 1457 | False | False | False |

## Interval Details

- `4h interval count` is the number of normal H4 transitions.
- `Gap candidates` are intervals of 8 hours or more and are treated as weekend or market-closure candidates.
- Daily-only CSVs and CSVs where 4h is not the primary interval must fail validation.

## Output Files

- `data\strategy_a_ohlc\EURUSD_4h.csv`
- `data\strategy_a_ohlc\USDJPY_4h.csv`

## Interpretation Guardrail

The normalized CSV files are inputs for mechanical, read-only Strategy A validation only. They do not prove profitability or live-trading viability and must not be used as trade instructions.
