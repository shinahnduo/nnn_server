# app/routers/create_page_router.py

from fastapi import APIRouter

router = APIRouter()

# 챕터 진행 상황 조회
@router.get("/progress/{chapter_id}")
async def get_chapter_progress(chapter_id: int):
    return {"message": f"{chapter_id}번 챕터 진행 상황 조회"}

# 이미지 저장
@router.post("/image")
async def save_image():
    return {"message": "이미지 저장"}

# 챕터 세부내용 저장 (사진, 제목, 내용 포함)
@router.post("/chapter-detail")
async def save_chapter_detail():
    return {"message": "챕터 세부내용 저장"}
