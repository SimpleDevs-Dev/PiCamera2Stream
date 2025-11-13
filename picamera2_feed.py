from flask import Flask, Response
from picamera2 import Picamera2
import cv2
import argparse

# Set up parser
parser = argparse.ArgumentParser(description="Pipe footage from PiCamera2 to Flask-based local server.")
# Add arguments to server
parser.add_argument("-p", "--port", help="The port you wish to launch the server on. Default=5000", type=int, default=5000)
parser.add_argument('-x', "--size_x", help="The intended width of the camera output. Default=640", type=int, default=640)
parser.add_argument('-y', "--size_y", help="The intended height of the camera output. Default=480", type=int, default=480)
parser.add_argument('-ae', "--auto_exposure", help="Do we want the camera to perform auto-exposure correction? Default=True", type=bool, default=True)
parser.add_argument('-awb', "--auto_white_balance", help="Do we want the camera to auto-select the appropriate white balance? Default=True", type=bool, default=True)
args = parser.parse_args()

# Set up the camera
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format":"XRGB8888", "size":(args.size_x, args.size_y)}))
camera.set_controls({"AeEnable":args.auto_exposure,"AwbEnable":args.auto_white_balance})
camera.start()

app = Flask(__name__)

def generate_frames():
    while True:
            frame = camera.capture_array()
            rotated = cv2.rotate(frame, cv2.ROTATE_180)
            ret, buffer = cv2.imencode('.jpg', rotated)
            frame = buffer.tobytes()
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/picamera2_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ =='__main__':

    #context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    #context.load_cert_chain(certfile='server.crt', keyfile='server.key')
    #app.run(host='0.0.0.0', port=5000, ssl_context=context)
    app.run(host='0.0.0.0', port=args.port)
