from flask import Blueprint,render_template,url_for,request
from ..models import *
from .. import db

auth = Blueprint('auth' , __name__)