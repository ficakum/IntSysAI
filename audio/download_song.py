import os
import requests
from spotdl import Song
from spotdl import Downloader
import sys
sys.path.append('../')
from config import conf


def download_song(song_name, dst_folder):
    try:
        downloader = Downloader()
        song = Song.from_search_term(song_name)
        downloader.download_song(song)

        curr_dir = os.getcwd()
        files = [file for file in os.listdir(curr_dir) if file.endswith(".mp3")]
        file_name = files[0]

        curr_loc = os.path.join(curr_dir, file_name)
        new_loc = os.path.join(curr_dir, dst_folder, conf["AUDIO_FILE_NAME"])

        if os.path.exists(new_loc):
            os.remove(new_loc)
        os.rename(curr_loc, new_loc)

        print(f"{file_name} downloaded")

        return conf["AUDIO_FILE_NAME"]
    
    except Exception as e:
        print('Spodl - Error downloading song: ' + str(e))


def download_album_cover_img(sp, track_id, dst_folder):
    try:
        track_info = sp.track(track_id)
        album_info = track_info["album"]
        images = album_info["images"]
        image = images[0]

        img_data = requests.get(image["url"]).content
       
        new_loc = os.path.join(dst_folder, conf["ALBUM_IMG_NAME"])
        if os.path.exists(new_loc):
            os.remove(new_loc)

        with open(new_loc, 'wb') as handler:
            handler.write(img_data)

        print("Album cover downloaded")

        return conf["ALBUM_IMG_NAME"]
    
    except Exception as e:
        print('Spotipy - Error downloading cover image: ' + str(e))