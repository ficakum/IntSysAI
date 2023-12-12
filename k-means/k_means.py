import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def load_data(csv_file):
    tracks_df = pd.read_csv(csv_file)

    # reduced_df = tracks_df[:1000]
    # pd.plotting.scatter_matrix(reduced_df[['danceability', 'instrumentalness', 'energy', 'tempo', 'valence']], figsize=(10, 10))
    # plt.show()
    # print(tracks_df[['danceability', 'instrumentalness', 'energy', 'tempo', 'valence']].corr())

    return tracks_df


def gen_result(tracks_df, dst_file):
    model = KMeans(n_clusters=5, n_init=10)
    model.fit(tracks_df[['danceability', 'instrumentalness', 'energy', 'tempo', 'valence']])

    # print(model.labels_[:10], '\n\n', min(model.labels_), max(model.labels_))
    tracks_df['type'] = model.labels_
    # print(tracks_df.head(10))

    tracks_df.to_csv(dst_file)


def recommend_songs(tracks_df, playlist):
    user_favorite_cluster = int(playlist.mode().loc[0]['type'])
    print(f'\nFavorite cluster: {user_favorite_cluster}\n')

    tracks_df = tracks_df[tracks_df.track_popularity > 70]
    suggestions = tracks_df[tracks_df.type == user_favorite_cluster]

    print(suggestions.head())


if __name__ == "__main__":
    # tracks = load_data('../dataset/spotify_songs.csv')
    # gen_result(tracks, 'result.csv')

    tracks = load_data('result.csv')  
    ids = ['0r7CVbZTWZgbTCYdfa2P31', '2I4jAMEOEUQD5V1byYCqNS', '6fvbl9D9VjMtLRQsuWPyYt', '06Pvy98db25O7wlfFFFIRM', '0WfKDYeUAoLA3vdvLKKWMW']
    favorites = tracks[tracks.track_id.isin(ids)]
    recommend_songs(tracks, playlist=favorites)



