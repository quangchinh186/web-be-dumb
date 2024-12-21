from flask import Blueprint, jsonify, request
from service.ProjectPermissionService import ProjectPermissionService
from jwtDecorator import jwt_required

# Define a blueprint for project_permission routes
project_permission_bp = Blueprint('project_permission', __name__)

@project_permission_bp.route('/project_permission/<project_permission_id>', methods=['GET'])
@jwt_required
def get_project_permission(project_permission_id):
    try:
        project_permission = ProjectPermissionService.getProjectPermissionById(project_permission_id)
        return jsonify(project_permission)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@project_permission_bp.route('/project_permissions/<project_id>', methods=['GET'])
def get_project_permissions(project_id):
    try:
        project_permissions = ProjectPermissionService.getProjectPermissionsByProjectId(project_id)
        return jsonify(project_permissions)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@project_permission_bp.route('/project_permission', methods=['POST'])
def create_project_permission():
    project_permission_details = request.json
    try:
        project_permission = ProjectPermissionService.createProjectPermission(**project_permission_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(project_permission)

@project_permission_bp.route('/project_permission/<project_permission_id>', methods=['PUT'])
def update_project_permission(project_permission_id):
    project_permission_details = request.json
    try:
        project_permission = ProjectPermissionService.updateProjectPermission(project_permission_id, **project_permission_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(project_permission)

@project_permission_bp.route('/project_permission/<project_permission_id>', methods=['DELETE'])
def delete_project_permission(project_permission_id):
    try:
        ProjectPermissionService.deleteProjectPermission(project_permission_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"message": "Delete project_permission with id: " + project_permission_id})

