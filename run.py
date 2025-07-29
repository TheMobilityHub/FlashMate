#!/usr/bin/env python3
"""
FlashMate Unified Run Manager
"""
import sys
import subprocess
import os
from pathlib import Path


def print_banner():
    print("=" * 50)
    print("    FlashMate - Firmware Extraction Tool")
    print("=" * 50)
    print()


def check_venv():
    if not hasattr(sys, "real_prefix") and not (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ):
        print("Virtual environment is not activated.")
        print("Please run env_config.bat first.")
        input("Press Enter to exit...")
        return False
    return True


def run_program():
    print("Running FlashMate...")
    print()
    try:
        project_root = Path(__file__).parent
        src_path = project_root / "src"
        sys.path.insert(0, str(src_path))
        from main import main as app_main

        app_main()
    except ImportError as e:
        print(f"Module import error: {e}")
        print("Make sure your virtual environment is activated.")
        input("Press Enter to exit...")
        return False
    except Exception as e:
        print(f"Runtime error: {e}")
        input("Press Enter to exit...")
        return False
    return True





def run_designer():
    print("Starting Qt Designer...")
    print()
    try:
        # Try to run pyside6-designer
        ui_file_path = Path(__file__).parent / "src" / "ui" / "main_window.ui"
        result = subprocess.run(
            ["pyside6-designer", str(ui_file_path)],
            capture_output=False,
            text=True,
            encoding="utf-8",
        )
        if result.returncode == 0:
            print("Qt Designer closed.")
        else:
            print("Qt Designer failed to start.")
        input("Press Enter to continue...")
        return True
    except FileNotFoundError:
        print("Qt Designer not found.")
        print("Please install pyside6-tools:")
        print("  pip install pyside6-tools")
        input("Press Enter to continue...")
        return False
    except Exception as e:
        print(f"Designer error: {e}")
        input("Press Enter to exit...")
        return False


def show_menu():
    print("Please select one of the following options:")
    print()
    print("[1] Run Program    - Run the application")
    print("[2] Qt Designer    - Open UI designer")
    print("[3] Exit           - Exit")
    print()


def get_user_choice():
    while True:
        try:
            choice = input("Select (1-3): ").strip()
            if choice in ["1", "2", "3"]:
                return choice
            else:
                print("Please select between 1 and 3.")
        except KeyboardInterrupt:
            print("\n\nExiting program.")
            sys.exit(0)


def main():
    if not check_venv():
        return 1
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print_banner()
        show_menu()
        choice = get_user_choice()
        if choice == "1":
            run_program()
        elif choice == "2":
            run_designer()
        elif choice == "3":
            print("Exiting program.")
            break
    return 0


if __name__ == "__main__":
    sys.exit(main())
