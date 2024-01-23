import sys
sys.path.append('../')
from models.track2 import Track

def add(trackInformation, startTime, state): 
    try:   
        track = Track(
            trackInformation=trackInformation,
            startTime=startTime,
            state=state 
            )
                
        track.save()

        return track

    except Exception as e:
        print('Track - Error adding: ' + str(e))

def update(track, group):
    try:
        track.group = group
        track.save()

    except Exception as e:
        print('Track - Error updating group: ' + str(e))