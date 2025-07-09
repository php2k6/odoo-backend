from fastapi import FastAPI
from app.database import engine, get_db
from sqlalchemy.orm import Session
import app.models
from app.routers import chatbot
app = FastAPI()
#optional to create all tables
#models.Base.metadata.create_all(bind=engine)
app.include_router(chatbot.router)

@app.get("/")
def root():
    return {"message" : "Hello World"}