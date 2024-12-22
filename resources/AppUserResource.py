from flask import Blueprint, jsonify, request
from service.AppUserService import AppUserService, AuthService
from jwtDecorator import jwt_required

# Define a blueprint for users routes
user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<id>', methods=['GET'])
@jwt_required
def get_user(id):
    try:
        user = AppUserService.getUserById(id)
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify(user)

@user_bp.route('/user/<id>', methods=['PUT'])
@jwt_required
def update_user(id):
    user_data = {
        'name': request.json['name'],
        'phone_number': request.json.get('phone_number', '')
    }
    try:
        user = AppUserService.updateUser(id, user_data)
    except Exception as e:
        return jsonify({"error": str(e)})
    
    return jsonify(user)

@user_bp.route('/user/<id>', methods=['DELETE'])
@jwt_required
def delete_user(id):
    try:
        AppUserService.deleteUser(id)
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify({"message": "user deleted"})

# Define a blueprint for auth routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    request_data = request.json
    email = request_data['email']
    password = request_data['password']
    try:
        user_token = AuthService.login(email, password)
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify({"token": user_token})

@auth_bp.route('/register', methods=['POST'])
def register():
    request_data = request.json
    print(request_data, 'request_data')
    user_data = {
        'email': request_data['email'],
        'password': request_data['password'],
        'name': request_data['name'],
        'phone_number': request_data.get('phone_number', '')
    }
    try:
        user_token = AuthService.register(user_data)
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify({"token": user_token})


@auth_bp.route('/recover', methods=['POST'])
def recover():
    return jsonify({"message": "Recover"})

@auth_bp.route('/reset', methods=['POST'])
def reset():
    return jsonify({"message": "Reset"})

