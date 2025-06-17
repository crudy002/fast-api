from fastapi import FastAPI
from src.routers import api_router

app = FastAPI()
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

app.include_router(api_router)