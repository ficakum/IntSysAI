import sys
import pandas as pd
import random
sys.path.append('../') 
from repositories.group_repository import *
from k_means.group_k_means import train, predict

def get_all_groups():
    groups = get_all()

    return groups

def get_group_playlist(group_id):
    playlist = get_playlist(group_id)

    return playlist

def get_df_from_series(series):
    columns = get_selected_columns()
    result_df = pd.DataFrame(columns=columns)
    result_df.loc[len(result_df.index)] = series.values

    return result_df

def get_playlist_vector(playlist):
    playlist_df = pd.DataFrame.from_records([track.to_mongo() for track in playlist])
    playlist_df.columns = get_columns()

    playlist_df['track_album_release_date'] = pd.to_datetime(playlist_df['track_album_release_date'])
    years = playlist_df["track_album_release_date"].dt.year
    playlist_df["release_year"] = years

    columns = get_selected_columns()
    playlist_df = playlist_df[columns]

    return playlist_df.mean()

def create_group_k_means_model(model_path):
    groups = get_all()

    columns = get_selected_columns()
    result_df = pd.DataFrame(columns=columns)

    for i, group in enumerate(groups):
        playlist = get_playlist(group.id)
        group_mean = get_playlist_vector(playlist)
        result_df.loc[len(result_df.index)] = group_mean.values

    clusters = train(result_df, model_path)

    for i, cluster in enumerate(clusters):
        update_cluster(groups[i], cluster)

def predict_cluster_for_group(group_id, model_path):
    group = get_by_id(group_id)
    playlist = get_playlist(group.id)
    group_mean = get_playlist_vector(playlist)
    result_df = get_df_from_series(group_mean)

    cluster = predict(result_df, model_path)[0]
    update_cluster(group, cluster)

    return cluster

def get_group_recommendations(user_playlist, num, model_path):
    playlist_mean = get_playlist_vector(user_playlist)
    result_df = get_df_from_series(playlist_mean)

    favorite_cluster  = predict(result_df, model_path)[0]
    recommendations = get_by_cluster(favorite_cluster, num)

    return recommendations

def get_random_group_recommendations(num):
    group_ids = [group.id for group in get_all_groups()]
    random_ids = random.sample(group_ids, num)
    recommendations = get_by_ids(random_ids)

    return recommendations