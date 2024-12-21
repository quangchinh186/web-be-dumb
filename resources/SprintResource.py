from flask import Blueprint, jsonify, request
from jwtDecorator import jwt_required
from service.SprintService import SprintService

# Define a blueprint for project routes
sprint_bp = Blueprint('sprint', __name__)

@sprint_bp.route('/sprint/<sprint_id>', methods=['GET'])
@jwt_required
def get_sprint(sprint_id):
    try:
        sprint = SprintService.getSprintById(sprint_id)
        return jsonify(sprint)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@sprint_bp.route('/sprints/<project_id>', methods=['GET'])
def get_sprints(project_id):
    try:
        sprints = SprintService.getSprintsByProjectId(project_id)
        return jsonify(sprints)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@sprint_bp.route('/sprint', methods=['POST'])
def create_sprint():
    sprint_details = request.json
    try:
        sprint = SprintService.createSprint(**sprint_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(sprint)

@sprint_bp.route('/sprint/<sprint_id>', methods=['PUT'])
def update_sprint(sprint_id):
    sprint_details = request.json
    try:
        sprint = SprintService.updateSprint(sprint_id, **sprint_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(sprint)

@sprint_bp.route('/sprint/<sprint_id>', methods=['DELETE'])
def delete_sprint(sprint_id):
    try:
        SprintService.deleteSprint(sprint_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"message": "Delete sprint with id: " + sprint_id})


