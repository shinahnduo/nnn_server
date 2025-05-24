from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import date, time

class ChapterDetail(BaseModel):
    id: str
    title: str
    content: str
    imageUrl: Optional[HttpUrl] = None

class Chapter(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    details: List[ChapterDetail] = []

class ScheduleOverview(BaseModel):
    id: str
    title: str
    date: date
    time: time
    description: Optional[str] = None
    chapters: List[Chapter] = []
