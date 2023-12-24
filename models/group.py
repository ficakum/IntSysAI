from mongoengine import *
from models.track import Track
from ..constants.constant import ValidatorConstants, ModelConstants

class Group (Document):
    meta={'collection': ModelConstants["GROUP"]}

    groupName = StringField(required=True, min_length=ValidatorConstants["GROUP_NAME_MIN"],
                             max_length=ValidatorConstants["GROUP_NAME_MAX"])
    currentTrack = ReferenceField(Track)
    maxMembers = IntField(default=ValidatorConstants["GROUP_MAX_MEMBERS_DEFAULT"], 
                          max_value=ValidatorConstants["GROUP_MAX_MEMBERS"])
    membersNum = IntField(default=ValidatorConstants["GROUP_MEMBERS_NUM_DEFAULT"])