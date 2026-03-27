# study-cli

学習時間を記録するCLIツール。

## 機能

- 学習の開始・終了をコマンドで記録
- 経過時間を自動計算
- 勉強した内容をメモとして保存
- 過去の記録を一覧表示・合計時間を集計

## 使い方

### 学習開始

```bash
python3 study.py start
```

### 学習終了

```bash
python3 study.py stop
```

終了時に何を勉強したか入力を求められる。

### 記録を見る

```bash
python3 study.py list
```

## 動作環境

- Python 3.x

## 技術スタック

- Python 標準ライブラリのみ使用（`sys` / `json` / `datetime` / `pathlib`）
