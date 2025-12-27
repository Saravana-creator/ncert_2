@echo off
echo Starting NCERT AI Service with Virtual Environment...
echo.

cd /d "%~dp0"

if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing/Updating dependencies...
pip install -r requirements.txt --quiet

echo.
echo Starting AI Service on port 8001...
echo.
python main.py

pause