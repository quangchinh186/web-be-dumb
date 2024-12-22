from flask import Blueprint, jsonify, request
from jwtDecorator import jwt_required
from service.ProjectService import ProjectService
from service.ProjectMemberService import ProjectMemberService

# Define a blueprint for project routes
project_bp = Blueprint('project', __name__)

@project_bp.route('/projects/<user_id>', methods=['GET'])
@jwt_required
def get_user_projects(user_id):
    projects = ProjectService.getUserProjects(user_id)
    return jsonify(projects)

@project_bp.route('/project/<id>', methods=['GET'])
def get_project(id):
    try:
        project = ProjectService.getProjectById(id)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    return jsonify(project)

@project_bp.route('/project', methods=['POST'])
def create_project():
    project_details = request.json
    print(project_details)
    user_id = project_details.pop('user_id')
    project = ProjectService.createProject(user_id, **project_details)
    ProjectMemberService.addMember(project['project_id'], user_id)
    return jsonify(project)

@project_bp.route('/project/<id>', methods=['PUT'])
def update_project(id):
    project_details = request.json
    user_id = project_details.pop('user_id')
    project = ProjectService.updateProject(id, user_id, **project_details)
    return jsonify(project)

@project_bp.route('/project/<id>', methods=['DELETE'])
def delete_project(id):
    return jsonify({"message": "Delete project with id: " + id})

@project_bp.route('/project/<id>/tasks', methods=['GET'])
def get_project_tasks(id):
    return jsonify({"message": "Tasks for project with id: " + id})
