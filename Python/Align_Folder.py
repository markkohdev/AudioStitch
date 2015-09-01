__author__ = 'Mark'
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import argparse
import os

def main():
    # Set up our commang line arguments
    parser = argparse.ArgumentParser(description="Take in a folder of video and/or audio files and find the alignment"
                                                 "of them all.")
    parser.add_argument("folder",type=str,help="The folder containing your audio and video files, relative to the current directory.")
    args = parser.parse_args()

    # Our DB settings
    config = {
        "database": {
            "host": "127.0.0.1",
            "user": "root",
            "passwd": "root",
            "db": "dejavu"
        }
    }


    # Get the files in our folder
    dir = os.path.expanduser(args.folder)
    files = os.listdir(dir)


    # Set up our dejavu instance
    djv = Dejavu(config)


    # Generate our corpus name - we'll add this functionality later.
    corpus = dir.replace(" ","")
    corpus = corpus.lower()

    # For now, let's just empty the DB before the experiment
    djv.db.empty()

    # Iterate through the files
    for filename in files:
        full_path = os.path.join(dir,filename)

        # For now we'll assume all the files are valid audio or video
        if (os.path.isfile(full_path)):

            print "Attempting to match {0}...".format(filename)

            # Try to match the song to the existing database
            songs = djv.recognize(FileRecognizer, full_path)

            if songs:
                for song in songs:
                    print song
            else:
                print "No matches found."

            print "Adding {0} to database...".format(filename)

            # Now let's add this song to the DB
            djv.fingerprint_file(full_path)

            print djv.db.get_num_fingerprints()






if __name__ == '__main__':
    main()