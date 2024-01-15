import whisper_timestamped as whisper
import os
import sys
sys.path.append('../')
from config import conf


def get_lyrics(directory):
    try:
        model = whisper.load_model("base")

        file_path = os.path.join(directory, conf["VOCALS_FILE_NAME"])

        audio = whisper.load_audio(file_path)  
        result = whisper.transcribe(model, audio)

        return result

    except Exception as e:
        print(e)