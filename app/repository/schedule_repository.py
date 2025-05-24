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

def update_schedule_for_user(uid: str, schedule_id: str, update_data: dict) -> dict:
    schedule_ref = db.collection("users").document(uid).collection("schedules").document(schedule_id)

    # 날짜+시간을 datetime으로 변환 (필요할 때만)
    if "date" in update_data or "time" in update_data:
        date_obj = update_data.pop("date", None)
        time_obj = update_data.pop("time", None)

        if date_obj or time_obj:
            old_doc = schedule_ref.get().to_dict() or {}
            existing_datetime = old_doc.get("datetime")

            # 기본값 처리
            from_db = datetime.fromisoformat(existing_datetime) if existing_datetime else datetime.now()
            combined = datetime.combine(date_obj or from_db.date(), time_obj or from_db.time())
            update_data["datetime"] = combined

    schedule_ref.update(update_data)
    updated_doc = schedule_ref.get().to_dict()
    return updated_doc

def delete_schedule_for_user(uid: str, schedule_id: str) -> None:
    schedule_ref = db.collection("users").document(uid).collection("schedules").document(schedule_id)
    schedule_ref.delete()