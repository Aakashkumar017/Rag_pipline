import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from rag_pipeline import build_retriever
from rag_brain import rag_pipeline
from llm_load import model



# ==========================
# Setup
# ==========================
load_dotenv()

llm=model()


st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📄 RAG PDF Chatbot")

# ==========================
# Upload Section
# ==========================
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:

    # Save file temporarily
    file_path = os.path.join("temp.pdf")

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully ✅")

    # ==========================
    # Cache retriever (IMPORTANT)
    # ==========================
    @st.cache_resource
    def get_retriever(file_path):
        return build_retriever(file_path)

    retriever = get_retriever(file_path)

    # ==========================
    # Chat History
    # ==========================
    if "history" not in st.session_state:
        st.session_state.history = []

    # Input
    user_input = st.text_input("Ask a question:")

    if st.button("Ask"):

        if user_input.strip() == "":
            st.warning("Please enter a question")
        else:
            with st.spinner("Thinking... 🤔"):
                answer = rag_pipeline(user_input, retriever, llm)

            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("AI", answer))

    # ==========================
    # Display Chat
    # ==========================
    st.subheader("💬 Chat History")

    for role, text in st.session_state.history:
        if role == "You":
            st.chat_message("user").write(text)
        else:
            st.chat_message("assistant").write(text)

else:
    st.info("Please upload a PDF to start.")