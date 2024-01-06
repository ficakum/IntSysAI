import sys
sys.path.append('../')
from models.track_information import TrackInformation


def add(track):    
    track.save()

def get_all():
    tracks = TrackInformation.objects
    return tracks

def get_by_id(id):
    track = TrackInformation.objects.filter(id=id).first()
    return track

def get_by_cluster(cluster):
    tracks = TrackInformation.objects.filter(cluster=cluster).limit(10)
    return tracks

def get_by_spotify_ids(ids):
    tracks = TrackInformation.objects.filter(externalId__in=ids)
    return tracks

def get_and_update(id, cluster):
    track = get_by_id(id)
    track.cluster = cluster
    track.save()

def update(track, cluster):
    track.cluster = cluster
    track.save()

def update_links(track, audio_link, img_link):
    track.audio_link = audio_link
    track.album_cover_link = img_link
    track.save()

def delete(id):
    track = get_by_id(id)
    track.delete()