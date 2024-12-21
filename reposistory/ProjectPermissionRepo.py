from sqlalchemy import select, asc
from reposistory.BaseReposistory import Reposistory
from model.ProjectPermission import ProjectPermission

class ProjectPermissionRepo(Reposistory):
    @classmethod
    def getById(cls, id):
        return cls.session.get(ProjectPermission, id)

    @classmethod
    def create(cls, **kwargs):
        projectPermission = ProjectPermission(**kwargs)
        cls.session.add(projectPermission)
        cls.session.commit()

    @classmethod
    def update(cls, projectPermission: ProjectPermission, **kwargs):
        projectPermission.update(**kwargs)
        cls.session.commit()

    @classmethod
    def delete(cls, projectPermission: ProjectPermission):
        cls.session.delete(projectPermission)
        cls.session.commit()