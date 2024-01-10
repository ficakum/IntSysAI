import pandas as pd
import matplotlib.pyplot as plt

from preprocess_dataset import prepare_dataset


def print_dataset_info(df):
    print("\nDataset info:\n")
    print(df.info())

    print(f"\nFirst 5 rows:\n {df.head()}\n")

    print(f"Number of rows in dataset: {len(df)}")
    print(f"Number of duplicates in dataset: {df.duplicated().sum()}")


def print_features_info(df):
    print("\nFeatures info:\n")

    unique_tracks = df["track_id"].nunique()
    print(f"Number of unique track ids: {unique_tracks}")

    unique_track_names = df["track_name"].nunique()
    print(f"Number of unique track names: {unique_track_names}")

    unique_actists = df["track_artist"].nunique()
    print(f"Number of unique artists: {unique_actists}")
 
    unique_albums_ids = df["track_album_id"].nunique()
    print(f"Number of unique album ids: {unique_albums_ids}")

    unique_album_names = df["track_album_name"].nunique()
    print(f"Number of unique album names: {unique_album_names}")

    df['track_album_release_date'] = pd.to_datetime(df['track_album_release_date'])
    years = df["track_album_release_date"].dt.year
    print(f"Number of unique release years: {years.nunique()}")
    print(f"Min year: {min(years)}")
    print(f"Max year: {max(years)}")

    unique_playlist_names = df["playlist_name"].nunique()
    print(f"Number of unique playlist names: {unique_playlist_names}")
    
    unique_playlist_ids = df["playlist_id"].nunique()
    print(f"Number of unique playlist ids: {unique_playlist_ids}")

    unique_genres = df["playlist_genre"].nunique()
    print(f"Number of unique genres: {unique_genres}")

    unique_subgenres = df["playlist_subgenre"].nunique()
    print(f"Number of unique subgenres: {unique_subgenres}")

    unique_keys = df["key"].nunique()
    print(f"Number of unique keys: {unique_keys}")


def visualize_features(df):
    plt.hist(df["track_popularity"])
    plt.xlabel("Popularity")
    plt.ylabel("Number of tracks")
    plt.show()

    df['track_album_release_date'] = pd.to_datetime(df['track_album_release_date'])
    years = df["track_album_release_date"].dt.year
    plt.hist(years)
    plt.xlabel("Year")
    plt.ylabel("Number of tracks")
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.hist(df["playlist_genre"])
    plt.xlabel("Genre")
    plt.ylabel("Number of tracks")
    plt.subplot(1, 2, 2)
    tmp_df = df.pivot_table(columns=['playlist_genre'], aggfunc='size')
    tmp_df.plot.pie(autopct='%1.1f%%')
    plt.show()



if __name__ == "__main__":
    dataset = pd.read_csv("../dataset/spotify_songs.csv")

    print_dataset_info(dataset)
    print_features_info(dataset)
    visualize_features(dataset)

    dataset = prepare_dataset(dataset)

    print_dataset_info(dataset)
    print_features_info(dataset)
    visualize_features(dataset)