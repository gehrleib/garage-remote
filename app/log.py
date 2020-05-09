from datetime import datetime
from flask import current_app
from os import path
from time import sleep

def log(str):
    f = open(path.join(current_app.config.basedir, 'log.txt'), 'a')
    f.write('{0} -- {1}\n'.format(datetime.now().strftime('%Y/%m/%d %H:%M:%S'), str))
    f.close()

def logger():
    try:

        while 1 >= 0:
            log("test")
            sleep(4)

    except KeyboardInterrupt:
        log("Program Shutdown")