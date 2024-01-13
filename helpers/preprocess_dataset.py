import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def normalize_features(df):
    minmax_scaler = MinMaxScaler(feature_range=(0, 1))
    
    columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
               'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'release_year'] 
    df[columns] = minmax_scaler.fit_transform(df[columns])

    return df

def encode_categorical_features(df):
    df = pd.get_dummies(df, columns = ['playlist_genre'])     

    return df

def prepare_dataset(df):
    df.dropna(inplace=True)

    df.drop_duplicates(subset=['track_id'], keep='first', inplace=True)
    df.drop_duplicates(subset=['track_name'], keep='first', inplace=True)

    # df['track_album_release_date'] = pd.to_datetime(df['track_album_release_date'])

    # years = df["track_album_release_date"].dt.year
    # df["release_year"] = years

    return df

def preprocess(df):
    preprocessed_df = prepare_dataset(df)
    preprocessed_df['track_album_release_date'] = pd.to_datetime(preprocessed_df['track_album_release_date'])
    years = preprocessed_df["track_album_release_date"].dt.year
    preprocessed_df["release_year"] = years
    preprocessed_df = normalize_features(preprocessed_df)
    # preprocessed_df = encode_categorical_features(preprocessed_df)

    columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
               'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'release_year']

    preprocessed_df = preprocessed_df[columns]

    return preprocessed_df
