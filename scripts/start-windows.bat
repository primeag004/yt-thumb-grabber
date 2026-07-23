@echo off
setlocal
cd /d "%~dp0.."
set HOST=127.0.0.1
set PORT=12076
echo Starting Niji Local at http://127.0.0.1:12076
start "Niji Local" http://127.0.0.1:12076
call npm start
endlocal
