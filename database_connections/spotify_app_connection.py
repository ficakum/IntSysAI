from spotdl import Spotdl
import sys
sys.path.append('../')
from config import config

def spotify_app_connect():
    spotdl = Spotdl(client_id=config["SPOTIFY_CLIENT_ID"], client_secret=config["SPOTIFY_CLIENT_SECRET"])