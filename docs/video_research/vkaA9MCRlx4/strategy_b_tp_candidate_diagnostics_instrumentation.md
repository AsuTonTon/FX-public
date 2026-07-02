# Strategy B TP Candidate Diagnostics Instrumentation

## 1. Purpose

This document records the diagnostics-only instrumentation added after the
Strategy B TP1 selection review.

The goal is to inspect alternative left-side TP candidates for each Strategy B
confirmation candidate. The export helps compare the currently selected nearest
TP1 with the next several valid left-side targets, their R distance, bar
distance from confirmation, and a simple local swing-prominence value.

This is not a Strategy B rule change. It does not create Strategy B2, does not
change parameters, and does not make any profitability claim.

## 2. Guardrails

- No market-data API is implemented.
- No broker API is implemented.
- No auto-trading, order placement, live trading, or real-money handling is
  implemented.
- Strategy C is not implemented.
- No parameter optimization is performed.
- Generated files under `results/` remain local and are not committed.

## 3. Behavior That Must Remain Unchanged

The instrumentation does not change:

- Strategy A-derived setup detection.
- Strategy B confirmation candidate creation.
- ADX, ATR buffer, stop-distance, minimum-RR, or target gates.
- TP1/TP2 selection.
- Trade acceptance or rejection.
- Backtest simulation.
- Trades, events, candidate acceptance, summary metrics, or profitability
  interpretation.

Existing Strategy B still selects targets as follows:

- Long TP1: nearest valid left-side swing high above entry.
- Long TP2: second-nearest valid left-side swing high above entry.
- Short TP1: nearest valid left-side swing low below entry.
- Short TP2: second-nearest valid left-side swing low below entry.

The diagnostics export uses the same ordered target list and writes up to the
first five valid target candidates.

## 4. Output

The Strategy B read-only runner now creates:

`results/strategy_b_readonly/tp_candidates/{PAIR}_strategy_b_tp_candidates.csv`

Example runner command:

```powershell
python -m src.backtest.strategy_b_runner `
  --input-dir data/strategy_a_ohlc `
  --pair-settings config/strategy_a_pairs.example.json `
  --output-dir results/strategy_b_readonly `
  --pairs USDJPY EURUSD
```

The output is local-only diagnostics data. It must not be treated as a trading
recommendation or a proof of profitability.

## 5. CSV Columns

| column | meaning |
| --- | --- |
| `pair` | Pair name passed to the runner. |
| `direction` | Candidate direction, `long` or `short`. |
| `setup_time` | EMA cross setup timestamp. |
| `touch_time` | First 20EMA touch timestamp. |
| `confirmation_time` | Body-close confirmation timestamp. |
| `entry_time` | Next-bar open timestamp. |
| `entry_price` | Next-bar open used by Strategy B. |
| `stop_price` | Stop price computed by current Strategy B rules, if available. |
| `risk` | Absolute entry-to-stop risk, if available. |
| `atr` | ATR value at confirmation. |
| `target_rank` | Rank in current Strategy B target ordering. Rank 1 is current TP1. |
| `target_price` | Candidate left-side swing target price. |
| `target_r` | Candidate target distance divided by risk, if risk is valid. |
| `swing_index` | Source swing candle index in the loaded bar sequence. |
| `swing_kind` | Swing type, `high` for long targets and `low` for short targets. |
| `swing_time` | Source swing candle timestamp. |
| `swing_bar_distance_from_confirmation` | Confirmation index minus swing index. |
| `swing_price_distance_from_entry` | Directional price distance from entry to target. |
| `swing_price_distance_atr` | Directional price distance divided by ATR, if available. |
| `simple_prominence` | Local fractal prominence in price units. |
| `simple_prominence_atr` | Local fractal prominence divided by ATR, if available. |
| `selected_tp1` | `True` for the currently selected TP1 row. |
| `selected_tp2` | `True` for the currently selected TP2 row, when present. |
| `accepted` | Whether the full Strategy B candidate was accepted as a trade. |
| `first_fail_reason` | First failing gate for rejected candidates. Empty when accepted. |

## 6. Simple Prominence Definition

Prominence is intentionally simple and deterministic:

- For a swing high, prominence is swing high minus the maximum high of the
  surrounding `swing_width` candles on each side.
- For a swing low, prominence is the minimum low of the surrounding
  `swing_width` candles on each side minus swing low.
- The value is also normalized by ATR when ATR is available.

The prominence calculation uses only candles already required to confirm the
fractal swing. A target swing is exported only when its right-side swing
confirmation candles are already closed before the Strategy B confirmation
candle.

This is a diagnostic proxy. It does not claim to capture the video's full
discretionary idea of meaningful structure.

## 7. Tests Added

The implementation is covered by tests for:

- TP1/TP2 selection staying unchanged.
- Accepted and rejected candidate decisions staying unchanged for fixtures.
- TP candidate diagnostics marking rank 1 as selected TP1.
- TP candidate diagnostics marking rank 2 as selected TP2 when present.
- Diagnostic R distances matching existing Strategy B target R values.
- Runner writing the `tp_candidates` CSV.
- Prominence being deterministic and left-side only relative to confirmation.

## 8. Next Diagnostic Use

Updated routing after the public diagnostic boundary:

Do not use this instrumentation as the next step for local candidate
comparison, rank review, or review-run preparation. Next local-only diagnostic,
packet, sample, Pass A / Pass B, worksheet, mapping, reveal-table, chart-packet,
or review-run work remains paused under
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md` until
explicit human approval is given after corpus input, visual evidence review, and
doctrine synthesis dependencies are addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.
