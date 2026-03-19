# backend/main.py

from fastapi import FastAPI
from backend.routes.query import router as query_router

app = FastAPI()

app.include_router(query_router, prefix="/query")

@app.get("/")
def root():
    return {"message": "ArogyaSLM running"}