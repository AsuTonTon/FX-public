# Strategy B Implementation Notes

## Scope

This note documents the first implementation of **Strategy B: Video-like Mechanical**.

The implementation is still local, read-only backtest logic. It does not include:

- market-data API
- broker API
- auto-trading
- order placement
- real-money handling
- Strategy C
- parameter optimization
- profitability claims

## Implemented Files

- `src/strategies/ema_wave3_strategy_b.py`
- `src/backtest/strategy_b_runner.py`
- `tests/test_ema_wave3_strategy_b.py`
- `tests/test_strategy_b_runner.py`
- `docs/video_research/vkaA9MCRlx4/strategy_b_implementation_notes.md`

Supporting type extension:

- `src/backtest/trade.py`

## Implemented Strategy B Rules

Strategy B keeps the Strategy A setup sequence:

1. EMA20 / EMA200 cross.
2. First 20EMA touch after the cross.
3. Body-close break of the reference candle.
4. Entry at the next candle open.

Strategy B adds:

- Left-side swing TP1 / TP2.
- Minimum RR gate.
- ATR(14).
- ATR buffer:

```text
buffer = max(pair_buffer, 0.10 * ATR(14), tick_size)
```

- Stop distance sanity check:

```text
0.25 * ATR(14) <= stop_distance <= 3.0 * ATR(14)
```

- 50% TP1 / 50% final management.
- Break-even stop on the remaining 50% after TP1.
- ADX(14) range filter:

```text
ADX(14) < 18 => no_trade
```

- Detailed `no_trade` reasons.

## Implementation Choices

### ATR

ATR is calculated as a simple rolling average of True Range over the configured period.

True Range uses:

- `high - low`
- `abs(high - previous_close)`
- `abs(low - previous_close)`

This is fixed for the first implementation. Wilder smoothing can be compared later only as a separate documented sensitivity test.

### ADX

ADX is calculated mechanically from 4H candles using only closed candles. The first implementation uses a simple rolling approach for directional movement and DX averaging. It is sufficient for deterministic unit testing and should not be tuned per pair.

### Swings

Swing detection uses a fractal-style rule:

- default width: `2` candles left and `2` candles right
- tests may use a smaller width for compact fixtures

A swing is valid only when its right-side confirmation candles are already closed before the Strategy B confirmation candle. This avoids future swing leakage.

### Stop Anchor

Initial implementation uses:

- Long: nearest valid left-side swing low below the reference candle low; otherwise reference candle low.
- Short: nearest valid left-side swing high above the reference candle high; otherwise reference candle high.

The ATR buffer is then applied outside that anchor.

### Same-Bar Ambiguity

The implementation uses conservative assumptions:

- If stop and TP1 are both hit before TP1 was previously confirmed, stop-loss wins.
- If TP1 and TP2 are hit in the same candle without the original stop being hit, TP1 and TP2 are both credited.
- After TP1, if break-even and TP2 are both hit in the same later candle, break-even wins.

## Changes From `strategy_b_spec_design.md`

The implementation follows the minimal Strategy B scope in the spec with these explicit choices:

- ATR uses simple rolling average, not Wilder smoothing.
- ADX uses simple rolling calculations for the first deterministic implementation.
- Break-even stop is the original entry price, not cost-adjusted entry.
- Strategy B has a dedicated runner/engine because partial exits do not fit the Strategy A full-exit engine cleanly.

## Not Implemented

- EMA slope filter.
- Double top / double bottom detection.
- News filter.
- Session or weekday filter.
- Optimizer.
- Strategy C.
- Live trading.
- Broker execution.
- Parameter search.

## Tests Added

The tests cover:

- swing high / swing low detection
- future swing exclusion
- TP1 / TP2 selection for long and short
- minimum RR pass/fail
- ATR calculation
- ATR buffer selection
- stop too narrow / too wide
- ADX below-threshold `no_trade`
- Strategy A setup index compatibility
- TP1 partial exit
- TP2 final exit
- TP1 then break-even exit
- same-bar stop/TP ambiguity
- Strategy B read-only runner outputs

## Next Validation Step

Post-boundary routing: this section is superseded for task routing by
`strategy_b_public_diagnostic_boundary_while_corpus_incomplete.md`.

Do not use this note to start real-data validation or any local-only diagnostic
run. Next local-only diagnostic, packet, sample, Pass A / Pass B, worksheet,
mapping, reveal-table, chart-packet, or review-run work remains paused under
the public boundary until explicit human approval is given after corpus input,
visual evidence review, and doctrine synthesis dependencies are addressed.

Safe next tasks should remain docs-only and should prefer corpus coverage,
evidence-registry, source-alignment, or boundary/status cleanup work.
