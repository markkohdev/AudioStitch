__author__ = 'Mark'
import matplotlib.pyplot as plt
import wave
import sys
import numpy as np
import math
import types
import os
import subprocess

returncode = subprocess.call(["ffmpeg", "-y", "-vn", "-i", "/tmp/tmphvdYec", "-f", "wav", "/tmp/jawn.wav"],stderr=open(os.devnull))

print returncode
