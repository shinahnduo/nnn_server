# app/routers/create_page_router.py

from fastapi import APIRouter, File, UploadFile, HTTPException
from app.service.file_upload_service import upload_file_to_dropbox
import os

router = APIRouter()

# 챕터 진행 상황 조회
@router.get("/progress/{chapter_id}")
async def get_chapter_progress(chapter_id: int):
    return {"message": f"{chapter_id}번 챕터 진행 상황 조회"}

# 이미지 저장
@router.post("/image")
async def save_image(file: UploadFile = File(...)):
    try:
        # 로컬에 임시 저장
        local_path = f"temp/{file.filename}"
        os.makedirs("temp", exist_ok=True)  # temp 디렉토리 생성
        with open(local_path, "wb") as f:
            f.write(await file.read())

        # Dropbox 경로 설정
        dropbox_path = f"/uploads/{file.filename}"

        # Dropbox로 파일 업로드
        uploaded_path = upload_file_to_dropbox(local_path, dropbox_path)

        # 로컬 파일 삭제
        os.remove(local_path)

        return {"message": "파일이 Dropbox에 저장되었습니다.", "dropbox_path": uploaded_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"파일 업로드 실패: {str(e)}")

# 챕터 세부내용 저장 (사진, 제목, 내용 포함)
@router.post("/chapter-detail")
async def save_chapter_detail():
    return {"message": "챕터 세부내용 저장"}
