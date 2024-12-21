from reposistory.SprintRepo import SprintRepo

class SprintService():
    @classmethod
    def getSprintById(cls, sprint_id):
        sprint = SprintRepo.getById(sprint_id)
        if sprint == None:
            raise Exception('sprint not found')
        return sprint.as_dict()
    
    @classmethod
    def getSprintsByProjectId(cls, project_id):
        sprints = []
        for item in SprintRepo.getByProjectId(project_id):
            sprints.append(item.as_dict())
        return sprints
    
    @classmethod
    def createSprint(cls, **kwargs):
        sprint = SprintRepo.create(**kwargs)
        return sprint
    
    @classmethod
    def updateSprint(cls, sprint_id, **kwargs):
        sprint = SprintRepo.getById(sprint_id)
        if sprint == None:
            raise Exception('sprint not found')
        
        sprint = SprintRepo.update(sprint, **kwargs)
        return sprint
    
    @classmethod
    def deleteSprint(cls, sprint_id):
        sprint = SprintRepo.getById(sprint_id)
        if sprint == None:
            raise Exception('sprint not found')
        
        SprintRepo.delete(sprint)
        return sprint_id