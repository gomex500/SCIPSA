import json
from flask import Blueprint, request, redirect, make_response
from config.connection import collections
from controllers.login_controller import login

web_auth = Blueprint('web_auth', __name__)

@web_auth.route('/login-form', methods=['POST'])
def login_form():

    data = {
        "userName": request.form['userName'],
        "password": request.form['password']
    }

    request._cached_data = json.dumps(data).encode('utf-8')

    response = login(collections('usuarios'))

    if response.status_code != 200:
        return "Usuario o contraseña incorrectos"

    token = response.json.get("token")

    resp = make_response(redirect('/dashboard'))
    resp.set_cookie('token', token)

    return resp


@web_auth.route('/register-form', methods=['POST'])
def register_form():

    data = {
        "userName": request.form['userName'],
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "telefono": request.form['telefono'],
        "password": request.form['password']
    }

    request._cached_data = json.dumps(data).encode('utf-8')

    response = signin(collections('usuarios'))

    if response.status_code != 200:
        return "Error al registrar usuario"

    return redirect('/')