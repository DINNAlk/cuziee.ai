from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.router import route_question
from app.db.database import engine, SessionLocal
from app.db.models import Base
from app.db.repository import (
    get_or_create_user,
    create_conversation,
    get_conversation,
    save_message,
    get_recent_messages,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cuziee AI v2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    username: str
    question: str
    conversation_id: int | None = None


@app.get("/")
def home():
    return {"message": "Cuziee AI v2 is running"}


@app.post("/ask")
def ask(req: QueryRequest):
    db = SessionLocal()

    try:
        user = get_or_create_user(db, req.username)

        if req.conversation_id:
            conversation = get_conversation(db, req.conversation_id)
            if conversation is None:
                conversation = create_conversation(db, user.id, title="New Chat")
        else:
            conversation = create_conversation(db, user.id, title="New Chat")

        old_messages = get_recent_messages(db, conversation.id, limit=20)

        history = []
        user_buffer = None

        for msg in old_messages:
            if msg.role == "user":
                user_buffer = msg.content
            elif msg.role == "assistant" and user_buffer is not None:
                history.append((user_buffer, msg.content))
                user_buffer = None

        save_message(db, conversation.id, "user", req.question)

        result = route_question(req.question, history)

        save_message(db, conversation.id, "assistant", result["answer"])

        return {
            "conversation_id": conversation.id,
            "category": result["category"],
            "used_web_search": result["used_web_search"],
            "answer": result["answer"]
        }

    finally:
        db.close()
