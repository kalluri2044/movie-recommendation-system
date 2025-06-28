@echo off
echo 🎬 Movie Recommendation System
echo ===============================
echo Starting Streamlit server...
echo.

cd /d "%~dp0"
python -m streamlit run app.py

echo.
echo Press any key to exit...
pause > nul
