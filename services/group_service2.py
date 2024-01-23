import sys
sys.path.append('../')
from repositories.group_repository2 import *


def add_group2(groupName, maxMembers, membersNum, cluster):
    return add(groupName, maxMembers, membersNum, cluster)

def update_curr_track(group, currentTrack):
    update(group, currentTrack)