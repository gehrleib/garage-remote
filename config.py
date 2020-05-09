from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    # Set Flask configuration variables from .env file.

    # General Flask Config
    SECRET_KEY = "supersecret"

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
        'sqlite:///' + path.join(basedir, 'garage-remote.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False