import requests
import base64
import spotipy
import sys
sys.path.append('../')
from config import conf


def get_access_token():
    client_id = conf["SPOTIFY_CLIENT_ID"]
    client_secret = conf["SPOTIFY_CLIENT_SECRET"]

    client_credentials = f"{client_id}:{client_secret}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    token_url = conf["SPOTIFY_TOKEN_URL"]
    headers = {
        'Authorization': f'Basic {client_credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']

        return access_token
    
    else:
        print("Error obtaining access token.")
        exit()

def spotify_api_connect():
    try:
        access_token = get_access_token()
        sp = spotipy.Spotify(auth=access_token)

        print("Spotify API: Connecting successful")

        return sp
    
    except Exception as e:
        print("Spotify API - Error connecting: " + str(e))
