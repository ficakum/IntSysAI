from mongoengine import *
from models.track_information2 import TrackInformation
from models.group2 import Group
import sys
sys.path.append('../')
from constants.constant import ModelConstants

class Track (Document):
    meta={"db_alias": "db2", 'collection': ModelConstants["TRACK"], 'strict': False}

    trackInformation = ReferenceField(TrackInformation)
    startTime = IntField()
    group = ReferenceField(Group)
    state = StringField()