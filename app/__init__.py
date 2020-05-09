from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Initialize the core application
    app = Flask(__name__, instance_relative_config=False)

    # Application Configurations
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from .auth import auth as auth_bp
        from .main import main as main_bp

        # Register Blueprints
        app.register_blueprint(auth_bp)
        app.register_blueprint(main_bp)

        # Create database models
        db.create_all()

        return app