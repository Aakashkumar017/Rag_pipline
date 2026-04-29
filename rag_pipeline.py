from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from warnings import warn_explicit     

def load_pdf(file_path):
    try:
        loader = PyPDFLoader(file_path)
        docs = loader.load()

        if not docs:
            raise ValueError("PDF loaded but no content found")

        print("✅ PDF loaded successfully")
        return docs

    except FileNotFoundError:
        raise FileNotFoundError("❌ File not found. Check path.")

    except Exception as e:
        raise RuntimeError(f"❌ PDF loading failed: {e}")

def splite_doc(docs):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=850,
        chunk_overlap=150
    )
    return splitter.split_documents(docs)


def load_huggingfaceembedding():
    try:
        embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("HuggingFaceEmbeddings model is scesfully load for embedding ")
        return embeddings
    except Exception :
        print("Model loading is fail")

def create_vectore_store(chunk,embeddings):
    vector_store=FAISS.from_documents(chunk,embeddings)
    return vector_store

def create_retriever(vector_store):
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5} 
    )



def build_retriever(file_path):

    docs = load_pdf(file_path)
    chunks = splite_doc(docs)
    embeddings = load_huggingfaceembedding()
    vector_store = create_vectore_store(chunks, embeddings)
    retriever = create_retriever(vector_store)

    return retriever