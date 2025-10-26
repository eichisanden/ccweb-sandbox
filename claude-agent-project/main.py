"""
Claude Agent SDK Example
A simple AI agent using the Claude Agent SDK
"""
import anyio
from claude_agent_sdk import (
    query,
    AssistantMessage,
    UserMessage,
    SystemMessage,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
    ToolResultBlock,
)
import json


def format_message(message) -> str:
    """Format a message for display based on its type"""
    # Determine message type
    if isinstance(message, AssistantMessage):
        msg_type = "🤖 Assistant"
    elif isinstance(message, UserMessage):
        msg_type = "👤 User"
    elif isinstance(message, SystemMessage):
        msg_type = "⚙️  System"
    elif isinstance(message, ResultMessage):
        msg_type = "✅ Result"
    else:
        msg_type = f"❓ {type(message).__name__}"

    # Format content blocks
    content_parts = []

    if hasattr(message, 'content'):
        if isinstance(message.content, str):
            content_parts.append(message.content)
        elif isinstance(message.content, list):
            for block in message.content:
                if isinstance(block, TextBlock):
                    content_parts.append(f"📝 {block.text}")
                elif isinstance(block, ToolUseBlock):
                    tool_info = f"🔧 Tool: {block.name}"
                    if hasattr(block, 'input') and block.input:
                        tool_info += f"\n   Input: {json.dumps(block.input, indent=2, ensure_ascii=False)}"
                    content_parts.append(tool_info)
                elif isinstance(block, ToolResultBlock):
                    result_info = f"🔨 Tool Result (ID: {block.tool_use_id})"
                    if hasattr(block, 'content'):
                        result_info += f"\n   {block.content}"
                    content_parts.append(result_info)
                else:
                    content_parts.append(f"   {type(block).__name__}: {block}")

    # Build final formatted message
    separator = "─" * 60
    formatted = f"\n{separator}\n{msg_type}\n{separator}\n"

    if content_parts:
        formatted += "\n".join(content_parts)
    else:
        # Fallback to str representation
        formatted += str(message)

    formatted += f"\n{separator}"

    return formatted


async def run_agent(user_message: str):
    """Run the agent with a user message"""
    try:
        print(f"\n🔄 Processing query...")
        async for message in query(prompt=user_message):
            print(format_message(message))
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


async def main():
    """Main function to run the agent"""
    print("Claude Agent SDK - Simple Example")
    print("=" * 50)

    try:
        # Example interaction
        user_input = "Hello! What can you help me with?"
        print(f"\nUser: {user_input}")

        await run_agent(user_input)

        # Another example
        print("\n" + "=" * 50)
        user_input2 = "What is 2 + 2?"
        print(f"\nUser: {user_input2}")

        await run_agent(user_input2)

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    anyio.run(main)
