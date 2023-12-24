from mongoengine import *
from models.track_information import TrackInformation
from models.group import Group
from ..constants.constant import ModelConstants

class Track (Document):
    meta={'collection': ModelConstants["TRACK"]}

    trackInformation = ReferenceField(TrackInformation)
    startTime: DateTimeField
    group: ReferenceField(Group)
    state: StringField()