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
from services.dropbox_service import *


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


@app.route('/create_model', methods=['PUT'])
def create_model():
    create_recommendation_model()

    return jsonify("Create model: Finished")

@app.route('/recommendations', methods=['GET'])
def recommendations():
    recommended_tracks = get_recommendations()
    resp = recommended_tracks.to_json()

    return resp


if __name__ == "__main__":
    db = mongo_db_connect() 
    
    # colls = db.list_collection_names()
    # print(colls)
    # db.drop_collection('Track_Information')

    dbx = dropbox_connect()
    spotify_app_connect()
    sp = spotify_api_connect()

    song = get_random_song()
    curr_dir = os.getcwd()
    venv_python = curr_dir + "/.spleeter_venv/Scripts/python"
    script = curr_dir + "/audio/extract_vocals.py"
    audio_link, vocals_link, instrumental_link, img_link = download_spotify_song(dbx, sp, song, "dataset/songs/", "/songs/", venv_python, script)
    # update_song_links(song, audio_link, vocals_link, instrumental_link, img_link)
    # song = get_random_song()
    # print(song.to_json())

    # app.run(host=config["HOST"], port=int(config["PORT"]))   
     
     