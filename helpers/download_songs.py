import os
import pandas as pd
import numpy as np
from spotdl import Song
from spotdl import Downloader
from spotdl import Spotdl

import sys
sys.path.append('../')
from config import config


if __name__ == '__main__':

    spotdl = Spotdl(client_id=config["SPOTIFY_CLIENT_ID"], client_secret=config["SPOTIFY_CLIENT_SECRET"])
    downloader = Downloader()

    data = pd.read_csv("../dataset/spotify_songs.csv")
    
    song_names = np.array(data["track_name"])
    song_names = song_names[1728:1729] 

    for song_name in song_names:
        song = Song.from_search_term(song_name)
        downloader.download_song(song)

        file_name = song.display_name
        print(f"{file_name} downloaded")

        dir_name = f"../dataset/songs/{file_name}"
        curr_dir = os.getcwd()

        os.mkdir(dir_name)
        os.rename(f"{os.path.join(curr_dir, file_name)}.mp3", f"{os.path.join(curr_dir, dir_name, file_name)}.mp3")
        