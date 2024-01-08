import pandas as pd
from statistics import mode
import sys
sys.path.append('../')
from models.track_information import TrackInformation
from helpers.preprocess_dataset import preprocess 
from repositories.track_information_repository import *
from k_means.k_means import train 


def load_from_csv(csv_file):
    tracks_df = pd.read_csv(csv_file)
    tracks_df = preprocess(tracks_df).reset_index(drop=True)

    for i in tracks_df.index:
        track_info = TrackInformation(
            name=tracks_df.loc[i, "track_name"],
            author=tracks_df.loc[i, "track_artist"],
            genre=tracks_df.loc[i, "playlist_genre"],
            externalId=tracks_df.loc[i, "track_id"],
            duration=tracks_df.loc[i, "duration_ms"], 
            popularity=tracks_df.loc[i, "track_popularity"],
            album_id=tracks_df.loc[i, "track_album_id"],
            album_name=tracks_df.loc[i, "track_album_name"],
            album_release_date=str(tracks_df.loc[i, "track_album_release_date"]),
            playlist_name=tracks_df.loc[i, "playlist_name"],
            playlist_id=tracks_df.loc[i, "playlist_id"],
            playlist_genre=tracks_df.loc[i, "playlist_genre"],
            playlist_subgenre=tracks_df.loc[i, "playlist_subgenre"],
            danceability=tracks_df.loc[i, "danceability"],
            energy=tracks_df.loc[i, "energy"],
            key=tracks_df.loc[i, "key"],
            loudness=tracks_df.loc[i, "loudness"],
            mode=tracks_df.loc[i, "mode"],
            speechiness=tracks_df.loc[i, "speechiness"],
            acousticness=tracks_df.loc[i, "acousticness"],
            instrumentalness=tracks_df.loc[i, "instrumentalness"],
            liveness=tracks_df.loc[i, "liveness"],
            valence=tracks_df.loc[i, "valence"],
            tempo=tracks_df.loc[i, "tempo"])
        
        add(track_info)

def create_recommendation_model():
    tracks = get_all()

    tracks_df = pd.DataFrame.from_records([track.to_mongo() for track in tracks])
    tracks_df.columns = ['_id', 'track_name', 'track_artist', 'playlist_genre', 'track_id', 'duration_ms', 'track_popularity',
                         'track_album_id', 'track_album_name', 'track_album_release_date', 'playlist_name', 'playlist_id',
                         'playlist_genre', 'playlist_subgenre', 'danceability', 'energy', 'key', 'loudness', 'mode',
                         'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'cluster']

    print(tracks_df.info())

    clusters = train(tracks_df)

    for i, cluster in enumerate(clusters):
        update_cluster(tracks[i], cluster)


def get_recommendations():
    listened_tracks_ids = ['0r7CVbZTWZgbTCYdfa2P31', '2I4jAMEOEUQD5V1byYCqNS', '6fvbl9D9VjMtLRQsuWPyYt', 
           '06Pvy98db25O7wlfFFFIRM', '0WfKDYeUAoLA3vdvLKKWMW']
    
    listened_tracks = get_by_spotify_ids(listened_tracks_ids)
    clusters = [track.cluster for track in listened_tracks]

    favorite_cluster = mode(clusters)
    print(f'Favorite cluster: {favorite_cluster}')

    recommendations = get_by_cluster(favorite_cluster)
    
    return recommendations

def update_song_links(track, audio_link, vocals_link, instrumental_link, img_link):
    update_links(track, audio_link, vocals_link, instrumental_link, img_link)

def get_random_song():
    tracks = get_all()
    track = tracks[105]

    return track
    



