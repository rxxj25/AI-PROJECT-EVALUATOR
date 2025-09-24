@echo off
echo ========================================
echo AI-Powered Project Evaluator
echo NatWest Hackathon 2025
echo ========================================
echo.
echo Starting the application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Install dependencies if requirements.txt exists
if exist requirements.txt (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo.
)

REM Start the application
echo Starting AI Project Evaluator...
echo.
echo Dashboard will be available at: http://localhost:5000
echo Press Ctrl+C to stop the application
echo.
python run.py

pause
