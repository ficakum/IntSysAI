import requests
import base64
import spotipy
import os
from dotenv import load_dotenv


def get_access_token():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    client_credentials = f"{client_id}:{client_secret}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {client_credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained successfully.")

        return access_token
    else:
        print("Error obtaining access token.")
        exit()


def get_song_data(track_id, token):
    sp = spotipy.Spotify(auth=token)

    track_info = sp.track(track_id)

    for key, value in track_info.items():
        print(f"{key}: {value}")


if __name__ == '__main__':

    load_dotenv()

    access_token = get_access_token()
    get_song_data('5dy3WUywjZcalTno1io8TQ', access_token)
