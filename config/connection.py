from http import client
from pymongo import MongoClient
from config.config import MONGO_URI

###inicializando conexion a base datos
client = MongoClient(MONGO_URI)
db = client['SCIPSA']

##funcion para obtener una collection
def collections(collection):
    collection = db[collection]
    return collection