from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class ScheduleCreateRequest(BaseModel):
    title: str
    date: date
    time: time
    description: Optional[str] = None

class ScheduleResponse(BaseModel):
    id: str
    title: str
    date: date
    time: time
    description: Optional[str] = None

class ScheduleUpdateRequest(BaseModel):
    title: Optional[str] = None
    date: Optional[date] = None
    time: Optional[time] = None
    description: Optional[str] = None
