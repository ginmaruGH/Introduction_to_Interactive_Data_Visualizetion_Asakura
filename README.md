# Python インタラクティブ・データビジュアライゼーション入門

[出版サイト](https://www.asakura.co.jp/detail.php?book_code=12258)

[サポートサイト](https://github.com/plotly-dash-book/plotly-dash-book)

- [Plotly Python](https://plotly.com/python/)
  - [Python API reference for plotly](https://plotly.com/python-api-reference/)
- [Dash Python User Guide](https://dash.plotly.com/)
  - [API Reference](https://dash.plotly.com/reference)
  - [Dash Example Index](https://dash-example-index.herokuapp.com/)
- [plotly/jupyter-dash](https://github.com/plotly/jupyter-dash)
  - [Introducing JupyterDash](https://medium.com/plotly/introducing-jupyterdash-811f1f57c02e)
  - [jupyter-dash/notebooks/getting_started.ipynb](https://github.com/plotly/jupyter-dash/blob/master/notebooks/getting_started.ipynb)

---

## Ch.0 はじめに

- 0-1 本書で扱うパッケージ
  - 0-1-1 plotly.py
  - 0-1-2 Plotly Express
  - 0-1-3 Dash
  - 0-1-4 Dash Cytoscape
- 0-2 本書について
  - 0-2-1 前提知識
  - 0-2-2 ターミナルの表記
  - 0-2-3 Pythonスクリプトの実行
  - 0-2-4 データ型
- 0-3 動作環境および環境構築
  - 0-3-1 対象OS
  - 0-3-2 プログラミング言語
  - 0-3-3 仮想環境
  - 0-3-4 パッケージのインストール
- 0-4 データセットおよびソースコード
  - 0-4-1 GitHubリポジトリ
  - 0-4-2 パッケージ同梱のデータセット
- 0-5 Jupyter Notebook
  - 0-5-1 Jupyter Notebookのインストール
  - 0-5-2 Jupyter Notebookの起動
  - 0-5-3 Notebookの作成
- 0-6 JupyterLab
  - 0-6-1 JupyterLabのインストール
  - 0-6-2 JupyterLabの起動
  - 0-6-3 Notebookの作成

## Ch.1 Plotly Express

- 1-1 Plotly Expressとは
  - 1-1-1 インタラクティブな可視化事例
- 1-2 Plotly Express入門
  - 1-2-1 グラフを描画する関数
  - 1-2-2 データ型
- 1-3 Plotly Express応用
  - 1-3-1 ファセット
  - 1-3-2 アニメーション
  - 1-3-3 スタイルの設定
- 1-4 Plotly Expressのさまざまなグラフ
  - 1-4-1 散布図（scatter関数）
  - 1-4-2 散布図行列（scatter_matrix関数）
  - 1-4-3 折れ線グラフ（line関数）
  - 1-4-4 棒グラフ（bar関数）
  - 1-4-5 面グラフ（area関数）
  - 1-4-6 エラーバー
  - 1-4-7 箱ひげ図（box関数）
  - 1-4-8 バイオリン図（violin関数）
  - 1-4-9 ヒストグラム（histogram関数）
  - 1-4-10 円グラフ（pie関数）
  - 1-4-11 サンバーストグラフ（sunburst関数）
  - 1-4-12 ツリーマップ（treemap関数）
  - 1-4-13 平行座標プロット（parallel_coordinates関数）
  - 1-4-14 平行プロット（parallel_categories関数）
  - 1-4-15 三角図（scatter_ternary・line_ternary関数）
  - 1-4-16 ポーラチャート（scatter_polar関数・line_polar関数・bar_polar関数）
  - 1-4-17 階級区分図（choropleth関数）
  - 1-4-18 地図上の散布図（scattergeo関数）
  - 1-4-19 3D散布図（scatter_3d関数・line_3d関数）

## Ch.2 plotly-py入門

- 2-1 plotly-pyとは
- 2-2 plotly-pyのコンセプト
  - 2-2-1 figureによる描画領域の作成
  - 2-2-2 traceによるグラフの登録
  - 2-2-3 layoutによるグラフの調整
- 2-3 plotly-pyの記法
  - 2-3-1 plotly-jsのデータ構造
  - 2-3-2 属性の設定方法
  - 2-3-3 コンストラクタの引数による指定
  - 2-3-4 属性への代入
  - 2-3-5 updateメソッドによる指定
  - 2-3-6 update_から始まるメソッドによる指定
  - 2-3-7 addから始まるメソッドによるtraceの追加
- 2-4 標準的なインタラクティブ操作
  - 2-4-1 ホバーツール
  - 2-4-2 凡例による要素の選択
  - 2-4-3 モードバーによる操作

## Ch.3 plotly-pyのさまざまなグラフ

- 3-1 基本的なグラフ
  - 3-1-1 折れ線グラフ（Scatter trace）
  - 3-1-2 散布図（Scatter trace）
  - 3-1-3 棒グラフ（Bar trace）
  - 3-1-4 面グラフ（Scatter trace）
  - 3-1-5 円グラフ（Pie trace）
  - 3-1-6 サンバーストグラフ（Sunburst trace）
  - 3-1-7 ツリーマップ（Treemap trace）
  - 3-1-8 テーブル（Table trace）
- 3-2 専門的なグラフ
  - 3-2-1 箱ひげ図（Box trace）
  - 3-2-2 バイオリン図（Violin trace）
  - 3-2-3 ヒストグラム（Histogram trace）
  - 3-2-4 2次元ヒストグラム（Histogram2d trace）
  - 3-2-5 エラーバー
  - 3-2-6 平行座標プロット（Parcoords trace）
  - 3-2-7 平行プロット（Parcats trace）
  - 3-2-8 ヒートマップ（Heatmap trace）
  - 3-2-9 等高線図（Contour trace）
  - 3-2-10 ポーラチャート（Scatterpolar trace）
  - 3-2-11 三角図（Scatterternary trace）
  - 3-2-12 ローソク足（Candlestick trace）
  - 3-2-13 ウォーターフォール図（Waterfall trace）
  - 3-2-14 ファンネル図（Funnel trace）
  - 3-2-15 階級区分図（Choropleth trace）
  - 3-2-16 地図上の散布図（Scattergeo trace）
  - 3-2-17 図上の折れ線グラフ（Scattergeo trace）
  - 3-2-18 mapboxの利用
- 3-3 3Dグラフ
  - 3-3-1 3D散布図（Scatter3d trace）
  - 3-3-2 3D折れ線グラフ（Scatter3d trace）
  - 3-3-3 サーフェスグラフ（Surface trace）
  - 3-3-4 メッシュグラフ（Mesh3d trace）

## Ch.4 plotly-py応用

- 4-1 サブプロット
- 4-2 グラフのカスタマイズ
  - 4-2-1 グラフのスタイル
  - 4-2-2 グラフサイズと余白
  - 4-2-3 軸の設定
  - 4-2-4 凡例の設定
  - 4-2-5 カラースケール
- 4-3 オブジェクトの描画
  - 4-3-1 テキストの描画と設定
  - 4-3-2 図形の描画
- 4-4 インタラクティブな可視化
  - 4-4-1 ホバーツールの設定
  - 4-4-2 コールバックによるインタラクティブな可視化
- 4-5 グラフを画像ファイルに出力

## Ch.5 Dash入門

- 5-1 Dashとは
  - 5-1-1 Dashを用いたインタラクティブな可視化事例
- 5-2 Dashの全体像
  - 5-2-1 コンポーネント
  - 5-2-2 スタイル設定
  - 5-2-3 グラフ作成
  - 5-2-4 レイアウト
  - 5-2-5 コールバック

## Ch.6 Dashレイアウト

- 6-1 コンポーネント
  - 6-1-1 コンポーネントの作成
  - 6-1-2 コンポーネントの主要な属性
- 6-2 スタイル設定
  - 6-2-1 コンポーネント自身のスタイル設定
  - 6-2-2 コンポーネントを配置する
  - 6-2-3 外部CSSを用いたスタイル設定
- 6-3 グラフの配置
  - 6-3-1 Plotly Expressを用いたグラフの配置
  - 6-3-2 plotly-pyを用いたグラフの配置
- 6-4 複数コンポーネントの配置
  - 6-4-1 Divコンポーネントの引数styleを用いた配置
  - 6-4-2 外部CSSを用いたスタイル設定
  - 6-4-3 スタイルシートをカスタマイズしたスタイル設定
  - 6-4-4 複数のコンポーネントを組み合わせた配置

## Ch.7 Dashコールバック

- 7-1 コールバック基礎
  - 7-1-1 コールバック概要
  - 7-1-2 入力データを即座に反映するコールバック
  - 7-1-3 複数の入出力が存在するコールバック
- 7-2 パターンマッチング・コールバック
  - 7-2-1 ALLセレクタ
  - 7-2-2 MATCHセレクタ
  - 7-2-3 ALLSMALLERセレクタ
- 7-3 コールバック応用
  - 7-3-1 画面遷移
  - 7-3-2 各レイアウトごとにコールバックが存在するアプリケーション
  - 7-3-3 グラフ上のマウス動作の活用
  - 7-3-4 特定の状態でのコールバックの更新停止
  - 7-3-5 連鎖コールバック

## Ch.8 Dashの標準コンポーネント

- 8-1 Dash HTML Components
  - 8-1-1 Dash HTML Componentsの概要
  - 8-1-2 文字列を用いたアプリケーション
  - 8-1-3 表示画像を切り替えるアプリケーション
- 8-2 Dash Core Components
  - 8-2-1 Dropdownコンポーネント
  - 8-2-2 Loadingコンポーネント
  - 8-2-3 Sliderコンポーネント
  - 8-2-4 Linkコンポーネント
  - 8-2-5 Locationコンポーネント
  - 8-2-6 Intervalコンポーネント
  - 8-2-7 Uploadコンポーネント
- 8-3 Dash DataTable
  - 8-3-1 テーブルを作成
  - 8-3-2 テーブルを一括してスタイル設定
  - 8-3-3 テーブルを要素ごとに装飾
  - 8-3-4 CSVファイルを用いたテーブル作成
  - 8-3-5 テーブルの表示幅の変更と固定表示
  - 8-3-6 テーブルの編集
  - 8-3-7 テーブルデータを地図に表示

## Ch.9 Dashの追加コンポーネント

- 9-1 DashCanvas
  - 9-1-1 DashCanvasコンポーネント
  - 9-1-2 画像ファイルを表示
  - 9-1-3 描き込み結果のCSVファイルを取得
  - 9-1-4 輪郭を指定した画像の切り抜き
- 9-2 Dash Bio
  - 9-2-1 Dash Bioのコンポーネント
  - 9-2-2 サーコスプロット
- 9-3 Dash DAQ
  - 9-3-1 計器を実装したアプリケーションの作成

## Ch.10 Dash Cytoscape入門

- 10-1 Dash Cytoscapeとは
- 10-2 ネットワーク可視化とは
  - 10-2-1 ノードとエッジ
  - 10-2-2 無向グラフと有向グラフ
  - 10-2-3 ネットワーク可視化における視覚表現
- 10-3 Dash Cytoscapeの基本
  - 10-3-1 基本的なネットワーク図の描画
- 10-4 ネットワークの構成要素
  - 10-4-1 ネットワーク構造の表現（エッジリストと隣接行列）
  - 10-4-2 Dash Cytoscapeにおけるネットワーク構造の表現
  - 10-4-3 要素辞書とデータ辞書
  - 10-4-4 データ辞書への独自キーの追加
  - 10-4-5 NetworkXを使ったほかのデータ形式からの変換
- 10-5 ノードの配置方法
  - 10-5-1 ノードの配置方法の基本
  - 10-5-2 手動的な配置（preset）
  - 10-5-3 自動的な配置（preset以外）
- 10-6 スタイル設定
  - 10-6-1 スタイル設定の基本
  - 10-6-2 スタイルの適用範囲（"selector"キー/セレクタ文字列）
  - 10-6-3 スタイル辞書（"style"キー）

## Ch.11 Dash Cytoscape応用

- 11-1 インタラクティブなネットワーク可視化
  - 11-1-1 Dash Cytoscapeにおけるコールバックの基本
  - 11-1-2 イベントコールバックの基本
- 11-2 複合ノード（Compound Node）

## Appendix

- A-1 パッケージ情報
  - A-1-1 plotly-py
  - A-1-2 plotly express
  - A-1-3 Dash
  - A-1-4 Dash Cytoscape
  - A-1-5 NetworkX
  - A-1-6 Jupyter Dash
- A-2 整然データ
  - A-2-1 整然データとは
  - A-2-2 雑然データから整然データへの変換
  - A-2-3 整然データを可視化
- A-3 Plotly Expressの関数とplotly-pyのクラスの対応表
- A-4 Notebook（ipynbファイル）を共有
  - A-4-1 nbviewer
  - A-4-2 binder
  - A-4-3 Colaboratory
- A-5 Dashアプリケーションのデプロイ
  - A-5-1 Herokuにデプロイする
  - A-5-2 Azureにデプロイする
  - A-5-3 GCPにデプロイする
- A-6 認証機能
  - A-6-1 認証機能の実装
- A-7 JupyterDash
  - A-7-1 Jupyter上でのアプリケーション作成
- A-8 Dashアプリケーションのモジュール分割
  - A-8-1 モジュール分割

## Reference

- [3次元平行座標プロット](https://www.ism.ac.jp/editsec/toukei/pdf/55-1-069.pdf)
- [COVID-19のデータを使ったインタラクティブ可視化事例](https://junkudo-event-20210112.readthedocs.io/ja/latest/index.html)
- [【保存版】Python Dash パーフェクトガイド](https://qiita.com/Yusuke_Pipipi/items/b74f269d112f180d2131)
- [pandasは遅い！大量データの高速化、最適化のノウハウを公開！](https://propen.dream-target.jp/blog/pandas)
