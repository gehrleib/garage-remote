import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SECRET_KEY = 'a-really-hard-to-guess-phrase'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'garage-remote.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False