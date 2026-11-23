@echo off
REM Double-click to download the latest scanner code and team data. Your config.ini is not touched.
cd /d "%~dp0"
title Update Betfair goals scanner
set BASE=https://raw.githubusercontent.com/diarmuid2612-debug/etoro2/ccr-9705f93d-mjevci/betting/scanner
powershell -NoProfile -Command "Invoke-WebRequest %BASE%/scan.py -OutFile scan.py; Invoke-WebRequest %BASE%/teams.csv -OutFile teams.csv; Invoke-WebRequest %BASE%/run_scan.bat -OutFile run_scan.bat"
if errorlevel 1 (echo Update FAILED - check your internet connection.) else (echo Scanner updated.)
echo.
pause
