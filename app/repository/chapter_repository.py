from app.core.firebase import db

def save_chapter_to_firestore(title: str, description: str = None) -> dict:
    chapter_ref = db.collection("chapters").document()
    chapter_data = {
        "id": chapter_ref.id,
        "title": title,
        "description": description
    }
    chapter_ref.set(chapter_data)
    return chapter_data
