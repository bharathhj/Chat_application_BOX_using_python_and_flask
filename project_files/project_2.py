from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Cool_shot'
sio: SocketIO = SocketIO(app)


@app.route('/')
def index():
    return render_template('./ChatAppPage.html')


@sio.on('my event')
def handle_my_custom_event(json):
    print('received something: ' + str(json))
    sio.emit('my response', json)


if __name__ == '__main__':
    sio.run(app, debug=True)
