from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "HOST": os.getenv("HOST"),
    "PORT": os.environ.get("PORT", 5000),
    "MONGODB_CONNECTION": os.getenv("MONGODB_CONNECTION"),
    "MONGODB_NAME": os.getenv("MONGODB_NAME"),
    "SPOTIFY_CLIENT_ID": os.getenv("SPOTIFY_CLIENT_ID"),
    "SPOTIFY_CLIENT_SECRET": os.getenv("SPOTIFY_CLIENT_SECRET"),
    "SPOTIFY_TOKEN_URL": os.getenv("SPOTIFY_TOKEN_URL"),
    "DROPBOX_TOKEN_URL" : os.getenv("DROPBOX_TOKEN_URL"),
    "DROPBOX_APP_KEY": os.getenv("DROPBOX_APP_KEY"),
    "DROPBOX_APP_SECRET": os.getenv("DROPBOX_APP_SECRET"),
    "DROPBOX_ACCESS_CODE_GENERATED": os.getenv("DROPBOX_ACCESS_CODE_GENERATED"),
    "DROPBOX_REFRESH_TOKEN": os.getenv("DROPBOX_REFRESH_TOKEN"),
    "RECOMMENDATIONS_NUM" : os.getenv("RECOMMENDATIONS_NUM"),
    "K_MEANS_MODEL_PATH" : os.getenv("K_MEANS_MODEL_PATH"),
    "DATASET_PATH" : os.getenv("DATASET_PATH"),
    "SONGS_FOLDER_PATH" : os.getenv("SONGS_FOLDER_PATH"),
    "DROPBOX_SONGS_FOLDER_PATH" : os.getenv("DROPBOX_SONGS_FOLDER_PATH"),
    "SPLEETER_VENV" : os.getenv("SPLEETER_VENV"),
    "EXTRACT_VOCALS_SCRIPT" : os.getenv("EXTRACT_VOCALS_SCRIPT"),
    "AUDIO_FILE_NAME" : os.getenv("AUDIO_FILE_NAME"),
    "VOCALS_FILE_NAME" : os.getenv("VOCALS_FILE_NAME"),
    "ACCOMPANIMENT_FILE_NAME" : os.getenv("ACCOMPANIMENT_FILE_NAME"),
    "ALBUM_IMG_NAME" : os.getenv("ALBUM_IMG_NAME")
}
