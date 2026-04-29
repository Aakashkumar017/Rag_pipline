# RAG PDF Chatbot

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)]()
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green.svg)]()
[![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange.svg)]()
[![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA%203.1-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

---

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system that allows users to upload PDF documents and ask natural language questions. The system retrieves relevant information from the document and generates answers strictly grounded in the provided context.

If the answer is not present in the document, the system explicitly responds with *"I don't know"*, preventing hallucinated outputs.

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

## 🏗️ Architecture & Workflow

![RAG Architecture](assets/architecture.png)
---

## Key Design Decisions

* Context-restricted prompting to eliminate hallucination
* MMR retrieval to improve diversity and reduce redundancy
* In-memory FAISS indexing for simplicity and speed
* Modular separation between ingestion, retrieval, and generation

---

## Project Structure

```text
├── app.py              # Streamlit UI
├── rag_pipeline.py     # Document processing and retrieval setup
├── rag_brain.py        # Query → prompt → LLM response
├── llm_load.py         # LLM configuration (Groq)
├── requirements.txt
├── README.md
└── assets/
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

* Vector index is in-memory and rebuilt for each upload
* Supports a single PDF per session
* Chat history is not persisted

---

## Summary

This project demonstrates a practical implementation of a RAG pipeline using vector search and large language models to generate accurate, document-grounded responses. It highlights strong understanding of retrieval systems, prompt design, and real-time AI application development.

---

## Author

Aakash Kumar
B.Tech Computer Science (Data Science)
