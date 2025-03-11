# Meetup Lokale LLMs 🚀

## 📄 Abstract
In diesem Meetup beschäftigen wir uns mit der Nutzung **lokaler Large Language Models (LLMs)** auf dem eigenen Rechner. Dazu setzen wir **Ollama** als LLM-Backend ein und nutzen **Gradio**, um eine einfache Chat-UI bereitzustellen. Zusätzlich testen wir die **Ollama API** mit speziell geschriebenen **Batch-Skripten**, die verschiedene Interaktionen ermöglichen. Ziel ist es, eine Umgebung zu schaffen, in der wir interaktiv mit einem lokalen LLM kommunizieren können, ohne auf Cloud-Dienste angewiesen zu sein.

## 🔧 Voraussetzungen
Damit das Projekt ausgeführt werden kann, benötigst du folgende Komponenten auf deinem System:

- **🐍 Python 3.8+** (am besten die neueste Version)
- **📦 Pip** (Python-Paketmanager, kommt mit Python)
- **💻 Ollama** (lokales LLM-Backend, kann [hier](https://ollama.com) installiert werden)
- **🌐 Internetverbindung** (zum einmaligen Installieren der Abhängigkeiten)
- **📜 Windows CMD oder eine andere Shell**, um die `.bat`-Skripte auszuführen

## 📂 Projektstruktur
```
📁 meetup-local-llms
├── 📁 slides
|   ├── 250311_meetup_workshop_local_llms_ollama_msty.pdf 
├── ollama-cmd.bat          # Batch-Skript zum direkten Start von Ollama
├── ollama-api.bat          # Batch-Skript zur Nutzung der Ollama API
├── ollama-chat.py          # GradioUI-Chatbot-Skript für Ollama via API
├── start-ollama-chatui.bat # Batch-Skript zum Start der Gradio-UI
├── requirements.txt        # Liste der benötigten Python-Pakete
├── README.md               # Dokumentation
```

## 🚀 Installation & Ausführung
### **1️⃣ Python & Ollama installieren**
Falls Python noch nicht installiert ist, kannst du es [hier herunterladen](https://www.python.org/downloads/). 
Wie du Ollama und alles weitere installierst, findest du in 📁 slides.

### **2️⃣ Repository klonen oder Dateien herunterladen**
Falls du das Projekt von GitHub holst:
```sh
git clone https://github.com/ScaDS/scads-ai-meetup-local-llms.git
cd scads-ai-meetup-local-llms
```
Wie du Git installieren kannst findest du [hier](https://git-scm.com/). 


### **3️⃣ Starten über die Batch-Dateien**
#### **Option 1: Direktes Arbeiten mit Ollama im Terminal**
Doppelklicke auf `ollama-cmd.bat`, um eine Terminal-Sitzung mit Ollama zu starten.

#### **Option 2: API-Nutzung testen**
Doppelklicke auf `ollama-api.bat`, um:
✅ Eine Eingabeaufforderung zur API-Nutzung zu öffnen
✅ Die IP des Ollama-Servers abzufragen
✅ Eine Frage an die API zu senden

#### **Option 3: Gradio UI starten**
Doppelklicke auf `start-ollama-chatui.bat`, um:
✅ **Die benötigten Abhängigkeiten zu installieren**
✅ **Den Gradio-Chatbot zu starten**

Alternativ kannst du alles manuell ausführen:
```sh
pip install -r requirements.txt
python chatbot.py
```

### **4️⃣ Chatbot im Browser öffnen**
Sobald Gradio läuft, kannst du den Chatbot in deinem Browser öffnen:  
**[http://127.0.0.1:7860](http://127.0.0.1:7860)**

Falls der Port bereits belegt ist, kannst du Gradio mit einem anderen Port starten:
```sh
python chatbot.py --server-port 7861
```

## 📜 Weitere Hinweise
- **⚡ Falls `start-ollama-chatui.bat` nicht funktioniert**, stelle sicher, dass Python korrekt installiert ist.
- **🔄 Falls du die Abhängigkeiten erneut installieren möchtest**, lösche einfach die `venv`-Umgebung (falls vorhanden) und starte `start-ollama-chatui.bat` erneut.
- **📢 Falls du nur mit der API arbeiten willst, kannst du `ollama-api.bat` nutzen**, um manuell Anfragen zu senden.

## 🎉 Viel Spaß beim Experimentieren mit lokalen LLMs! 🤖💬

