from .extensions import db
from flask_migrate import Migrate

migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)
    