from sqlalchemy import select
from reposistory.BaseReposistory import Reposistory
from model.Project import Project

class ProjectRepo(Reposistory):
    @classmethod
    def getProjectByID(cls, id):
        project = cls.session.get(Project, id)
        return project
    
    @classmethod
    def getUserProjects(cls, user_id):
        projects = cls.session.query(Project).filter(Project.created_by == user_id).all()
        return projects
    
    @classmethod
    def searchProjects(cls, name):
        projects = cls.session.query(Project).filter(Project.name.like(f"%{name}%")).all()
        return projects
    
    @classmethod
    def create(cls, user_id, **kwargs):
        project = Project(**kwargs)
        project.created_by = user_id
        project.updated_by = user_id
        cls.session.add(project)
        cls.session.commit()
        
        return project
    
    @classmethod
    def update(cls, project: Project, user_id, **kwargs):
        project.updated_by = user_id
        project.update(**kwargs)
        cls.session.commit()
        return project

    @classmethod
    def delete(cls, project: Project):
        cls.session.delete(project)
        cls.session.commit()