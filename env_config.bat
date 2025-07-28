@echo off
chcp 65001 >nul
echo ========================================
echo    FlashMate Environment Setup
echo ========================================
echo.

:: Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed.
    echo Please install Python 3.8 or higher: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo SUCCESS: Python %PYTHON_VERSION% found

:: Check if virtual environment exists
if exist "venv" (
    echo.
    echo SUCCESS: Existing virtual environment found.
    echo PROCESSING: Activating virtual environment...
    call "venv\Scripts\activate.bat"
    if errorlevel 1 (
        echo ERROR: Failed to activate virtual environment
        echo Creating new virtual environment...
        goto :create_venv
    )
    echo SUCCESS: Virtual environment activated successfully
    goto :ask_run
)

:create_venv
echo.
echo PROCESSING: Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo SUCCESS: Virtual environment created successfully

:: Activate virtual environment
echo.
echo Activating virtual environment...
call "venv\Scripts\activate.bat"
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo SUCCESS: Virtual environment activated successfully

:: Upgrade pip
echo.
echo PROCESSING: Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo WARNING: Failed to upgrade pip (continuing...)
)

:: Install dependencies
echo.
echo INSTALLING: Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo SUCCESS: Dependencies installed successfully

:: Install in development mode
echo.
echo INSTALLING: Installing in development mode...
pip install -e .
if errorlevel 1 (
    echo ERROR: Failed to install in development mode
    pause
    exit /b 1
)
echo SUCCESS: Development mode installation completed

:ask_run
echo.
echo ========================================
echo    SUCCESS: Environment setup completed!
echo ========================================
echo.
echo Would you like to run the application?
echo.
echo [1] Run
echo [2] Exit
echo.
set /p choice="Please select (1 or 2): "

if "%choice%"=="1" (
    echo.
    echo STARTING: Starting FlashMate...
    python run.py
) else (
    echo.
    echo You can run the application with:
    echo   python run.py
    echo.
    echo ========================================
    pause
)
