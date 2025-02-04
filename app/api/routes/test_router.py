from fastapi import APIRouter

test_router = APIRouter(prefix='/test')

@test_router.get("/", tags=['test_router'])
async def read_root():
    return {"message": "Welcome to Advanced FastAPI Project!"}