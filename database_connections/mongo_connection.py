from mongoengine import *
from mongoengine.connection import disconnect
import sys
sys.path.append('../')
from config import config

def mongo_db_connect():
    try:
        con = connect(host=config["MONGODB_CONNECTION"] + config["MONGODB_NAME"])
        db = con.get_database(config["MONGODB_NAME"])

        print("Mongo: Connecting successful")

        return db
    
    except Exception as e:
        print("Mongo - Error connecting: " + str(e))

def mongo_db_disconnect():
    disconnect()