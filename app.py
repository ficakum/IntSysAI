from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS

from config import config
from database_connections.mongo_connection import *
from database_connections.dropbox_connection import dropbox_connect
from database_connections.spotify_app_connection import spotify_app_connect
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
    # for track in recommended_tracks:
    #     print(track.name)
    resp = recommended_tracks.to_json()

    return resp

@app.route('/dropbox_files', methods=['GET'])
def dropbox_files():
    files = list_all_files(dbx, "/" + request.args.get('folder'))
    resp = files.to_json()

    return resp


if __name__ == "__main__":
    mongo_db_connect() 
    dbx = dropbox_connect()
    spotify_app_connect()

    song = get_random_song()
    song_link = download_spotify_song(dbx, song.name, "./dataset/songs/", "/songs/")
    update_song_link(song, song_link)

    song = get_random_song()
    print(song.to_json())

    # app.run(host=config["HOST"], port=int(config["PORT"]))
    