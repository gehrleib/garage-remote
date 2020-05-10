from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import platform
import subprocess

# Globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()
camera = None
relay = None

def create_app():
    # Initialize the core application
    app = Flask(__name__, instance_relative_config=False)

    # Application Configurations
    app.config.from_object('config.Config')

    # Initalize platform
    system = {0: 'PC', 1: 'RASPBERRY'}

    is_raspberry = 'arm' in platform.machine().lower()

    if is_raspberry:
        import app.relay as relay

        # Detect camera
        cam = subprocess.check_output('vcgencmd get_camera', shell=True)
        has_camera = int(cam.split()[1][-1])

        if has_camera:
            import app.camera as camera
        else:
            import app.dummy_camera as camera
    else:
        import app.dummy_relay as relay
        import app.dummy_camera as camera

    print('\n')
    print(' * Platform: %s' % (system[is_raspberry]))
    print(' * Operating system: %s' % (platform.system()))
    if not is_raspberry:
        print(' * Working with dummy modules for relay and camera')
    else:
        if has_camera:
            print(' * Camera module attached')
        else:
            print(' * No camera module attached')
    print('\n')

    # Initialize relay and pins
    global relay
    relay = relay.Relay(app.config['PINS'])

    # Initialize camera
    global camera
    camera = camera.PiCamera()
    camera.resolution = (499, 443)

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