# rag_pipeline.py
def rag_pipeline(query, retriever, llm):
    try:
        # 🔹 Retrieve relevant documents
        docs = retriever.invoke(query)

        if not docs:
            return "No relevant information found in document."

        # 🔹 Build context
        context = "\n\n".join([
            f"[Page {doc.metadata.get('page')} | Source: {doc.metadata.get('source')}] \n{doc.page_content}"
            for doc in docs
        ])

        # 🔹 Prompt
        prompt = f"""
You are a helpful assistant.

RULES:
- Answer ONLY from the provided context
- If answer is not explicitly present → say "I don't know"

Context:
{context}

Question:
{query}

Give a clear, structured answer.
"""

        # 🔹 LLM call
        result = llm.invoke(prompt)

        return result.content

    except Exception as e:
        return f"Error: {e}"