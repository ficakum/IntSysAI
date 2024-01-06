import os
import pandas as pd
import numpy as np
from spotdl import Song
from spotdl import Downloader


def download_song(song_name, dst_folder):
    downloader = Downloader()

    song = Song.from_search_term(song_name)
    downloader.download_song(song)

    file_name = song.display_name
    print(f"{file_name} downloaded")

    dir_name = dst_folder + file_name
    os.mkdir(dir_name)

    curr_dir = os.getcwd()
    curr_loc = f"{os.path.join(curr_dir, file_name)}.mp3"
    new_loc = f"{os.path.join(curr_dir, dir_name, file_name)}.mp3"

    os.rename(curr_loc, new_loc)

    return new_loc, file_name + ".mp3"