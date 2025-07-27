#!/usr/bin/env python3
"""
FlashMate Clean Script (Windows Only)
"""
import shutil
from pathlib import Path

def main():
    """Main function"""
    project_root = Path(__file__).parent.parent
    
    print("Starting FlashMate project clean...")
    
    # Directories to clean
    clean_dirs = [
        project_root / "build" / "dist",
        project_root / "build" / "work",
        project_root / "__pycache__",
        project_root / "src" / "__pycache__",
    ]
    
    # Files to clean
    clean_files = [
        project_root / "*.spec",
    ]
    
    # Clean directories
    for dir_path in clean_dirs:
        if dir_path.exists():
            print(f"Deleting {dir_path} ...")
            try:
                shutil.rmtree(dir_path)
                print(f"{dir_path} deleted.")
            except Exception as e:
                print(f"Failed to delete {dir_path}: {e}")
    
    # Clean files
    for file_pattern in clean_files:
        for file_path in project_root.glob(file_pattern.name):
            print(f"Deleting {file_path} ...")
            try:
                file_path.unlink()
                print(f"{file_path} deleted.")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
    
    print("Clean completed!")

if __name__ == "__main__":
    main() 