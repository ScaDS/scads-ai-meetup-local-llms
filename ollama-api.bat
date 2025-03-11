@echo off
setlocal enabledelayedexpansion

:: IP manuell eingeben (ohne Speicherung)
set /p OLLAMA_IP="Bitte die IP des Ollama-Endpoints eingeben (z. B. 127.0.0.1): "

:: Möglichkeit, das Skript zu beenden
if "%OLLAMA_IP%"=="" (
    echo [INFO] Keine IP eingegeben. Skript wird beendet.
    exit
)

:: Frage und Modell abfragen
echo.
set /p USER_INPUT="Gib deine Frage ein: "

:: Möglichkeit, das Skript zu beenden
if "%USER_INPUT%"=="" (
    echo [INFO] Keine Frage eingegeben. Skript wird beendet.
    exit
)

set /p MODEL="Welches Modell soll genutzt werden? (Standard: llama3.2:1b) > "
if "%MODEL%"=="" set MODEL=llama3.2:1b

:: API Call und JSON-Response speichern
echo.
echo [INFO] Frage wird an die Ollama API gesendet...
curl -s -X POST http://%OLLAMA_IP%:11434/api/generate -H "Content-Type: application/json" -d "{\"model\":\"%MODEL%\",\"prompt\":\"%USER_INPUT%\"}" 
echo.
pause
exit
