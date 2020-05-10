from flask import Blueprint, render_template
from flask_login import login_required, current_user
import platform
import subprocess


system = {0: 'PC', 1: 'RASPBERRY'}

# Check platform
is_raspberry = 'arm' in platform.machine().lower()

if is_raspberry:
    from . import relay as relay

    #detect camera
    cam = subprocess.check_output('vcgencmd get_camera', shell=True)
    has_camera = int(cam.split()[1][-1])

    if has_camera:
        from . import camera as picamera
    else:
        from . import dummy_camera as picamera
else:
    from . import dummy_camera as picamera
    from . import dummy_relay as relay

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

# define gpio ids
garage = 11

# initialize relay and pins
pins = [garage]
relay = relay.Relay(pins)

# initialize camera
camera = picamera.PiCamera()
camera.resolution = (499, 443)

DOOR_STATUS = None

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def dashboard():
    """Serve logged-in Dashboard."""
    global DOOR_STATUS
    if DOOR_STATUS is None:
        DOOR_STATUS = "Closed"
    return render_template('dashboard.html', name=current_user.name, status=DOOR_STATUS)

@main.route('/door')
@login_required
def handle_door_click():
    """Toggle the status of the switch."""
    global DOOR_STATUS
    relay.pulse(garage, duration=2.5)
    DOOR_STATUS = 'Open' if DOOR_STATUS == 'Closed' else 'Closed'
    return dashboard()

@main.route('/cam')
def handle_camera_click():
    """Get snapshot from camera"""
    if has_camera:
        filename = 'camera.png'
        folder = 'static/'
        camera.capture(folder+filename)
        message = ''
    else:
        message = 'Default image'

    return message