__author__ = 'Mark'
from dejavu import Dejavu

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

    djv.fingerprint_directory("../../../Desktop/media/dejavu",[".wav",".mp3",".mov",".MOV"])


    print djv.db.get_num_fingerprints()