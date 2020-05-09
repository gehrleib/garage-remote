from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

DOOR_STATUS = None

@main.route('/')
@login_required
def dashboard():
    """Serve logged-in Dashboard."""
    global DOOR_STATUS
    if DOOR_STATUS is None:
        DOOR_STATUS = "Closed"
    return render_template('dashboard.html', name=current_user.name, status=DOOR_STATUS)

@main.route('/toggle')
@login_required
def toggle():
    """Toggle the status of the switch."""
    global DOOR_STATUS
    DOOR_STATUS = 'Open' if DOOR_STATUS == 'Closed' else 'Closed'
    return dashboard()