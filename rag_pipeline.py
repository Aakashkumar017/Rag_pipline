from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(file_path):
    try:
        loader=PyPDFLoader(r"C:\Users\Amit kumar\Desktop\new_learnig\BOOK\ML_Book_Notes_Part1.pdf")
        docs=loader.load()
        print("PDF is Scessfully ")
        return docs
    except FileNotFoundError:
        print("File not found check you path")
        exit()
    except Exception as e:
        print(f"Loading faild {e}")

def splite_doc(docs):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
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
        search_type="mmr",
        search_kwargs={"k": 3, "fetch_k": 10, "lambda_mult": 0.7}
    )



def build_retriever(file_path):

    docs = load_pdf(file_path)
    chunks = splite_doc(docs)
    embeddings = load_huggingfaceembedding()
    vector_store = create_vectore_store(chunks, embeddings)
    retriever = create_retriever(vector_store)

    return retriever
# ==========================
# 6. Retrieve Query
# ==========================
# def retrieve_query(query, retriever):
#     return retriever.invoke(query)

# if __name__ == "__main__":

#     file_path = r"C:\Users\Amit kumar\Desktop\new_learnig\BOOK\ML_Book_Notes_Part1.pdf"

#     docs = load_pdf(file_path)
#     chunks = splite_doc(docs)
#     embeddings = load_huggingfaceembedding()
#     vector_store = create_vectore_store(chunks, embeddings)
#     retriever = create_retriever(vector_store)

#     # Test
#     query = "machine learning"
#     results = retrieve_query(query, retriever)

#     print("\n🔍 Retrieved Results:\n")
#     for doc in results:
#         print(doc.page_content[:150])
#         print("------")