# AI Agent Workspace

複数のLLM（Claude、OpenAI）とフレームワーク（OpenAI Agents SDK）を使用したAIエージェントプロジェクトのワークスペースです。

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

#### OpenAI Agents SDK
```bash
cd openai-agents-project
cp .env.example .env
# .env にOPENAI_API_KEYを設定
uv sync
uv run main.py
```

## 📁 プロジェクト構造

```
ccweb-sandbox/
├── launcher.py                 # 🎯 メニューランチャー（推奨）
├── claude-agent-project/       # Claude Agent プロジェクト
│   ├── main.py                # 対話型チャットアプリケーション
│   ├── pyproject.toml         # プロジェクト設定
│   └── README.md              # プロジェクト詳細
├── openai-agent-project/       # OpenAI Agent プロジェクト
│   ├── main.py                # 対話型チャットアプリケーション
│   ├── pyproject.toml         # プロジェクト設定
│   ├── .env.example           # 環境変数サンプル
│   └── README.md              # プロジェクト詳細
├── openai-agents-project/      # OpenAI Agents SDK プロジェクト
│   ├── main.py                # マルチエージェントチャット
│   ├── pyproject.toml         # プロジェクト設定
│   ├── .env.example           # 環境変数サンプル
│   └── README.md              # プロジェクト詳細
└── README.md                   # このファイル
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

### 3. OpenAI Agents SDK (openai-agents-project/)
- **マルチエージェントシステム**: 複数の専門エージェント連携
- **ツール統合**: Python関数を簡単にツール化
- **ハンドオフ機能**: エージェント間のタスク委譲
- **セッション管理**: 自動的な会話履歴保持
- **プロバイダー非依存**: 100以上のLLMをサポート
- エージェント例:
  - Assistant（汎用アシスタント）
  - MathExpert（数学専門エージェント）

## 📖 使い方

1. **ランチャーを起動**
   ```bash
   python launcher.py
   ```

2. **メニューから選択**
   - `1`: Claude Agent チャットを起動
   - `2`: OpenAI Agent チャットを起動
   - `3`: OpenAI Agents SDK チャットを起動（マルチエージェント）
   - `4`: 終了

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

### OpenAI Agent / OpenAI Agents SDK
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

### OpenAI Agents SDK
- [OpenAI Agents SDK ドキュメント](https://openai.github.io/openai-agents-python/)
- [GitHub リポジトリ](https://github.com/openai/openai-agents-python)
- [PyPI パッケージ](https://pypi.org/project/openai-agents/)

## 🎯 各プロジェクトの特徴比較

| 特徴 | Claude Agent | OpenAI Agent | OpenAI Agents SDK |
|------|-------------|--------------|-------------------|
| **SDK/API** | Claude Agent SDK | OpenAI API | OpenAI Agents SDK |
| **ストリーミング** | ✅ | ✅ | ❌ |
| **ツール使用** | ✅ 自動実行 | ❌ | ✅ Python関数 |
| **マルチエージェント** | ❌ | ❌ | ✅ |
| **ハンドオフ** | ❌ | ❌ | ✅ |
| **会話履歴** | 自動管理 | 手動管理 | 自動管理 |
| **Web検索** | ✅ | ❌ | カスタム実装可 |
| **ファイル操作** | ✅ | ❌ | カスタム実装可 |
| **適用場面** | 高度な自律型 | シンプルなチャット | 複雑なワークフロー |

## 📝 ライセンス

このプロジェクトはサンプルプロジェクトです。
