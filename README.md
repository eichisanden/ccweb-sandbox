# AI Agent Workspace

複数のLLM（Claude、OpenAI）を使用したAIエージェントプロジェクトのワークスペースです。

## 🚀 クイックスタート

### ランチャーを使用する方法（推奨）

```bash
python launcher.py
```

メニューが表示されるので、番号を選択してEnterキーを押してください。

### 直接実行する方法

#### Claude Agent
```bash
cd claude-agent-project
uv sync
uv run main.py
```

#### OpenAI Agent
```bash
cd openai-agent-project
cp .env.example .env
# .env にOPENAI_API_KEYを設定
uv sync
uv run main.py
```

## 📁 プロジェクト構造

```
ccweb-sandbox/
├── launcher.py              # 🎯 メニューランチャー（推奨）
├── claude-agent-project/    # Claude Agent プロジェクト
│   ├── main.py             # 対話型チャットアプリケーション
│   ├── pyproject.toml      # プロジェクト設定
│   └── README.md           # プロジェクト詳細
├── openai-agent-project/    # OpenAI Agent プロジェクト
│   ├── main.py             # 対話型チャットアプリケーション
│   ├── pyproject.toml      # プロジェクト設定
│   ├── .env.example        # 環境変数サンプル
│   └── README.md           # プロジェクト詳細
└── README.md               # このファイル
```

## 🌟 機能

### 1. Claude Agent (claude-agent-project/)
- Claude Agent SDKを使用したインタラクティブなチャット
- ストリーミング応答のサポート
- Web検索、ファイル操作などのツール使用
- メッセージタイプの視覚的な表示（絵文字付き）
- Richライブラリによる美しいターミナル表示

### 2. OpenAI Agent (openai-agent-project/)
- OpenAI Chat Completions APIを使用した対話型チャット
- ストリーミング応答のサポート
- 会話履歴の管理（マルチターン対話）
- Richライブラリによる美しいマークダウン表示
- 複数モデルのサポート（GPT-4o、GPT-4、GPT-3.5など）

## 📖 使い方

1. **ランチャーを起動**
   ```bash
   python launcher.py
   ```

2. **メニューから選択**
   - `1`: Claude Agent チャットを起動
   - `2`: OpenAI Agent チャットを起動
   - `3`: 終了

3. **チャットを楽しむ**
   - メッセージを入力してEnterキーで送信
   - `quit`、`exit`、または `q` で終了
   - Ctrl+C でも終了可能

4. **メニューに戻る**
   - チャット終了後、Enterキーでメニューに戻ります

## 🛠️ 必要な環境

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) パッケージマネージャー

### Claude Agent
- Claude Code 2.0.0+

### OpenAI Agent
- OpenAI APIキー（[こちら](https://platform.openai.com/api-keys)から取得）
- `.env`ファイルに`OPENAI_API_KEY`を設定

## 📚 参考リンク

### Claude Agent
- [Claude Agent SDK ドキュメント](https://docs.claude.com/en/api/agent-sdk/python)
- [GitHub リポジトリ](https://github.com/anthropics/claude-agent-sdk-python)
- [PyPI パッケージ](https://pypi.org/project/claude-agent-sdk/)

### OpenAI Agent
- [OpenAI Platform ドキュメント](https://platform.openai.com/docs)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Chat Completions API ガイド](https://platform.openai.com/docs/guides/text-generation)

## 📝 ライセンス

このプロジェクトはサンプルプロジェクトです。
