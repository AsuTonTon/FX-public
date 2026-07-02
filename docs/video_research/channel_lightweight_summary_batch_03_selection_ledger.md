# Channel Lightweight Summary Batch 03 Selection Ledger

Task: `channel_lightweight_summary_batch_03_selection`

This ledger records a bounded Batch 03 selection audit. Japanese auto captions were used only as local working evidence under ignored paths. This file contains timestamped paraphrases only; it does not contain raw transcript text, subtitle blocks, caption URLs, video, audio, market data, generated data, backtest results, or Strategy A/B changes.

`not stated` means the inspected caption evidence did not support that field strongly enough for this audit.

## Ledger rows

### 14G-U6spfLM

- source_title: 【知らないと損する】高勝率手法でも負ける条件とは？/第142話
- content_type: regular_video
- timestamp references: 06:13-07:32; 07:32-08:15; 08:18-09:50; 10:10-11:20
- setup/context: 4時間足のポンド系ショート事例。2点のダブルトップから黒いネックラインを引き、抜けた波を1波、その後の戻しを2波候補として扱う。ユーロポンドロングとあわせてポンド売り方向の通貨強弱も根拠にする。
- entry: ネックライン抜け後の戻しで赤矢印からショート。ネックラインまで深く戻らないと判断し、多少の戻しを想定して先に入る。
- stop/invalidation: 青ラインに損切りを置いたことは述べるが、そのラインの構造的アンカーは not stated。
- TP/exit: 直近安値方向へ伸びる想定だったが、1時間足の長い下ヒゲ陰線、細かい波で5波終了に見える可能性、関連通貨ペア側の比較を理由に紫矢印で早めに利確する。
- range/trend filter: 4時間足の波形、ネックライン、通貨強弱を複合して方向を判断する。
- timeframe/session: 4時間足チャート。エントリーと利確は足確定1時間前の判断として説明される。 session/time-of-day は not stated。
- indicator usage: not stated.
- RR: not stated.
- trade management: 保有放置ではなく、反対方向を示す下ヒゲや別解釈の波が出た時に早めに利確する管理例。
- discretionary elements: ネックラインまで戻らない判断、通貨強弱の解釈、波の数え方、早期利確判断には裁量が残る。
- relation to Batch 01/02 findings: O1/O3を支持し、B2-O2/B2-O8の構造的出口と早期退出を追加検証する。損切りアンカーはB2-O1を十分には支持しない。
- audited relevance class: direct_mechanical_rule
- confidence: medium
- selection decision and reason: selected_for_batch_03. ネックライン抜け後の戻し、通貨強弱、下ヒゲによる早期利確という反復可能な判断列があるため。

### 5SZn-cM0D4M

- source_title: 【4時間足の衝撃】1日5分のチェックで月100万。チャートに張り付くほど負ける「逆説の真実」【FX講座Part3】
- content_type: regular_video
- timestamp references: 01:30-01:38; 02:18-03:40; 05:20-07:40; 08:20-09:20
- setup/context: チャンネル内の時間足別トレード定義を説明する講義。4時間足トレードを中長期寄りの軸として扱い、スキャルピングは上位足環境認識より短期のプライスアクション精度が重要になると説明する。
- entry: スキャルピングでは2つ以上の根拠と期待値の高い場所を重視する、と述べるが、個別のエントリー条件は not stated。
- stop/invalidation: not stated.
- TP/exit: not stated.
- range/trend filter: 4時間足のエリオット波動、チャートパターン、トレンドフォローを勝率順に位置づけるが、個別セットアップの判定条件は not stated。
- timeframe/session: 4時間足確定のタイミングで確認したりアラートを置く運用、4時間足を日足/週足へ拡張する考え方を説明する。具体的な市場セッションは not stated。
- indicator usage: not stated.
- RR: 4時間足トレードは頻度が低く、勝率や想定回数に応じてロットを変える考えを述べる。個別RR条件は not stated。
- trade management: 月内の想定チャンス数や勝率に応じてロットを調整する考えを述べる。
- discretionary elements: トレードスタイル、リスク、ロット配分は人によって決める必要があるとする。
- relation to Batch 01/02 findings: O1/B2-O3の時間足整合性を背景教義として補強するが、B2-O4の具体的な遅延エントリー条件までは示さない。
- audited relevance class: doctrine_or_context
- confidence: medium
- selection decision and reason: deferred_not_batch_03. 時間足教義として有用だが、Batch 03最終基準の直接的な機械ルールには届かない。

