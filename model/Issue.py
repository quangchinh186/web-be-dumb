import enum
from datetime import datetime
from .BaseModel import Base
from .AppUser import AppUser
from .Project import Project
from .Sprint import Sprint
from sqlalchemy.sql.functions import now
from sqlalchemy import ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship 
from typing import Optional

class IssueStatus(enum.Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    IN_REVIEW = 'in_review'
    TESTING = 'testing'
    DONE = 'done'


class Issue(Base):
    __tablename__ = 'issues'

    #column
    issue_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(Enum(IssueStatus), default=IssueStatus.TODO)
    description: Mapped[str] = mapped_column(String(1000))
    created_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=now())
    updated_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=now(), onupdate=now())
    
    #foreign key
    created_by: Mapped[int] = mapped_column(ForeignKey("app_users.user_id"))
    assigned_to: Mapped[Optional[int]] = mapped_column(ForeignKey("app_users.user_id"), nullable=True, server_default=None)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.project_id"))
    sprint_id: Mapped[Optional[int]] = mapped_column(ForeignKey("sprints.sprint_id"), nullable=True, server_default=None)

    #mapping
    reporter: Mapped[AppUser] = relationship(primaryjoin=AppUser.user_id == created_by)
    assignee: Mapped[AppUser] = relationship(primaryjoin=AppUser.user_id == assigned_to)
    project: Mapped[Project] = relationship(primaryjoin=Project.project_id == project_id)
    sprint: Mapped[Sprint] = relationship(primaryjoin=Sprint.sprint_id == sprint_id)


    def as_dict(self):
        dict_rep = super().as_dict()
        dict_rep['status'] = self.status.value
        dict_rep['created_by'] = self.reporter.name
        
        return dict_rep