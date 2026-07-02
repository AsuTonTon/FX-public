# Strategy A Real Data Read-only Validation Plan

## 目的

Strategy A: Core Mechanical を、実データ取得API・ブローカーAPI・発注・自動売買なしで、手元の4時間足OHLC CSVに対して読み取り専用で検証できる土台を作る。

この基盤は収益性を断定するものではない。出力される成績は、指定CSVと固定ルールに対する機械的な検証結果であり、将来の成績や実運用可能性を示すものではない。

## 実装範囲

- ローカルCSV読み込み: `src/backtest/csv_loader.py`
- ペア別設定読み込み: `src/backtest/pair_config.py`
- Strategy A RR比較ランナー: `src/backtest/strategy_a_runner.py`
- ペア設定例: `config/strategy_a_pairs.example.json`
- テスト:
  - `tests/test_csv_loader.py`
  - `tests/test_pair_config.py`
  - `tests/test_strategy_a_runner.py`

Strategy B/C は実装しない。

## 禁止事項

- 実データ取得APIの呼び出し
- ブローカーAPI連携
- 発注処理
- 自動売買
- 実資金運用
- Strategy B/C の実装
- 収益性の断定

## 4時間足OHLC CSV入力仕様

1ファイルにつき1通貨ペアを想定する。推奨ファイル名は以下。

- `EURUSD_4h.csv`
- `USDJPY_4h.csv`
- または `EURUSD.csv`, `USDJPY.csv`

必須列:

| 列 | 内容 |
|---|---|
| `timestamp` | 足の時刻。`time`, `datetime`, `date` も許容 |
| `open` | 始値 |
| `high` | 高値 |
| `low` | 安値 |
| `close` | 終値 |

入力ルール:

- 文字コードは `UTF-8` または `UTF-8 with BOM` を想定。
- タイムスタンプはISO形式を推奨。例: `2026-01-01T00:00:00`
- 行は古い足から新しい足へ昇順に並べる。
- タイムスタンプ重複は不可。
- `high >= open/close`、`low <= open/close`、`high >= low` を満たすこと。
- 各行は確定済みの4時間足のみを入れること。
- 週末・祝日などによる時間ギャップは、実データCSV側の仕様として扱う。

最小例:

```csv
timestamp,open,high,low,close
2026-01-01T00:00:00,1.1000,1.1050,1.0980,1.1020
2026-01-01T04:00:00,1.1020,1.1060,1.1010,1.1040
```

## ペア別設定

ペア別に以下を設定する。

| 項目 | 内容 |
|---|---|
| `tick_size` | 最小価格単位 |
| `assumed_spread` | 検証で仮定するスプレッド |
| `buffer` | 損切りに加えるバッファ。省略時は `assumed_spread + tick_size` |

設定例:

```json
{
  "pairs": {
    "USDJPY": {
      "tick_size": 0.001,
      "assumed_spread": 0.015
    },
    "EURUSD": {
      "tick_size": 0.00001,
      "assumed_spread": 0.0001
    },
    "GBPUSD": {
      "tick_size": 0.00001,
      "assumed_spread": 0.00015
    },
    "AUDUSD": {
      "tick_size": 0.00001,
      "assumed_spread": 0.00012
    },
    "USDCAD": {
      "tick_size": 0.00001,
      "assumed_spread": 0.00015
    },
    "USDCHF": {
      "tick_size": 0.00001,
      "assumed_spread": 0.00015
    },
    "EURJPY": {
      "tick_size": 0.001,
      "assumed_spread": 0.02
    },
    "GBPJPY": {
      "tick_size": 0.001,
      "assumed_spread": 0.03
    }
  }
}
```

初期例は8ペアのみ。上記の値は入力形式を示すための仮定値であり、現在の実スプレッドや推奨値ではない。

## RR比較ランナー

ローカルCSVに対して、Strategy AをRR別に実行する。

既定RR:

- `1.0`
- `1.5`
- `2.0`
- `3.0`

実行例:

```bash
python -m src.backtest.strategy_a_runner \
  --input-dir data/strategy_a_ohlc \
  --pair-settings config/strategy_a_pairs.example.json \
  --output-dir results/strategy_a_readonly \
  --pairs EURUSD USDJPY
```

このコマンドはローカルCSVを読むだけで、外部API・ブローカー・発注機能には接続しない。
CSVのタイムスタンプ間隔は、4時間の正の倍数であることを検証する。4時間足として扱えない間隔がある場合はvalidation errorとして停止する。

## 出力

指定した出力ディレクトリに以下を作成する。

```text
results/strategy_a_readonly/
  summary.md
  trades/
    EURUSD_rr_1_0_trades.csv
    EURUSD_rr_1_5_trades.csv
  events/
    EURUSD_rr_1_0_events.csv
    EURUSD_rr_1_5_events.csv
  metrics/
    EURUSD_rr_1_0_metrics.json
    EURUSD_rr_1_5_metrics.json
    metrics_comparison.csv
```

`summary.md` にはRR別の比較表を出す。ただし、結果は検証対象CSVに対する機械的な集計であり、収益性の断定には使わない。

## 評価指標

既存の `calculate_metrics()` を使い、以下を出力する。

- `trade_count`
- `win_rate`
- `average_r`
- `median_r`
- `profit_factor`
- `max_consecutive_losses`
- `max_drawdown_r`
- `total_r`
- `yearly_r`

## 既知の制約

- CSV内の価格が買値/売値のどちら由来かは判定しない。
- スプレッド・手数料・スリッページは、現時点では `buffer` による損切り側の保守化だけで表現する。
- エントリー価格は確認足の次足始値で固定。
- TP/SLが同一足で両方到達した場合は、既存エンジンの保守設定によりSL優先。
- 年末年始、指標発表、週末クローズなどの売買停止条件は未実装。
- 実データCSVの品質やデータ提供元の仕様は別途確認が必要。

## 次に必要な確認

1. 使用するCSVの提供元、タイムゾーン、足確定時刻を記録する。
2. 各ペアの `tick_size`, `assumed_spread`, `buffer` を固定する。
3. 同一データでRR 1.0 / 1.5 / 2.0 / 3.0 を比較し、結果が過剰最適化になっていないか確認する。
4. 取引コスト、スリッページ、週末・指標発表除外を別仕様として追加するか判断する。
5. Strategy B/Cへ進む前に、Strategy Aの基礎挙動とイベントログを確認する。
