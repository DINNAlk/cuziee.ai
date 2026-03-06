from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from app.config import MODEL_NAME, TEMPERATURE, OPENAI_API_KEY


SYSTEM_PROMPT = """
You are Cuziee AI.

You help users understand emotions and relationships.
You encourage healthy communication, confidence, and respect.
Never promote manipulation or toxic behavior.
"""


prompt = PromptTemplate.from_template(
"""
{system_prompt}

Conversation history:
{history}

Human: {input}

AI:
"""
)

llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=OPENAI_API_KEY
)

parser = StrOutputParser()
chain = prompt | llm | parser


def chat(message: str, history=None):
    if history is None:
        history = []

    history_text = ""

    for item in history:
        if isinstance(item, dict):
            role = item.get("role", "")
            content = item.get("content", "")

            if role == "user":
                history_text += f"Human: {content}\n"
            elif role == "assistant":
                history_text += f"AI: {content}\n"

        elif isinstance(item, (list, tuple)) and len(item) == 2:
            user_msg, ai_msg = item
            history_text += f"Human: {user_msg}\nAI: {ai_msg}\n"

    response = chain.invoke({
        "system_prompt": SYSTEM_PROMPT,
        "history": history_text,
        "input": message
    })

    return response