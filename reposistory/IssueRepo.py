from sqlalchemy import select
from reposistory.BaseReposistory import Reposistory
from model.Issue import Issue

class IssueRepo(Reposistory):
    @classmethod
    def getById(cls, id):
        issue = cls.session.get(Issue, id)
        return issue
    
    @classmethod
    def create(cls, **kwargs):
        issue = Issue(**kwargs)
        cls.session.add(issue)
        cls.session.commit()
        return issue.issue_id
    
    @classmethod
    def update(cls, issue: Issue, **kwargs):
        issue.update(**kwargs)
        cls.session.commit()

    @classmethod
    def delete(cls, issue: Issue):
        cls.session.delete(issue)
        cls.session.commit()
