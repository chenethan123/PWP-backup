from flask import Flask, request, jsonify
from adafruit_motorkit import MotorKit
import time
import requests

kit = MotorKit(0x40)
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <h1>Robot Control</h1>
        <button onclick="sendCommand('forward')">Forward</button>
        <button onclick="sendCommand('backward')">Backward</button>
        <button onclick="sendCommand('left')">Left</button>
        <button onclick="sendCommand('right')">Right</button>
        <button onclick="sendCommand('stop')">Stop</button>

        <script>
        function sendCommand(command) {
            fetch('/control', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 'command': command })
            })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
        }
        </script>
    </body>
    </html>
    '''

@app.route('/move', methods=['POST'])
def control():
    command = request.json[command]
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
  print("Move forward")
  kit.motor1.throttle=0.8
  kit.motor2.throttle=-0.8


def backward():
    print("Move backward")
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
    app.run(host='0.0.0.0')
