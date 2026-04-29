import streamlit as st
import os
import hashlib
from dotenv import load_dotenv

from rag_pipeline import build_retriever
from rag_brain import rag_pipeline
from llm_load import model

# ==========================
# Setup
# ==========================
load_dotenv()
llm = model()

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📄 RAG PDF Chatbot")

# ==========================
# Helper: File Hash
# ==========================
def get_file_hash(file):
    return hashlib.md5(file.getvalue()).hexdigest()

# ==========================
# Upload PDF
# ==========================
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:

    file_hash = get_file_hash(uploaded_file)

    # ==========================
    # Reset when new file uploaded
    # ==========================
    if "current_file_hash" not in st.session_state:
        st.session_state.current_file_hash = None

    if st.session_state.current_file_hash != file_hash:
        st.session_state.current_file_hash = file_hash
        st.session_state.history = []
        st.session_state.retriever = None
        st.cache_resource.clear()   # 🔥 clear old cache

    # ==========================
    # Build Retriever (cached by hash)
    # ==========================
    @st.cache_resource
    def get_retriever(file_bytes):
        temp_path = "temp.pdf"
        with open(temp_path, "wb") as f:
            f.write(file_bytes)

        return build_retriever(temp_path)

    if st.session_state.retriever is None:
        with st.spinner("Processing PDF..."):
            st.session_state.retriever = get_retriever(uploaded_file.getvalue())

    retriever = st.session_state.retriever

    st.success(f"PDF loaded: {uploaded_file.name} ✅")

    # ==========================
    # Chat History
    # ==========================
    if "history" not in st.session_state:
        st.session_state.history = []

    # ==========================
    # Input
    # ==========================
    user_input = st.text_input("Ask a question:")

    if st.button("Ask"):

        if user_input.strip() == "":
            st.warning("Please enter a question")

        else:
            with st.spinner("Thinking... 🤔"):
                answer = rag_pipeline(
                    query=user_input,
                    retriever=retriever,
                    llm=llm,
                    history=st.session_state.history
                )

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