from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_service import ask_question

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/chat")
def chat(query: Query):
    answer = ask_question(query.question)
    return {"answer": answer}