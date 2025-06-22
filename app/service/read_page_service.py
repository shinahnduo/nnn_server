from pprint import pprint

from pydantic import json

from app.repository.chapter_detail_repository import get_detail, update_chapter_detail, get_chapter_progress


def get_detail(detailId: str) -> dict:
    try:
        return get_detail(detailId)
    except Exception as e:
        raise

def update_chapter_details(uid: str, schedule_id: str, chapter_id: str, detail_data: list) -> list:
    try:
        updated_detail_list = []
        for detail in detail_data:
            detail_id = detail["id"]
            pprint(detail)
            updated_detail_data = update_chapter_detail(uid, schedule_id, chapter_id, detail_id, detail)
            updated_detail_list.append(updated_detail_data)
        return updated_detail_list
    except Exception as e:
        raise

def get_details_by_chapter(uid: str, schedule_id: str, chapter_id: str) -> dict:
    try:
        return get_chapter_progress(uid, schedule_id, chapter_id)
    except Exception as e:
        raise