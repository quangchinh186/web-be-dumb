from .ProjectResource import project_bp
from .AppUserResource import user_bp, auth_bp
from .ProjectMemberResource import project_member_bp
from .SprintResource import sprint_bp

blueprints = [project_bp, user_bp, auth_bp, project_member_bp, sprint_bp]