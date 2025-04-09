from app.core.firebase import db

def save_chapter_detail(uid: str, schedule_id: str, chapter_id: str, detail_data: dict) -> dict:
    detail_ref = (
        db.collection("users")
        .document(uid)
        .collection("schedules")
        .document(schedule_id)
        .collection("chapters")
        .document(chapter_id)
        .collection("details")
        .document()
    )
    detail_doc = {
        "id": detail_ref.id,
        **detail_data
    }
    detail_ref.set(detail_doc)
    return detail_doc

def get_chapter_detail(
    uid: str,
    schedule_id: str,
    chapter_id: str,
    detail_id: str
) -> dict:
    detail_ref = (
        db.collection("users")
        .document(uid)
        .collection("schedules")
        .document(schedule_id)
        .collection("chapters")
        .document(chapter_id)
        .collection("details")
        .document(detail_id)
    )
    detail_doc = detail_ref.get()
    if not detail_doc.exists:
        raise ValueError(f"Detail {detail_id} not found")
    return detail_doc.to_dict()

def delete_chapter_detail(
    uid: str,
    schedule_id: str,
    chapter_id: str,
    detail_id: str
) -> None:
    detail_ref = (
        db.collection("users")
        .document(uid)
        .collection("schedules")
        .document(schedule_id)
        .collection("chapters")
        .document(chapter_id)
        .collection("details")
        .document(detail_id)
    )
    detail_ref.delete()

# 챕터 진행상황 조회
def get_chapter_progress(uid: str, schedule_id: str, chapter_id: str) -> dict:
    chapter_ref = (
        db.collection("users")
        .document(uid)
        .collection("schedules")
        .document(schedule_id)
        .collection("chapters")
        .document(chapter_id)
    )
    chapter_doc = chapter_ref.get()
    if not chapter_doc.exists:
        raise ValueError(f"Chapter {chapter_id} not found")
    return chapter_doc.to_dict()

# 챕터 세부내용 조회
def get_detail(
    detail_id: str
) -> dict:
    detail_ref = (
        db.collection("details")
        .document(detail_id)
    )
    detail_doc = detail_ref.get()
    if not detail_doc.exists:
        raise ValueError(f"Detail {detail_id} not found")
    return detail_doc.to_dict()

# 챕터 세부내용 저장
def update_chapter_detail(detail_id: str, detail_data: dict) -> dict:
    detail_ref = (
        db.collection("details")
        .document(detail_id)
    )
    detail_ref.update(detail_data)
    return {"id": detail_id, **detail_data}