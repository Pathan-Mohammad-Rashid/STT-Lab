@echo off
for /L %%i in (1,1,5) do (
    echo Sequential Run %%i: >> sequential_output.txt
    powershell -Command "Measure-Command { pytest }" >> sequential_output.txt 2>&1
)
