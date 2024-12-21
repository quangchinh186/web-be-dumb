from datetime import datetime

from .BaseModel import Base

from sqlalchemy.sql.functions import now
from sqlalchemy import String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from typing import Optional, List

class Permission(Base):
    __tablename__ = 'permissions'

    #column
    permission_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    
    # def __repr__(self) -> str:
    #     return f"{self.comment_id} - {self.content} - {self.creator} - {self.edited}"
    
    # def as_dict(self):
    #     asdict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    #     asdict.__setitem__('creator', self.creator.__repr__())
    #     return asdict