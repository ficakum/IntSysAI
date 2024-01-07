import os
from spleeter.separator import Separator
from spleeter.audio import Codec


def separate_vocals(directory):
    separator = Separator('spleeter:2stems')

    for _, dirs, _ in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(directory, dir)
            file_path = os.path.join(dir_path, dir + ".mp3")

            separator.separate_to_file(file_path, directory, codec=Codec.MP3)