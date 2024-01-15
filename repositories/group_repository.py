import sys
sys.path.append('../')
from models.group import Group
from models.track import Track


def get_all():
    try:
        tracks = Group.objects
        return tracks
    
    except Exception as e:
        print('GROUP - Error getting all: ' + str(e))

def get_by_id(id):
    try:
        track = Group.objects.filter(id=id).first()
        return track
    
    except Exception as e:
        print('GROUP - Error getting by id: ' + str(e))

def get_by_cluster(cluster, num):
    try:
        groups = Group.objects.filter(cluster=cluster).limit(num)
        return groups
    
    except Exception as e:
        print('GROUP - Error getting by cluster: ' + str(e))

def get_playlist(group_id):
    try:
        tracks = Track.objects.filter(group=group_id)
        tracks_info = []
        for track in tracks:
            tracks_info.append(track.trackInformation)

        return tracks_info
    
    except Exception as e:
        print('GROUP - Error getting by playlist: ' + str(e))

def update_cluster(group, cluster):
    try:
        group.cluster = cluster
        group.save()

    except Exception as e:
        print('GROUP - Error updating cluster: ' + str(e))

def get_columns():
    return ['_id', 'track_name', 'track_artist', 'playlist_genre', 'track_id', 'duration_ms', 'track_popularity',
                         'track_album_id', 'track_album_name', 'track_album_release_date', 'playlist_name', 'playlist_id',
                         'playlist_genre', 'playlist_subgenre', 'danceability', 'energy', 'key', 'loudness', 'mode',
                         'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'cluster', 'audio_link',
                         'vocals_link', 'instrumental_link', 'album_cover_link']

def get_selected_columns():
    return ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
               'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'release_year']