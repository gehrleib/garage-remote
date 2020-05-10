from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)

class Relay(object):
    """Relay class provides methods to operate a relay module
    which is attached to the RasperryPi GPIO pins
    """
    def __init__(self, pins=None):
        """Initialize the GPIO interface and pins
        Args:
            pins (LIST): List of pins that shall be activated
        """

        # set GPIO numbering mode
        # BCM - Use numbering 1-40
        GPIO.setmode(GPIO.BCM)

        # activate GPIO channels and their default state
        if pins:
            for pin in pins:
                GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

    def on(self, pin):
        GPIO.output(pin, GPIO.LOW)

    def off(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def reset(self):
        """Reset all GPIO pins and free them"""
        GPIO.cleanup()

    def pulse(self, pin, duration=0.2):
        """Sends pulse with specified duration to the given pin"""
        self.toggle(pin)
        sleep(duration)
        self.toggle(pin)

    def toggle(self, pin):
        """Toggle pin state"""
        GPIO.output(pin, not GPIO.input(pin))

    def state(self, pin):
        """Returns pin state 0 or 1"""
        return GPIO.input(pin)