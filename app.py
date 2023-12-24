from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS

from config import config
from database_connections.mongo_connection import *
from services.track_information_service import *

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

@app.route('/load_dataset', methods=['POST'])
def load_dataset():
    load_from_csv("dataset/spotify_songs.csv")

    return jsonify("Load dataset: Finished")

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


if __name__ == "__main__":
    db_connect() 

    # tracks = get_all()
    # for track in tracks:
    #     print(track.cluster)

    app.run(host=config["HOST"], port=int(config["PORT"]))
    