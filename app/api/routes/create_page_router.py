from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from app.service.create_page_service import save_chapter_detail_service, get_chapter_progress_service
from app.service.file_service import save_image_to_dropbox, get_image_link_from_dropbox
import os
import json

router = APIRouter()

# 챕터 진행 상황 조회
@router.get("/progress/{uid}/{schedule_id}/{chapter_id}")
async def get_chapter_progress(uid: str, schedule_id: str, chapter_id: str):
    try:
        progress = get_chapter_progress_service(uid, schedule_id, chapter_id)
        return {"message": "챕터 진행 상황 조회 성공", "progress": progress}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"챕터 진행 상황 조회 실패: {str(e)}")

# 챕터 세부내용 저장
@router.post("/chapter-detail/{uid}/{schedule_id}/{chapter_id}")
async def save_chapter_detail(
    uid: str,
    schedule_id: str,
    chapter_id: str,
    detail_data: str = Form(...),  # Form으로 문자열로 받음
    file: UploadFile = File(None)  # Optional image file
):
    try:
        print(detail_data)
        print(file)
        detail_data_dict = json.loads(detail_data)
        detail = save_chapter_detail_service(uid, schedule_id, chapter_id, detail_data_dict, file)
        return {"message": "챕터 세부내용 저장 성공", "detail": detail}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"챕터 세부내용 저장 실패: {str(e)}")

#이미지저장
@router.post("/image")
async def save_image(file: UploadFile = File(...)):
    try:
        # Save the image to Dropbox
        dropbox_path = save_image_to_dropbox(file)
        return {"message": "파일이 Dropbox에 저장되었습니다.", "dropbox_path": dropbox_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"파일 업로드 실패: {str(e)}")
    
# Dropbox 이미지 조회
@router.get("/image-link")
async def get_image_link(dropbox_path: str):
    try:
        link = get_image_link_from_dropbox(dropbox_path)
        return {"message": "이미지 링크 조회 성공", "link": link}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"이미지 링크 조회 실패: {str(e)}")