from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Novel(Base):
    __tablename__ = "novels"

    novel_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    summary = Column(Text, nullable=True)
    author_id = Column(Integer, nullable=False)
    total_pages = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    # 관계 설정
    contents = relationship("NovelContent", back_populates="novel")
    characters = relationship("NovelCharacter", back_populates="novel")
    categories = relationship("NovelCategory", back_populates="novel")
    permissions = relationship("NovelUserPermission", back_populates="novel")

class NovelCategory(Base):
    __tablename__ = "novel_categories"

    category_id = Column(Integer, ForeignKey("categories.category_id"), primary_key=True)
    novel_id = Column(Integer, ForeignKey("novels.novel_id"), primary_key=True)

    # 관계 설정
    novel = relationship("Novel", back_populates="categories")
    category = relationship("Category", back_populates="novels")

class NovelUserPermission(Base):
    __tablename__ = "novel_user_permissions"

    novel_id = Column(Integer, ForeignKey("novels.novel_id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("novel_permissions.permission_id"), primary_key=True)
    user_id = Column(Integer, nullable=False)

    # 관계 설정
    novel = relationship("Novel", back_populates="permissions")
    permission = relationship("NovelPermission", back_populates="users")
