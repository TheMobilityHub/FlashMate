import os
import sys
from pathlib import Path

# 실행파일 위치 기준으로 Database 폴더 설정
def get_database_path():
    """실행파일과 같은 위치에 Database 폴더 생성"""
    if getattr(sys, 'frozen', False):
        # PyInstaller로 빌드된 실행파일인 경우
        base_path = Path(sys.executable).parent
    else:
        # 개발 모드인 경우
        base_path = Path(__file__).parent.parent.parent
    
    return base_path / "FlashMate_Database"

# 상수 정의
DATABASE_PATH = get_database_path()
SUPPORTED_EXTENSIONS = ['.hex', '.s19', '.bin', '.elf']
MAX_ZIP_SIZE_MB = 1000
LOG_LEVEL = "INFO"

# UI 관련 상수
WINDOW_TITLE = "FlashMate - Firmware Extraction Tool"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 파일 처리 관련 상수
MAX_FILES_TO_PROCESS = 2  # 정확히 2개의 ZIP 파일만 처리
TEMP_EXTRACTION_DIR = "temp_extraction" 