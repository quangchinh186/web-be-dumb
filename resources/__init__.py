from .AppUserResource import user_bp, auth_bp
from .IssueResource import issue_bp
from .PermissionResource import permission_bp
from .ProjectMemberResource import project_member_bp
from .ProjectPermissionResource import project_permission_bp
from .ProjectResource import project_bp
from .SprintResource import sprint_bp

blueprints = [project_bp, user_bp, auth_bp, project_member_bp, sprint_bp, issue_bp, permission_bp, project_permission_bp]