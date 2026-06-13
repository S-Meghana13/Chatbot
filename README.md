# 📚 AI Knowledge Assistant (RAG Chatbot)

An AI-powered chatbot that answers questions from PDF documents using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features
- Upload and process PDF documents
- Intelligent question answering using RAG
- FAISS vector database for fast retrieval
- Google Gemini LLM integration
- Streamlit web interface

---

## 🧠 Tech Stack
- Python
- LangChain (LCEL)
- FAISS (Vector Database)
- Google Gemini API
- Streamlit
- Sentence Transformers

---

## 📁 Project Structure

rag_chatbot/
│
├── app.py
├── chatbot.py
├── create_vector_db.py
├── requirements.txt
├── .env.example
│
├── documents/
├── vector_db/
├── utils/
└── README.md


---

## ⚙️ How It Works

1. Load PDF documents  
2. Split into chunks  
3. Create embeddings  
4. Store in FAISS vector DB  
5. Retrieve relevant context  
6. Send to Gemini LLM  
7. Generate final answer  

---

