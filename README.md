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

