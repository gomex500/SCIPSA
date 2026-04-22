from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from models.User import UserModel
from controllers.jwt import crear_token
import json
import bcrypt

#controlador mostrar usuarios
def obtener_usuarios(collections):
    try:
        users = []
        for doc in collections.find():
            user = UserModel(doc).__dict__
            user['_id'] = str(doc['_id'])
            # Evitar agregar la contraseña a la lista de usuarios
            user.pop('password', None)
            users.append(user)

        return jsonify(users)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar usuario
def obtener_usuario(collections, id):
    try:
        doc = collections.find_one({'_id': ObjectId(id)})
        user_data = UserModel(doc).__dict__
        user_data['_id'] = str(doc['_id'])
        return jsonify(user_data)
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response