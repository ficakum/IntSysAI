from mongoengine import *
import sys
sys.path.append('../')
from constants.constant import ModelConstants
from models.track_information2 import TrackInformation

class Lyrics (DynamicDocument):
    meta={"db_alias": "db2", 'collection': ModelConstants["LYRICS"]}

    text = StringField()
    segments = ListField()
    language = StringField() 
    language_probs = DictField()
    track_information = ReferenceField(TrackInformation)
    
 
