from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.task_service import TaskService
from app.utils.decorators import admin_required, role_required
from app.utils.validators import validate_task


task_bp = Blueprint("task", __name__)

@task_bp.route("",  methods = ["POST"])
@jwt_required()
def create_task():
    user_id = int(get_jwt_identity())
    data = request.get_json()
    validate_task(data)
    task = TaskService.create_task(
        user_id = user_id,
        title = data.get("title"),
        description = data.get("description")
    )
    return jsonify(task.to_dict()), 201

@task_bp.route("", methods = ["GET"])
@jwt_required()
def get_tasks():
    user_id = int(get_jwt_identity())
    tasks = TaskService.get_tasks(user_id)
    return jsonify([t.to_dict() for t in tasks])

@task_bp.route("/<int:task_id>", methods = ["PUT"])
@jwt_required()
@admin_required
def update_task(task_id):
    user_id = int(get_jwt_identity())
    data = request.get_json()
    validate_task(data)
    task = TaskService.update_task(task_id, user_id, data)

    if not task:
        return jsonify({"msg" : "Task not found"}), 404
    
    updated = TaskService.update_task(task_id, user_id, data)
    return jsonify(updated.to_dict()), 200

@task_bp.route("/<int:task_id>", methods = ["DELETE"])
@jwt_required()
@admin_required
def delete_task(task_id):
    user_id = int(get_jwt_identity())
    success = TaskService.delete_task(task_id, user_id)

    if not success:
        return jsonify({"msg": "Task not found"}), 404

    return jsonify({"msg": "Task deleted"})