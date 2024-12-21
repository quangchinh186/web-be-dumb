import enum
from datetime import datetime
from .BaseModel import Base
from sqlalchemy.sql.functions import now
from sqlalchemy import String, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import mapped_column, Mapped

class SprintStatus(enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class Sprint(Base):
    __tablename__ = 'sprints'

    #column
    sprint_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=True)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(Enum(SprintStatus), default=SprintStatus.NEW)
    
    #foreign key
    created_by: Mapped[int] = mapped_column(ForeignKey("app_users.user_id"))
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.project_id'))

    # def __repr__(self) -> str:
    #     return f"Message: {self.content} \nBy: {self.user_id} - At: {self.sent_time}"
    
