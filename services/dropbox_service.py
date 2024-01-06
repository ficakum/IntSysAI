import sys
sys.path.append('../')
from repositories.dropbox_repository import *
from audio.download_songs import download_song, download_cover_img

    
def get_dropbox_link(dbx, dropbox_file_path):
    link = dropbox_get_link(dbx, dropbox_file_path)

    print(link)

def download_spotify_song(dbx, sp, song, dst_folder, dropbox_folder_path):
    local_audio_file_path, audio_file_name, audio_ext = download_song(song.name, dst_folder)
    local_img_file_path, img_file_name, img_ext = download_cover_img(song.externalId, audio_file_name, sp, dst_folder)

    dropbox_folder_path = dropbox_folder_path + audio_file_name

    _, dropbox_audio_file_path = dropbox_upload_file(dbx, audio_file_name, local_audio_file_path, dropbox_folder_path, audio_ext)
    _, dropbox_img_file_path = dropbox_upload_file(dbx, img_file_name, local_img_file_path, dropbox_folder_path, img_ext)

    audio_link = dropbox_get_link(dbx, dropbox_audio_file_path)
    img_link = dropbox_get_link(dbx, dropbox_img_file_path)

    return audio_link, img_link



    

