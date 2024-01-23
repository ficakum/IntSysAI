import sys
sys.path.append('../')
from models.lyrics2 import Lyrics

def add(text, segments, language, language_probs, track_information): 
    try:   
        lyr = Lyrics(
            text=text,
            segments=segments,
            language=language,
            language_probs=language_probs,
            track_information=track_information, 
            )
                
        lyr.save()

    except Exception as e:
        print('Lyrics - Error adding: ' + str(e))