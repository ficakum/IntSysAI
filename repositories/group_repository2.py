import sys
sys.path.append('../')
from models.group2 import Group

def add(groupName, maxMembers, membersNum, cluster): 
    try:   
        group = Group(
            groupName=groupName,
            maxMembers=maxMembers,
            membersNum=membersNum,
            cluster=cluster, 
            )
                
        group.save()

        return group

    except Exception as e:
        print('Group - Error adding: ' + str(e))


def update(group, currentTrack):
    try:
        group.currentTrack = currentTrack
        group.save()

    except Exception as e:
        print('Group - Error updating current track: ' + str(e))