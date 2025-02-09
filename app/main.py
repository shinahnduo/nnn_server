from fastapi import FastAPI

from app.api.routes.test_router import test_router
from app.core.database import engine, Base, test_insert_user, test_select_users, test_update_user, test_delete_user

app = FastAPI()

app.include_router(test_router)

@app.get('/')
def home():
    return "home"

