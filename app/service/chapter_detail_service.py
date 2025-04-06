from app.schema.chapter_detail_schema  import ChapterDetailCreateRequest, ChapterDetailResponse
from app.repository.chapter_detail_repository import save_chapter_detail, get_chapter_detail, delete_chapter_detail


def create_chapter_detail(
    uid: str,
    schedule_id: str,
    chapter_id: str,
    detail_data: ChapterDetailCreateRequest
) -> ChapterDetailResponse:
    saved = save_chapter_detail(
        uid=uid,
        schedule_id=schedule_id,
        chapter_id=chapter_id,
        detail_data=detail_data.dict()
    )
    return ChapterDetailResponse(**saved)

def fetch_chapter_detail(uid: str, schedule_id: str, chapter_id: str, detail_id: str) -> ChapterDetailResponse:
    detail_data = get_chapter_detail(uid, schedule_id, chapter_id, detail_id)
    return ChapterDetailResponse(**detail_data)

def remove_chapter_detail(uid: str, schedule_id: str, chapter_id: str, detail_id: str) -> dict:
    delete_chapter_detail(uid, schedule_id, chapter_id, detail_id)
    return {"message": f"Detail {detail_id} deleted from chapter {chapter_id}"}