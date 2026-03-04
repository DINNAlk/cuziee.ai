from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from app.config import MODEL_NAME, TEMPERATURE, OPENAI_API_KEY


SYSTEM_PROMPT = """
You are LoveAgent AI.

You help users understand emotions and relationships.
You encourage healthy communication, confidence, and respect.
Never promote manipulation or toxic behavior.
"""


prompt = PromptTemplate.from_template(
"""
{system_prompt}

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


def chat(message: str):

    response = chain.invoke({
        "system_prompt": SYSTEM_PROMPT,
        "input": message
    })

    return response