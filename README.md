# 📄 RAG PDF Chatbot


Upload a PDF → Ask questions → Get accurate, context-based answers

*(Add your demo video or screenshots here)*

---

## 🖼️ RAG Workflow Diagram

<img width="338" height="462" alt="image" src="https://github.com/user-attachments/assets/1752819b-9916-4dcd-9aa0-1ba5659ce79f" />


> This diagram represents the complete flow of the system from user query to final answer using retrieval and generation.

---

## 🧠 Key Features

* 📂 Upload any PDF dynamically
* 💬 Ask natural language questions
* 🔍 Context-aware answers using FAISS
* 🚫 No hallucination (answers only from document)
* ⚡ Fast retrieval with cached vector database
* 🌐 Clean Streamlit UI
* 🧾 Source-aware responses

---

## 🔄 System Workflow

```text
User Input
   ↓
Streamlit UI
   ↓
PDF Upload
   ↓
Text Chunking
   ↓
Embeddings (MiniLM)
   ↓
FAISS Vector Store
   ↓
Retriever (MMR)
   ↓
Context Building
   ↓
LLM (Groq - LLaMA)
   ↓
Final Answer
```

---

## 🧠 RAG Pipeline Explained

### 1. 📄 Document Loading

* PDF is uploaded via Streamlit
* Processed using `PyPDFLoader`

---

### 2. ✂️ Text Chunking

* Documents split into smaller chunks
* Improves retrieval accuracy

---

### 3. 🔢 Embedding Generation

* Each chunk → vector representation
* Model used:

```
sentence-transformers/all-MiniLM-L6-v2
```

---

### 4. 📦 Vector Storage (FAISS)

* Stores embeddings efficiently
* Enables fast similarity search

---

### 5. 🔍 Retrieval (MMR)

* Query converted to embedding
* Retrieves diverse + relevant chunks

---

### 6. 🧾 Context Creation

* Relevant chunks combined into context

---

### 7. 🤖 LLM Processing

* Context + Query sent to Groq LLM

---

### 8. ✅ Final Answer

* Structured, accurate, context-based response

---

## 🏗️ Project Structure

```text
project/
│
├── app.py              # Streamlit UI
├── rag_pipeline.py     # Core RAG logic
├── rag_brain.py        # FAISS + retriever setup
├── llm_load.py         # LLM configuration
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
    └── rag_architecture.png
```

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit
* **LLM:** Groq (LLaMA 3.1 / 3.3)
* **Framework:** LangChain
* **Vector DB:** FAISS
* **Embeddings:** Sentence Transformers
* **Language:** Python

---

## 🧪 Example

### ❓ Question

```
What is machine learning?
```

### ✅ Output

```
Machine Learning is a field of AI that enables systems to learn from data, identify patterns, and make decisions with minimal human intervention.
```

---

## ▶️ How to Run Locally

### 1. Clone repository

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup environment variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run the application

```bash
streamlit run app.py
```

---

## 🔐 Security Notes

* `.env` is excluded (API keys are safe)
* FAISS index stored locally
* No external data sharing

---

## 📊 Performance Highlights

* ⚡ Fast similarity search with FAISS
* 🧠 Accurate retrieval-based answers
* 🔁 Cached retriever for efficiency

---

## 🎯 Future Improvements

* Multi-PDF support
* Source highlighting
* Confidence score
* Cloud deployment
* Authentication system

---

## 👨‍💻 Author

**Aakash Kumar**
B.Tech CSE (Data Science)
Aspiring Data Scientist | ML Engineer

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repository
👉 Share it with others

---
