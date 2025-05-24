from pydantic import BaseModel, HttpUrl
from typing import Optional

class ChapterDetailCreateRequest(BaseModel):
    imageUrl: Optional[HttpUrl] = None
    title: str
    content: str

class ChapterDetailResponse(BaseModel):
    id: str
    imageUrl: Optional[HttpUrl] = None
    title: str
    content: str
