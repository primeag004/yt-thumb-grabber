@echo off
setlocal
where node >nul 2>nul
if errorlevel 1 (
  echo Node.js 18 or newer is required. Install it from https://nodejs.org/
  exit /b 1
)

echo Installing Niji Local (no telemetry, no runtime dependencies)...
call npm install --no-audit --no-fund
if errorlevel 1 exit /b 1

echo.
echo Done. Start the UI with scripts\start-windows.bat
endlocal
