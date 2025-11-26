from flask import Blueprint

api_v1 = Blueprint("api_v1", __name__,url_prefix = "/api/v1")

from .auth import auth_bp
from .task import task_bp

api_v1.register_blueprint(auth_bp, url_prefix="/auth")
api_v1.register_blueprint(task_bp, url_prefix="/tasks")