import enum
from datetime import datetime
from .BaseModel import Base
from .AppUser import AppUser
from sqlalchemy.sql.functions import now
from sqlalchemy import String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional

class ProjectStatus(enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class Project(Base):
    __tablename__ = 'projects'

    #column
    project_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(1000))
    status: Mapped[Optional[str]] = mapped_column(Enum(ProjectStatus), default=ProjectStatus.NEW)
    description: Mapped[Optional[str]] = mapped_column(String(1000))
    image_url: Mapped[Optional[str]] = mapped_column(String(100))
    created_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=now())
    updated_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=now(), onupdate=now())
    
    #foreign key
    created_by: Mapped[int] = mapped_column(ForeignKey("app_users.user_id"))
    updated_by: Mapped[int] = mapped_column(ForeignKey("app_users.user_id"))

    #mapping
    owner: Mapped[AppUser] = relationship(primaryjoin=AppUser.user_id == created_by)
    updater: Mapped[AppUser] = relationship(primaryjoin=AppUser.user_id == updated_by)

    def as_dict(self):
        project = super().as_dict()
        project['status'] = project['status'].value
        return project
    