### BxQyDLIWE0U

- source_title: 【ゆっくり実況】ブレイク手法はこうすれば勝てる/FX.XM10万円チャレンジ/第23話
- content_type: regular_video
- timestamp references: 01:44-02:45; 02:50-03:20; 04:10-04:45
- setup/context: エリオット波動の3波残りを取りに行くブレイク手法。1波の値幅を測り、2波の起点へ当て、3波がまだ伸び切っていないことを条件にする。
- entry: 直近高値をブレイクした時にエントリーする。
- stop/invalidation: not stated.
- TP/exit: 1波と同じ値幅が伸び切ったところを決済目標にする。結果部分では短時間で決済したことを示す。
- range/trend filter: エリオット波動の3波判定が前提。レンジ判定は not stated。
- timeframe/session: not stated.
- indicator usage: not stated.
- RR: ブレイク手法の欠点としてリスクリワードが悪くなりがちと説明する。
- trade management: staged exit or break-even procedure は not stated。
- discretionary elements: 1波/2波/3波の数え方と、3波が伸び切っていない判断には裁量が残る。
- relation to Batch 01/02 findings: PR #22のcarry-forward rowを再確認。O2/O3とB2-O6を支持し、O4はTP側のみ支持する。損切り条件がないためB2-O1は not supported。
- audited relevance class: direct_mechanical_rule
- confidence: medium
- selection decision and reason: selected_for_batch_03. carry-forward候補として再検証し、stopは欠けるが、波の残余、直近高値ブレイク、1波値幅TP、RR弱点が timestamp-supported で残るため。

### DT4FEDZttes

- source_title: 【高勝率手法】ブレイクアウト×〇〇を組み合わせたらマジで勝てる。/第117話
- content_type: regular_video
- timestamp references: 04:45-05:45; 05:45-07:25; 07:30-10:50; 11:20-13:00
- setup/context: 1時間足の実トレード解説。ブレイクエントリーを単独ではなく、4時間足/日足/週足の環境認識と組み合わせる。
- entry: 1波の直近高値、切り下げライン、または水平線を越えて足が確定したタイミングでエントリーする。3波起点から入るより、ブレイク確定後に入る方が見ている人のタイミングが揃うと説明する。
- stop/invalidation: 赤ラインを損切りと述べるが、赤ラインの構造的アンカーは not stated。
- TP/exit: 教科書的には1波値幅を3波起点へ当てた紫丸。4時間足/日足/週足の余地が大きい場合はオレンジラインまで伸ばす判断もするが、シナリオを事前に持たず青矢印で切ったことをミスとして反省する。
- range/trend filter: 上位足の方向とエントリー方向が一致しているかを確認する。週足チャネル上限ラインの抜けと押し目もロング根拠にする。
- timeframe/session: 1時間足での entry/exit に加え、4時間足、日足、週足の方向確認を使う。 session/time-of-day は not stated。
- indicator usage: not stated.
- RR: ブレイク単体の勝率やRRだけでは弱く、上位足環境認識を足すことで値幅と勝率が改善すると説明する。固定RRは not stated。
- trade management: 利確ラインを変更するなら、エントリー前に複数シナリオを考えておく必要がある。予定外に途中で切ると判断がぶれる。
- discretionary elements: 波のカウント、上位足の方向、目標を紫丸にするかオレンジラインにするかには裁量が残る。
- relation to Batch 01/02 findings: BxQyDLIWE0Uのブレイク行を拡張し、O1/O2/O3/O4/B2-O3/B2-O6を強く支持する。B2-O8はミス例として支持する。
- audited relevance class: direct_mechanical_rule
- confidence: high
- selection decision and reason: selected_for_batch_03. ブレイク継続と上位足整合の組み合わせを、entry/TP/managementまで具体化するため。

