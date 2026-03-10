# Cuziee AI v2

Cuziee is an AI-powered conversational assistant designed to help users think through life situations, emotions, relationships, and personal growth.

The system routes user questions to specialized expert models such as education, wealth, relationships, and mindset analysis. If the AI determines that a question requires up-to-date or external information, it can automatically search the web and include relevant results.

Cuziee provides both a FastAPI backend API and a Gradio chat interface for interacting with the AI assistant.

------------------------------------------------------------

Features

AI-powered conversation using OpenAI models
Router-based expert AI system
Specialized expert models for different life areas
Automatic web search when the AI requires updated information
Conversation history awareness
LangSmith tracing to monitor AI reasoning and responses
FastAPI backend API for programmatic access
Browser chat interface using Gradio
Modular architecture for easy expansion and experimentation

------------------------------------------------------------

Expert AI Models

Cuziee currently includes multiple expert models that handle different types of questions.

The router automatically selects the most appropriate model to answer the user's question.

------------------------------------------------------------

Smart Web Search

If the AI detects that a question requires recent or real-world information, the system can perform a web search and include relevant results.

This allows Cuziee to answer questions about:

recent events  
current trends  
sports results  
new technologies  
real-world factual information

------------------------------------------------------------

AI Observability

Cuziee integrates LangSmith to monitor how the AI agent operates internally.

Developers can inspect:

router decisions  
model prompts  
expert model responses  
tool usage such as web search  
full reasoning traces

------------------------------------------------------------

Technologies Used

Python  
FastAPI  
LangChain  
OpenAI API  
Tavily Search API  
LangSmith  
Gradio  
Pydantic  
Python-dotenv  

------------------------------------------------------------

Project Architecture

Cuziee
│
├── app
│   ├── main.py
│   ├── router.py
│   └── config.py
│
├── models
│   ├── base_model.py
│   ├── education_model.py
│   ├── wealth_model.py
│   ├── relationship_model.py
│   └── mental_model.py
│
├── tools
│   └── web_search.py
│
├── ui
│   └── gradio_app.py
│
├── .env
├── requirements.txt
└── README.md

------------------------------------------------------------

Setup and Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/cuziee.git
cd cuziee

Create a virtual environment

python -m venv .venv

Activate it

Windows

.venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

------------------------------------------------------------

Environment Variables

Create a .env file in the project root.

OPENAI_API_KEY=your_openai_api_key  
TAVILY_API_KEY=your_tavily_api_key  
LANGSMITH_API_KEY=your_langsmith_api_key  
LANGSMITH_TRACING=true  
LANGSMITH_PROJECT=Cuziee-v2  

Important:

Use your own OpenAI API key to obtain better and more accurate AI responses.

------------------------------------------------------------

Running the API

Start the FastAPI server

uvicorn app.main:app --reload

Open API documentation

http://127.0.0.1:8000/docs

------------------------------------------------------------

Running the Chat Interface

Run the Gradio chat interface

python -m ui.gradio_app

Open in browser

http://127.0.0.1:7860

------------------------------------------------------------

Future Plans

Cuziee is evolving into a multi-expert AI assistant system.

------------------------------------------------------------

Project Status

This project is currently in the development stage.

More features and improvements are coming soon.

Await...
Let's gooo...

---

## Support Me !
[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/dinushapiun)    