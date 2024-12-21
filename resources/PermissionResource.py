from flask import Blueprint, jsonify, request
from service.PermissionService import PermissionService
from jwtDecorator import jwt_required

permission_bp = Blueprint('permission', __name__)

@permission_bp.route('/permissions', methods=['GET'])
@jwt_required
def get_permissions():
    permissions = PermissionService.getAllPermissions()
    return jsonify(permissions)
