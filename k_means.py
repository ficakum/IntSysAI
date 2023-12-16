import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
from datetime import datetime
import numpy as np
from sklearn.metrics import silhouette_score
pd.options.mode.chained_assignment = None 

from preprocess_dataset import preprocess



def load_data(csv_file):
    tracks_df = pd.read_csv(csv_file)

    return tracks_df



def elbow_method(points, kmin, kmax):
    cost =[]
    for i in range(kmin, kmax):
        kmeans = KMeans(n_clusters = i, n_init=20)
        kmeans.fit(points)
        
        cost.append(kmeans.inertia_)     
    
    plt.plot(range(kmin, kmax), cost, color ='g', linewidth ='3')
    plt.xlabel("Value of K")
    plt.ylabel("Squared Error (Cost)")
    plt.show() 
    

def silhouette_method(points, kmin, kmax):
    cost =[]
    for i in range(kmin, kmax):
        kmeans = KMeans(n_clusters = i, n_init=20)
        kmeans.fit(points)
        
        cost.append(silhouette_score(points, kmeans.labels_, metric = 'euclidean'))
    
    
    plt.plot(range(kmin, kmax), cost, color ='g', linewidth ='3')
    plt.xlabel("Value of K")
    plt.ylabel("Silhouette score")
    plt.show()


def create_clusters(tracks_df, preprocessed_tracks, k, dst_file):
    model = KMeans(n_clusters=k, n_init=20)
    result = model.fit(preprocessed_tracks)

    # save to file
    tracks_df['cluster'] = result.labels_
    tracks_df.to_csv(dst_file, index=False)
    
    # visualize clusters
    # tSNE = TSNE(n_components=2)
    # tSNE_result = tSNE.fit_transform(preprocessed_tracks)

    # sns.scatterplot(x=tSNE_result[:, 0], y=tSNE_result[:, 1], hue=result.labels_, alpha=0.5, s=7)

    plt.show()


def train(csv_path):
    tracks = load_data(csv_path)
    preprocessed_tracks = preprocess(tracks)

    columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
               'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'release_year']

    preprocessed_tracks = preprocessed_tracks[columns]

    # kmin = 5
    # kmax = 20
    # elbow_method(preprocessed_tracks, kmin, kmax)
    # silhouette_method(preprocessed_tracks, kmin, kmax)

    create_clusters(tracks, preprocessed_tracks, 20, 'k_means_result.csv')


def calculate_weighted_popularity(release_date):
    release_date = datetime.strptime(release_date, '%Y-%m-%d')

    time_span = datetime.now() - release_date

    weight = 1 / (time_span.days + 1)

    return weight


def recommend_songs(tracks_df, playlist):
    user_favorite_cluster = int(playlist.mode().loc[0]['cluster'])
    print(f'\nFavorite cluster: {user_favorite_cluster}\n')

    suggestions = tracks_df[tracks_df.cluster == user_favorite_cluster]
    suggestions = suggestions[~suggestions['track_id'].isin(playlist['track_id'])]
    
    # waited_popularities = [calculate_weighted_popularity(suggestions["track_album_release_date"][ind]) 
    #                        for ind in suggestions.index]
    # suggestions["popularity_score"] = waited_popularities
    # suggestions.sort_values('popularity_score', ascending=False, inplace=True)

    print(suggestions.head())



def predict(csv_path):
    tracks = load_data(csv_path)  

    listened_tracks_ids = ['0r7CVbZTWZgbTCYdfa2P31', '2I4jAMEOEUQD5V1byYCqNS', '6fvbl9D9VjMtLRQsuWPyYt', 
           '06Pvy98db25O7wlfFFFIRM', '0WfKDYeUAoLA3vdvLKKWMW']
    listened_tracks = tracks[tracks.track_id.isin(listened_tracks_ids)]

    recommend_songs(tracks, playlist=listened_tracks)


if __name__ == "__main__":
    
    # train('dataset/spotify_songs.csv')

    predict('k_means_result.csv')
   



