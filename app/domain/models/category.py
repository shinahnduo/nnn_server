from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from .base import Base

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)

    # 관계 설정
    novels = relationship("NovelCategory", back_populates="category")
