__author__ = 'Mark'
from pylab import specgram
import numpy as np
import math
import matplotlib.pyplot as plt
from DSPUtils import *
from TKFileUtils import *

def nextpow2(i):
    n = 1
    while n < i:
        n *= 2
    return n

pi = np.pi
fft = np.fft.fft

# create a wave with 1Mhz and 0.5Mhz frequencies
# dt = 2e-9
# t = np.arange(0, 10e-6, dt)
# y = np.cos(2 * pi * 1e6 * t) + (np.cos(2 * pi * 2e6 *t) * np.cos(2 * pi * 2e6 * t))
# y *= np.hanning(len(y))
# yy = np.concatenate((y, ([0] * 10 * len(y))))

# Get the file signal
filename = pickaudiofile()
signal = getsignal(filename)

# Get signal parameters
(nchannels, sampwidth, Fs, nframes, comptype, compname) = signal.getparams()
songlength = nframes / Fs  # Total length of the song (in seconds)
T = 1.0 / Fs


# Prompt user for window
print "There are", nframes, "samples in the chosen audio file at a sample rate of", Fs, "Hz"
print "The song is", songlength, "seconds long."
WindowStartTime = float((raw_input("Starting time (0): ") or 0))
WindowEndTime = float(input("End time: "))
WindowLengthTime = WindowEndTime - WindowStartTime

# Assertion
if WindowEndTime < WindowStartTime or WindowEndTime > songlength:
    print "I'm sorry, that is not a valid end time"
    sys.exit(0)

# Determine our sample numbers
WindowStart = int(math.floor(WindowStartTime * Fs))
WindowEnd = int(math.floor(WindowEndTime * Fs))
L = WindowEnd - WindowStart

# Get the actual audio data
y = signal.readframes(WindowEnd)  # Read the samples up to the end of the window
y = np.fromstring(y, 'Int16')
y = y[WindowStart:]  # Chop the beginning of the signal up to the start of the window

# Generate the time vector
timevec = np.linspace(0, L - 1, L) * T
tOffset = timevec + WindowStartTime  # Vector from 0 to number of Samples and multiply by our sample rate


NFFT = 2048 # Next power of 2 from length of y
FreqStops = NFFT / 2 + 1
FreqSpace = np.linspace(0, 1, FreqStops)

# y *= np.hanning(len(y))
Y = abs(np.fft.fft(y, NFFT))
freqaxis = Fs / 2 * FreqSpace


# plotting the data
plt.subplot(311)
plt.plot(timevec, y, 'r')
plt.xlabel('Time (micro seconds)')
plt.ylabel('Amplitude')
plt.grid()

# plotting the spectrum
plt.subplot(312)
#plt.plot(freqaxis[0:600], Y[0:600], 'k')
#plt.plot(Y)
plt.plot(freqaxis[0:500],Y[0:500],'k')
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.grid()

# plotting the specgram
plt.subplot(313)
Pxx, freqs, bins, im = specgram(y, NFFT=NFFT, Fs=Fs, noverlap=128)
plt.show()