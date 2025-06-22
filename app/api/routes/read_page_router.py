from typing import List

from fastapi import APIRouter, HTTPException, Depends, Body

from app.core.deps import get_current_user
from app.schema.chapter_detail_schema import ChapterDetailResponse
from app.service.read_page_service import get_detail, update_chapter_detail, get_details_by_chapter, \
    update_chapter_details

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
@router.put("/schedule/{schedule_id}/chapter/{chapter_id}/details")
async def update_chapter_detail(schedule_id: str,
                          chapter_id: str,
                          detail_data: list = Body(...),
                          uid: str = Depends(get_current_user, )
                          ):
    try:
        updated_detail = update_chapter_details(uid, schedule_id, chapter_id, detail_data)
        print(updated_detail)
        return {"message": "챕터 세부내용 저장 성공", "detail": updated_detail}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"챕터 세부내용 저장 실패: {str(e)}")


# 챕터 정보 조회
@router.get(
    "/schedule/{schedule_id}/chapter/{chapter_id}",
    response_model=List[ChapterDetailResponse]
)
def get_chapter_detail_api(
        schedule_id: str,
        chapter_id: str,
        uid: str = Depends(get_current_user)
):
    detail_data_list = get_details_by_chapter(uid, schedule_id, chapter_id)
    print(detail_data_list)
    return detail_data_list
