@echo off
setlocal EnableDelayedExpansion
:: Logging setup
set "logfile=%~dp0telemetry_disable_log_%DATE:/=-%_%TIME::=-%.log"
echo [*] Logging to: "%logfile%"
