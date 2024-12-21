from reposistory.ProjectMemberRepo import ProjectMemberRepo

class ProjectMemberService():
    @classmethod
    def getMemberInProject(cls, project_id):
        members = []
        for member in ProjectMemberRepo.getMemberInProject(project_id):
            members.append(member.as_dict())

        return members
    
    @classmethod
    def addMember(cls, project_id, user_id):
        if ProjectMemberRepo.checkMember(project_id, user_id):
            raise Exception('User already in project')
        member = ProjectMemberRepo.addMember(project_id, user_id)
        return member.as_dict()
    
    @classmethod
    def removeMember(cls, project_id, user_id):
        if not ProjectMemberRepo.checkMember(project_id, user_id):
            raise Exception('User not in project')
        ProjectMemberRepo.removeMember(project_id, user_id)