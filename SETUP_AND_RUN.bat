@echo off
REM ========================================
REM  SETUP_AND_RUN.bat - Windows Batch File
REM  One-Click Setup for Fact-Checker
REM ========================================

echo.
echo ==================================================
echo    AUTOMATED FACT-CHECKER SETUP FOR WINDOWS
echo ==================================================
echo.
echo This will install everything and run the app!
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1] Installing dependencies...
echo.
python -m pip install -q pandas numpy scikit-learn sentence-transformers faiss-cpu flask flask-cors nltk langdetect google-trans-new streamlit

echo [2] Creating sample data...
echo.
python SETUP_AND_RUN.py

pause
