from fastapi import FastAPI
from pydantic import BaseModel

from agent import chat
from app.router import route_question
from emotion import detect_emotion

app = FastAPI(title="Cuziee AI v2")


class QueryRequest(BaseModel):
    question: str



@app.get("/")
def home():
    return {"message": "Cuziee AI v2 running"}


@app.post("/ask")
def ask(req: QueryRequest):
    result = route_question(req.question)
    return result