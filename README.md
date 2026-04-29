# RAG PDF Chatbot

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)]()
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green.svg)]()
[![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange.svg)]()
[![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA%203.1-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

---

## Overview

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system that allows users to upload PDF documents and ask natural language questions.

The system retrieves the most relevant document chunks using FAISS-based similarity search and generates answers strictly grounded in the provided context.

If the answer is not present in the document, the system explicitly responds with *"Not found in document"*, preventing hallucinated outputs.

---

## 🏗️ Architecture & Workflow

![RAG Architecture](assets/architecture.png)
---

## Demo

### Application Interface

<img width="1366" height="597" alt="image" src="https://github.com/user-attachments/assets/4affaa55-0f14-4240-af05-4fb094f36fd8" />


### Response Example

<img width="1365" height="594" alt="image" src="https://github.com/user-attachments/assets/75e2dbb2-ed27-4c6c-bd8a-ec583d5dd2de" />


The system allows users to:

* Upload a PDF document
* Ask questions in natural language
* Receive accurate, context-based answers

---

## Key Design Decisions

* Context-restricted prompting to eliminate hallucination
* Similarity-based retrieval to ensure accurate and relevant context selection
* FAISS vector database for efficient semantic search (supports persistence for faster reuse)
* Modular separation between ingestion, retrieval, and generation

---

## Project Structure

```text
├── app.py
├── rag_pipeline.py
├── rag_brain.py
├── llm_load.py
├── requirements.txt
├── README.md
└── assets/
    ├── rag_architecture.png     
    ├── app_screenshot_1.png
    └── app_screenshot_2.png
    
```

---

## Setup

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag-pdf-chatbot
pip install -r requirements.txt
```

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## Limitations

* FAISS index is currently in-memory and rebuilt on each upload, increasing processing time for large documents  
* Supports only a single PDF per session (no multi-document retrieval)  
* Chat history is session-based and not persisted across runs  
---

## Summary
This project presents a practical implementation of a Retrieval-Augmented Generation (RAG) pipeline that combines FAISS-based vector search with large language models to produce accurate, context-grounded responses from PDF documents. It demonstrates a strong understanding of document ingestion, semantic retrieval, prompt engineering, and real-time AI system design.

---

## Author

Aakash Kumar
B.Tech Computer Science (Data Science)
