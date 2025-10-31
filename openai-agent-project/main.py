"""
OpenAI Agent Example
A simple AI agent using the OpenAI Chat Completions API
"""
import os
import anyio
from openai import AsyncOpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.rule import Rule

# Initialize rich console
console = Console()

# Conversation history
messages = []


def create_client():
    """Create and configure the OpenAI client"""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    return AsyncOpenAI(api_key=api_key)


def display_message(role: str, content: str):
    """Display a message with rich formatting"""
    if role == "assistant":
        msg_type = "🤖 Assistant"
        panel_style = "cyan"
    elif role == "user":
        msg_type = "👤 User"
        panel_style = "green"
    elif role == "system":
        msg_type = "⚙️ System"
        panel_style = "yellow"
    else:
        msg_type = f"❓ {role}"
        panel_style = "white"

    # Render content as Markdown for beautiful formatting
    md = Markdown(content)
    console.print(Panel(md, title=msg_type, border_style=panel_style))


async def run_chat(client: AsyncOpenAI, user_message: str, model: str = "gpt-4o-mini"):
    """Run the chat with streaming"""
    try:
        # Add user message to history
        messages.append({"role": "user", "content": user_message})

        console.print("\n[bold cyan]🔄 Processing query...[/bold cyan]")

        # Create streaming chat completion
        stream = await client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

        # Collect the streamed response
        collected_content = ""
        console.print()
        console.print(Panel.fit("🤖 Assistant", border_style="cyan"))

        async for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                collected_content += content
                console.print(content, end="", markup=False)

        console.print()  # New line after streaming

        # Add assistant response to history
        messages.append({"role": "assistant", "content": collected_content})

        console.print()

    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {str(e)}")


async def main():
    """Main function to run the agent"""
    console.print()
    console.rule("[bold cyan]🤖 OpenAI Agent - Interactive Chat[/bold cyan]")
    console.print()
    console.print("[dim]Type your message and press Enter to chat with OpenAI.[/dim]")
    console.print("[dim]Commands: 'quit', 'exit' to end, 'clear' to clear history[/dim]\n")

    try:
        # Initialize the client
        client = create_client()
        console.print("[green]✅ OpenAI client initialized successfully![/green]\n")

        while True:
            # Get user input
            console.rule(style="dim")
            try:
                user_input = console.input("[bold green]👤 You:[/bold green] ").strip()
            except EOFError:
                console.print("\n\n[bold yellow]👋 Session ended.[/bold yellow]")
                break

            # Check for exit commands
            if user_input.lower() in ["quit", "exit", "q"]:
                console.print("\n[bold yellow]👋 Goodbye![/bold yellow]")
                break

            # Check for clear command
            if user_input.lower() == "clear":
                messages.clear()
                console.print("[yellow]🗑️  Conversation history cleared.[/yellow]")
                continue

            # Skip empty inputs
            if not user_input:
                console.print("[yellow]⚠️  Please enter a message.[/yellow]")
                continue

            # Process the query
            await run_chat(client, user_input)

    except ValueError as e:
        console.print(f"\n[bold red]❌ Configuration Error:[/bold red] {e}")
        console.print("\n[yellow]Please create a .env file with your OPENAI_API_KEY[/yellow]")
        console.print("[dim]Copy .env.example to .env and add your API key[/dim]")
    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]👋 Session interrupted. Goodbye![/bold yellow]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {e}")


if __name__ == "__main__":
    anyio.run(main)
