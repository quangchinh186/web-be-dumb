import jwt
from functools import wraps
from flask import request, jsonify
import os
from dotenv import load_dotenv

load_dotenv('util/.env')
SECRET_KEY = os.getenv("JWT_SECRET_KEY")

def jwt_required(f):
    """JWT validation decorator."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the token from the Authorization header
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Bearer token format
        if not token:
            return jsonify({"message": "Token is missing!"}), 403

        try:
            # Decode the JWT token
            decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            # You can attach the decoded token payload to the request object
            # for access in the view function if necessary
            request.user = decoded_payload  # Storing the decoded data in request for later use
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 403

        return f(*args, **kwargs)

    return decorated_function