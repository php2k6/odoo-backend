from fastapi import FastAPI
from database import engine, get_db
from sqlalchemy.orm import Session
import models
app = FastAPI()
#optional to create all tables
#models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message" : "Hello World"}