### FZ_1z3jC5_Y

- source_title: 【何が起きた？】鉄板手法でエントリーするもまさかの260万円負け？/第133話
- content_type: regular_video
- timestamp references: 04:50-05:45; 06:07-07:42; 07:42-09:20
- setup/context: シルバー4時間足の負けトレード解説。下降トレンドの最後の戻り高値を抜けた想定から、トレンドライン抜けエントリーを検証する。
- entry: オレンジの切り下げライン抜けの黒矢印陽線で入ったが、後から見ると青ラインの方がきれいで、黒矢印の抜けは甘かったと反省する。
- stop/invalidation: 本来の損切りは赤ライン付近。実際は根拠崩れと週末を理由に青丸でクローズした。適切には青丸のプライスアクションを見て、少しリバウンド後または割られた時に切ると説明する。
- TP/exit: 水色丸周辺の長い上ヒゲで5波終了の可能性を見れば途中利確できたと説明する。
- range/trend filter: ラインの引き方、抜けの強さ、連続上ヒゲによる上値抵抗を確認する。甘い抜けなら見送る。
- timeframe/session: 4時間足チャート。週末持ち越しを避ける文脈はあるが、市場セッション条件は not stated。
- indicator usage: not stated.
- RR: not stated.
- trade management: エントリー後に5波終了や上ヒゲ抵抗が見えたら、期待だけで保有せず途中利確または早期撤退を検討する。
- discretionary elements: どの切り下げラインがきれいか、抜けが甘いか、上ヒゲを5波終了と見るかは裁量が残る。
- relation to Batch 01/02 findings: O7/B2-O5のfalse-break rejectionを具体化し、B2-O8のpremise weakening exitを負け事例で支持する。
- audited relevance class: direct_mechanical_rule
- confidence: medium
- selection decision and reason: selected_for_batch_03. case-study controlだが、弱い抜け、上ヒゲ、根拠崩れの撤退条件が反復可能な運用ルールとして示されるため。

### FwoDV2YrZOE

- source_title: 【大敗北】年末アノマリーの大チャンスで1400万円負けました（今後の展開予想あり） /第202話
- content_type: regular_video
- timestamp references: 03:40-06:00; 06:00-08:40; 08:40-11:40; 11:40-16:50
- setup/context: ゴールドの年末アノマリーとFOMC後の実トレード反省。12月安値、前年チャート、FOMC後の値動き、4時間足ダブルボトムのフラクタルを使う。
- entry: FOMC発表後、上昇して大きく戻され、再上昇したところを底が確定したと見てエントリーする。
- stop/invalidation: 通常は4時間足の直近安値へ損切りを置くが、この事例では短期足を見続けて浅い損切りにしたため負けたと説明する。
- TP/exit: 現在地からのテクニカル entry は難度が上がるとし、浅い押し目ポジションは一旦利確しておく考えを示す。
- range/trend filter: 4時間足ダブルボトム、ダブルボトム内ダブルボトム、前年の12月値動きとの比較を使う。
- timeframe/session: 5分足の entry、4時間足の根拠、FOMCというイベントタイミング、深夜の短期足監視が扱われる。
- indicator usage: not stated.
- RR: 浅い損切りにするとRRは改善しやすいが、通常根拠から外れると説明する。
- trade management: イベント直後に急がず値動きが落ち着くのを待つか、通常どおり4時間足の損切りを使う必要がある。
- discretionary elements: アノマリー、FOMC後の底確定、前年との類似、浅い押し目の扱いは裁量が大きい。
- relation to Batch 01/02 findings: B2-O3のtimeframe shortcut riskとB2-O1のstop anchorを支持する。session/time-of-day audit controlとして有用だが、季節/イベント依存が強い。
- audited relevance class: partial_mechanical_rule
- confidence: medium
- selection decision and reason: deferred_not_batch_03. case-studyとして有用だが、年末アノマリー/FOMC依存が強く、Batch 03最終セットの汎用 direct rule としては採用しない。

