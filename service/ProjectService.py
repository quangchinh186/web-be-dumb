from reposistory.ProjectRepo import ProjectRepo
from .BaseService import BaseService

class ProjectService(BaseService):
    # GET
    @classmethod
    def getProjectById(cls, project_id):
        project = ProjectRepo.getProjectByID(project_id)
        if project == None:
            raise Exception('project not found')
        return project.as_dict()
    
    @classmethod
    def searchProject(cls, name):
        projects = []
        for item in ProjectRepo.searchProjects(name):
            projects.append(item.as_dict())
        return projects

    @classmethod
    def getUserProjects(cls, user_id):
        projects = []
        for item in ProjectRepo.getUserProjects(user_id):
            projects.append(item.as_dict())
        return projects

    # POST
    @classmethod
    def createProject(cls, user_id, **kwargs):
        project = ProjectRepo.create(user_id, **kwargs)
        return project.as_dict()

    # PUT
    @classmethod
    def updateProject(cls, project_id, user_id, update_data):
        project = ProjectRepo.getProjectByID(project_id)
        if project == None:
            raise Exception('project not found')
        
        project = ProjectRepo.update(project, user_id, **update_data)
        return project.as_dict()

    @classmethod        
    def deleteProject(cls, project_id):
        ProjectRepo.delete(project_id)