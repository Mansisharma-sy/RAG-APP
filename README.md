# AI Document Assistant (RAG with Ollama)

## Features
- Upload PDF
- Ask questions
- Local LLM (Ollama)
- No API cost

- PDF → Text → Chunks → Embeddings → Vector DB → Question → Retrieve → LLM → Answer
  -Upload a PDF
  -Convert it into searchable data
  -Ask questions
  -Get answers based ONLY on that PDF


 - Backend Framework
FastAPI
Handles APIs (/upload, /chat)
Super fast + async

 -AI Framework
LangChain
Connects LLM + embeddings + vector DB
Gives you ready pipelines (RetrievalQA)

 -LLM (Brain)
Ollama
Runs models locally (like llama3)
No API cost

 -Vector Database
FAISS
Stores document embeddings
Finds relevant chunks

 -Document Loader
PyPDFLoader
Extracts text from PDF

## Run

```bash
ollama pull llama3
ollama serve
uvicorn app.main:app --reload
