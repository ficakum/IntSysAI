import sys
sys.path.append('../')
from models.track_information import TrackInformation


def add(name, author, genre, externalId, duration, popularity, album_id, album_name, album_release_date, playlist_name,
         playlist_id, playlist_genre, playlist_subgenre, danceability, energy, key, loudness, mode, speechiness, 
         acousticness, instrumentalness, liveness, valence, tempo): 
    try:   
        track_info = TrackInformation(
            name=name,
            author=author,
            genre=genre,
            externalId=externalId,
            duration=duration, 
            popularity=popularity,
            album_id=album_id,
            album_name=album_name,
            album_release_date=str(album_release_date),
            playlist_name=playlist_name,
            playlist_id=playlist_id,
            playlist_genre=playlist_genre,
            playlist_subgenre=playlist_subgenre,
            danceability=danceability,
            energy=energy,
            key=key,
            loudness=loudness,
            mode=mode,
            speechiness=speechiness,
            acousticness=acousticness,
            instrumentalness=instrumentalness,
            liveness=liveness,
            valence=valence,
            tempo=tempo)
                
        track_info.save()

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

def get_by_cluster(cluster, num):
    try:
        tracks = TrackInformation.objects.filter(cluster=cluster).limit(num)
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

def get_columns():
    return ['_id', 'track_name', 'track_artist', 'playlist_genre', 'track_id', 'duration_ms', 'track_popularity',
                         'track_album_id', 'track_album_name', 'track_album_release_date', 'playlist_name', 'playlist_id',
                         'playlist_genre', 'playlist_subgenre', 'danceability', 'energy', 'key', 'loudness', 'mode',
                         'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'cluster', 'audio_link',
                         'vocals_link', 'instrumental_link', 'album_cover_link']
