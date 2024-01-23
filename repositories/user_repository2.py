import sys
sys.path.append('../')
from models.user2 import User

def add(userName, email, password, songList): 
    try:   
        user = User(
            userName=userName,
            email=email,
            password=password,
            songList=songList, 
            )
                
        user.save()
        
        return user

    except Exception as e:
        print('User - Error adding: ' + str(e))

def update(user, group):
    try:
        user.group = group
        user.save()

    except Exception as e:
        print('User - Error updating group: ' + str(e))