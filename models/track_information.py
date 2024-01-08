from mongoengine import *
import sys
sys.path.append('../')
from constants.constant import ValidatorConstants, ModelConstants

class TrackInformation (DynamicDocument):
    meta={'collection': ModelConstants["TRACK_INFORMATION"]}
    
    name = StringField(required=True)
    author = StringField(required=True)
    genre = StringField()
    externalId = StringField(unique=True)
    duration = FloatField(min_value=ValidatorConstants["TRACK_DURATION_MIN"])
    popularity = FloatField()
    album_id = StringField()
    album_name = StringField()
    album_release_date = StringField()
    playlist_name = StringField()
    playlist_id = StringField()
    playlist_genre = StringField()
    playlist_subgenre = StringField()
    danceability = FloatField(required=True)
    energy = FloatField(required=True)
    key = FloatField(required=True)
    loudness = FloatField(required=True)
    mode = FloatField(required=True)
    speechiness = FloatField(required=True)
    acousticness = FloatField(required=True)
    instrumentalness = FloatField(required=True)
    liveness = FloatField(required=True)
    valence = FloatField(required=True)
    tempo = FloatField(required=True)
    cluster = IntField(default=ValidatorConstants["TRACK_CLUSTER_DEFAULT"])
    audio_link = StringField()
    vocals_link = StringField()
    instrumental_link = StringField()
    album_cover_link = StringField()