### JDjq7FrKdF8

- source_title: 【爆益の裏技】騙しを逆手に取って稼ぐトレード手法
- content_type: regular_video
- timestamp references: 00:00-03:40; 03:40-05:40; 05:40-10:00
- setup/context: ブレイク、ダブルトップ/ボトム、レンジ、トレンドライン、三角持ち合い、インジケーター、チャネル、エリオット波動などで起きる騙しを体系的に扱う。
- entry: 騙し回避のため、上位足の確定を待つ、ラインを信用しすぎない、複数根拠で入る、波形のきれいさを見る、急激な動きに突っ込まない、という原則を示す。
- stop/invalidation: 他者のストップが狩られる位置や、横軸レンジ割れ後のショート燃料は説明するが、自分のstop placementは not stated。
- TP/exit: not stated.
- range/trend filter: 横軸レンジの下抜けがショート燃料になり、その後のストップ買いが上昇燃料になるという見方を示す。
- timeframe/session: 上位足確定を待つとするが、具体的な時間足は not stated。
- indicator usage: RSIやMACDのシグナル単体ではなくローソク足を重視すると説明する。
- RR: not stated.
- trade management: 騙しの特徴を知れば無駄な損切りを減らせるとするが、管理手順は not stated。
- discretionary elements: 燃料の有無、波形のきれいさ、ライン信用度の判断は抽象度が高い。
- relation to Batch 01/02 findings: O7/rG3ELeTim8U系の騙し観察を広げるが、B2-O1/O2/O8のような具体的stop/TP/managementには届かない。
- audited relevance class: partial_mechanical_rule
- confidence: medium
- selection decision and reason: deferred_not_batch_03. liquidity/sweep doctrineとして有用だが、個別の反復エントリー、stop、TPが不十分。

### QErPg-ZvR1s

- source_title: 【必ず負ける】絶対にトレードをしてはいけないNG相場とは？
- content_type: regular_video
- timestamp references: 00:00-04:40; 04:20-07:00; 07:00-09:20; 09:20-12:00
- setup/context: トレードしてはいけない相場の共通点を扱う。チャンス相場を言語化するより、負けやすい相場を避けることに重点を置く。
- entry: 根拠に絡まない小さいレンジ、意味のない横軸調整、急なボラ低下、コマ足の連続では entry を見送る。波形が汚く最後の押し安値/戻り高値やトレンド方向が分からない時も見送る。
- stop/invalidation: not stated.
- TP/exit: 5波トレード自体は否定しないが、利確目標が明確に決められる場所だけで entry する。左側の波や上位足を見てもTPが決めにくい時は避ける。
- range/trend filter: ボラの小さい横軸調整、方向感のない汚い波形、左側の波が見えずエリオット波動がカウントしづらい場面をNG相場とする。
- timeframe/session: 4時間足チャート例、日足/4時間足、週足/月足によるTP目標確認を扱う。 session/time-of-day は not stated。
- indicator usage: not stated.
- RR: not stated.
- trade management: 負けていたはずのトレードをスルーすることを重視する。
- discretionary elements: 波形がきれいか、ボラ低下や小レンジをどう判断するかには裁量が残る。
- relation to Batch 01/02 findings: B2-O5のregime rejectionを強く支持し、O3/O4/O6も補強する。TPが決まらない場合に避ける点はB2-O2を補強する。
- audited relevance class: direct_mechanical_rule
- confidence: high
- selection decision and reason: selected_for_batch_03. range/filter logicとTP可否によるentry rejectionを具体的に示すため。

