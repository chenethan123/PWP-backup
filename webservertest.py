from flask import Flask, request, jsonify
from adafruit_motorkit import MotorKit
import time
import requests

kit = MotorKit(0x40)
app = Flask(__name__)

@app.route('/')


@app.route('/move', methods=['POST'])
def control():
    command = request.json['command']
    if command == 'forward':
        forward()
    elif command == 'backward':
        backward()
    elif command == 'left':
        left(0.9)
    elif command == 'right':
        right(0.85)
    elif command == 'stop':
        stop()
    else:
        return jsonify({'status': 'error', 'message': 'Invalid command'})

    return jsonify({'status': 'success', 'message': 'Command executed'})

def forward():
  kit.motor1.throttle=0.8
  kit.motor2.throttle=-0.8


def backward():
    kit.motor1.throttle = -0.8
    kit.motor2.throttle = 0.8


def left(time):
    kit.motor1.throttle=-0.8
    kit.motor2.throttle=-0.8
    time.sleep(time)
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0
  

def right(time):
    kit.motor1.throttle=0.8
    kit.motor2.throttle=0.8
    time.sleep(time)
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0

def stop():
    kit.motor1.throttle = 0.0
    kit.motor2.throttle = 0.0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
