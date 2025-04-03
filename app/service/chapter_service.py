from app.schema.chapter_schema import ChapterCreateRequest, ChapterResponse
from app.repository.chapter_repository import save_chapter_to_firestore

def create_chapter(chapter_data: ChapterCreateRequest) -> ChapterResponse:
    saved = save_chapter_to_firestore(
        title=chapter_data.title,
        description=chapter_data.description
    )
    return ChapterResponse(**saved)
