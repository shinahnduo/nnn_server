from pydantic import BaseModel
from typing import Optional

class ChapterCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None

class ChapterResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
