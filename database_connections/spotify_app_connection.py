from spotdl import Spotdl
import sys
sys.path.append('../')
from config import config

def spotify_app_connect():
    try:
        spotdl = Spotdl(client_id=config["SPOTIFY_CLIENT_ID"], client_secret=config["SPOTIFY_CLIENT_SECRET"])

        print("Spotify app: Connecting successful")
        
    except Exception as e:
        print("Spotify app - Error connecting: " + str(e))