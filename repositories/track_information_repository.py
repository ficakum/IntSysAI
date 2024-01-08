import sys
sys.path.append('../')
from models.track_information import TrackInformation


def add(track): 
    try:   
        track.save()

    except Exception as e:
        print('TRACK_INFORMATION - Error adding: ' + str(e))

def get_all():
    try:
        tracks = TrackInformation.objects
        return tracks
    
    except Exception as e:
        print('TRACK_INFORMATION - Error getting all: ' + str(e))

def get_by_id(id):
    try:
        track = TrackInformation.objects.filter(id=id).first()
        return track
    
    except Exception as e:
        print('TRACK_INFORMATION - Error getting by id: ' + str(e))

def get_by_cluster(cluster):
    try:
        tracks = TrackInformation.objects.filter(cluster=cluster).limit(10)
        return tracks
    
    except Exception as e:
        print('TRACK_INFORMATION - Error getting by cluster: ' + str(e))

def get_by_spotify_ids(ids):
    try:
        tracks = TrackInformation.objects.filter(externalId__in=ids)
        return tracks
    
    except Exception as e:
        print('TRACK_INFORMATION - Error getting by spotify ids: ' + str(e))

def update_cluster(track, cluster):
    try:
        track.cluster = cluster
        track.save()

    except Exception as e:
        print('TRACK_INFORMATION - Error updating cluster: ' + str(e))

def update_links(track, audio_link, vocals_link, instrumental_link, img_link):
    try:
        track.audio_link = audio_link
        track.vocals_link = vocals_link
        track.instrumental_link = instrumental_link
        track.album_cover_link = img_link
        track.save()
    
    except Exception as e:
        print('TRACK_INFORMATION - Error updating links: ' + str(e))

def delete(id):
    try:
        track = get_by_id(id)
        track.delete()

    except Exception as e:
        print('TRACK_INFORMATION - Error deleting: ' + str(e))