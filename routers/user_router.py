from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from config.connection import collections
from controllers.user_controller import (
    obtener_usuarios,
    obtener_usuario
)

#inicializando rutas de usuario
user_routes = Blueprint('user_routes', __name__)

#validacion de token
@user_routes.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"message": "No autorizado"}), 401


#ruta mostrar usuarios
@user_routes.route('/users', methods=['GET'])
def obtener_usuarios_ruta():
    return obtener_usuarios(collections('usuarios'))

#ruta mostrar usuario
@user_routes.route('/user/<id>', methods=['GET'])
def obtener_usuario_ruta(id):
    return obtener_usuario(collections('usuarios'), id)