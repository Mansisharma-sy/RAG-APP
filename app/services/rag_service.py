from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ✅ Ollama imports
from langchain_ollama import OllamaLLM, OllamaEmbeddings

from langchain.chains import RetrievalQA

db = None


def create_vector_store(documents):
    global db

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    # ✅ Local embeddings (NO API KEY)
    embeddings = OllamaEmbeddings(model="llama3")

    db = FAISS.from_documents(chunks, embeddings)

    return db


def ask_question(query: str):
    global db

    if db is None:
        return "No document uploaded yet."

    retriever = db.as_retriever()

    # ✅ Local LLM
    llm = OllamaLLM(model="llama3")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    result = qa.run(query)
    return result
