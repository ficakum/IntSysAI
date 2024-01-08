import sys
import os
import subprocess
sys.path.append('../')
from repositories.dropbox_repository import *
from audio.download_song import download_song, download_cover_img

    
def get_dropbox_link(dbx, dropbox_file_path):
    link = dropbox_get_link(dbx, dropbox_file_path)

    print(link)

def download_spotify_song(dbx, sp, song, local_folder, dropbox_folder, venv, script):
    # download files
    song_folder, audio_file_name, local_audio_file_path = download_song(song.name, local_folder)

    args = [venv, script, local_folder, local_audio_file_path]
    subprocess.run(args)
    vocals_file_name, instrumental_file_name = "vocals.mp3", "accompaniment.mp3"

    local_folder = local_folder + song_folder
    img_file_name = download_cover_img(sp, song.externalId, local_folder)

    # upload files
    dropbox_folder = dropbox_folder + song_folder
    dropbox_audio = dropbox_upload_file(dbx, audio_file_name, local_folder, dropbox_folder)
    dropbox_vocals = dropbox_upload_file(dbx, vocals_file_name, local_folder, dropbox_folder)
    dropbox_instrumental = dropbox_upload_file(dbx, instrumental_file_name, local_folder, dropbox_folder)
    dropbox_img = dropbox_upload_file(dbx, img_file_name, local_folder, dropbox_folder)

    # get links
    audio_link = dropbox_get_link(dbx, dropbox_audio)
    vocals_link = dropbox_get_link(dbx, dropbox_vocals)
    instrumental_link = dropbox_get_link(dbx, dropbox_instrumental)
    img_link = dropbox_get_link(dbx, dropbox_img)

    return audio_link, vocals_link, instrumental_link, img_link
