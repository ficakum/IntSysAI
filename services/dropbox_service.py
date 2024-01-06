import sys
sys.path.append('../')
from repositories.dropbox_repository import *
from audio.download_songs import download_song

    
def get_dropbox_link(dbx, dropbox_file_path):
    link = dropbox_get_link(dbx, dropbox_file_path)

    print(link)

def download_spotify_song(dbx, song_name, dst_folder, dropbox_folder_path):
    local_file_path, file_name = download_song(song_name, dst_folder)

    _, dropbox_file_path = dropbox_upload_file(dbx, file_name, local_file_path, dropbox_folder_path)

    file_link = dropbox_get_link(dbx, dropbox_file_path)

    return file_link



    

