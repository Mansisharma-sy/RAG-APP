# AI Document Assistant (RAG with Ollama)

## Features
- Upload PDF
- Ask questions
- Local LLM (Ollama)
- No API cost

## Run

```bash
ollama pull llama3
ollama serve
uvicorn app.main:app --reload
