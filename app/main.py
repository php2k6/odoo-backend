from fastapi import FastAPI
from app.database import engine, get_db
from sqlalchemy.orm import Session
import app.models
from app.routers import chatbot
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
#optional to create all tables
#models.Base.metadata.create_all(bind=engine)
app.include_router(chatbot.router)


origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          
    allow_credentials=True,         
    allow_methods=["*"],
    allow_headers=["*"],   
)
@app.get("/")
def root():
    return {"message" : "Hello World"}