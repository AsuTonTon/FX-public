# Strategy A Validation Report

対象実装:

- `src/strategies/ema_wave3_strategy_a.py`
- `src/backtest/engine.py`
- `src/backtest/metrics.py`
- `src/backtest/trade.py`
- `tests/test_ema_wave3_strategy_a.py`
- `tests/test_backtest_metrics.py`
- `docs/video_research/vkaA9MCRlx4/strategy_a_implementation_notes.md`

このレポートは、Strategy A: Core Mechanical の実装品質とテスト通過状況を確認するもの。実データ取得、ブローカーAPI連携、自動売買、Strategy B/C 実装は行っていない。収益性は評価しない。

## pytest実行結果

実行コマンド:

```bash
python -B -m pytest
```

結果:

```text
17 passed in 0.41s
```

## 品質チェック結果

### ruff check

実行コマンド:

```bash
python -m ruff check src tests
```

結果:

```text
All checks passed!
```

### ruff format --check

実行コマンド:

```bash
python -m ruff format --check src tests
```

結果:

```text
9 files already formatted
```

### black --check

実行コマンド:

```bash
python -m black --check src tests
```

結果:

```text
No module named black
```

判定: black は環境に未導入。無理に追加せず、ruff formatで代替確認済み。

### mypy

実行コマンド:

```bash
python -m mypy src tests
```

結果:

```text
Success: no issues found in 9 source files
```

## 実装ファイル一覧

- `src/strategies/ema_wave3_strategy_a.py`
  - Strategy AのEMA計算、クロス判定、初回20EMAタッチ、基準足実体抜け、失効、EntryOrder生成。
- `src/backtest/engine.py`
  - 足ベースのTP/SL/end_of_data決済、同一足TP/SL時の保守的SL優先、実行済みentry/exitイベント記録。
- `src/backtest/metrics.py`
  - R倍数ベースの集計指標。
- `src/backtest/trade.py`
  - OHLCBar、Trade、EntryOrder、BacktestEvent、BacktestResultなどのデータ構造。
- `tests/test_ema_wave3_strategy_a.py`
  - Strategy Aのシグナル生成・失効・エントリー・TP/SL/end_of_dataテスト。
- `tests/test_backtest_metrics.py`
  - metrics計算テスト。
- `docs/video_research/vkaA9MCRlx4/strategy_a_implementation_notes.md`
  - 実装仕様、変更点、未実装点、テスト方法、次ステップ。

## 仕様通りに実装できた点

### A. Future leak / lookahead bias

- EMAは終値系列から再帰的に計算しており、各足のEMA値は過去値と現在終値だけで決まる。
- Strategy Aではスイング抽出を使っていないため、スイング由来の未来足参照はない。
- クロス判定は前足EMAと現在足EMAのみ。
- 20EMAタッチ判定は現在足の `low <= ema20 <= high` のみ。
- 実体抜け判定は現在足終値と基準足高値/安値のみ。
- エントリー価格は確認足ではなく次足始値。
- バックテストのTP/SL判定はエントリー足以降のみ。

判定: future leakリスクは低い。

### B. Entry logic

- ゴールデンクロス: 前足 `ema20 <= ema200`、現在足 `ema20 > ema200`。
- デッドクロス: 前足 `ema20 >= ema200`、現在足 `ema20 < ema200`。
- クロス後、最初の20EMAタッチだけを基準足として保存。
- 2回目以降の20EMAタッチは `ignored_touch` イベントとして記録し、基準足を更新しない。
- ロングは基準足後、終値が基準足高値を上回る場合のみ確認。
- ショートは基準足後、終値が基準足安値を下回る場合のみ確認。
- 確認足の次足始値でEntryOrderを生成。

判定: Strategy A仕様どおり。

### C. Expiration logic

- クロス後30本を超えて20EMAタッチがない場合、`touch_timeout` で失効。
- 基準足後10本を超えて実体抜けがない場合、`confirmation_timeout` で失効。
- 実体抜け前に反対クロスが出た場合、`opposite_cross` で失効。

判定: Strategy A仕様どおり。

### D. Backtest execution

- ロングは `low <= stop` でSL、`high >= take_profit` でTP。
- ショートは `high >= stop` でSL、`low <= take_profit` でTP。
- 同一足でTP/SLが両方到達した場合、`conservative_same_bar=True` の初期設定ではSL優先。
- TP到達時は `+RR`、SL到達時は `-1R`。
- 最終足までTP/SLに到達しない場合は `end_of_data` として終値でR倍数を計算。
- 約定済みentryイベントはBacktestEngine側で記録するよう調整済み。

判定: 最小足ベースエンジンとして仕様どおり。OHLC内の約定順序は分からないため、同一足TP/SLは保守的処理。

### E. Metrics

- `trade_count`: R倍数が入っているTrade数。
- `win_rate`: R倍数が正のトレード比率。
- `average_r`: R倍数平均。
- `median_r`: R倍数中央値。
- `profit_factor`: 正R合計 / 負R絶対値合計。負けがなく勝ちがある場合は `inf`。
- `max_consecutive_losses`: 連続負け最大数。
- `max_drawdown_r`: 累積Rのピークからの最大低下幅。
- `total_r`: R倍数合計。
- `yearly_r`: exit_timeから抽出できる年ごとのR合計。

判定: pytestで期待値検証済み。

## 仕様から変更した点

- `buffer` は `spread + 1 tick` 自動計算ではなく、固定価格幅パラメータとした。tick sizeやspread定義が未確定のため。
- TP/SLが同一足で両方到達した場合はSL優先とした。仕様内では足内順序が未定義のため、保守的な仮定。
- TP/SL未到達のままデータ末尾に来た場合は `end_of_data` 終値決済とした。テスト可能性のための明示処理。
- テストfixtureではEMAクロスを短いデータで発生させるため、`fast_period=2`, `slow_period=3` を使用。本番デフォルトは `20/200` のまま。
- レビュー中に、entryイベントはシグナル生成側ではなくBacktestEngine側で実行済みイベントとして記録する形に調整した。
- レビュー中に、mypy対応としてテスト補助関数 `make_bars` の型注釈を `Sequence[float]` に変更した。
