from fastapi import FastAPI

from app.api.routes.test_router import test_router
from app.core.database import Base

app = FastAPI()

app.include_router(test_router)

@app.get('/')
def home():
    return "home"


