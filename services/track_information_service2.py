import sys
sys.path.append('../')
from repositories.track_information_repository2 import *


def add_song2(name, author, genre, externalId, duration, popularity, album_id, album_name, album_release_date, playlist_name,
         playlist_id, playlist_genre, playlist_subgenre, danceability, energy, key, loudness, mode, speechiness, 
         acousticness, instrumentalness, liveness, valence, tempo, cluster, audio_link, vocals_link, instrumental_link, album_cover_link, has_lyrics):
    
    return add(name, author, genre, externalId, duration, popularity, album_id, album_name, album_release_date, playlist_name,
         playlist_id, playlist_genre, playlist_subgenre, danceability, energy, key, loudness, mode, speechiness, 
         acousticness, instrumentalness, liveness, valence, tempo, cluster, audio_link, vocals_link, instrumental_link, album_cover_link, has_lyrics)
