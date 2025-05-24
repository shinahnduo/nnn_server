from pydantic import BaseModel
from typing import Optional

class ChapterCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None

class ChapterResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

class ChapterUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None