"""Logged-in page routes."""
from flask import Blueprint, current_app, redirect, render_template, url_for
from flask_login import login_required, current_user
from app import camera, relay

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def dashboard():
    """Serve logged-in Dashboard."""
    return render_template('dashboard.html', name=current_user.name, status='Closed')

@main.route('/door')
@login_required
def handle_door_click():
    """Toggle the status of the switch."""
    relay.pulse(current_app.config['DOOR'], duration=2.5)
    return redirect(url_for('main.dashboard'))

@main.route('/cam')
def handle_camera_click():
    """Get snapshot from camera"""
    camera.capture('static/camera.png')
    return