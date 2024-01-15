import sys
sys.path.append('../') 
from repositories.user_repository import *

def get_all_users():
    groups = get_all()

    return groups

def get_listened_songs(id):
    playlist = get_songs(id)

    return playlist