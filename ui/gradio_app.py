import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/ask"

CURRENT_USERNAME = "dinusha"
CURRENT_CONVERSATION_ID = None


def respond(message, history):
    global CURRENT_CONVERSATION_ID

    payload = {
        "username": CURRENT_USERNAME,
        "question": message,
        "conversation_id": CURRENT_CONVERSATION_ID
    }

    try:
        response = requests.post(API_URL, json=payload)
        data = response.json()

        CURRENT_CONVERSATION_ID = data["conversation_id"]

        return data["answer"].strip()

    except Exception:
        return "Backend server is not running. Start FastAPI first."



demo = gr.ChatInterface(
    fn=respond,
    title="Cuziee AI v2",
    description="Router-based AI assistant with expert models and persistent memory",
    textbox=gr.Textbox(
        placeholder="Ask Cuziee anything..."
    )
)

demo.launch()
