from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "SPOTIFY_CLIENT_ID": os.getenv("SPOTIFY_CLIENT_ID"),
    "SPOTIFY_CLIENT_SECRET": os.getenv("SPOTIFY_CLIENT_SECRET"),
    "MONGODB_CONNECTION": os.getenv("MONGODB_CONNECTION"),
    "MONGODB_NAME": os.getenv("MONGODB_NAME"), 
    "PORT": os.environ.get("PORT", 5000),
    "HOST": os.getenv("HOST"),
    "SPOTIFY_TOKEN_URL": os.getenv("SPOTIFY_TOKEN_URL"),
    "DROPBOX_APP_KEY": os.getenv("DROPBOX_APP_KEY"),
    "DROPBOX_APP_SECRET": os.getenv("DROPBOX_APP_SECRET"),
    "DROPBOX_ACCESS_CODE_GENERATED": os.getenv("DROPBOX_ACCESS_CODE_GENERATED"),
    "DROPBOX_REFRESH_TOKEN": os.getenv("DROPBOX_REFRESH_TOKEN")
}
