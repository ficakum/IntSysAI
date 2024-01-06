import os
import requests
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

    return new_loc, file_name, ".mp3"


def download_cover_img(track_id, audio_file_name, sp, dst_folder):
    track_info = sp.track(track_id)
    album_info = track_info["album"]
    images = album_info["images"]
    image = images[0]
    img = "cover_img"
    img_name = img + ".jpg"

    img_data = requests.get(image["url"]).content
    with open(img_name, 'wb') as handler:
        handler.write(img_data)

    dir_name = dst_folder + audio_file_name
    curr_dir = os.getcwd()
    curr_loc = os.path.join(curr_dir, img_name)
    new_loc = os.path.join(curr_dir, dir_name, img_name)

    os.rename(curr_loc, new_loc)

    return new_loc, img, ".jpg"