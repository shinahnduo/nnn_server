from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.router import router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 환경에서는 모든 origin 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(router)

# @app.get('/')
# def home():
#     return "home"