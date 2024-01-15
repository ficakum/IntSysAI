import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def normalize_features(df):
    minmax_scaler = MinMaxScaler(feature_range=(0, 1))
    df = minmax_scaler.fit_transform(df)

    return df

def preprocess(df):
    preprocessed_df = normalize_features(df)

    return preprocessed_df
