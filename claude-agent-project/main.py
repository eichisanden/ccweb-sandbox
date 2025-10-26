"""
Claude Agent SDK Example
A simple AI agent using the Anthropic Claude API
"""
import os
from anthropic import Anthropic
from dotenv import load_dotenv


def create_agent():
    """Create and configure the Claude agent"""
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

    client = Anthropic(api_key=api_key)
    return client


def run_agent(client, user_message: str, max_tokens: int = 1024):
    """Run the agent with a user message"""
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        return message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function to run the agent"""
    print("Claude Agent SDK - Simple Example")
    print("=" * 50)

    try:
        # Initialize the agent
        client = create_agent()
        print("Agent initialized successfully!")

        # Example interaction
        user_input = "Hello! What can you help me with?"
        print(f"\nUser: {user_input}")

        response = run_agent(client, user_input)
        print(f"\nAgent: {response}")

    except ValueError as e:
        print(f"\nConfiguration Error: {e}")
        print("\nPlease create a .env file with your ANTHROPIC_API_KEY")
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
