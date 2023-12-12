import os
from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
from spleeter.audio import Codec

if __name__ == '__main__':

    separator = Separator('spleeter:2stems')

    directory = './dataset/songs'
    for subdir, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(directory, dir)
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)

                # version 1
                separator.separate_to_file(file_path, directory, codec=Codec.MP3)

                # version 2
                # audio_loader = AudioAdapter.default()
                # sample_rate = 44100
                # waveform, _ = audio_loader.load(file_path, sample_rate=sample_rate)

                # prediction = separator.separate(waveform)