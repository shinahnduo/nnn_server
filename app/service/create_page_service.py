import os
from app.repository.chapter_detail_repository import save_chapter_detail, get_chapter_progress
from app.service.file_service import save_image_to_dropbox

def get_chapter_progress_service(uid: str, schedule_id: str, chapter_id: str) -> dict:
    try:
        return get_chapter_progress(uid, schedule_id, chapter_id)
    except Exception as e:
        raise

def save_chapter_detail_service(uid: str, schedule_id: str, chapter_id: str, detail_data: dict, file=None) -> dict:
    try:
        if file:
            image_path = save_image_to_dropbox(file)
            detail_data["image_path"] = image_path

        return save_chapter_detail(uid, schedule_id, chapter_id, detail_data)
    except Exception as e:
        raise