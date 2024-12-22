from sqlalchemy import select
from reposistory.BaseReposistory import Reposistory
from model.Issue import Issue

class IssueRepo(Reposistory):
    @classmethod
    def getById(cls, id):
        issue = cls.session.get(Issue, id)
        return issue
    
    @classmethod
    def getBySprintId(cls, sprint_id):
        issues = cls.session.execute(select(Issue)
                                     .filter(Issue.sprint_id == sprint_id)
                                     .order_by(Issue.created_time.desc())).scalars().all()
        return issues
    
    @classmethod
    def getByProjectId(cls, project_id):
        issues = cls.session.execute(select(Issue)
                                     .filter(Issue.project_id == project_id)
                                     .order_by(Issue.created_time.desc())).scalars().all()
        return issues
    
    @classmethod
    def create(cls, **kwargs):
        issue = Issue(**kwargs)
        cls.session.add(issue)
        cls.session.commit()
        return issue.as_dict()
    
    @classmethod
    def update(cls, issue: Issue, **kwargs):
        issue.update(**kwargs)
        cls.session.commit()

    @classmethod
    def delete(cls, issue: Issue):
        cls.session.delete(issue)
        cls.session.commit()
