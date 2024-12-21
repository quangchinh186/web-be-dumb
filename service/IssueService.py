from reposistory.IssueRepo import IssueRepo

class IssueService():
    @classmethod
    def getIssueById(cls, issue_id):
        issue = IssueRepo.getById(issue_id)
        if issue == None:
            raise Exception('issue not found')
        return issue.as_dict()
    
    @classmethod
    def getIssuesBySprintId(cls, sprint_id):
        issues = []
        for item in IssueRepo.getBySprintId(sprint_id):
            issues.append(item.as_dict())
        return issues
    
    @classmethod
    def createIssue(cls, **kwargs):
        issue = IssueRepo.create(**kwargs)
        return issue
    
    @classmethod
    def updateIssue(cls, issue_id, **kwargs):
        issue = IssueRepo.getById(issue_id)
        if issue == None:
            raise Exception('issue not found')
        
        issue = IssueRepo.update(issue, **kwargs)
        return issue
    
    @classmethod
    def deleteIssue(cls, issue_id):
        issue = IssueRepo.getById(issue_id)
        if issue == None:
            raise Exception('issue not found')
        
        IssueRepo.delete(issue)
        return issue_id
