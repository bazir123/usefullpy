@echo off
setlocal

:: === CONFIGURATION ===
set "PROGRAM_PATH="C:\Users\user\Desktop\program.exe""
set "PROGRAM_NAME=program.exe"  :: Just the file name, used for killing
set "DELAY_BEFORE_ENTER=3"
set "WAIT_TIME=100"                 :: Time in seconds (100 sec)
set "DELAY_AFTER_CLOSE=2"
:LOOP
echo Starting program...
start "" "%PROGRAM_PATH%"
echo Waiting %DELAY_BEFORE_ENTER% seconds for the window to appear...
timeout /t %DELAY_BEFORE_ENTER% /nobreak >nul
echo Sending ENTER key...
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('~')"
echo Waiting %WAIT_TIME% seconds before closing...
timeout /t %WAIT_TIME% /nobreak >nul
echo Closing the program...
taskkill /f /im %PROGRAM_NAME% >nul 2>&1
echo Waiting %DELAY_AFTER_CLOSE% seconds before restarting...
timeout /t %DELAY_AFTER_CLOSE% /nobreak >nul
goto LOOP
