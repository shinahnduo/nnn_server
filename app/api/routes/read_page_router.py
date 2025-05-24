from fastapi import APIRouter, HTTPException
from app.service.read_page_service import get_detail, update_chapter_detail

router = APIRouter()

# 챕터 세부내용 조회
@router.get("/chapter/detail/{detailId}")
async def read_chapter_detail(detailId: str):
    try:
        detail = get_detail(detailId)
        return {"message": "챕터 세부내용 조회 성공", "detail": detail}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"챕터 세부내용 조회 실패: {str(e)}")

# 챕터 세부내용 저장 (읽기 모드에서도 수정 가능한 경우)
@router.post("/chapter/detail")
async def update_chapter_detail(detail_id: str, detail_data: dict):
    try:
        updated_detail = update_chapter_detail(detail_id, detail_data)
        return {"message": "챕터 세부내용 저장 성공", "detail": updated_detail}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"챕터 세부내용 저장 실패: {str(e)}")