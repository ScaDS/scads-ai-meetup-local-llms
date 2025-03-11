import gradio as gr
import requests
import json
import time

# Standardwerte für die API
DEFAULT_IP = "http://192.168.0.2:11434"
DEFAULT_MODEL = "qwen2.5:14b"

# Funktion für die Ollama API (gibt nur den fertigen Text zurück!)
def respond(message, chat_history, ip, model):
    endpoint = f"{ip}/api/generate"
    payload = {"model": model, "prompt": message}

    try:
        response = requests.post(endpoint, json=payload)
        response_text = response.text.strip()

        # JSON-Parsing mit Fehlerhandling (Kombiniert alle "response"-Teile zu einem Satz)
        try:
            bot_message = ""
            for line in response_text.split("\n"):
                json_obj = json.loads(line)
                if "response" in json_obj:
                    bot_message += json_obj["response"]  # Alle Stücke zusammensetzen
        except json.JSONDecodeError:
            bot_message = f"Fehler: Ungültige Antwort von Ollama → {response_text}"

    except requests.exceptions.RequestException as e:
        bot_message = f"Fehler: Keine Verbindung zur Ollama API → {str(e)}"

    # Nachrichtenverlauf aktualisieren (Gradio-konformes JSON-Format)
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_message})

    time.sleep(1)  # Simulierte Antwortverzögerung
    return "", chat_history

# Erstelle die Gradio-App
with gr.Blocks() as demo:
    gr.Markdown("# 🦙 Ollama Chatbot mit Gradio")

    # IP & Modell-Felder
    with gr.Row():
        ip_input = gr.Textbox(value=DEFAULT_IP, label="Ollama API IP")
        model_input = gr.Textbox(value=DEFAULT_MODEL, label="Modell wählen")

    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(label="Deine Nachricht")
    clear = gr.ClearButton([msg, chatbot])

    # User-Eingabe verbindet sich mit der Ollama API
    msg.submit(lambda m, h: respond(m, h, ip_input.value, model_input.value), [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()
