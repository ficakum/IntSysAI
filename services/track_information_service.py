import pandas as pd
from statistics import mode
import sys
sys.path.append('../')
from helpers.preprocess_dataset import preprocess 
from repositories.track_information_repository import *
from k_means.k_means import train, predict


def load_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    df = preprocess(df).reset_index(drop=True)

    for i in df.index:         
        add(df.loc[i, "track_name"], df.loc[i, "track_artist"], df.loc[i, "playlist_genre"], df.loc[i, "track_id"],
            df.loc[i, "duration_ms"], df.loc[i, "track_popularity"], df.loc[i, "track_album_id"], df.loc[i, "track_album_name"],
            df.loc[i, "track_album_release_date"], df.loc[i, "playlist_name"], df.loc[i, "playlist_id"],
            df.loc[i, "playlist_genre"], df.loc[i, "playlist_subgenre"], df.loc[i, "danceability"], df.loc[i, "energy"],
            df.loc[i, "key"], df.loc[i, "loudness"], df.loc[i, "mode"], df.loc[i, "speechiness"],
            df.loc[i, "acousticness"], df.loc[i, "instrumentalness"], df.loc[i, "liveness"], df.loc[i, "valence"],
            df.loc[i, "tempo"])

def create_k_means_model(model_path):
    tracks = get_all()

    tracks_df = pd.DataFrame.from_records([track.to_mongo() for track in tracks])
    tracks_df.columns = get_columns()
    tracks_df.drop(["audio_link", "vocals_link", "instrumental_link", "album_cover_link"], axis=1, inplace=True)

    clusters = train(tracks_df, model_path)

    for i, cluster in enumerate(clusters):
        update_cluster(tracks[i], cluster)

def predict_track_cluster(track_info_id, model_path):
    track = get_by_id(track_info_id)

    track_df = pd.DataFrame.from_records([track.to_mongo()])
    track_df.columns = get_columns()
    track_df.drop(["audio_link", "vocals_link", "instrumental_link", "album_cover_link"], axis=1, inplace=True)

    cluster = predict(track_df, model_path)[0]
    update_cluster(track_info_id, cluster)

    return cluster

def get_recommendations(num):
    listened_tracks_ids = ['0r7CVbZTWZgbTCYdfa2P31', '2I4jAMEOEUQD5V1byYCqNS', '6fvbl9D9VjMtLRQsuWPyYt', 
           '06Pvy98db25O7wlfFFFIRM', '0WfKDYeUAoLA3vdvLKKWMW']
    
    listened_tracks = get_by_spotify_ids(listened_tracks_ids)
    clusters = [track.cluster for track in listened_tracks]

    favorite_cluster = mode(clusters)
    print(f'Favorite cluster: {favorite_cluster}')

    recommendations = get_by_cluster(favorite_cluster, num)
    
    return recommendations

def update_song_links(track, audio_link, vocals_link, instrumental_link, img_link):
    update_links(track, audio_link, vocals_link, instrumental_link, img_link)

def get_random_song():
    tracks = get_all()
    track = tracks[101]

    return track
