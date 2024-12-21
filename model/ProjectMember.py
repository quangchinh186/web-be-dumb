from .BaseModel import Base


from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from typing import Optional

class ProjectMember(Base):
    __tablename__ = 'project_members'

    #column
    project_member_id: Mapped[int] = mapped_column(primary_key=True)

    #foreign key
    user_id: Mapped[int] = mapped_column(ForeignKey("app_users.user_id"))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.project_id"))

    # def __repr__(self) -> str:
    #     return f"id: {self.conversation_id}, name: {self.conversation_name}"
    