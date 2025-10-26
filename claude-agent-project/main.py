"""
Claude Agent SDK Example
A simple AI agent using the Claude Agent SDK
"""
import anyio
from claude_agent_sdk import query


async def run_agent(user_message: str):
    """Run the agent with a user message"""
    try:
        print(f"\nAgent: ", end="", flush=True)
        async for message in query(prompt=user_message):
            print(message, end="", flush=True)
        print()  # New line after streaming completes
    except Exception as e:
        print(f"\nError: {str(e)}")


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
