from flask import Flask
from .config import Config
from .extensions import jwt, bcrypt
from .routes import api_v1
from .database import init_db
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    
    CORS(app)

    app.config.from_object(Config)

    init_db(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    app.register_blueprint(api_v1)

    return app
