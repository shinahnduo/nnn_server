from app.schema.chapter_schema import ChapterCreateRequest, ChapterResponse, ChapterUpdateRequest
from app.repository.chapter_repository import save_chapter_for_schedule, update_chapter_for_schedule, \
    delete_chapter_for_schedule


def create_chapter_for_schedule(uid: str, schedule_id: str, chapter_data: ChapterCreateRequest) -> ChapterResponse:
    saved = save_chapter_for_schedule(
        uid=uid,
        schedule_id=schedule_id,
        title=chapter_data.title,
        description=chapter_data.description
    )
    return ChapterResponse(**saved)

def update_chapter(uid: str, schedule_id: str, chapter_id: str, chapter_data: ChapterUpdateRequest) -> ChapterResponse:
    updated = update_chapter_for_schedule(
        uid=uid,
        schedule_id=schedule_id,
        chapter_id=chapter_id,
        update_data=chapter_data.dict(exclude_unset=True)
    )
    return ChapterResponse(**updated)

def delete_chapter(uid: str, schedule_id: str, chapter_id: str) -> dict:
    delete_chapter_for_schedule(uid, schedule_id, chapter_id)
    return {"message": f"Chapter {chapter_id} deleted from schedule {schedule_id}"}