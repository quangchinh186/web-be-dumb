from sqlalchemy import select
from reposistory.BaseReposistory import Reposistory
from model.Permission import Permission

class PermissionRepo(Reposistory):
    @classmethod
    def getAll(cls):
        permissions = cls.session.query(Permission).all()
        return permissions
    
    @classmethod
    def create(cls, **kwargs):
        permission = Permission(**kwargs)
        cls.session.add(permission)
        cls.session.commit()
        return permission
        
    @classmethod
    def update(cls, permission: Permission, **kwargs):
        permission.update(**kwargs)
        cls.session.commit()

    @classmethod
    def delete(cls, permission: Permission):
        cls.session.delete(permission)
        cls.session.commit()