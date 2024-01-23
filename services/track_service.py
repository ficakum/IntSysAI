import sys
sys.path.append('../')
from repositories.track_repository import *

def get_all_tracks():
    return get_all()

def delete_track(id):
    delete(id)