__author__ = 'Mark'
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

if __name__ == '__main__':
    config = {
        "database": {
            "host": "127.0.0.1",
            "user": "root",
            "passwd": "root",
            "db": "dejavu",
        }
    }

    djv = Dejavu(config)

    songs = djv.recognize(FileRecognizer, "../../../Desktop/media/jeff_alliy_clipped.wav")

    for song in songs:
        print song
