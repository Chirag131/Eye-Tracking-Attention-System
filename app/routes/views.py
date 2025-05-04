from flask import Blueprint,render_template,url_for,request
from ..models import *
from .. import db

views = Blueprint('views' , __name__)

@views.route('/')
def index():
    return "<h1>HI</h1>"