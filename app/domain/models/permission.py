import enum
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
from .base import Base

class PermissionEnum(str, enum.Enum):
    OWNER = "OWNER"
    CONTRIBUTOR = "CONTRIBUTOR"
    READER = "READER"

class NovelPermission(Base):
    __tablename__ = "novel_permissions"

    permission_id = Column(Integer, primary_key=True, autoincrement=True)
    permission_name = Column(Enum(PermissionEnum), nullable=False)

    # 관계 설정
    users = relationship("NovelUserPermission", back_populates="permission")
