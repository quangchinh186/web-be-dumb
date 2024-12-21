from flask import Blueprint, jsonify, request
from service.IssueService import IssueService
from jwtDecorator import jwt_required

issue_bp = Blueprint('issue', __name__)

@issue_bp.route('/issue/<issue_id>', methods=['GET'])
@jwt_required
def get_issue(issue_id):
    try:
        issue = IssueService.getIssueById(issue_id)
        return jsonify(issue)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@issue_bp.route('/issues/<sprint_id>', methods=['GET'])
def get_issues(sprint_id):
    try:
        issues = IssueService.getIssuesBySprintId(sprint_id)
        return jsonify(issues)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@issue_bp.route('/issue', methods=['POST'])
def create_issue():
    issue_details = request.json
    try:
        issue = IssueService.createIssue(**issue_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(issue)

@issue_bp.route('/issue/<issue_id>', methods=['PUT'])
def update_issue(issue_id):
    issue_details = request.json
    try:
        issue = IssueService.updateIssue(issue_id, **issue_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(issue)

@issue_bp.route('/issue/<issue_id>', methods=['DELETE'])
def delete_issue(issue_id):
    try:
        IssueService.deleteIssue(issue_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"message": "Delete issue with id: " + issue_id})

