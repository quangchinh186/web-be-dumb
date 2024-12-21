from reposistory.ProjectPermissionRepo import ProjectPermissionRepo

class ProjectPermissionService():
    @classmethod
    def getProjectPermissionById(cls, project_permission_id):
        project_permission = ProjectPermissionRepo.getById(project_permission_id)
        if project_permission == None:
            raise Exception('project_permission not found')
        return project_permission.as_dict()
    
    @classmethod
    def getProjectPermissionsByProjectId(cls, project_id):
        project_permissions = []
        for item in ProjectPermissionRepo.getByProjectId(project_id):
            project_permissions.append(item.as_dict())
        return project_permissions
    
    @classmethod
    def createProjectPermission(cls, **kwargs):
        project_permission = ProjectPermissionRepo.create(**kwargs)
        return project_permission
    
    @classmethod
    def updateProjectPermission(cls, project_permission_id, **kwargs):
        project_permission = ProjectPermissionRepo.getById(project_permission_id)
        if project_permission == None:
            raise Exception('project_permission not found')
        
        project_permission = ProjectPermissionRepo.update(project_permission, **kwargs)
        return project_permission
    
    @classmethod
    def deleteProjectPermission(cls, project_permission_id):
        project_permission = ProjectPermissionRepo.getById(project_permission_id)
        if project_permission == None:
            raise Exception('project_permission not found')
        
        ProjectPermissionRepo.delete(project_permission)
        return project_permission_id