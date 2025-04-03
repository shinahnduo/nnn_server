from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import main_page_router, create_page_router, read_page_router
from app.api.routes.router import router
from app.core.database import engine
from app.domain.models import Base

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(main_page_router.router)
app.include_router(create_page_router.router)
app.include_router(read_page_router.router)
