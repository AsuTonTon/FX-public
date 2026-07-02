# Strategy A Implementation Notes

## 実装した仕様

実装対象は `backtest_spec_v1.md` の `Strategy A: Core Mechanical` のみ。

- 4時間足OHLC配列を入力として扱う。実データ取得、ブローカーAPI、発注処理は実装していない。
- EMA(20), EMA(200)を終値ベースで計算する。
- ゴールデンクロスは、前足で `ema20 <= ema200`、現在足で `ema20 > ema200`。
- デッドクロスは、前足で `ema20 >= ema200`、現在足で `ema20 < ema200`。
- 20EMAタッチは `low <= ema20 <= high`。
- クロス後の最初の20EMAタッチだけを基準足にする。
- ロングは、基準足後に終値が基準足高値を上回ったら確認。
- ショートは、基準足後に終値が基準足安値を下回ったら確認。
- エントリー価格は確認足の次足始値。
- 損切りは、ロングが基準足安値 `- buffer`、ショートが基準足高値 `+ buffer`。
- 利確は固定RR。初期値は `1.5R`、`StrategyAConfig.rr_multiple` で変更可能。
- 失効は、クロス後30本以内に20EMAタッチなし、基準足後10本以内に実体抜けなし、実体抜け前の反対クロス。
- バックテストエンジンは、足ベースでTP/SL/end-of-dataを判定し、R倍数を記録する。
- 同じ足でTPとSLの両方に到達した場合は、初期設定では保守的にSLを優先する。
- Metricsは、trade_count、win_rate、average_r、median_r、profit_factor、max_consecutive_losses、max_drawdown_r、total_r、yearly_rを計算する。

## 作成ファイル

- `src/strategies/ema_wave3_strategy_a.py`
- `src/backtest/engine.py`
- `src/backtest/metrics.py`
- `src/backtest/trade.py`
- `tests/test_ema_wave3_strategy_a.py`
- `tests/test_backtest_metrics.py`

## backtest_spec_v1.md から変更した点

- Strategy Aのみを実装し、Strategy B/Cは未実装。
- 入力は実データCSVではなく、テスト用のOHLC配列または辞書配列に限定。
- `buffer` は価格単位の固定値としてパラメータ化した。`spread + 1 tick` の自動計算は、tick sizeやスプレッド定義が未確定のため未実装。
- TP/SLが同一足で両方ヒットした場合の順序は動画内・仕様内で未定義のため、保守的にSL優先とした。
- ポジションが最後の足までTP/SLに到達しない場合は `end_of_data` として終値決済する。
- `bars_held` は、エントリー足で決済した場合を1本として数える。

## 未実装の点

- Strategy B/C。
- 実FXデータ取得。
- ブローカーAPI連携。
- 自動売買、発注、実資金管理。
- スプレッド履歴、手数料、スリッページの実適用。
- ペア別tick sizeの自動判定。
- CSVローダーやレポート出力。
- 複数銘柄をまたいだポートフォリオ集計。
- 左側スイング利確、ATRバッファ、ADX/EMA傾きレンジ除外、ダブルボトム判定。

## テスト方法

```bash
python -m pytest
```

テスト内容:

- ゴールデンクロス検出。
- デッドクロス検出。
- 初回20EMAタッチのみ採用。
- 2回目以降の20EMAタッチ無視。
- 基準足高値を終値で抜けた場合のロング確認。
- 基準足安値を終値で抜けた場合のショート確認。
- 確認足の次足始値エントリー。
- 反対クロス失効。
- 30本/10本失効。
- TP到達時の `+RR`。
- SL到達時の `-1R`。
- Rベースmetrics計算。

## 次に必要な実データ検証ステップ

実データ検証へ進む前に、以下を決める必要がある。

- 対象通貨ペア。
- 4時間足データの取得元。
- スプレッド、手数料、スリッページの扱い。
- tick sizeとbufferの定義。
- 同一足TP/SL同時到達時の約定順序を保守的に扱うか、別シナリオで比較するか。
- 固定RRを `1.0R`, `1.5R`, `2.0R`, `3.0R` で比較する実験設計。

この実装は検証用であり、収益性を示すものではない。
