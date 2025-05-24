import os
from app.repository.chapter_detail_repository import get_chapter_progress, update_chapter_detail
from app.service.file_service import save_image_to_dropbox

def get_chapter_progress_service(uid: str, schedule_id: str, chapter_id: str) -> dict:
    try:
        return get_chapter_progress(uid, schedule_id, chapter_id)
    except Exception as e:
        raise

def update_chapter_detail_service(uid: str, schedule_id: str, chapter_id: str, detail_id: str,  detail_data: dict, file=None) -> dict:
    try:
        if file:
            image_path = save_image_to_dropbox(file)
            detail_data["image_path"] = image_path

        return update_chapter_detail(uid, schedule_id, chapter_id, detail_id, detail_data)
    except Exception as e:
        raise