import sys
sys.path.append('../')
from models.track import Track

def get_all():
    try:
        track = Track.objects
        return track
    
    except Exception as e:
        print('Track - Error getting all: ' + str(e))

def get_by_id(id):
    try:
        track = Track.objects.filter(id=id).first()
        return track
    
    except Exception as e:
        print('Track - Error getting by id: ' + str(e))

def delete(id):
    try:
        track = get_by_id(id)
        track.delete()

    except Exception as e:
        print('Track - Error deleting: ' + str(e))