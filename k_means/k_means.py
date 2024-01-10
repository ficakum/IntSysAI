import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
from sklearn.metrics import silhouette_score
from joblib import dump, load
pd.options.mode.chained_assignment = None 

import sys
sys.path.append('../')
from helpers.preprocess_dataset import *


def elbow_method(points, kmin, kmax):
    cost = []
    for i in range(kmin, kmax):
        kmeans = KMeans(n_clusters = i, n_init=20)
        kmeans.fit(points)
        
        cost.append(kmeans.inertia_)     
    
    plt.plot(range(kmin, kmax), cost, color ='g', linewidth ='3')
    plt.xlabel("Value of K")
    plt.ylabel("Squared Error (Cost)")
    plt.show() 
    

def silhouette_method(points, kmin, kmax):
    cost = []
    for i in range(kmin, kmax):
        kmeans = KMeans(n_clusters = i, n_init=20)
        kmeans.fit(points)
        
        cost.append(silhouette_score(points, kmeans.labels_, metric = 'euclidean'))
    
    plt.plot(range(kmin, kmax), cost, color ='g', linewidth ='3')
    plt.xlabel("Value of K")
    plt.ylabel("Silhouette score")
    plt.show()


def create_clusters(preprocessed_tracks, k, model_path):
    model = KMeans(n_clusters=k, n_init=20)
    result = model.fit(preprocessed_tracks)

    dump(model, model_path)

    return result.labels_


def train(tracks, model_path):
    preprocessed_tracks = preprocess(tracks)

    # kmin = 5
    # kmax = 20
    # elbow_method(preprocessed_tracks, kmin, kmax)
    # silhouette_method(preprocessed_tracks, kmin, kmax)

    clusters = create_clusters(preprocessed_tracks, 20, model_path)
    
    return clusters


def predict(track, model_path):
    preprocessed_track = preprocess(track)

    model = load(model_path)
    res = model.predict(preprocessed_track)

    return res   
