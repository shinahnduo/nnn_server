from fastapi import FastAPI

from app.api.routes.test_router import test_router

app = FastAPI()

app.include_router(test_router)

@app.get('/')
def home():
    return "home"

