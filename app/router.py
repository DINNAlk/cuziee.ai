from langchain_openai import ChatOpenAI
from langsmith import traceable

from app.config import MODEL_NAME, OPENAI_API_KEY
from models.education_model import EducationModel
from models.mental_model import MentalModel
from models.relationship_model import RelationshipModel
from models.wealth_model import WealthModel
from tools.web_search import search_web


router_llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0,
    api_key=OPENAI_API_KEY
)

judge_llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0,
    api_key=OPENAI_API_KEY
)

relationship_model = RelationshipModel()
education_model = EducationModel()
wealth_model = WealthModel()
mental_model = MentalModel()


def build_history_text(history) -> str:
    if history is None:
        return ""

    history_text = ""

    for item in history:
        if isinstance(item, dict):
            role = item.get("role", "")
            content = item.get("content", "")

            if role == "user":
                history_text += f"User: {content}\n"
            elif role == "assistant":
                history_text += f"AI: {content}\n"

        elif isinstance(item, (list, tuple)) and len(item) == 2:
            user_msg, ai_msg = item
            history_text += f"User: {user_msg}\nAI: {ai_msg}\n"

    return history_text.strip()


@traceable(name="choose_category", run_type="chain")
def choose_category(question: str, history_text: str = ""):
    prompt = f"""
You are an AI router.

Choose the single best category for the user's question.

Available categories:
- education -> studying, exams, school, university, learning
- wealth -> money, finance, income, business, budgeting
- relationships -> crush, dating, love, jealousy in relationships, breakup, communication with partner
- mental -> mindset, emotions, overthinking, confidence, behavior, attitude, emotional analysis

Rules:
- Return only one category name.
- Do not explain your answer.
- If the question is mainly about feelings, behavior, or understanding someone's attitude, choose mental.
- If the question is mainly about crushes, love, dating, or relationship communication, choose relationships.

Conversation history:
{history_text}

Question:
{question}
"""

    response = router_llm.invoke(prompt)
    category = response.content.strip().lower()

    valid_categories = {"education", "wealth", "relationships", "mental"}

    if category not in valid_categories:
        return "mental"

    return category


@traceable(name="should_use_web_ai", run_type="chain")
def should_use_web_ai(question: str, answer: str) -> bool:
    prompt = f"""
You are a decision AI.

Decide whether web search is needed.

Use web search if:
- the question asks for latest, current, recent, today, this year, or real-time information
- the answer may be outdated, uncertain, incomplete, or weak
- the topic involves news, sports, prices, winners, trends, recent events, or factual updates

Do not use web search if:
- the question can be answered with general reasoning or stable knowledge
- the answer is already sufficient without external updates

Question:
{question}

Current Answer:
{answer}

Return only one token:
use_web
or
no_web
"""

    response = judge_llm.invoke(prompt)
    decision = response.content.strip().lower()

    return decision.startswith("use_web")


@traceable(name="route_question", run_type="chain")
def route_question(question: str, history=None):
    history_text = build_history_text(history)
    category = choose_category(question, history_text)

    if category == "education":
        answer = education_model.run(question, history_text)
    elif category == "wealth":
        answer = wealth_model.run(question, history_text)
    elif category == "relationships":
        answer = relationship_model.run(question, history_text)
    else:
        answer = mental_model.run(question, history_text)

    used_web_search = False
    web_result = ""

    if should_use_web_ai(question, answer):
        used_web_search = True
        web_result = search_web(question)
        answer = f"{answer}\n\nAdditional web information:\n{web_result}"

    return {
        "category": category,
        "used_web_search": used_web_search,
        "answer": answer
    }