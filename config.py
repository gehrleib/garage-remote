from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    # Set Flask configuration variables from .env file.

    # General Flask Config
    FLASK_APP = 'wsgi.py'
    SECRET_KEY = "supersecret"

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'garage-remote.db')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False