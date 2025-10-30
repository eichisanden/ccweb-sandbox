"""
Claude Agent SDK Example
A simple AI agent using the Claude Agent SDK
"""
import anyio
from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    AssistantMessage,
    UserMessage,
    SystemMessage,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
    ToolResultBlock,
)
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.syntax import Syntax
from rich.json import JSON
from rich.rule import Rule

# Initialize rich console
console = Console()


# Configure agent options to enable web search
AGENT_OPTIONS = ClaudeAgentOptions(
    allowed_tools=[
        "Read",
        "Write",
        "Edit",
        "Bash",
        "Glob",
        "Grep",
        "WebSearch",  # Enable web search
        "WebFetch",   # Enable web fetch
    ],
    permission_mode="acceptEdits",  # Auto-accept file edits for smoother workflow
)


def display_message(message):
    """Display a message with rich formatting based on its type"""
    # Determine message type and style
    if isinstance(message, AssistantMessage):
        msg_type = "🤖 Assistant"
        panel_style = "cyan"
    elif isinstance(message, UserMessage):
        msg_type = "👤 User"
        panel_style = "green"
    elif isinstance(message, SystemMessage):
        msg_type = "⚙️ System"
        panel_style = "yellow"
    elif isinstance(message, ResultMessage):
        msg_type = "✅ Result"
        panel_style = "green"
    else:
        msg_type = f"❓ {type(message).__name__}"
        panel_style = "white"

    # Process content blocks
    if hasattr(message, 'content'):
        if isinstance(message.content, str):
            # Simple string content
            console.print(Panel(message.content, title=msg_type, border_style=panel_style))
        elif isinstance(message.content, list):
            for block in message.content:
                if isinstance(block, TextBlock):
                    # Render text as Markdown for beautiful formatting
                    md = Markdown(block.text)
                    console.print(Panel(md, title=msg_type, border_style=panel_style))
                elif isinstance(block, ToolUseBlock):
                    # Display tool usage with syntax highlighting
                    tool_title = f"🔧 Tool: {block.name}"
                    if hasattr(block, 'input') and block.input:
                        json_obj = JSON.from_data(block.input)
                        console.print(Panel(json_obj, title=tool_title, border_style="magenta"))
                    else:
                        console.print(Panel(f"Tool: {block.name}", title=tool_title, border_style="magenta"))
                elif isinstance(block, ToolResultBlock):
                    # Display tool results
                    result_title = f"🔨 Tool Result (ID: {block.tool_use_id[:8]}...)"
                    if hasattr(block, 'content'):
                        content = str(block.content)
                        # Try to render as markdown if it looks like text
                        if len(content) < 5000 and '\n' in content:
                            console.print(Panel(Markdown(content), title=result_title, border_style="blue"))
                        else:
                            console.print(Panel(content, title=result_title, border_style="blue"))
                    else:
                        console.print(Panel("(no content)", title=result_title, border_style="blue"))
                else:
                    # Fallback for unknown block types
                    console.print(Panel(str(block), title=f"{type(block).__name__}", border_style="white"))
        else:
            # Fallback for non-list, non-string content
            console.print(Panel(str(message.content), title=msg_type, border_style=panel_style))
    else:
        # Fallback if no content attribute
        console.print(Panel(str(message), title=msg_type, border_style=panel_style))


async def run_agent(user_message: str):
    """Run the agent with a user message"""
    try:
        console.print("\n[bold cyan]🔄 Processing query...[/bold cyan]")
        async for message in query(prompt=user_message, options=AGENT_OPTIONS):
            display_message(message)
    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {str(e)}")


async def main():
    """Main function to run the agent"""
    console.print()
    console.rule("[bold cyan]🤖 Claude Agent SDK - Interactive Chat[/bold cyan]")
    console.print()
    console.print("[dim]Type your message and press Enter to chat with Claude.[/dim]")
    console.print("[dim]Commands: 'quit' or 'exit' to end the session[/dim]\n")

    try:
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

            # Skip empty inputs
            if not user_input:
                console.print("[yellow]⚠️  Please enter a message.[/yellow]")
                continue

            # Process the query
            await run_agent(user_input)
            console.print()  # Add spacing between conversations

    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]👋 Session interrupted. Goodbye![/bold yellow]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {e}")


if __name__ == "__main__":
    anyio.run(main)
