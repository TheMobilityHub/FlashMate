#!/usr/bin/env python3
"""
FlashMate Main Application
"""
import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

def main():
    """Main function"""
    try:
        from PySide6.QtWidgets import QApplication
        from ui.main_window import MainWindow
        
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
        
    except ImportError as e:
        print(f"❌ Module import error: {e}")
        print("Make sure your virtual environment is activated.")
        print("Please run env_config.bat.")
        input("Press Enter to exit...")
        return 1
    except Exception as e:
        print(f"❌ Runtime error: {e}")
        input("Press Enter to exit...")
        return 1

if __name__ == "__main__":
    main() 