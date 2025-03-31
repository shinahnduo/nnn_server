import requests
from app.core.config import Config

class NotionClient:
    BASE_URL = "https://api.notion.com/v1/pages"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {Config.NOTION_API_KEY}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def create_page(self, title: str, content: str):
        """
        Notion 데이터베이스에 새로운 페이지를 추가합니다.
        """
        payload = {
            "parent": {"database_id": Config.NOTION_DATABASE_ID},
            "properties": {
                "title": [
                    {
                        "text": {"content": title}
                    }
                ]
            },
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"text": {"content": content}}]
                    }
                }
            ]
        }

        response = requests.post(self.BASE_URL, json=payload, headers=self.headers)
        return response.json()
