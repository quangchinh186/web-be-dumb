from reposistory.BaseReposistory import Reposistory
from model.Sprint import Sprint
from sqlalchemy import select

class SprintRepo(Reposistory):
    @classmethod
    def getById(cls, id):
        sprint = cls.session.get(Sprint, id)
        return sprint
    
    @classmethod
    def getByProjectId(cls, project_id):
        sprints = cls.session.query(Sprint).filter(Sprint.project_id == project_id).all()
        return sprints
    
    @classmethod
    def create(cls, **kwargs):
        sprint = Sprint(**kwargs)
        cls.session.add(sprint)
        cls.session.commit()
        return sprint.sprint_id
    
    @classmethod
    def update(cls, user: Sprint, **kwargs):
        user.update(**kwargs)
        cls.session.commit()

    @classmethod
    def delete(cls, user: Sprint):
        cls.session.delete(user)
        cls.session.commit()