### U9xsvLmdIOw

- source_title: 【マジで勝てる】水平線上のプライスアクションを伝授する。【第3弾】
- content_type: regular_video
- timestamp references: 00:00-02:20; 01:30-03:40; 03:40-06:20; 05:00-07:40
- setup/context: 4時間足の重要水平線を5分足で下抜けした場面を比較し、水平線上のプライスアクションを学ぶ講義。
- entry: 堅実に下落しているA型では、長期足根拠があってもすぐロングせず、もう一段落ちるのを待つか短期足がダウ理論で上へ切り替わった時に入る。B型の急落は水平線周辺のロング損切りを狩って燃料化する動きとして扱える。
- stop/invalidation: 他者のロング損切りが赤水平線周辺に置かれている想定は説明するが、自分の損切り位置は not stated。
- TP/exit: B型で既存ショートを持っていて建値に余裕と利益があるなら、少し様子を見て上昇途中で利確してもよい。新規ショートは水平線の根拠が弱いので見送る。
- range/trend filter: 4時間足など上位足で実体レベルで水平線が止められているかを確認する。簡単に割れた水平線はブレイク根拠として弱い。
- timeframe/session: 5分足のプライスアクションと4時間足水平線を組み合わせる。 session/time-of-day は not stated。
- indicator usage: not stated.
- RR: not stated.
- trade management: 既存ショートは、建値余裕と含み益がある場合だけ様子見し、上昇しそうなら途中利確する。
- discretionary elements: 急落がstop-runか、水平線の信用度、短期足ダウ転換の判断には裁量が残る。
- relation to Batch 01/02 findings: O7とB2-O5を強く支持し、rG3ELeTim8U系の騙し観察を水平線上の実運用に狭める。B2-O8も部分的に支持する。
- audited relevance class: direct_mechanical_rule
- confidence: high
- selection decision and reason: selected_for_batch_03. liquidity/sweep、水平線信頼度、上位足確定、entry/exit判断が具体的に接続されているため。

### VsFnbo-yPN4

- source_title: 【完璧な利確】鉄板のトレンドフォロー手法で頭から尻尾まで取ってみた。ガチ解説/第51話
- content_type: regular_video
- timestamp references: 04:20-07:40; 07:40-09:20
- setup/context: ポンド円4時間足のトレンドフォロー実例。クロス円全体が売れる形で、最も伸びそうなポンド円を選ぶ。
- entry: オレンジチャネル上限タッチ後に下落し、上昇の最後の押し安値ラインを下へブレイク。赤丸への戻りを起点に、4時間足1本の確定を待って下へ行くのを確認してから entry する。
- stop/invalidation: not stated.
- TP/exit: 当初はチャネル下限、その次に青い水平線を目標にする。本来は伸ばす予定だったが、短期足の小さなダブルボトムと4時間足の大きな下ヒゲに違和感を覚えて青矢印で利確する。
- range/trend filter: 通貨強弱、チャネル上限、最後の押し安値ブレイク、4時間足確定を使う。
- timeframe/session: 4時間足環境認識と5分足 entry/exit。 session/time-of-day は not stated。
- indicator usage: not stated.
- RR: not stated.
- trade management: 予定TPまで持たず、4時間足の下ヒゲなど価格行動が弱まる時に途中決済する。
- discretionary elements: 4時間足の下ヒゲを「違和感」と見る部分は本人も感覚的と説明するため、管理判断には裁量が大きい。
- relation to Batch 01/02 findings: O1/O2/O3とB2-O4を支持し、B2-O8をcase-studyで補強する。早期利確は裁量が強いためB2-O7も支持する。
- audited relevance class: direct_mechanical_rule
- confidence: medium
- selection decision and reason: selected_for_batch_03. 通貨強弱、4時間足確定待ち、チャネル/押し安値ブレイク、途中利確判断が timestamp-supported で残るため。

