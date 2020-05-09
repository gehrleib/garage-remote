from flask import Blueprint, render_template
from flask_login import login_required, current_user

home = Blueprint('home', __name__)

DOOR_STATUS = None

@home.route('/')
def index():
    global DOOR_STATUS
    if current_user.is_authenticated:
        if DOOR_STATUS is None:
            DOOR_STATUS = "Closed"
        return render_template('home.html', name=current_user.name, status=DOOR_STATUS)
    else:
        return render_template('login.html')

@home.route('/toggle')
@login_required
def toggle():
    global DOOR_STATUS
    DOOR_STATUS = 'Open' if DOOR_STATUS == 'Closed' else 'Closed'
    return index()