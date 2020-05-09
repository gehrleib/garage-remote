from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def create_app():
    # Initialize the core application
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    with app.app_context():
        # Import parts of our application   
        from .auth import auth as auth_bp
        from .home import home as home_bp

        # Register Blueprints
        app.register_blueprint(auth_bp)
        app.register_blueprint(home_bp)

        return app