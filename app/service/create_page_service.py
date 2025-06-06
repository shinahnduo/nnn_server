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
            title = detail_data["title"]
            user_summary = detail_data["content"]
            # 최종 프롬프트 생성
            blog_prompt = f"""
            당신은 전문 블로거입니다. 아래 세 가지 정보를 기반으로 매끄럽고 감성적인 블로그 글을 작성해 주세요.

            1. **사용자가 제공한 제목:**  
            - "{title}"
            
            2. **사용자가 제공한 글감 요약:**  
            - "{user_summary}"

            3. **이미지 분석 결과:**  
            - "{analyzed_image}"

            블로그 글 작성 조건:
            - 위 세 정보를 자연스럽게 엮어 서론, 본론, 결론 구조로 작성해주세요.
            - 너무 딱딱하지 않게 **감성적인 문장**을 사용해 주세요.
            - 중간중간 독자의 공감을 유도할 수 있는 문장도 넣어주세요.
            - 블로그 스타일은 일상 공유 또는 라이프스타일 중심의 개인적인 톤으로 해주세요.
            - 글 길이는 약 300~500자 정도로 적당히 유지해주세요.
            """
            generated_ai_content = await generate_ai_content(blog_prompt)
            return generated_ai_content
        else:
            title = detail_data["title"]
            user_summary = detail_data["content"]
            blog_prompt = f"""
            당신은 전문 블로거입니다. 아래 두 가지 정보를 기반으로 매끄럽고 감성적인 블로그 글을 작성해 주세요.

            1. **사용자가 제공한 제목:**  
            - "{title}"
            
            2. **사용자가 제공한 글감 요약:**  
            - "{user_summary}"

            블로그 글 작성 조건:
            - 위 두 정보를 자연스럽게 엮어 서론, 본론, 결론 구조로 작성해주세요.
            - 너무 딱딱하지 않게 **감성적인 문장**을 사용해 주세요.
            - 중간중간 독자의 공감을 유도할 수 있는 문장도 넣어주세요.
            - 블로그 스타일은 일상 공유 또는 라이프스타일 중심의 개인적인 톤으로 해주세요.
            - 글 길이는 약 300~500자 정도로 적당히 유지해주세요.
            """
            generated_ai_content = await generate_ai_content(blog_prompt)
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
                        "text": """
                            당신은 이미지 분석 전문가입니다. 다음 이미지를 분석해 주세요.  
                            분석 기준은 다음과 같습니다:
                            
                            1. 이 이미지에 등장하는 **주요 요소**들을 나열하세요 (예: 사람, 동물, 사물, 장소 등).
                            2. **배경/장소**는 어디로 추정되며, 어떤 분위기인가요?
                            3. 등장인물의 **행동**, **표정**, **의상** 등을 기반으로 어떤 상황인지 설명해 주세요.
                            4. 이 이미지가 전달하려는 **감정**이나 **메시지**가 있다면 무엇인가요?
                            5. 해당 이미지를 활용해 블로그 콘텐츠를 작성한다면, 어떤 **키워드**나 **주제**가 적절할까요?
                            
                            최종 결과는 아래와 같은 형식으로 정리해주세요:
                            - 주요 요소:
                            - 배경과 분위기:
                            - 등장인물/행동 설명:
                            - 전달하는 감정/메시지:
                            - 추천 키워드/주제:
                        """
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