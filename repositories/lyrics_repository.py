import sys
sys.path.append('../')
from models.lyrics import Lyrics

def add_lyrics(track_info, lyrics):
    try:
        lyr = Lyrics(
            text = lyrics["text"],
            segments = lyrics["segments"],
            language = lyrics["language"],
            language_probs = lyrics["language_probs"],
            track_information = track_info
        )
        lyr.save()
    
    except Exception as e:
        print('LYRICS - Error adding: ' + str(e))

def get_by_track_info_id(track_info_id):
    try:
        lyrics = Lyrics.objects.filter(track_information=track_info_id).first()
        return lyrics
    
    except Exception as e:
        print('LYRICS - Error getting by track_info id: ' + str(e))