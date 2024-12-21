from reposistory.PermissionRepo import PermissionRepo

class PermissionService():
    @classmethod
    def getAllPermissions(cls):
        permissions = []
        for item in PermissionRepo.getAll():
            permissions.append(item.as_dict())
        return permissions