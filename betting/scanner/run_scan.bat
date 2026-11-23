@echo off
REM Double-click to run the Betfair goals scanner.
cd /d "%~dp0"
title Betfair goals scanner
python scan.py %*
echo.
pause
