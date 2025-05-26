from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import db, User

login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import app as main_app
    app.register_blueprint(main_app)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))