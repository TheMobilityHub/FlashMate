#!/usr/bin/env python3
"""
FlashMate Main Application
"""
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))


def main():
    """Main function"""
    try:
        from PySide6.QtWidgets import QApplication
        from PySide6.QtUiTools import QUiLoader
        from PySide6.QtCore import QFile

        app = QApplication(sys.argv)

        # Load UI file
        ui_path = Path(__file__).parent / "ui" / "main_window.ui"
        ui_file = QFile(str(ui_path))

        if not ui_file.open(QFile.ReadOnly):
            print(f"ERROR: Could not open UI file: {ui_path}")
            input("Press Enter to exit...")
            return 1

        # Load the UI
        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()

        if not window:
            print(f"ERROR: Could not load UI file: {ui_path}")
            input("Press Enter to exit...")
            return 1

        # Set window title
        window.setWindowTitle("FlashMate")

        window.show()
        sys.exit(app.exec())

    except ImportError as e:
        print(f"ERROR: Module import error: {e}")
        print("Make sure your virtual environment is activated.")
        print("Please run env_config.bat.")
        input("Press Enter to exit...")
        return 1
    except Exception as e:
        print(f"ERROR: Runtime error: {e}")
        input("Press Enter to exit...")
        return 1


if __name__ == "__main__":
    main()
