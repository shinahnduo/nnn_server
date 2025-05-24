from datetime import datetime

from app.schema.schedule_schema import ScheduleCreateRequest, ScheduleResponse, ScheduleUpdateRequest
from app.repository.schedule_repository import save_schedule_for_user, update_schedule_for_user, \
    delete_schedule_for_user


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

def update_schedule(uid: str, schedule_id: str, update_data: ScheduleUpdateRequest) -> ScheduleResponse:
    updated = update_schedule_for_user(uid, schedule_id, update_data.dict(exclude_unset=True))
    from datetime import datetime
    dt: datetime = updated["datetime"]
    return ScheduleResponse(
        id=updated["id"],
        title=updated["title"],
        description=updated.get("description"),
        date=dt.date(),
        time=dt.time()
    )

def delete_schedule(uid: str, schedule_id: str) -> dict:
    delete_schedule_for_user(uid, schedule_id)
    return {"message": f"Schedule {schedule_id} deleted successfully"}