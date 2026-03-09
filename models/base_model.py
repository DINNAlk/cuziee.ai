from langchain_openai import ChatOpenAI
from langsmith import traceable

from app.config import MODEL_NAME, TEMPERATURE, OPENAI_API_KEY


class BaseExpertModel:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            api_key=OPENAI_API_KEY
        )

    @traceable(name="expert_model_run",run_type="chain")
    def run(self, question: str, history_text: str = "") -> str:
        prompt = f"""
{self.system_prompt}

Conversation history:
{history_text}

General behavior rules:
- Be supportive and practical.
- Reply in a warm, natural, and lovely vibe.
- Do not always ask questions to the user.
- Prefer giving useful suggestions, interpretations, or solutions first.
- Ask follow-up questions only when really necessary.
- Do not mention category names unless the user asks.
- Keep the response clear, human, and emotionally aware.


User Question:
{question}

Answer:
"""

        response = self.llm.invoke(prompt)
        return response.content.strip()