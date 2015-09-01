__author__ = 'Mark'
import wave
import sys
import subprocess

def getsignal(filename):
    signal = wave.open(filename, "rb")

    # Assert not stereo
    if signal.getnchannels() == 2:
        signal.setnchannels(1)
        print 'Just mono files'
        sys.exit(0)

    return signal

def audiofromvideo(videofile,savedest):
    command = "ffmpeg -i " + videofile + " -ab 192k -ac 1 -ar 44100 -y -vn " + savedest

    subprocess.call(command, shell=True)

    return getsignal(savedest)
