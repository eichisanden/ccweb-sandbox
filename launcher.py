#!/usr/bin/env python3
"""
AI Agent Project Launcher
Interactive menu to run different components of the project
"""
import subprocess
import sys
import os


def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("🎯 AI Agent Project Launcher")
    print("=" * 60)
    print("\n[Menu]")
    print("1. 🤖 Run AI Agent Interactive Chat")
    print("2. 👋 Exit")
    print()


def run_chat():
    """Run the AI Agent chat application"""
    try:
        print("\n" + "─" * 60)
        print("🚀 Starting AI Agent Chat...")
        print("─" * 60 + "\n")

        # Get the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Run the chat application
        result = subprocess.run(
            ["uv", "run", "main.py"],
            cwd=os.path.join(script_dir, "claude-agent-project")
        )

        print("\n" + "─" * 60)
        print("✅ Chat session ended")
        print("─" * 60)

        return result.returncode
    except FileNotFoundError:
        print("\n❌ Error: 'uv' command not found. Please install uv first.")
        print("   Visit: https://docs.astral.sh/uv/")
        return 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


def main():
    """Main function to run the launcher"""
    print("\n🌟 Welcome to AI Agent Project!")

    while True:
        show_menu()

        try:
            choice = input("👉 Select an option (1-2): ").strip()

            if choice == "1":
                run_chat()
                input("\n📌 Press Enter to return to menu...")
            elif choice == "2":
                print("\n👋 Thank you for using AI Agent Project. Goodbye!")
                break
            else:
                print("\n⚠️  Invalid option. Please select 1 or 2.")

        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Session ended. Goodbye!")
            break


if __name__ == "__main__":
    main()
