from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.item import Item

api_router = APIRouter()

@api_router.get("/items")
async def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return {"items": [{"id": item.id, "name": item.name} for item in items]}

@api_router.post("/items")
async def create_item(name: str, db: Session = Depends(get_db)):
    item = Item(name=name)
    db.add(item)
    db.commit()
    db.refresh(item)
    return {"id": item.id, "name": item.name}