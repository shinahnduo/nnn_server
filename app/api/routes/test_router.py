from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.firebase import add_data

test_router = APIRouter(prefix='/test')

class DataModel(BaseModel):
    name: str
    description: str

@test_router.get("/", tags=['test_router'])
async def read_root():
    return {"message": "Welcome to Advanced FastAPI Project!"}

@test_router.post("/add_to_firebase", tags=['test_router'])
async def add_to_firebase(data: DataModel):
    try:
        add_data("example_collection", data.dict())
        return {"message": "Data added to Firebase successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))