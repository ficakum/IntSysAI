import requests
import base64
import spotipy
import sys
sys.path.append('../')
from config import config


def get_access_token():
    client_id = config["SPOTIFY_CLIENT_ID"]
    client_secret = config["SPOTIFY_CLIENT_SECRET"]

    client_credentials = f"{client_id}:{client_secret}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    token_url = config["SPOTIFY_TOKEN_URL"]
    headers = {
        'Authorization': f'Basic {client_credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Spotify API: Access token obtained successfully.")

        return access_token
    else:
        print("Error obtaining access token.")
        exit()

def spotify_api_connect():
    access_token = get_access_token()
    sp = spotipy.Spotify(auth=access_token)

    return sp

