import gradio as gr
from app.agent import chat


def respond(message, history):
    return chat(message, history)


demo = gr.ChatInterface(
    fn=respond,
    title="Cuziee AI V1",
    description="Your emotional AI companion",
    textbox=gr.Textbox(placeholder="Talk to Cuziee...")
)

demo.launch()