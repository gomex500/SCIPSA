from flask import Blueprint, render_template, request, redirect, make_response
from config.connection import collections
from controllers.login_controller import login, signin
import json

web_auth = Blueprint('web_auth', __name__)

# vista login
@web_auth.route('/')
def login_view():
    return render_template('login.html')

# vista registro
@web_auth.route('/register')
def register_view():
    return render_template('register.html')