# OpenAI Agents Project

OpenAI Agents SDKを使用したマルチエージェントAIシステムのプロジェクト

## 概要

OpenAI Agents SDKは、2025年3月にリリースされた軽量で強力なマルチエージェントワークフレームワークです。このプロジェクトでは、複数のエージェント、ツール、ハンドオフ機能を使用した対話型チャットシステムを実装しています。

## セットアップ手順

### 1. 依存関係のインストール

```bash
cd openai-agents-project
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
openai-agents-project/
├── main.py              # メインプログラム
├── pyproject.toml       # プロジェクト設定と依存関係
├── .env.example         # 環境変数のサンプル
├── .env                 # 実際の環境変数（gitignore対象）
├── .gitignore          # Git除外設定
└── README.md           # このファイル
```

## 主な機能

### 🤖 マルチエージェントシステム
- **Assistant**: メインアシスタントエージェント（汎用的な質問対応）
- **MathExpert**: 数学専門エージェント（複雑な計算や数学的説明）

### 🔧 ツール統合
- `get_current_time()`: 現在時刻の取得
- `calculate()`: 数式の計算（安全な評価）

### 🔄 ハンドオフ機能
- Assistantから MathExpertへのタスク委譲
- MathExpertから Assistantへの制御の返却
- シームレスなエージェント間連携

### 💬 セッション管理
- 自動的な会話履歴の保持
- マルチターン対話のサポート
- `clear`コマンドでセッションリセット

### 🎨 美しいUI
- Richライブラリによるターミナル表示
- マークダウンレンダリング
- カラフルなパネルとボーダー
- エージェントごとの色分け

## 使用方法

### 基本的な使い方

1. プログラムを起動
2. メッセージを入力してEnterキーで送信
3. エージェントからの応答を確認
4. 必要に応じてエージェント間でタスクが委譲される

### コマンド

- `quit` / `exit` / `q`: チャットを終了
- `clear`: セッション（会話履歴）をクリア
- Ctrl+C: セッションを中断

### 使用例

```
👤 You: 現在の時刻を教えて

🤖 Assistant: [現在時刻が表示される]

👤 You: (2 + 3) * 5を計算して

🤖 Assistant: [計算結果: 25]

👤 You: フィボナッチ数列について詳しく説明して

🤖 MathExpert: [数学的な詳細説明]
```

## OpenAI Agents SDK の特徴

### Core Primitives

1. **Agents**: 指示とツールを装備したLLM
2. **Handoffs**: エージェント間のタスク委譲
3. **Guardrails**: 入出力の検証（オプション）
4. **Sessions**: 自動的な会話履歴管理
5. **Tracing**: デバッグとモニタリング

### 利点

- **軽量**: 最小限の抽象化で使いやすい
- **柔軟**: プロバイダー非依存（100以上のLLMをサポート）
- **強力**: 複雑なマルチエージェントワークフローに対応
- **自動化**: セッション管理が自動的

## カスタマイズ

### エージェントの追加

新しいエージェントを追加する場合:

```python
new_agent = Agent(
    name="SpecialistName",
    instructions="エージェントの役割と指示",
    tools=[tool1, tool2],
    model="gpt-4o-mini",
)
```

### ツールの追加

Python関数を簡単にツールとして追加:

```python
def your_tool(param: str) -> str:
    """
    ツールの説明（自動的にスキーマ生成）

    Args:
        param: パラメータの説明

    Returns:
        結果の説明
    """
    # ツールの実装
    return result
```

### ハンドオフの設定

エージェント間の委譲を設定:

```python
agent1.handoffs.append(
    Handoff(
        agent=agent2,
        description="agent2に委譲する条件の説明"
    )
)
```

## 技術スタック

- **openai-agents**: OpenAI Agents SDK (マルチエージェントフレームワーク)
- **rich**: ターミナルの美しい表示
- **python-dotenv**: 環境変数管理
- **Python 3.12+**: 最新のPython機能を活用

## 参考リンク

- [OpenAI Agents SDK ドキュメント](https://openai.github.io/openai-agents-python/)
- [GitHub リポジトリ](https://github.com/openai/openai-agents-python)
- [PyPI パッケージ](https://pypi.org/project/openai-agents/)
- [OpenAI Platform](https://platform.openai.com/)

## 注意事項

- OpenAI APIの使用には課金が発生します
- APIキーは`.env`ファイルで管理し、Gitにコミットしないでください
- セッションは現在メモリ内にのみ保存されます（プログラム終了で消失）

## 今後の拡張予定

- [ ] より多くの専門エージェントの追加
- [ ] Guardrails（入出力検証）の実装
- [ ] Tracingの有効化とログ出力
- [ ] カスタムツールの拡充
- [ ] 複雑なマルチエージェントワークフローの例
- [ ] セッションの永続化
