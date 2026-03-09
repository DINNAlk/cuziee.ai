import gradio as gr
from app.router import route_question


def respond(message, history):
    result = route_question(message, history)
    answer = result["answer"].strip()
    return answer


demo = gr.ChatInterface(
    fn=respond,
    title="Cuziee AI v2",
    description="Router-based AI assistant with expert models | DEMO",
    textbox=gr.Textbox(
        placeholder="Ask Cuziee anything..."
    )
)

demo.launch()