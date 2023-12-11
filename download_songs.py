from dotenv import load_dotenv
import os
from spotdl import Song
from spotdl import Downloader
from spotdl import Spotdl
import pandas as pd
import numpy as np


if __name__ == '__main__':

    load_dotenv()
    spotdl = Spotdl(client_id=os.getenv("SPOTIFY_CLIENT_ID"), client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"))
    downloader = Downloader()

    data = pd.read_csv("dataset/spotify_songs.csv")
    # print(data.info())
    
    song_names = np.array(data["track_name"])
    song_names = song_names[1:2] 

    for song_name in song_names:
        song = Song.from_search_term(song_name)
        downloader.download_song(song)

        file_name = song.display_name
        print(f"{file_name} downloaded")

        dir_name = f"dataset/songs/{file_name}"
        os.mkdir(dir_name)
        curr_path = os. getcwd()
        print(curr_path)
        os.rename(curr_path + f"/{file_name}" + ".mp3", curr_path + f"/{dir_name}/{file_name}" + ".mp3")
        

