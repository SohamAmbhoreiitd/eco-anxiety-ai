# Eco-Anxiety AI Counselor 🌿

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://react.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-yellow.svg)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A **full-stack AI chatbot** application designed to provide **empathetic, action-oriented, and psychologically-informed** support for users experiencing eco-anxiety.  
Built with a **Retrieval-Augmented Generation (RAG)** architecture to ensure responses are safe, relevant, and based on a curated knowledge base.

---

## 🌟 Features
- 💬 **Empathetic AI Chat** – LLM configured to be supportive and kind.
- 📚 **RAG Architecture** – Strictly answers from a custom knowledge base.
- 🚨 **Critical Safety Layer** – Detects severe distress & offers emergency contacts.
- 🎨 **Clean Web UI** – Responsive React frontend for a smooth chat experience.

---

## ⚙️ Tech Stack

### **Backend**
- **Framework:** FastAPI
- **AI Orchestration:** LangChain
- **LLM Providers:** Groq (LLaMA 3), OpenAI (GPT-3.5+), Google (Gemini)
- **Embeddings:** `sentence-transformers` (via Hugging Face)
- **Vector Database:** ChromaDB

### **Frontend**
- **Framework:** React.js
- **Styling:** Plain CSS

---

## 🏗️ System Architecture

```text
[ React Frontend ]  <--->  [ FastAPI Backend ]  <--->  [ LangChain Orchestrator ]
         ↑                        ↑                           ↑
         |                        |                           |
   User Interface           API Endpoints            LLM + RAG Pipeline
                                                            ↑
                                                            |
                                                  [ ChromaDB Vector Store ]
                                                            ↑
                                                            |
                                                 [ Curated Knowledge Base ]

# 🚀 Setup & Installation

## **Prerequisites**
- Python **3.9+**
- Node.js **v18+** and npm

---

## **Backend Setup**

```bash
# Clone the repository
git clone <your-repository-url>
cd eco-anxiety-ai

# Create and activate virtual environment (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Set up your API key(s):

Create a .env file in the root of the backend folder.

Add your API keys:

env
Copy
Edit
GROQ_API_KEY="gsk_YourSecretGroqKeyGoesHere"
OPENAI_API_KEY="sk-YourOpenAIKey"
Build the Vector Database:

Temporarily modify app/core.py to call create_vector_db() (as done during development).

Run:

bash
Copy
Edit
python app/core.py
A chroma_db folder will be created.

Revert the changes in app/core.py.

Frontend Setup
bash
Copy
Edit
cd ../frontend  # Navigate to frontend folder
npm install
▶️ Running the Application
Open two terminal windows:

1. Run Backend
bash
Copy
Edit
cd eco-anxiety-ai
uvicorn app.main:app --reload
Backend runs at: http://localhost:8000

2. Run Frontend
bash
Copy
Edit
cd frontend
npm start
Frontend opens at: http://localhost:3000

You can now interact with the chatbot in your browser.

🗺️ Roadmap
Phase 4: Analytics & Deployment

PostgreSQL for anonymized analytics

Cloud deployment (Render, Vercel)

User feedback system

Phase 5: Advanced Features & Personalization

Personalized recommendation engine

"Mood to Action" structured journey planner

User accounts with saved progress

Fine-tuned open-source model specialized for eco-anxiety

📜 License
This project is licensed under the MIT License.

css
Copy
Edit
