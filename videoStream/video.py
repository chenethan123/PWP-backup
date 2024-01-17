from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(-1)


def render_template():
    indexHTML = '''<!DOCTYPE html>
<html>


  <body>
    <h1>Live streaming</h1>
<p>
   <center>
       <button onclick="window.location.href = '/video';">Video Stream</button>
   </center>
   </p>


    </body>


</html>'''
    return indexHTML


def generate_frames():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template()


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
