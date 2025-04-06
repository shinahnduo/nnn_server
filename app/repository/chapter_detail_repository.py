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
