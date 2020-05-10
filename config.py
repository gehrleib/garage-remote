"""Flask app configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config(object):
    """Set Flask configuration from environment variables."""

    FLASK_APP = 'wsgi'
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPALTES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + path.join(basedir, 'garage-remote.db')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # GPIO Pins
    DOOR = 11
    PINS = [DOOR]