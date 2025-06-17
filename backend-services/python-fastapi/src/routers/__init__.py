from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/items")
async def read_items():
    return {"items": [{"name": "Item 1"}, {"name": "Item 2"}]}