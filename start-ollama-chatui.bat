@echo off
echo [INFO] Starte die Ollama Gradio Chat-App...

:: Überprüfen, ob Python installiert ist
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python ist nicht installiert oder nicht im PATH!
    pause
    exit
)

:: Installiere Abhängigkeiten aus requirements.txt
echo [INFO] Installiere benoetigte Bibliotheken...
pip install -r requirements.txt

:: Starte das Python-Skript in einem neuen Fenster
start /B python ollama_chat.py

pause
