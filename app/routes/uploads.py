from fastapi import APIRouter, UploadFile, File
import os

from langchain_community.document_loaders import PyPDFLoader
from app.services.rag_service import create_vector_store

router = APIRouter()

# Folder to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save file
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Load PDF
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        # Create vector store (RAG)
        create_vector_store(documents)

        return {
            "message": "File uploaded and processed successfully",
            "filename": file.filename
        }

    except Exception as e:
        return {"error": str(e)}