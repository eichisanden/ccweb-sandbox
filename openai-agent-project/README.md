# OpenAI Agent Project

OpenAI Chat Completions APIを使用したシンプルなAIエージェントプロジェクト

## セットアップ手順

### 1. 依存関係のインストール

```bash
cd openai-agent-project
uv sync
```

### 2. 環境変数の設定

`.env.example`をコピーして`.env`を作成し、OpenAI APIキーを設定します:

```bash
cp .env.example .env
```

`.env`ファイルを編集してAPIキーを追加:

```
OPENAI_API_KEY=your_actual_api_key_here
```

APIキーは[OpenAI Platform](https://platform.openai.com/api-keys)から取得できます。

### 3. 実行

```bash
uv run main.py
```

## プロジェクト構造

```
openai-agent-project/
├── main.py              # メインプログラム
├── pyproject.toml       # プロジェクト設定と依存関係
├── .env.example         # 環境変数のサンプル
├── .env                 # 実際の環境変数（gitignore対象）
├── .gitignore          # Git除外設定
└── README.md           # このファイル
```

## 主な機能

- 🤖 OpenAI Chat Completions APIを使用した対話型エージェント
- 📡 ストリーミング応答のサポート
- ⚡ 非同期処理による効率的な実装
- 💬 会話履歴の管理（マルチターン対話）
- 🎨 **Richライブラリによる美しいターミナル表示**
  - マークダウンの綺麗なレンダリング
  - カラフルなパネルとボーダー
  - リアルタイムストリーミング表示

## 使用方法

### 基本的な使い方

1. プログラムを起動
2. メッセージを入力してEnterキーで送信
3. AIからのストリーミング応答を確認

### コマンド

- `quit` / `exit` / `q`: チャットを終了
- `clear`: 会話履歴をクリア
- Ctrl+C: セッションを中断

## カスタマイズ

`main.py`の設定を編集して以下をカスタマイズできます:

### モデルの変更

`run_chat`関数のデフォルトモデルを変更:

```python
async def run_chat(client: AsyncOpenAI, user_message: str, model: str = "gpt-4o-mini"):
    # "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo" などに変更可能
```

### その他のカスタマイズ

- システムプロンプトの追加
- 温度パラメータの調整
- 最大トークン数の設定
- メッセージフォーマット

## 技術スタック

- **openai**: OpenAI API用の公式Python SDK
- **anyio**: 非同期I/Oライブラリ
- **rich**: ターミナルの美しい表示を実現するライブラリ
- **python-dotenv**: 環境変数管理
- **Python 3.12+**: 最新のPython機能を活用

## 参考リンク

- [OpenAI Platform ドキュメント](https://platform.openai.com/docs)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Chat Completions API ガイド](https://platform.openai.com/docs/guides/text-generation)
- [PyPI パッケージ](https://pypi.org/project/openai/)

## 注意事項

- OpenAI APIの使用には課金が発生します
- APIキーは`.env`ファイルで管理し、Gitにコミットしないでください
- 会話履歴は現在メモリ内にのみ保存されます（プログラム終了で消失）

## 今後の拡張予定

- [ ] 会話履歴の永続化（ファイル保存）
- [ ] システムプロンプトの設定機能
- [ ] 関数/ツール呼び出しの実装
- [ ] 複数モデルの選択機能
- [ ] トークン使用量の表示
