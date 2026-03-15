import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

DATABASE_URL = os.getenv("DATABASE_URL")

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.7