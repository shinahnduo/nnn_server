from app.repository.main_page_repository import get_full_schedule_data
from app.schema.main_page_schema import ScheduleOverview
from typing import List

def get_main_page_data(uid: str) -> List[ScheduleOverview]:
    raw_data = get_full_schedule_data(uid)
    return [ScheduleOverview(**item) for item in raw_data]
