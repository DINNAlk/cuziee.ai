# Cuziee AI

Cuziee is an AI-powered conversational assistant designed to help users discuss life situations, relationships, mindset, education, and personal growth.

The system routes each question to specialized AI expert models that provide contextual responses based on the user's problem. It can also perform web searches when the AI determines that current or external information is required.

Cuziee includes a FastAPI backend, a Gradio chat interface, expert AI models, database-based conversation memory, and web search capabilities.

The project is designed with a modular architecture so that additional expert models, tools, and intelligence systems can be added in future versions.

---

## Features

Router-based AI architecture that selects the most relevant expert model for each question.

Specialized AI expert models for:

- Education  
- Wealth and financial mindset  
- Relationships and emotional situations  
- Mental attitude and behavioral analysis  

Conversation memory stored in a PostgreSQL database so chats can persist across sessions.

Automatic web search using Tavily when the AI determines that the answer may require current or external information.

LangSmith tracing support for monitoring how the AI agent routes questions and generates responses.

FastAPI backend API for programmatic access.

Gradio chat interface for a simple browser-based user experience.

Modular architecture designed for future AI expansion.

---

## Technologies Used

Python  
FastAPI  
Gradio  
LangChain  
LangSmith  
OpenAI API  
Tavily Web Search API  
PostgreSQL  
SQLAlchemy  
Pydantic  
Python-dotenv  

---

## Project Architecture
Cuziee
│
├── app
│ ├── main.py
│ ├── router.py
│ ├── config.py
│ └── db
│ ├── database.py
│ ├── models.py
│ └── repository.py
│
├── models
│ ├── base_model.py
│ ├── education_model.py
│ ├── wealth_model.py
│ ├── relationship_model.py
│ └── mental_model.py
│
├── tools
│ └── web_search.py
│
├── ui
│ └── gradio_app.py
│
├── .env
├── requirements.txt
└── README.md


---

## Setup and Installation

Clone the repository.

---

## Setup and Installation

Clone the repository.
git clone https://github.com/YOUR_USERNAME/cuziee.git

cd cuziee


Create a virtual environment.


python -m venv .venv


Activate it.

Windows:


.venv\Scripts\activate


Install dependencies.


pip install -r requirements.txt


---

## Environment Variables

Create a `.env` file in the project root.


OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=Cuziee-v2

DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/cuziee_db

Important:

Use your own OpenAI API key to obtain better and more accurate AI responses.

---

## Database Setup

Create the PostgreSQL database.
CREATE DATABASE cuziee_db;


You can manage the database using DBeaver or any PostgreSQL client.

The application will automatically create the required tables when the backend server starts.

---

## Running the Backend API

Start the FastAPI server.


python -m uvicorn app.main:app --reload


Open the API documentation.


http://127.0.0.1:8000/docs


---

## Running the Chat Interface

Start the Gradio chat interface.


python -m ui.gradio_app


Open the chat interface in your browser.


http://127.0.0.1:7860


---

## How the AI Works

1. The user sends a question from the Gradio interface.
2. The request is sent to the FastAPI backend.
3. The router AI decides which expert model should answer the question.
4. The selected expert model generates a response using the OpenAI model.
5. If the AI determines that external information is needed, a web search is performed.
6. The final response is returned to the user and saved in the database.


---

## Support Me !
[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/dinushapiun)    