# garage-remote

Remote garage control using a RaspberryPi written mainly in Python.

A web server based on Flask runs on the RPi.

A web site can be launched to offer one button  which interact with the server. From within the network where the RPi is running, the server can be contacted via "localhost:9000".

#### Installation

On a fresh install of Raspbian Lite:

```
sudo apt update
sudo apt install git python-pip
sudo python -m pip install flask flask-login flask-sqlalchemy flask-wtf email_validator
sudo git clone https://github.com/gehrleib/garage-remote.git
```

Starting the server:

```
cd garage-remote
sudo python wsgi.py
```

To launch it automatically put the following lines into the file "/etc/rc.local":

```
sudo python /home/pi/garage-remote/wsgi.py
...
exit 0
```

Ensure startup script is running

```
sudo reboot
```

#### Configuration

Configuration is handled by creating a .env file. This should contain the following variables (replace the values with your own):

```
FLASK_ENV="production"
SECRET_KEY="YOURSECRETKEY"
```