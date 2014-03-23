import os
import coderbot
from handler import camera, signal, logo
from threading import Thread

from flask import Flask, render_template, request
#from flask_sockets import Sockets

bot = coderbot.CoderBot.get_instance()
cam_h = camera.CameraHandler.get_instance()

app = Flask(__name__,static_url_path="")
#sockets = Sockets(app)

@app.route("/")
def home():
    return render_template('control.html', host=request.host[:request.host.find(':')])

@app.route("/blockly")
def blockly():
    return render_template('blockly.html')

@app.route("/bot")
def handle_bot():
    cmd = request.args.get('cmd')
    param = request.args.get('param')
    if cmd == "forward":
        bot.forward(float(param))
    elif cmd == "left":
        bot.left(float(param))
    elif cmd == "right":
        bot.right(float(param))
    elif cmd == "backward":
        bot.backward(float(param))
    elif cmd == "stop":
        bot.stop()
    elif cmd == "set_handler":
        print "param: " + str(param)
        try:
          handler = int(param) if int(param) >= 0 else None
          cam_h.set_active_handler(handler)
      
        except e:
          print e 

    elif cmd == "say":
        print "say: " + str(param)
	bot.say(param)
        
    return "ok"

"""
@sockets.route('/bot_ws')
def bot_ws(ws):
  while True:
    m = ws.receive()
    print m
    if m == "forward":
      bot.forward()
    if m == "backward":
      bot.backward()
    if m == "left":
      bot.left()
    if m == "right":
      bot.right()
    elif m == "stop":
      bot.stop()

cam_h = camera.CameraHandler.get_instance()

def init():
  cam_h.add_handler(camera.SimpleHandler())
  cam_h.add_handler(signal.SignalHandler(coderbot.CoderBot.get_instance()))
  cam_h.add_handler(logo.LogoHandler("coderdojo-logo.png", coderbot.CoderBot.get_instance()))
  cam_h.set_active_handler(None)
  cam_h.start()

init()
"""

def run_server():
  app.run(host="0.0.0.0", port=8080, use_reloader=False)
