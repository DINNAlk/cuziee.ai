# 💬 Cuziee AI

Cuziee is an AI-powered emotional companion that allows users to chat about feelings, relationships, and personal situations.  
The system uses a language model to generate supportive responses and can detect basic emotions from user messages.

Cuziee provides both:

- a **FastAPI backend API**
- a **Gradio chat interface**

for interacting with the AI assistant.

---

## Features

- AI conversation using OpenAI models  
- Emotion detection from user messages  
- Context-aware responses with conversation history  
- FastAPI backend API for programmatic access  
- Simple browser chat interface using Gradio  
- Lightweight and easy to run locally  

---

## Technologies Used

- Python  
- FastAPI  
- LangChain  
- OpenAI API  
- Gradio  
- Pydantic  
- Python-dotenv  

---

## Setup & Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/cuziee.git
cd cuziee
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```
OPENAI_API_KEY=your_openai_api_key
```

**Important:**  
Use your own **OpenAI API key** to get better and more accurate AI responses.

---

## ▶️ Running the API

Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

Open API documentation

```
http://127.0.0.1:8000/docs
```

---

## Running the Chat Interface

Run the Gradio chat interface

```bash
python ui.py
```
Open in browser

```
http://127.0.0.1:7860
```

---
## Project Status

This project is currently in the **development stage**.

More features and improvements are coming soon.

Stay tuned...

Await... Let's gooo... 

---


