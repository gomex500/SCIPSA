from decouple import config

##configurando variables de entorno
DEBUG = True  # O False, dependiendo de tu necesidad
PORT = 5000   # O el puerto que estés utilizando
MONGO_URI = config('MONGO_URI')
SECRET_KEY = config('SECRET_KEY')