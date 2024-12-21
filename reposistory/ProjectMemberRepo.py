from sqlalchemy import select
from reposistory.BaseReposistory import Reposistory
from model.ProjectMember import ProjectMember

class ProjectMemberRepo(Reposistory):
    @classmethod
    def checkMember(cls, project_id, user_id):
        member = cls.session.query(ProjectMember).filter(ProjectMember.project_id == project_id, ProjectMember.user_id == user_id).first()
        return member

    @classmethod
    def getMemberInProject(cls, project_id):
        members = cls.session.query(ProjectMember).filter(ProjectMember.project_id == project_id).all()
        return members
    
    @classmethod
    def addMember(cls, project_id, user_id):
        member = ProjectMember(project_id=project_id, user_id=user_id)
        cls.session.add(member)
        cls.session.commit()
        return member
    
    @classmethod
    def removeMember(cls, project_id, user_id):
        member = cls.session.query(ProjectMember).filter(ProjectMember.project_id == project_id, ProjectMember.user_id == user_id).first()
        cls.session.delete(member)
        cls.session.commit()