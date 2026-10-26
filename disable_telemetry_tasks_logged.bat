@echo off
setlocal EnableDelayedExpansion
:: Logging setup
set "logfile=%~dp0telemetry_disable_log_%DATE:/=-%_%TIME::=-%.log"
echo [*] Logging to: "%logfile%"
echo Windows Telemetry Task Disabler >> "%logfile%"
echo Started: %DATE% %TIME% >> "%logfile%"
echo ---------------------------------------- >> "%logfile%"
:: Admin check
>nul 2>&1 net session || (
  echo [!] Please run this script as Administrator.
  echo [!] Admin check failed >> "%logfile%"
  pause
  exit /b
)
echo [*] Disabling telemetry-related scheduled tasks...
echo Disabling tasks... >> "%logfile%"
:: List of telemetry tasks to disable
