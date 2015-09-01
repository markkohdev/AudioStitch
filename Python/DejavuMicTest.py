__author__ = 'Mark'
from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer

if __name__ == '__main__':
    config = {
        "database": {
            "host": "127.0.0.1",
            "user": "root",
            "passwd": "root",
            "db": "dejavu"
        }
    }

    djv = Dejavu(config)

    song = djv.recognize(MicrophoneRecognizer, seconds=5) # Defaults to 10 seconds.

    print song