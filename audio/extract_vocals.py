import sys
from spleeter.separator import Separator
from spleeter.audio import Codec


def separate_vocals(directory, file_path):
    try:
        separator = Separator("spleeter:2stems")
        separator.separate_to_file(file_path, directory, codec=Codec.MP3)
        
        print("Spleeter: Extracting done successfully.")

    except Exception as e:
        print('Spleeter - Error extracting: ' + str(e))

if __name__ == "__main__":
    separate_vocals(sys.argv[1], sys.argv[2])