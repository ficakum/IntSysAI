from mongoengine import *
from mongoengine.connection import disconnect

import sys
sys.path.append('../')
from config import config

def mongo_db_connect():
    con = connect(host=config["MONGODB_CONNECTION"] + config["MONGODB_NAME"])
    db = con.get_database(config["MONGODB_NAME"])

    # colls = db.list_collection_names()
    # print(colls)

    # db.drop_collection('Track_Information')

def mongo_db_disconnect():
    disconnect()