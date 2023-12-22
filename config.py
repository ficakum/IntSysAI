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
    "SPOTIFY_TOKEN_URL": os.getenv("SPOTIFY_TOKEN_URL")
}
