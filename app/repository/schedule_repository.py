from app.core.firebase import db
from datetime import datetime, time as time_cls

def save_schedule_for_user(uid: str, schedule_data: dict) -> dict:
    # 🔁 datetime.date + time → datetime.datetime
    date_obj = schedule_data.pop("date")
    time_obj = schedule_data.pop("time")

    combined_datetime = datetime.combine(date_obj, time_obj or time_cls())

    doc_ref = db.collection("users").document(uid).collection("schedules").document()
    data = {
        "id": doc_ref.id,
        "title": schedule_data["title"],
        "description": schedule_data.get("description"),
        "datetime": combined_datetime  # ✅ 변환된 datetime 저장
    }

    doc_ref.set(data)
    return data
