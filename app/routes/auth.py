from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services.auth_service import AuthService
from app.utils.validators import validate_register, validate_login

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods = ["POST"])
def register():
    data = request.get_json()
    errors = validate_register(data)
    if errors:
        return jsonify({"errors": errors}), 400
    user, error = AuthService.register_user(
        name = data.get("name"),
        email = data.get("email"),
        password = data.get("password")
    )

    if error:
        return jsonify ({"msg" : error}), 400
    return jsonify({"msg" : "User created successfully"}), 201

@auth_bp.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    errors = validate_login(data)
    if errors:
        return jsonify({"errors": errors}), 400    
    
    token, error = AuthService.login_user(
        email = data.get("email"),
        password = data.get("password")
    )
    if error:
        return jsonify({"msg" : error}), 401
    
    return jsonify({"access_token" : token}), 200

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    claims = get_jwt()

    return {
        "id": user_id,
        "email": claims.get("email"),
        "role": claims.get("role")
    }, 200