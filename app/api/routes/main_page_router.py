# app/routers/main_page_router.py

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.schema.chapter_schema import ChapterCreateRequest, ChapterResponse
from app.schema.schedule_schema import ScheduleResponse, ScheduleCreateRequest
from app.service import chapter_service
from app.service.schedule_service import create_schedule_for_user

router = APIRouter()


# 프로필 조회 API
@router.get("/profile")
async def get_profile():
    return {"message": "프로필 조회"}


# 메인 페이지 조회
@router.get("/")
async def get_main_page():
    return {"message": "메인 페이지 조회"}


# 일정 저장
@router.post("/schedule", response_model=ScheduleResponse)
async def create_schedule_api(
        schedule: ScheduleCreateRequest,
        uid: str = 'test01'
        # uid: str = Depends(get_current_user)
):
    return create_schedule_for_user(uid, schedule)


# 일정 수정
@router.put("/schedule/{schedule_id}")
async def update_schedule(schedule_id: int):
    return {"message": f"{schedule_id}번 일정 수정"}


# 일정 삭제
@router.delete("/schedule/{schedule_id}")
async def delete_schedule(schedule_id: int):
    return {"message": f"{schedule_id}번 일정 삭제"}


# 챕터 저장
@router.post("/schedule/{schedule_id}/chapter", response_model=ChapterResponse)
def create_chapter_api(
    schedule_id: str = Path(..., description="챕터를 저장할 스케줄 ID"),
    chapter: ChapterCreateRequest = ...,
    uid: str = 'test01'
    # uid: str = Depends(get_current_user)
):
    return chapter_service.create_chapter_for_schedule(uid, schedule_id, chapter)


# 챕터 수정
@router.put("/chapter/{chapter_id}")
async def update_chapter(chapter_id: int):
    return {"message": f"{chapter_id}번 챕터 수정"}


# 챕터 삭제
@router.delete("/chapter/{chapter_id}")
async def delete_chapter(chapter_id: int):
    return {"message": f"{chapter_id}번 챕터 삭제"}


# 챕터 세부내용 조회
@router.get("/chapter-detail/{chapter_id}")
async def get_chapter_detail(chapter_id: int):
    return {"message": f"{chapter_id}번 챕터 세부내용 조회"}


# 챕터 세부내용 삭제
@router.delete("/chapter-detail/{chapter_id}")
async def delete_chapter_detail(chapter_id: int):
    return {"message": f"{chapter_id}번 챕터 세부내용 삭제"}
