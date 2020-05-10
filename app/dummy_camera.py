class PiCamera(object):
    """Dummy class for developing on Windows without the need to
    import Raspberry Pi camera module
    """

    def __init__(self):
        pass

    def capture(self, pin):
        pass

    def resolution(self, pin):
        pass