import sys
sys.path.append('../')
from repositories.dropbox_repository import *
from audio.download_songs import download_song


def list_all_files(dbx, folder_name):
    df = dropbox_list_files(dbx, folder_name)
    print(df)

    return df

def upload_file(dbx, local_path, local_file, dropbox_file_path):
    dropbox_upload_file(dbx, local_path, local_file, dropbox_file_path)
    
def get_dropbox_link(dbx, dropbox_file_path):
    link = dropbox_get_link(dbx, dropbox_file_path)

    print(link)

def download_spotify_song(dbx, song_name, dst_folder, dropbox_folder_path):
    local_file_path, file_name = download_song(song_name, dst_folder)

    upload_file(dbx, file_name, local_file_path, dropbox_folder_path)

