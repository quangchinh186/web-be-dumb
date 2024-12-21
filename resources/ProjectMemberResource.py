from flask import Blueprint, jsonify, request
from jwtDecorator import jwt_required
from service.ProjectMemberService import ProjectMemberService

# Define a blueprint for project member routes
project_member_bp = Blueprint('project_member', __name__)

@project_member_bp.route('/project/<project_id>/members', methods=['GET'])
@jwt_required
def get_project_members(project_id):
    members = ProjectMemberService.getMemberInProject(project_id)
    return jsonify(members)

@project_member_bp.route('/project/<project_id>/member', methods=['POST'])
@jwt_required
def add_project_member(project_id):
    user_id = request.json.get('user_id')
    try:
        member = ProjectMemberService.addMember(project_id, user_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(member)

@project_member_bp.route('/project/<project_id>/member', methods=['DELETE'])
@jwt_required
def remove_project_member(project_id):
    user_id = request.json.get('user_id')
    try:
        ProjectMemberService.removeMember(project_id, user_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"message": "User removed from project"})
