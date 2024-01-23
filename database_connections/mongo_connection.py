from mongoengine import *
from mongoengine.connection import disconnect
import sys
sys.path.append('../')
from config import conf

def mongo_db_connect():
    try:
        con1 = connect(alias='db1', host=conf["MONGODB_CONNECTION"] + conf["MONGODB_NAME"])
        db1 = con1.get_database(conf["MONGODB_NAME"])

        con2 = connect(alias='db2', host="mongodb://localhost:27017/" + "AUDITORIUM")
        db2 = con2.get_database("AUDITORIUM")

        print("Mongo: Connecting successful")

        return db1, db2
    
    except Exception as e:
        print("Mongo - Error connecting: " + str(e))

def mongo_db_disconnect():
    disconnect()