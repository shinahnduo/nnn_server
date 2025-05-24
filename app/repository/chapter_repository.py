from app.core.firebase import db

def save_chapter_for_schedule(uid: str, schedule_id: str, title: str, description: str = None) -> dict:
    chapter_ref = (
        db.collection("users")
        .document(uid)
        .collection("schedules")
        .document(schedule_id)
        .collection("chapters")
        .document()
    )
    chapter_data = {
        "id": chapter_ref.id,
        "title": title,
        "description": description
    }
    chapter_ref.set(chapter_data)
    return chapter_data


def update_chapter_for_schedule(uid: str, schedule_id: str, chapter_id: str, update_data: dict) -> dict:
    chapter_ref = (
        db.collection("users")
        .document(uid)
        .collection("schedules")
        .document(schedule_id)
        .collection("chapters")
        .document(chapter_id)
    )

    chapter_ref.update(update_data)
    updated_doc = chapter_ref.get().to_dict()
    return updated_doc

def delete_chapter_for_schedule(uid: str, schedule_id: str, chapter_id: str) -> None:
    chapter_ref = (
        db.collection("users")
        .document(uid)
        .collection("schedules")
        .document(schedule_id)
        .collection("chapters")
        .document(chapter_id)
    )
    chapter_ref.delete()