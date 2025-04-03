from app.schema.chapter_schema import ChapterCreateRequest, ChapterResponse
from app.repository.chapter_repository import save_chapter_for_schedule


def create_chapter_for_schedule(uid: str, schedule_id: str, chapter_data: ChapterCreateRequest) -> ChapterResponse:
    saved = save_chapter_for_schedule(
        uid=uid,
        schedule_id=schedule_id,
        title=chapter_data.title,
        description=chapter_data.description
    )
    return ChapterResponse(**saved)

