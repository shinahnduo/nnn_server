from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.test_router import test_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router)

# @app.get('/')
# def home():
#     return "home"