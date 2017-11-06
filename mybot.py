import sys
sys.path.append(r'/home/pi/pysrc')
sys.path.append(r'/home/pi/coderbot')
sys.path.append(r'/home/pi/coderbot/viz')
import pydevd
from coderbot import CoderBot, PIN_PUSHBUTTON
from camera import Camera
from motion import Motion
from viz import camera, streamer, image, blob

pydevd.settrace('10.0.0.9')
mybot = Motion()