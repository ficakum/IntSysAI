from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
import os
from config import config
from database_connections.mongo_connection import *
from database_connections.dropbox_connection import dropbox_connect
from database_connections.spotify_app_connection import spotify_app_connect
from database_connections.spotify_api_connection import spotify_api_connect
from services.track_information_service import *
from services.song_service import *
from services.lyrics_service import *


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


@app.route('/create_recommendation_model', methods=['PUT'])
def create_recommendation_model():
    create_k_means_model(config["K_MEANS_MODEL_PATH"])

    return "K-means model created."

@app.route('/predict_cluster/<track_info_id>', methods=['PUT'])
def predict_cluster(track_info_id):
    cluster = predict_track_cluster(track_info_id, config["K_MEANS_MODEL_PATH"])
    resp = {"cluster": int(cluster)}

    return resp

@app.route('/recommendations/<group_id>', methods=['GET'])
def recommendations(group_id):
    recommended_tracks = get_recommendations(group_id, config["RECOMMENDATIONS_NUM"])
    resp = recommended_tracks.to_json()

    return resp

@app.route('/lyrics/<track_info_id>', methods=['GET'])
def lyrics(track_info_id):
    lyr = get_song_lyrics(track_info_id)
    resp = lyr.to_json()

    return resp

@app.route('/load_dataset/<sample_size>', methods=['POST'])
def load_dataset(sample_size):
    load_from_csv(config["DATASET_PATH"], int(sample_size))

    return "Dataset loaded."

@app.route('/download_album_imgs', methods=['PUT'])
def download_album_imgs():
    songs = get_all_songs()

    for song in songs:
        img_link = download_cover_img(dbx, sp, song, config["SONGS_FOLDER_PATH"], config["DROPBOX_SONGS_FOLDER_PATH"])
        update_img_link(song, img_link)

    return "Album images downloaded."

@app.route('/download_songs', methods=['PUT'])
def download_songs():
    curr_dir = os.getcwd()
    venv_python = curr_dir + config["SPLEETER_VENV"]
    script = curr_dir + config["EXTRACT_VOCALS_SCRIPT"]

    songs = get_all_songs()

    for song in songs:
        download_spotify_song(song, config["SONGS_FOLDER_PATH"], venv_python, script)
        
        audio_link, vocals_link, instrumental_link = upload_to_dropbox(dbx, song, config["SONGS_FOLDER_PATH"], config["DROPBOX_SONGS_FOLDER_PATH"])
        update_audio_links(song, audio_link, vocals_link, instrumental_link)
        print(song.to_json())
        
        lyrics_dict = download_lyrics(config["SONGS_FOLDER_PATH"])
        add_song_lyrics(song, lyrics_dict)

    return "Songs downloaded."


if __name__ == "__main__":
    db = mongo_db_connect() 
    dbx = dropbox_connect()
    spotify_app_connect()
    sp = spotify_api_connect()
    
    app.run(host=config["HOST"], port=int(config["PORT"]))   
     