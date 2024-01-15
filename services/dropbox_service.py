import sys
import subprocess
sys.path.append('../')
from repositories.dropbox_repository import *
from audio.download_song import download_song, download_album_cover_img
from audio.extract_lyrics import get_lyrics
from config import conf


def download_cover_img(dbx, sp, song, local_folder, dropbox_folder):
    img_file_name = download_album_cover_img(sp, song.externalId, local_folder)
    dropbox_folder = dropbox_folder + song.name.replace("/", "-") + " - " + song.author.replace("/", "-").replace("\\", "-")
    dropbox_img = dropbox_upload_file(dbx, img_file_name, local_folder, dropbox_folder)
    img_link = dropbox_get_link(dbx, dropbox_img)

    return img_link

def download_spotify_song(song, local_folder, venv, script):
    audio_file_name = download_song(song.name, local_folder)
    subprocess.run([venv, script, local_folder, local_folder + audio_file_name]) 
    
def upload_to_dropbox(dbx, song, local_folder, dropbox_folder):
    dropbox_folder = dropbox_folder + song.name.replace("/", "-") + " - " + song.author.replace("/", "-").replace("\\", "-")
    dropbox_audio = dropbox_upload_file(dbx, conf["AUDIO_FILE_NAME"], local_folder, dropbox_folder)
    dropbox_vocals = dropbox_upload_file(dbx, conf["VOCALS_FILE_NAME"], local_folder, dropbox_folder)
    dropbox_instrumental = dropbox_upload_file(dbx, conf["ACCOMPANIMENT_FILE_NAME"], local_folder, dropbox_folder)

    audio_link = dropbox_get_link(dbx, dropbox_audio)
    vocals_link = dropbox_get_link(dbx, dropbox_vocals)
    instrumental_link = dropbox_get_link(dbx, dropbox_instrumental)

    return audio_link, vocals_link, instrumental_link

def download_lyrics(local_folder):
    lyrics = get_lyrics(local_folder)

    return lyrics

