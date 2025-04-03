from datetime import datetime

from app.schema.schedule_schema import ScheduleCreateRequest, ScheduleResponse
from app.repository.schedule_repository import save_schedule_for_user

def create_schedule_for_user(uid: str, schedule_data: ScheduleCreateRequest) -> ScheduleResponse:
    saved = save_schedule_for_user(uid, schedule_data.dict())
    # datetime 필드를 분해해서 Pydantic이 기대하는 필드로 조립
    dt: datetime = saved["datetime"]
    return ScheduleResponse(
        id=saved["id"],
        title=saved["title"],
        description=saved.get("description"),
        date=dt.date(),
        time=dt.time()
    )
