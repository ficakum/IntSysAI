import whisper_timestamped as whisper
import json
import os

if __name__ == '__main__':

    try:
        model = whisper.load_model("base")

        directory = '../dataset/songs'
        for subdir, dirs, files in os.walk(directory):
            for dir in dirs:
                dir_path = os.path.join(directory, dir)
                file_path = os.path.join(dir_path, "vocals.mp3")

                audio = whisper.load_audio(file_path)  
                result = whisper.transcribe(model, audio)

                json_object = json.dumps(result, indent = 2, ensure_ascii = False)
                json_path = os.path.join(dir_path, "lyrics.json")
                with open(json_path, "w") as out_file:
                    out_file.write(json_object)

    except Exception as e:
        print(e)