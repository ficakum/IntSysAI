from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
import os
from config import conf
from database_connections.mongo_connection import *
from database_connections.dropbox_connection import dropbox_connect
from database_connections.spotify_app_connection import spotify_app_connect
from database_connections.spotify_api_connection import spotify_api_connect
from services.track_information_service import *
from services.group_service import *
from services.user_service import *
from services.dropbox_service import *
from services.lyrics_service import *
from services.track_service import *
from services.track_information_service2 import *
from services.user_service2 import *
from services.group_service2 import *
from services.lyrics_service2 import *
from services.track_service2 import *


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


@app.route('/create_song_recommendation_model', methods=['PUT'])
def create_song_recommendation_model():
    create_song_k_means_model(conf["SONG_K_MEANS_MODEL_PATH"])

    return "Song K-means model created."

@app.route('/predict_song_cluster/<track_info_id>', methods=['PUT'])
def predict_song_cluster(track_info_id):
    cluster = predict_track_cluster(track_info_id, conf["SONG_K_MEANS_MODEL_PATH"])
    resp = {"cluster": int(cluster)}

    return resp

@app.route('/song_recommendations/<group_id>', methods=['GET'])
def song_recommendations(group_id):
    playlist = get_group_playlist(group_id)
    if len(playlist) > 0:
        recommended_tracks = get_song_recommendations(playlist, conf["RECOMMENDATIONS_NUM"])
    else:
        recommended_tracks = get_random_song_recommendations(conf["RECOMMENDATIONS_NUM"])
    resp = recommended_tracks.to_json()

    return resp

@app.route('/create_group_recommendation_model', methods=['PUT'])
def create_group_recommendation_model():
    create_group_k_means_model(conf["GROUP_K_MEANS_MODEL_PATH"])

    return "Group K-means model created."

@app.route('/predict_group_cluster/<group_id>', methods=['PUT'])
def predict_group_cluster(group_id):
    cluster = predict_cluster_for_group(group_id, conf["GROUP_K_MEANS_MODEL_PATH"])
    resp = {"cluster": int(cluster)}

    return resp

@app.route('/group_recommendations/<user_id>', methods=['GET'])
def group_recommendations(user_id):
    user_playlist = get_listened_songs(user_id)
    if len(user_playlist) > 0:
        recommended_groups = get_group_recommendations(user_playlist, conf["RECOMMENDATIONS_NUM"], conf["GROUP_K_MEANS_MODEL_PATH"])
    else:
        recommended_groups = get_random_group_recommendations(conf["RECOMMENDATIONS_NUM"])
    resp = recommended_groups.to_json()

    return resp

@app.route('/lyrics/<track_info_id>', methods=['GET'])
def lyrics(track_info_id):
    lyr = get_song_lyrics(track_info_id)
    if lyr != None:
        resp = lyr.to_json()
    else:
        resp = ('', 204)

    return resp

@app.route('/load_song_dataset/<sample_size>', methods=['POST'])
def load_song_dataset(sample_size):
    load_from_csv(conf["DATASET_PATH"], int(sample_size))

    return "Dataset loaded."

@app.route('/download_album_imgs', methods=['PUT'])
def download_album_imgs():
    songs = get_all_songs()

    for song in songs:
        img_link = download_cover_img(dbx, sp, song, conf["SONGS_FOLDER_PATH"], conf["DROPBOX_SONGS_FOLDER_PATH"])
        update_img_link(song, img_link)

    return "Album images downloaded."

@app.route('/download_songs', methods=['PUT'])
def download_songs():
    curr_dir = os.getcwd()
    venv_python = curr_dir + conf["SPLEETER_VENV"]
    script = curr_dir + conf["EXTRACT_VOCALS_SCRIPT"]

    songs = get_all_songs()

    for song in songs:
        download_spotify_song(song, conf["SONGS_FOLDER_PATH"], venv_python, script)
        
        audio_link, vocals_link, instrumental_link = upload_to_dropbox(dbx, song, conf["SONGS_FOLDER_PATH"], conf["DROPBOX_SONGS_FOLDER_PATH"])
        update_audio_links(song, audio_link, vocals_link, instrumental_link)
        print(song.to_json())
        
        lyrics_dict = download_lyrics(conf["SONGS_FOLDER_PATH"])
        add_song_lyrics(song, lyrics_dict)
        update_lyrics(song, True)

    return "Songs downloaded."

def transfer():
    songs = get_all_songs()
    new_songs = dict()
    for i, song in enumerate(songs):
        new_song = add_song2(song.name, song.author, song.genre, song.externalId, song.duration, song.popularity, song.album_id, song.album_name, song.album_release_date, song.playlist_name,
            song.playlist_id, song.playlist_genre, song.playlist_subgenre, song.danceability, song.energy, song.key, song.loudness, song.mode, song.speechiness, 
            song.acousticness, song.instrumentalness, song.liveness, song.valence, song.tempo, song.cluster, song.audio_link, song.vocals_link, song.instrumental_link, song.album_cover_link, song.has_lyrics)
    
        if song.has_lyrics:
            lyr = get_song_lyrics(song.id)
            add_lyrics2(lyr.text, lyr.segments, lyr.language, lyr.language_probs, new_song)
        new_songs[song.id] = new_song

    users = get_all_users()
    new_users = dict()
    for i, user in enumerate(users):
        songs_list = user.songList
        songs_list_new = []
        for s in songs_list:
            songs_list_new.append(new_songs[s.id])
        new_user = add_user2(user.userName, user.email, user.password, songs_list_new)
        new_users[user.id] = new_user

    tracks = get_all_tracks()
    new_tracks = dict()
    for i, track in enumerate(tracks):
        new_track = add_track2(new_songs[track.trackInformation.id], track.startTime, track.state)
        new_tracks[track.id] = new_track

    groups = get_all_groups()
    new_groups = dict()
    for i, group in enumerate(groups):
        new_group = add_group2(group.groupName, group.maxMembers, group.membersNum, group.cluster)
        if group.currentTrack != None:
            update_curr_track(new_group, new_tracks[group.currentTrack].id)
        new_groups[group.id] = new_group

    for i, user in enumerate(users):
        if user.group != None:
            update_user2(new_users[user.id], new_groups[user.group.id])
        
    for i, track in enumerate(tracks):
        update_track2(new_tracks[track.id], new_groups[track.group.id])


if __name__ == "__main__":
    db1, db2 = mongo_db_connect() 
    dbx = dropbox_connect()
    spotify_app_connect()
    sp = spotify_api_connect()

    # transfer()

    # app.run(host=conf["HOST"], port=int(conf["PORT"]))   
     