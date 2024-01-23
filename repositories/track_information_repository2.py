import sys
sys.path.append('../')
from models.track_information2 import TrackInformation

def add(name, author, genre, externalId, duration, popularity, album_id, album_name, album_release_date, playlist_name,
         playlist_id, playlist_genre, playlist_subgenre, danceability, energy, key, loudness, mode, speechiness, 
         acousticness, instrumentalness, liveness, valence, tempo, cluster, audio_link, vocals_link, instrumental_link, album_cover_link, has_lyrics): 
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
            tempo=tempo,
            cluster=cluster,
            audio_link=audio_link,
            vocals_link=vocals_link,
            instrumental_link=instrumental_link,
            album_cover_link=album_cover_link,
            has_lyrics=has_lyrics)
                
        track_info.save()

        return track_info

    except Exception as e:
        print('TRACK_INFORMATION - Error adding: ' + str(e))