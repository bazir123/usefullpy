@echo off
setlocal enabledelayedexpansion

set input=file.txt
set max=20000
set count=0
set fileIndex=1
for /f "usebackq delims=" %%A in ("%input%") do (
    if !count! EQU 0 (
        set outfile=output_!fileIndex!.txt
    )
    echo %%A>>!outfile!
    set /a count+=1
