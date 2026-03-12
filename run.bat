@echo off
echo Starting OC Pass Rates Viewer...
echo.
echo Please keep this command prompt open while using the viewer.
echo If it does not open automatically, go to http://localhost:8000 in your browser.
echo.

:: Generate the data/index.json file first
echo Generating data index...
python generate_index.py
echo.

:: Start python http.server in a new command window
start /min cmd /c "python -m http.server 8000"

:: Wait a moment for server to start
timeout /t 2 > nul

:: Open default browser
start http://localhost:8000
