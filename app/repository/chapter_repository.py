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
