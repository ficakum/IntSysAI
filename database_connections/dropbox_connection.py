import dropbox
from dropbox.exceptions import AuthError

import sys
sys.path.append('../')
from config import config


def dropbox_connect():
    """Create a connection to Dropbox."""

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
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx