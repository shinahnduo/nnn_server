# app/routers/read_page_router.py

from fastapi import APIRouter

router = APIRouter()

# 챕터 세부내용 조회
@router.get("/chapter-detail/{chapter_id}")
async def read_chapter_detail(chapter_id: int):
    return {"message": f"{chapter_id}번 챕터 세부내용 조회"}

# 챕터 세부내용 저장 (읽기 모드에서도 수정 가능한 경우)
@router.post("/chapter-detail")
async def update_chapter_detail():
    return {"message": "챕터 세부내용 저장"}
