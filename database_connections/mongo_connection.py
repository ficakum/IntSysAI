from mongoengine import *
from mongoengine.connection import disconnect
import sys
sys.path.append('../')
from config import conf

def mongo_db_connect():
    try:
        # con = connect(host=conf["MONGODB_CONNECTION"] + conf["MONGODB_NAME"])
        # db = con.get_database(conf["MONGODB_NAME"])
        con = connect(host=conf["MONGODB_CONNECTION_LOCAL"] + conf["MONGODB_NAME_LOCAL"])
        db = con.get_database(conf["MONGODB_NAME_LOCAL"])

        print("Mongo: Connecting successful")

        return db
    
    except Exception as e:
        print("Mongo - Error connecting: " + str(e))

def mongo_db_disconnect():
    disconnect()