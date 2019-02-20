from flask import Flask
from flask_socketio import SocketIO


app = Flask(
        __name__,
        static_url_path = '',
        static_folder = 'static',
        template_folder = 'templates'
        )

app.config['SECRET_KEY'] = 'kjashf9872i3fhd387wsvjb'
socket = SocketIO(app)

from app.controllers import home, socketio

