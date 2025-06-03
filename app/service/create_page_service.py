import httpx
from fastapi import HTTPException

from app.repository.chapter_detail_repository import get_chapter_progress, update_chapter_detail
from app.service.file_service import save_image_to_dropbox, get_image_link_from_dropbox


def get_chapter_progress_service(uid: str, schedule_id: str, chapter_id: str) -> dict:
    try:
        return get_chapter_progress(uid, schedule_id, chapter_id)
    except Exception as e:
        raise

def update_chapter_detail_service(uid: str, schedule_id: str, chapter_id: str, detail_id: str,  detail_data: dict, file=None) -> dict:
    try:
        if file:
            image_path = save_image_to_dropbox(file)
            detail_data["imageUrl"] = get_image_link_from_dropbox(image_path)

        return update_chapter_detail(uid, schedule_id, chapter_id, detail_id, detail_data)
    except Exception as e:
        raise

async def generate_ai_content_service(detail_data: dict, file=None) -> dict:
    try:
        if file:
            image_path = save_image_to_dropbox(file)
            detail_data["imageUrl"] = get_image_link_from_dropbox(image_path)
            analyzed_image = await analyze_image(detail_data["imageUrl"])
            combined_text = (
                    "이미지에 대한 내용이야\n"
                    + str(analyzed_image) + "\n"
                    + "실제 사용자가 작성한 내용이야\n"
                    + str(detail_data["content"]) + "\n"
                    + "이미지에 대한 내용과 사용자가 작성한 내용을 합쳐서 10줄의 문장을 블로그 형식 작성할 수 있게 만들어줘.")
            generated_ai_content = await generate_ai_content(combined_text)
            return generated_ai_content
        else:
            combined_text = (
                    + "실제 사용자가 작성한 내용이야\n"
                    + str(detail_data["content"]) + "\n"
                    + "사용자가 작성한 내용을 합쳐서 10줄의 문장을 블로그 형식 작성할 수 있게 만들어줘.")
            generated_ai_content = await generate_ai_content(combined_text)
            return generated_ai_content
    except Exception as e:
        raise


async def generate_ai_content(content: str):
    print("content: " + str(content))
    payload = {
        "model": "grok-3-latest",
        "stream": False,
        "messages": [
            {
                "role": "system",
                "content": "You are a test assistant."
            },
            {
                "role": "user",
                "content": str(content)
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer xai-sZK8oAIyt1jkuu7Q0UrwzxBB0OLFQNPdcCiKp4Vekb9E7m5nxCTiKOVvmnB6vV8R9BBOIHd0MzU7OqeP",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            print("start generate ai content")
            response = await client.post("https://api.x.ai/v1/chat/completions", json=payload, headers=headers)
            print("finish generate ai content")
            print(response.json())
            response.raise_for_status()
        except httpx.HTTPError as e:
            print("Exception object:", repr(e))
            print("httpx.HTTPError: ", e)
            print("Status Code:", e.response.status_code)
            print("Response Text:", e.response.text)
            raise HTTPException(status_code=500, detail=str(e))

    return response.json()['choices'][0]['message']['content']

async def analyze_image(imageUrl: str):
    payload = {
        "model": "grok-2-vision-latest",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": str(imageUrl),
                            "detail": "high"
                        }
                    },
                    {
                        "type": "text",
                        "text": "이 이미지를 다음 다섯 항목 기준으로 각 항목별로 2줄 이상으로 분석해줘: 1. 주요 객체 2. 배경 유형 3. 이미지 내 텍스트 4. 색상 구성 5. 감정 또는 분위기"
                    }
                ]
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer xai-sZK8oAIyt1jkuu7Q0UrwzxBB0OLFQNPdcCiKp4Vekb9E7m5nxCTiKOVvmnB6vV8R9BBOIHd0MzU7OqeP",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print("start")
            response = await client.post("https://api.x.ai/v1/chat/completions", json=payload, headers=headers)
            print("image analyze finished: ",response)
            response.raise_for_status()
        except httpx.HTTPError as e:
            print("Exception object:", repr(e))
            print("httpx.HTTPError: ", e)
            print("Status Code:", e.response.status_code)
            print("Response Text:", e.response.text)
            raise HTTPException(status_code=500, detail=str(e))

    return response.json()['choices'][0]['message']['content']