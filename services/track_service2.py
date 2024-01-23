import sys
sys.path.append('../')
from repositories.track_repository2 import *


def add_track2(trackInformation, startTime, state):
    return add(trackInformation, startTime, state)

def update_track2(track, group):
    update(track, group)