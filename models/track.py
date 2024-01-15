from mongoengine import *
from models.track_information import TrackInformation
from models.group import Group
import sys
sys.path.append('../')
from constants.constant import ModelConstants

class Track (Document):
    meta={'collection': ModelConstants["TRACK"], 'strict': False}

    trackInformation = ReferenceField(TrackInformation)
    startTime = DateTimeField
    group = ReferenceField(Group)
    state = StringField()