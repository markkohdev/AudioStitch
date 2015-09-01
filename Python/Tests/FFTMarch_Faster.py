import matplotlib.pyplot as plt

import numpy as np
import wave
import sys
import math
import pyaudio
from Tkinter import Tk
from tkFileDialog import askopenfilename


def nextpow2(i):
    n = 1
    while n < i: n *= 2
    return n

# Get the wav file data from startframe to startframe+n
def getwavdata(signal,startframe,n):
    signal.setpos(startframe)
    y = signal.readframes(n)
    y = np.fromstring(y, 'Int16')
    return y

# def getfftwindow(signal,startframe,endframe):

# Prompt the user for the filename
FilePicker = Tk()
FilePicker.withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()

# Assert file selected
if filename == "":
    print("File select canceled.")
    sys.exit(0)

FilePicker.destroy()  # Destory our TKinter instance

spf = wave.open(filename, "rb")
playsignal = wave.open(filename, "rb")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = spf.getparams()


# Assert not stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)

# Set the signal parameters
Fs = spf.getframerate()  # Sampling Frequency
T = 1.0 / Fs  # Sampling Rate (every T seconds)
L = spf.getnframes()  # Number of samples
Lwav = L / Fs  # Total length of the song (in seconds)

# Set up PyAudio for playing
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(playsignal.getsampwidth()),
                channels=playsignal.getnchannels(),
                rate=Fs,
                output=True)

# Set up the plot window
#plt.subplot(211)  # Waveform plot
plt.title('Waveform')
plt.xlabel("Time(milliseconds)")
plt.ylabel("Amplitude")
# plt.subplot(212)  # FFT Plot
# plt.title('Frequencies')
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("|Y(f)|")
# plt.tight_layout()
plt.show(block=False)

# Our window size should be a power of two
WindowSize = pow(2, 10)

# Generate the time vector
t = np.linspace(0, WindowSize - 1, WindowSize) * T

# Perform some pre-calculation for the FFT
NFFT = nextpow2(WindowSize)  # Next power of 2 from length of y
FreqSpace = np.linspace(0, 1, NFFT / 2 + 1)


# We'll start at 0
StartFrame = 0

# Read the entire audio signal
spf.setpos(0)
wholesignal = spf.readframes(L)
wholesignal = np.fromstring(wholesignal, 'Int16')
wholebytestream = playsignal.readframes(L)

PlotList = []
SoundList = []

# Preprocess
print("Preprocessing...")
# Iterate by window blocks
while StartFrame < 30*WindowSize:
    # Set up our frames
    EndFrame = StartFrame + WindowSize
    StartTime = StartFrame/float(Fs)
    EndTime = EndFrame/float(Fs)

    # Offset the time vector
    tOffset = t + StartTime

    y = wholesignal[StartFrame:EndFrame]

    # NFFT = nextpow2(L)  # Next power of 2 from length of y
    Y = np.fft.fft(y, NFFT) / WindowSize
    freqaxis = Fs / 2 * FreqSpace
    Yadj = 2 * abs(Y[0:NFFT / 2 + 1])

    PlotList.insert(0,[freqaxis,Yadj])

    # read data
    # playsignal.setpos(StartFrame)
    # data = playsignal.readframes(WindowSize)
    #stream.write(wholebytestream[StartFrame*sampwidth*2:EndFrame*sampwidth*2])
    SoundList.insert(0,wholebytestream[StartFrame*sampwidth:EndFrame*sampwidth])

    StartFrame += WindowSize + 1

print("Playing...")
# Iterate by window blocks
for i in range (0,len(PlotList)):
    plt.clf()
    plt.plot(PlotList[i][0], PlotList[i][1])
    plt.draw()

    # read data
    # playsignal.setpos(StartFrame)
    # data = playsignal.readframes(WindowSize)
    stream.write(SoundList[i])

p.terminate()

raw_input("Press Enter to continue...")

# # The old way
# # Let's set up the FFT
# fft = np.fft.fft(y)  # Take the FFT of y
# fft = fft[:len(fft) / 2 + 1]  # Only take the first half+1 of the FFT so we don't have negative frequencies
# scaledfft = [20 * math.log(abs(x), 10) for x in fft]   # Scale the FFT so it's a little easier to see
#
# freqs = 1000 / 2 * np.linspace(0, 1, len(y) / 2 + 1)  # Get our frequencies vector for the x axis


# # If we wanna play the audio
# player = pyaudio.PyAudio()
# stream = player.open(format = player.get_format_from_width(spf.getsampwidth()),
# channels = spf.getnchannels(),
# rate = spf.getframerate(),
#                      output = True)
# playstream = signal
# stream.write(playstream)
#
# stream.stop_stream()
# stream.close()
#
# player.terminate()

sys.exit(0)