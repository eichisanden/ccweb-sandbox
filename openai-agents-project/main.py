"""
OpenAI Agents SDK Example
A multi-agent AI system using the OpenAI Agents SDK
"""
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.rule import Rule

from agents import Agent, Runner, Session, Handoff

# Initialize rich console
console = Console()


def get_current_time() -> str:
    """Get the current time as a tool example."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression safely.

    Args:
        expression: A mathematical expression to evaluate (e.g., "2 + 2", "10 * 5")

    Returns:
        The result of the calculation as a string
    """
    try:
        # Safe evaluation of simple math expressions
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"


def create_agents():
    """Create the AI agents with tools and instructions"""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    # Main assistant agent with tools
    assistant = Agent(
        name="Assistant",
        instructions="""You are a helpful AI assistant with access to various tools.
        You can:
        - Answer general questions
        - Get the current time
        - Perform mathematical calculations
        - Hand off to a specialized math expert for complex calculations

        Be friendly and helpful!""",
        tools=[get_current_time, calculate],
        model="gpt-4o-mini",
    )

    # Specialized math expert agent
    math_expert = Agent(
        name="MathExpert",
        instructions="""You are a mathematics expert.
        Help users solve complex mathematical problems step by step.
        Use the calculate tool for computations.
        When done, return control to the main assistant.""",
        tools=[calculate],
        model="gpt-4o-mini",
    )

    # Set up handoff from assistant to math expert
    assistant.handoffs.append(
        Handoff(
            agent=math_expert,
            description="Transfer to math expert for complex calculations or mathematical explanations"
        )
    )

    # Set up handoff back to assistant
    math_expert.handoffs.append(
        Handoff(
            agent=assistant,
            description="Return to main assistant"
        )
    )

    return assistant, math_expert


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
    elif role == "tool":
        msg_type = "🔧 Tool"
        panel_style = "magenta"
    else:
        msg_type = f"❓ {role}"
        panel_style = "white"

    # Render content as Markdown
    md = Markdown(content)
    console.print(Panel(md, title=msg_type, border_style=panel_style))


def main():
    """Main function to run the agent"""
    console.print()
    console.rule("[bold cyan]🤖 OpenAI Agents SDK - Interactive Chat[/bold cyan]")
    console.print()
    console.print("[dim]Multi-agent system with tool usage and handoffs[/dim]")
    console.print("[dim]Commands: 'quit', 'exit' to end, 'clear' to clear session[/dim]\n")

    try:
        # Initialize agents
        console.print("[cyan]🔄 Initializing agents...[/cyan]")
        assistant, math_expert = create_agents()
        console.print("[green]✅ Agents initialized successfully![/green]")
        console.print("[dim]  - Assistant (main agent with tools)[/dim]")
        console.print("[dim]  - MathExpert (specialized math agent)[/dim]\n")

        # Create a session for maintaining conversation history
        session = Session()

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
                session = Session()
                console.print("[yellow]🗑️  Session cleared.[/yellow]")
                continue

            # Skip empty inputs
            if not user_input:
                console.print("[yellow]⚠️  Please enter a message.[/yellow]")
                continue

            # Run the agent
            console.print("\n[bold cyan]🔄 Processing...[/bold cyan]\n")

            try:
                # Run agent with session
                result = Runner.run_sync(
                    starting_agent=assistant,
                    input=user_input,
                    session=session,
                )

                # Display the response
                if result.final_output:
                    display_message("assistant", result.final_output)

                # Show which agent responded if not the main assistant
                if hasattr(result, 'agent_name') and result.agent_name != "Assistant":
                    console.print(f"[dim]Response from: {result.agent_name}[/dim]")

                console.print()

            except Exception as e:
                console.print(f"\n[bold red]❌ Error:[/bold red] {str(e)}\n")

    except ValueError as e:
        console.print(f"\n[bold red]❌ Configuration Error:[/bold red] {e}")
        console.print("\n[yellow]Please create a .env file with your OPENAI_API_KEY[/yellow]")
        console.print("[dim]Copy .env.example to .env and add your API key[/dim]")
    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]👋 Session interrupted. Goodbye![/bold yellow]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {e}")


if __name__ == "__main__":
    main()