### k4nDAp3t8js

- source_title: 【FX】三角持ち合いの「ダマシ」を完全に回避して700万稼いだ方法 #shorts #trading
- content_type: short
- timestamp references: 00:00-01:15
- setup/context: ポンドスイス日足の三角持ち合いを扱うShort。三角持ち合いは騙しが多くタイミングが難しいと説明する。
- entry: 抜け確定や1回目のリターンムーブではなく、波形イメージが成立しやすい2回目の深いリターンムーブ後の上昇で入る。
- stop/invalidation: 抜け確定や1回目のリターンムーブで入り、4時間足の直近安値に損切りを置くと負ける可能性が高いと説明する。
- TP/exit: 4時間足で3波になる可能性がある位置を見て、5分足プライスアクションで利確する。
- range/trend filter: 長期調整後の波形イメージを重視する。三角持ち合いの初回抜けをそのまま信用しない。
- timeframe/session: 日足、4時間足、5分足を使う。 session/time-of-day は not stated。
- indicator usage: not stated.
- RR: not stated.
- trade management: 5分足プライスアクションで利確するが、詳細条件は not stated。
- discretionary elements: 本編にあるという2つの強い根拠はShort内では省略されているため、証拠が不足する。
- relation to Batch 01/02 findings: O7/B2-O5のfalse-break filterを支持するが、Short内の省略によりB2-O4やB2-O8は限定的。
- audited relevance class: partial_mechanical_rule
- confidence: medium
- selection decision and reason: deferred_not_batch_03. Shortは有用だが、根拠の一部を本編参照としており、最終選定はregular_videoの直接証拠を優先した。

### k5Uc57QyLok

- source_title: 【もう負けない】無駄な損切りを完全消滅させる途中利確の裏技とは？/第106話
- content_type: regular_video
- timestamp references: 04:20-07:00; 06:30-07:50; 07:50-09:50; 09:20-11:40
- setup/context: オージー円4時間足の途中利確事例。4時間足では下目線だが、週足/月足チャネルでは上目線の根拠があり、短期方向と上位足方向が揃っていない。
- entry: 黒矢印の小さな陰線確定後に入る。entryそのものの全条件は not stated。
- stop/invalidation: 赤ラインに損切りを置いたことは述べるが、赤ラインのアンカーは not stated。
- TP/exit: 青ラインあたりで途中利確。理由は、緑丸を最後の押し安値と見ると緑水平線でダブルボトムのように見え、水色矢印の4時間足陽線確定が下落の勢いを止める可能性が高いから。もしその足が陰線や実体の小さいコマ足なら保有した可能性がある。
- range/trend filter: 週足/月足チャネルでは上目線、4時間足では下目線。方向が揃わず波が汚い場面は初心者は見送る選択肢もある。
- timeframe/session: 4時間足 entry/exit判断、週足/月足の環境認識。 session/time-of-day は not stated。
- indicator usage: not stated.
- RR: not stated.
- trade management: 方向不一致の時は、上位足起点付近の4時間足プライスアクションを見て途中利確する。
- discretionary elements: 最後の押し安値候補、水平線抵抗帯、4時間足陽線の意味付けには裁量が残る。
- relation to Batch 01/02 findings: B2-O8を強く支持し、O1/O3/B2-O3の時間足整合も補強する。見送り判断はB2-O5と関係する。
- audited relevance class: direct_mechanical_rule
- confidence: high
- selection decision and reason: selected_for_batch_03. partial-profit/trade-management gapを、上位足不一致と4時間足陽線確定という具体条件で埋めるため。

## Audit class counts

| audited relevance class | count |
| --- | ---: |
| direct_mechanical_rule | 8 |
| partial_mechanical_rule | 3 |
| doctrine_or_context | 1 |

## Selection counts

| selection decision | count |
| --- | ---: |
| selected_for_batch_03 | 8 |
| deferred_not_batch_03 | 4 |
