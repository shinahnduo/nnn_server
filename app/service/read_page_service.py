from app.repository.chapter_detail_repository import get_detail, update_chapter_detail, get_chapter_progress


def get_detail(detailId: str) -> dict:
    try:
        return get_detail(detailId)
    except Exception as e:
        raise

def update_chapter_detail(detail_id: str, detail_data: dict) -> dict:    
    try:
        return update_chapter_detail(detail_id, detail_data)
    except Exception as e:
        raise

def get_details_by_chapter(uid: str, schedule_id: str, chapter_id: str) -> dict:
    try:
        return get_chapter_progress(uid, schedule_id, chapter_id)
    except Exception as e:
        raise