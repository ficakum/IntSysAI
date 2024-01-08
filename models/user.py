from mongoengine import *
from models.group import Group
import sys
sys.path.append('../')
from constants.constant import ValidatorConstants, ModelConstants

class User (Document):
    meta={'collection': ModelConstants["USER"]}

    userName = StringField(required=True, unique=True, min_length=ValidatorConstants["USER_NAME_MIN"], 
                           max_length=ValidatorConstants["USER_NAME_MAX"])
    email = StringField(required=True, unique=True)
    password = StringField()
    group: ReferenceField(Group)