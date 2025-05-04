from flask import Blueprint,render_template,url_for,request,Response
from ..functions.generateFrames import generate_frames
from ..models import *
from .. import db

views = Blueprint('views' , __name__)


@views.route('/')
def index():
    return render_template('index.html')

@views.route('/video')
def video_feed():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


