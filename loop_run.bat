@echo off
setlocal

:: === CONFIGURATION ===
set "PROGRAM_PATH="C:\Users\user\Desktop\program.exe""
set "PROGRAM_NAME=program.exe"  :: Just the file name, used for killing
set "DELAY_BEFORE_ENTER=3"
set "WAIT_TIME=100"                 :: Time in seconds (100 sec)
set "DELAY_AFTER_CLOSE=2"
:LOOP
