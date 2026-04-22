from datetime import datetime

##modelo de objeto usuario
class UserModel:
    def __init__(self, data):
        self.userName = data.get('userName', '')
        self.nombre = data.get('nombre', '')
        self.apellido = data.get('apellido', '')
        self.email = data.get('email', '')
        self.password = data.get('password', '')
        self.telefono = data.get('telefono', '')
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())