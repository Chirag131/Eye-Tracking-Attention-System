from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME = "Attention.py"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = ""
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .routes.views import views
    from .routes.auth import auth

    from .models import UserSession,AttentionLog

    app.register_blueprint(views , url_prefix = "/")
    app.register_blueprint(auth , url_prefix = "/")

    create_database(app)

    return app


def create_database(app):
    with app.app_context():
        db.create_all()
