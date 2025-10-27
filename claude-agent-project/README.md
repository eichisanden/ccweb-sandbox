# Claude Agent Project

Claude Agent SDKを使用したシンプルなAIエージェントプロジェクト

## セットアップ手順

### 1. 依存関係のインストール

```bash
cd claude-agent-project
uv sync
```

### 2. 実行

```bash
uv run main.py
```

## プロジェクト構造

```
claude-agent-project/
├── main.py              # メインプログラム
├── pyproject.toml       # プロジェクト設定と依存関係
├── .env.example         # 環境変数のサンプル
├── .gitignore          # Git除外設定
└── README.md           # このファイル
```

## 主な機能

- 🤖 Claude Agent SDKを使用した対話型エージェント
- 📡 ストリーミング応答のサポート
- ⚡ 非同期処理による効率的な実装
- 🌐 Web検索機能（WebSearch / WebFetch）を有効化
- 📝 ファイル操作ツール（Read / Write / Edit）を許可
- 💻 コマンド実行ツール（Bash / Grep / Glob）を許可
- 🎨 メッセージタイプの視覚的な表示（絵文字付き）

## カスタマイズ

`main.py`の設定を編集して以下をカスタマイズできます:

### ツールの許可設定

`AGENT_OPTIONS`でエージェントが使用できるツールを制御できます:

```python
AGENT_OPTIONS = ClaudeAgentOptions(
    allowed_tools=[
        "Read", "Write", "Edit",  # ファイル操作
        "Bash", "Glob", "Grep",   # コマンド実行
        "WebSearch", "WebFetch",  # Web検索
    ],
    permission_mode="acceptEdits",  # 編集を自動承認
)
```

### その他のカスタマイズ

- プロンプトの内容
- エージェントとの対話フロー
- エラーハンドリング
- メッセージフォーマット

## 技術スタック

- **claude-agent-sdk**: Claude Code用の公式SDK
- **anyio**: 非同期I/Oライブラリ
- **Python 3.12+**: 最新のPython機能を活用

## 参考リンク

- [Claude Agent SDK ドキュメント](https://docs.claude.com/en/api/agent-sdk/python)
- [GitHub リポジトリ](https://github.com/anthropics/claude-agent-sdk-python)
- [PyPI パッケージ](https://pypi.org/project/claude-agent-sdk/)

## 今後の拡張予定

- [ ] カスタムツールの実装
- [ ] エラーハンドリングの強化
- [ ] 会話履歴の保存機能
- [ ] インタラクティブなチャット機能
