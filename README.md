# 🌿 ArogyaSLM — Ayurvedic Intelligence Engine for Bharat

> A hybrid neuro-symbolic AI system for Ayurvedic health guidance using RAG + Dosha reasoning.

---

## 🚀 Overview

ArogyaSLM is a lightweight AI system designed to provide **Ayurvedic health insights** based on user symptoms.

It combines:

* 🧠 Small Language Models (SLM)
* 📚 Retrieval-Augmented Generation (RAG)
* 🌿 Rule-based Dosha Inference

to generate **context-aware and grounded Ayurvedic responses**.

---

## 🧠 Current Features (Implemented)

* 🔍 RAG-based knowledge retrieval using FAISS
* 🧠 LLM-based response generation (HuggingFace pipeline)
* 🌿 Dosha inference engine (Vata, Pitta, Kapha)
* 🔀 Context fusion (RAG + Dosha → prompt)
* ⚡ FastAPI backend with `/query` endpoint
* 📄 Structured Ayurvedic response generation

---

## 🏗️ System Architecture (Implemented Flow)

```
User Input (Text)
        ↓
Query API (/query)
        ↓
Context Builder (Fusion Layer)
   ↙             ↘
RAG Retriever     Dosha Engine
        ↓
Prompt Builder
        ↓
LLM Generator
        ↓
Response Output (JSON)
```

---

## ⚙️ Tech Stack (Current)

### Backend

* Python
* FastAPI

### AI / NLP

* HuggingFace Transformers (LLM)
* Sentence Transformers (Embeddings)

### Retrieval

* FAISS (Vector Database)
* LangChain (RAG pipeline)

---

## 🧪 How It Works

1. User sends symptoms via API
2. System retrieves relevant Ayurvedic knowledge (RAG)
3. Dosha is inferred using rule-based logic
4. Retrieved knowledge + dosha are fused into prompt
5. LLM generates structured Ayurvedic response
6. Response returned via API

---

## 📦 Project Structure

```
arogya-slm/
│
├── backend/
│   ├── main.py
│   ├── routes/query.py
│   ├── core/
│   │   ├── llm.py
│   │   ├── prompt.py
│   ├── rag/
│   │   ├── retriever.py
│   ├── knowledge_graph/
│   │   ├── dosha.py
│   ├── fusion/
│   │   ├── fusion.py
│
├── data/
│   ├── raw/ayurveda_texts.txt
```

---

## ⚡ Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/your-repo/arogya-slm.git
cd arogya-slm
```

---

### 2. Setup Environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Run Server

```bash
uvicorn backend.main:app --reload
```

---

### 4. Test API

Open:
👉 http://127.0.0.1:8000/docs

Use `/query` endpoint:

```json
{
  "user_input": "I have dry skin and anxiety"
}
```

---

## 📌 Example Output

```json
{
  "dosha": "Vata",
  "response": "..."
}
```

---

## 🔐 Disclaimer

* This system provides **informational Ayurvedic guidance only**
* Not a substitute for professional medical advice

---

## 🚀 Next Steps (Planned Features)

* 🧠 Conversation Memory
* 🛡️ Safety & Validation Layer
* 🌐 Multilingual Support (Indic languages)
* 🎤 Voice Input (Speech-to-Text)
* 🕸️ Knowledge Graph Integration

---

## 💡 Vision

To build a **scalable, culturally-aligned AI system** that makes Ayurvedic knowledge accessible across Bharat.