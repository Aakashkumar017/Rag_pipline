from dotenv import load_dotenv
from llm_load import model
from rag_pipeline import build_retriever
from rag_brain import rag_pipeline

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


# ==========================
# Setup
# ==========================
load_dotenv()

llm = model()

file_path = r" "
retriever = build_retriever(file_path)


# ==========================
# Chat System
# ==========================
chat_history = [
    SystemMessage(content="You are an AI that answers questions from PDF.")
]

while True:
    user_input = input("You: ")

    if not user_input.strip():
        print("Waiting for input...")
        continue

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Goodbye!")
        break

    if user_input.lower() == "history":
        print("\n📜 Chat History:")
        for msg in chat_history:
            if isinstance(msg, HumanMessage):
                print(f"You: {msg.content}")
            elif isinstance(msg, AIMessage):
                print(f"AI: {msg.content}")
        continue

    # Add user message
    chat_history.append(HumanMessage(content=user_input))

    # ==========================
    # ✅ PASS HISTORY TO PIPELINE
    # ==========================
    result = rag_pipeline(
        query=user_input,
        retriever=retriever,
        llm=llm,
        chat_history=chat_history   # ✅ FIX
    )

    # Add AI response
    chat_history.append(AIMessage(content=result))

    print("AI:", result)