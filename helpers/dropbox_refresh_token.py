import webbrowser
import base64
import requests
import json

import sys
sys.path.append('../')
from config import config

def get_access_code():
    APP_KEY = config["DROPBOX_APP_KEY"]
    url = f'https://www.dropbox.com/oauth2/authorize?client_id={APP_KEY}&' \
          f'response_type=code&token_access_type=offline'

    webbrowser.open(url)


def get_refresh_token():
    APP_KEY = config["DROPBOX_APP_KEY"]
    APP_SECRET = config["DROPBOX_APP_SECRET"]
    ACCESS_CODE_GENERATED = config["DROPBOX_ACCESS_CODE_GENERATED"]

    BASIC_AUTH = base64.b64encode(f'{APP_KEY}:{APP_SECRET}'.encode())

    headers = {
        'Authorization': f"Basic {BASIC_AUTH}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = f'code={ACCESS_CODE_GENERATED}&grant_type=authorization_code'

    response = requests.post('https://api.dropboxapi.com/oauth2/token',
                            data=data,
                            auth=(APP_KEY, APP_SECRET))
    
    print(json.dumps(json.loads(response.text), indent=2))