import os
import shutil
from spleeter.separator import Separator
from spleeter.audio import Codec
import sys
sys.path.append('../')
import config


def separate_vocals(directory, file_path):
    try:
        separator = Separator("spleeter:2stems")
        separator.separate_to_file(file_path, directory, codec=Codec.MP3)

        curr_dir = os.getcwd()

        curr_loc = os.path.join(curr_dir, directory, "audio", config["VOCALS_FILE_NAME"])
        new_loc = os.path.join(curr_dir, directory, config["VOCALS_FILE_NAME"])
        if os.path.exists(new_loc):
            os.remove(new_loc)
        os.rename(curr_loc, new_loc)

        curr_loc = os.path.join(curr_dir, directory, "audio", config["ACCOMPANIMENT_FILE_NAME"])
        new_loc = os.path.join(curr_dir, directory, config["ACCOMPANIMENT_FILE_NAME"])
        if os.path.exists(new_loc):
            os.remove(new_loc)
        os.rename(curr_loc, new_loc)

        shutil.rmtree(directory + "/audio")

        print("Spleeter: Extracting done successfully.")

    except Exception as e:
        print('Spleeter - Error extracting: ' + str(e))

if __name__ == "__main__":
    separate_vocals(sys.argv[1], sys.argv[2])