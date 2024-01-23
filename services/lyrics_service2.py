import sys
sys.path.append('../')
from repositories.lyrics_repository2 import *


def add_lyrics2(text, segments, language, language_probs, track_information):
    add(text, segments, language, language_probs, track_information)
