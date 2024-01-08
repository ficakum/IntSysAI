import dropbox
from dropbox.exceptions import AuthError
import sys
import webbrowser
import base64
import requests
import json
sys.path.append('../')
from config import config


def get_access_code():
    try:
        APP_KEY = config["DROPBOX_APP_KEY"]
        url = f'https://www.dropbox.com/oauth2/authorize?client_id={APP_KEY}&' \
            f'response_type=code&token_access_type=offline'

        webbrowser.open(url)

    except Exception as e:
        print("Dropbox - Error opening authorization page: " + str(e))


def get_refresh_token():
    try:
        APP_KEY = config["DROPBOX_APP_KEY"]
        APP_SECRET = config["DROPBOX_APP_SECRET"]
        ACCESS_CODE_GENERATED = config["DROPBOX_ACCESS_CODE_GENERATED"]

        BASIC_AUTH = base64.b64encode(f'{APP_KEY}:{APP_SECRET}'.encode())

        token_url = config["DROPBOX_TOKEN_URL"]
        headers = {
            'Authorization': f"Basic {BASIC_AUTH}",
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = f'code={ACCESS_CODE_GENERATED}&grant_type=authorization_code'
        response = requests.post(token_url, data=data, auth=(APP_KEY, APP_SECRET), headers=headers)
        
        print("Dropbox refresh token: " + json.dumps(json.loads(response.text), indent=2))

    except Exception as e:
        print("Dropbox - Error getting refresh token: " + str(e))


def dropbox_connect():
    try:
        APP_KEY = config["DROPBOX_APP_KEY"]
        APP_SECRET = config["DROPBOX_APP_SECRET"]
        REFRESH_TOKEN = config["DROPBOX_REFRESH_TOKEN"]
      
        dbx = dropbox.Dropbox(
            app_key = APP_KEY,
            app_secret = APP_SECRET,
            oauth2_refresh_token = REFRESH_TOKEN
        )

        print("Dropbox: Connecting successful")
        
    except AuthError as e:
        print("Dropbox - Error connecting with access token: " + str(e))
        
    return dbx