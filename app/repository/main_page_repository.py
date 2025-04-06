from app.core.firebase import db
from datetime import datetime

def get_full_schedule_data(uid: str) -> list:
    schedules_ref = db.collection("users").document(uid).collection("schedules")
    schedules = []

    for schedule_doc in schedules_ref.stream():
        schedule = schedule_doc.to_dict()
        dt = schedule["datetime"]
        parsed_dt = datetime.fromisoformat(dt) if isinstance(dt, str) else dt

        schedule_data = {
            "id": schedule["id"],
            "title": schedule["title"],
            "description": schedule.get("description"),
            "date": parsed_dt.date(),
            "time": parsed_dt.time(),
            "chapters": []
        }

        chapters_ref = schedules_ref.document(schedule["id"]).collection("chapters")
        for chapter_doc in chapters_ref.stream():
            chapter = chapter_doc.to_dict()
            chapter_data = {
                "id": chapter["id"],
                "title": chapter["title"],
                "description": chapter.get("description"),
                "details": []
            }

            details_ref = chapters_ref.document(chapter["id"]).collection("details")
            for detail_doc in details_ref.stream():
                detail = detail_doc.to_dict()
                chapter_data["details"].append(detail)

            schedule_data["chapters"].append(chapter_data)

        schedules.append(schedule_data)

    return schedules
