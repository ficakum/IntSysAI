import sys
sys.path.append('../')
from repositories.user_repository2 import *


def add_user2(userName, email, password, songList):
    return add(userName, email, password, songList)

def update_user2(user, group):
    update(user, group)