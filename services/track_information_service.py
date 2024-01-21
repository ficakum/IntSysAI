import pandas as pd
from statistics import mode
import random
import sys
sys.path.append('../')
from k_means.preprocess_song_dataset import prepare_dataset 
from repositories.track_information_repository import *
from k_means.song_k_means import train, predict


def get_all_songs():
    tracks = get_all()

    return tracks

def load_from_csv(csv_file, sample_size):
    df = pd.read_csv(csv_file)
    df = prepare_dataset(df).reset_index(drop=True)

    indexes = list(df.index)
    indexes = random.sample(indexes, sample_size)

    for i in indexes:         
        add(df.loc[i, "track_name"], df.loc[i, "track_artist"], df.loc[i, "playlist_genre"], df.loc[i, "track_id"],
            df.loc[i, "duration_ms"], df.loc[i, "track_popularity"], df.loc[i, "track_album_id"], df.loc[i, "track_album_name"],
            df.loc[i, "track_album_release_date"], df.loc[i, "playlist_name"], df.loc[i, "playlist_id"],
            df.loc[i, "playlist_genre"], df.loc[i, "playlist_subgenre"], df.loc[i, "danceability"], df.loc[i, "energy"],
            df.loc[i, "key"], df.loc[i, "loudness"], df.loc[i, "mode"], df.loc[i, "speechiness"],
            df.loc[i, "acousticness"], df.loc[i, "instrumentalness"], df.loc[i, "liveness"], df.loc[i, "valence"],
            df.loc[i, "tempo"])

def create_song_k_means_model(model_path):
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
    update_cluster(track, cluster)

    return cluster

def get_song_recommendations(playlist, num):
    clusters = [track.cluster for track in playlist]

    favorite_cluster = mode(clusters)
    recommendations = get_by_cluster(favorite_cluster, num)
    
    return recommendations

def update_audio_links(track, audio_link, vocals_link, instrumental_link):
    update_links(track, audio_link, vocals_link, instrumental_link)

def update_img_link(track, img_link):
    update_album_cover_link(track, img_link)

def update_lyrics(track, value):
    update_has_lyrics(track, value)

def get_random_song_recommendations(num):
    track_ids = [group.id for group in get_all()]
    random_ids = random.sample(track_ids, num)
    recommendations = get_by_ids(random_ids)

    return recommendations
