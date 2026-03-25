# app/routes/auth.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db import models
from app.core.security import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(username: str, password: str, db: Session = Depends(get_db)):
    user = models.User(username=username, password=password)
    db.add(user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or user.password != password:
        return {"error": "Invalid credentials"}
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token}