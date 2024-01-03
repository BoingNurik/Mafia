@echo off

call %~dp0mafia\bot\venv\Scripts\activate

cd %~dp0mafia\bot

set TOKEN=6794927045:AAF2CyMxqA76tSYqq78zWCSGKIMNKs3l6HY
python main.py

pause