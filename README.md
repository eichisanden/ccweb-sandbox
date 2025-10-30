# AI Agent Workspace

Claude Agent SDKを使用したAIエージェントプロジェクトのワークスペースです。

## 🚀 クイックスタート

### ランチャーを使用する方法（推奨）

```bash
python launcher.py
```

メニューが表示されるので、番号を選択してEnterキーを押してください。

### 直接実行する方法

```bash
cd claude-agent-project
uv sync
uv run main.py
```

## 📁 プロジェクト構造

```
ccweb-sandbox/
├── launcher.py              # 🎯 メニューランチャー（推奨）
├── claude-agent-project/    # AI Agentプロジェクト
│   ├── main.py             # 対話型チャットアプリケーション
│   ├── pyproject.toml      # プロジェクト設定
│   └── README.md           # プロジェクト詳細
└── README.md               # このファイル
```

## 🌟 機能

### 対話型チャット
- Claude Agent SDKを使用したインタラクティブなチャット
- ストリーミング応答のサポート
- メッセージタイプの視覚的な表示（絵文字付き）
- ツール使用の詳細なログ表示

## 📖 使い方

1. **ランチャーを起動**
   ```bash
   python launcher.py
   ```

2. **メニューから選択**
   - `1`: AI Agent チャットを起動
   - `2`: 終了

3. **チャットを楽しむ**
   - メッセージを入力してEnterキーで送信
   - `quit`、`exit`、または `q` で終了
   - Ctrl+C でも終了可能

4. **メニューに戻る**
   - チャット終了後、Enterキーでメニューに戻ります

## 🛠️ 必要な環境

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) パッケージマネージャー
- Claude Code 2.0.0+

## 📚 参考リンク

- [Claude Agent SDK ドキュメント](https://docs.claude.com/en/api/agent-sdk/python)
- [GitHub リポジトリ](https://github.com/anthropics/claude-agent-sdk-python)
- [PyPI パッケージ](https://pypi.org/project/claude-agent-sdk/)

## 📝 ライセンス

このプロジェクトはサンプルプロジェクトです。
