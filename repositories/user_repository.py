import sys
sys.path.append('../')
from models.user import User


def get_all():
    try:
        tracks = User.objects
        return tracks
    
    except Exception as e:
        print('USER - Error getting all: ' + str(e))

def get_by_id(id):
    try:
        user = User.objects.filter(id=id).first()
        return user
    
    except Exception as e:
        print('USER - Error getting by id: ' + str(e))

def get_songs(id):
    try:
        user = get_by_id(id)
        print(user.to_json())
        tracks_info = []
        for track in user.songList:
            tracks_info.append(track)

        return tracks_info
    
    except Exception as e:
        print('USER - Error getting by id: ' + str(e))