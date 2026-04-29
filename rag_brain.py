def rag_pipeline(query, retriever, llm, history=None):

    # 🔹 Convert history into text
    history_text = ""
    if history:
        for role, msg in history[-6:]:   # last 3 turns
            history_text += f"{role}: {msg}\n"

    # 🔹 Better retrieval query
    enhanced_query = f"{history_text}\nCurrent question: {query}"

    docs = retriever.invoke(enhanced_query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a document-based QA assistant.

CONTEXT:
{context}

CHAT HISTORY (reference only, do not override context):
{history_text}

QUESTION:
{query}

RULES:
1. Answer ONLY using the CONTEXT above.
2. If the answer is not explicitly present, reply exactly: "Not found in document."
3. Do NOT guess, infer, or use outside knowledge.
4. Prefer exact phrases from the context when possible.
5. Keep the answer concise (1–3 sentences).

ANSWER:
"""
    result = llm.invoke(prompt)
    return result.content