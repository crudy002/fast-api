from fastapi import FastAPI
from src.database import init_db
from src.routers import api_router

app = FastAPI()
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}