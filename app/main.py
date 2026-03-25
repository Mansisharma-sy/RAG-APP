# app/main.py
import os

from fastapi import FastAPI
from app.routes import auth
from app.routes import uploads
from app.routes import chat
from app.db.database import Base, engine
from dotenv import load_dotenv

load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(uploads.router)
app.include_router(chat.router)