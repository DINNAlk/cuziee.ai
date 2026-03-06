from fastapi import FastAPI
from pydantic import BaseModel

from agent import chat
from emotion import detect_emotion

app = FastAPI(title="Cuziee AI")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Cuziee AI API running"}


@app.post("/chat")
def chat_api(req: ChatRequest):
    emotion = detect_emotion(req.message)
    response = chat(req.message)

    print(response)

    return {
        "emotion": emotion,
        "response": response
    }