import sys
sys.path.append('../')
from repositories.lyrics_repository import *


def add_song_lyrics(track_info, lyrics):
    add_lyrics(track_info, lyrics)

def get_song_lyrics(track_info_id):
    return get_by_track_info_id(track_info_id)

def get_all_lyrics():
    return get_all()