from app.infrastructure.notion_client import NotionClient

class NotionService:
    def __init__(self):
        self.notion_client = NotionClient()

    def add_new_page(self, title: str, content: str):
        """
        새로운 글을 Notion에 추가하는 서비스 로직
        """
        response = self.notion_client.create_page(title, content)
        return response
