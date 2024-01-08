import os
import requests
from spotdl import Song
from spotdl import Downloader


def download_song(song_name, dst_folder):
    try:
        downloader = Downloader()
        song = Song.from_search_term(song_name)
        downloader.download_song(song)

        file_name = song.display_name
        dir_name = dst_folder + file_name
        os.mkdir(dir_name)

        file_name_with_ext = file_name + ".mp3"
        curr_dir = os.getcwd()
        curr_loc = os.path.join(curr_dir, file_name_with_ext)
        new_loc = os.path.join(curr_dir, dir_name, file_name_with_ext)
        os.rename(curr_loc, new_loc)

        print(f"{file_name} downloaded")

        return file_name, file_name_with_ext, new_loc
    
    except Exception as e:
        print('Spodl - Error downloading song: ' + str(e))


def download_cover_img(sp, track_id, dst_folder):
    try:
        track_info = sp.track(track_id)
        album_info = track_info["album"]
        images = album_info["images"]
        image = images[0]

        img_name_with_ext = "cover_img.jpg"
        img_data = requests.get(image["url"]).content
        with open(img_name_with_ext, 'wb') as handler:
            handler.write(img_data)

        curr_dir = os.getcwd()
        curr_loc = os.path.join(curr_dir, img_name_with_ext)
        new_loc = os.path.join(curr_dir, dst_folder, img_name_with_ext)
        os.rename(curr_loc, new_loc)

        print("Album cover downloaded")

        return img_name_with_ext
    
    except Exception as e:
        print('Spotipy - Error downloading song: ' + str(e))