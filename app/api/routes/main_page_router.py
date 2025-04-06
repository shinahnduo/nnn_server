# app/routers/main_page_router.py
from typing import List

from fastapi import APIRouter, Depends, Path

from app.core.deps import get_current_user
from app.schema.chapter_detail_schema import ChapterDetailResponse, ChapterDetailCreateRequest
from app.schema.chapter_schema import ChapterCreateRequest, ChapterResponse, ChapterUpdateRequest
from app.schema.main_page_schema import ScheduleOverview
from app.schema.schedule_schema import ScheduleResponse, ScheduleCreateRequest, ScheduleUpdateRequest
from app.service import chapter_service
from app.service.chapter_detail_service import create_chapter_detail, fetch_chapter_detail, remove_chapter_detail
from app.service.chapter_service import update_chapter, delete_chapter
from app.service.main_page_service import get_main_page_data
from app.service.schedule_service import create_schedule_for_user, update_schedule, delete_schedule

router = APIRouter()


# 프로필 조회 API
@router.get("/profile")
async def get_profile():
    return {"message": "프로필 조회"}


# 메인 페이지 조회
@router.get("/main", response_model=List[ScheduleOverview])
def get_main_page(
        uid: str = Depends(get_current_user)
):
    return get_main_page_data(uid)


# 일정 저장
@router.post("/schedule", response_model=ScheduleResponse)
async def create_schedule_api(
        schedule: ScheduleCreateRequest,
        uid: str = Depends(get_current_user)
):
    return create_schedule_for_user(uid, schedule)


# 일정 수정
@router.put("/schedule/{schedule_id}", response_model=ScheduleResponse)
def update_schedule_api(
        schedule_id: str,
        update_data: ScheduleUpdateRequest,
        uid: str = Depends(get_current_user)
):
    return update_schedule(uid, schedule_id, update_data)


@router.delete("/schedule/{schedule_id}")
def delete_schedule_api(
        schedule_id: str,
        uid: str = Depends(get_current_user)
):
    return delete_schedule(uid, schedule_id)


# 챕터 저장
@router.post("/schedule/{schedule_id}/chapter", response_model=ChapterResponse)
def create_chapter_api(
        schedule_id: str = Path(..., description="챕터를 저장할 스케줄 ID"),
        chapter: ChapterCreateRequest = ...,
        uid: str = Depends(get_current_user)
):
    return chapter_service.create_chapter_for_schedule(uid, schedule_id, chapter)


# 챕터 수정
@router.put("/schedule/{schedule_id}/chapter/{chapter_id}", response_model=ChapterResponse)
async def update_chapter_api(
        schedule_id: str,
        chapter_id: str,
        chapter_data: ChapterUpdateRequest,
        uid: str = Depends(get_current_user)
):
    return update_chapter(uid, schedule_id, chapter_id, chapter_data)


# 챕터 삭제
@router.delete("/schedule/{schedule_id}/chapter/{chapter_id}")
def delete_chapter_api(
        schedule_id: str,
        chapter_id: str,
        uid: str = Depends(get_current_user)
):
    return delete_chapter(uid, schedule_id, chapter_id)


# 챕터 세부내용 생성
@router.post(
    "/schedule/{schedule_id}/chapter/{chapter_id}/detail",
    response_model=ChapterDetailResponse
)
def create_chapter_detail_api(
        schedule_id: str,
        chapter_id: str,
        detail: ChapterDetailCreateRequest,
        uid: str = Depends(get_current_user)
):
    return create_chapter_detail(uid, schedule_id, chapter_id, detail)


# 챕터 세부내용 조회
@router.get(
    "/schedule/{schedule_id}/chapter/{chapter_id}/detail/{detail_id}",
    response_model=ChapterDetailResponse
)
def get_chapter_detail_api(
        schedule_id: str,
        chapter_id: str,
        detail_id: str,
        uid: str = Depends(get_current_user)
):
    return fetch_chapter_detail(uid, schedule_id, chapter_id, detail_id)


# 챕터 세부내용 삭제
@router.delete("/schedule/{schedule_id}/chapter/{chapter_id}/detail/{detail_id}")
def delete_chapter_detail_api(
        schedule_id: str,
        chapter_id: str,
        detail_id: str,
        uid: str = Depends(get_current_user)
):
    return remove_chapter_detail(uid, schedule_id, chapter_id, detail_id)
