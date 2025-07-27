@echo off
chcp 65001 >nul
echo ========================================
echo    FlashMate 환경 설정
echo ========================================
echo.

:: Python 설치 확인
echo Python 설치 확인 중...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python이 설치되어 있지 않습니다.
    echo Python 3.8 이상을 설치해주세요: https://www.python.org/downloads/
    echo 설치 시 "Add Python to PATH" 옵션을 체크해주세요.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% 발견

:: 가상환경 존재 여부 확인
if exist "venv" (
    echo.
    echo ✅ 기존 가상환경이 발견되었습니다.
    echo 🔄 가상환경을 활성화합니다...
    call "venv\Scripts\activate.bat"
    if errorlevel 1 (
        echo ❌ 가상환경 활성화 실패
        echo 가상환경을 다시 생성합니다...
        goto :create_venv
    )
    echo ✅ 가상환경 활성화 완료
    goto :ask_run
)

:create_venv
echo.
echo 🔄 가상환경 생성 중...
python -m venv venv
if errorlevel 1 (
    echo ❌ 가상환경 생성 실패
    pause
    exit /b 1
)
echo ✅ 가상환경 생성 완료

:: 가상환경 활성화
echo.
echo 가상환경 활성화 중...
call "venv\Scripts\activate.bat"
if errorlevel 1 (
    echo ❌ 가상환경 활성화 실패
    pause
    exit /b 1
)
echo ✅ 가상환경 활성화 완료

:: pip 업그레이드
echo.
echo 🔄 pip 업그레이드 중...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo ⚠️  pip 업그레이드 실패 (계속 진행)
)

:: 의존성 설치
echo.
echo 📦 의존성 설치 중...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ 의존성 설치 실패
    pause
    exit /b 1
)
echo ✅ 의존성 설치 완료

:: 개발 모드 설치
echo.
echo 🔧 개발 모드 설치 중...
pip install -e .
if errorlevel 1 (
    echo ❌ 개발 모드 설치 실패
    pause
    exit /b 1
)
echo ✅ 개발 모드 설치 완료

:ask_run
echo.
echo ========================================
echo    🎉 환경 설정 완료!
echo ========================================
echo.
echo 애플리케이션을 실행하시겠습니까?
echo.
echo [1] 실행
echo [2] 종료
echo.
set /p choice="선택하세요 (1 또는 2): "

if "%choice%"=="1" (
    echo.
    echo 🚀 FlashMate를 실행합니다...
    python run.py
) else (
    echo.
    echo 다음 명령어로 실행할 수 있습니다:
    echo   python run.py
    echo.
    echo ========================================
    pause
) 