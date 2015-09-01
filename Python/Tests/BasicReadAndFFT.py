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


# Prompt the user for the filename
FilePicker = Tk()
FilePicker.withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()

# Make sure they selected a file
if filename == "":
    print("File select canceled.")
    sys.exit(0)

spf = wave.open(filename, "rb")
playjawn = wave.open(filename, "rb")
FilePicker.destroy()  # Destory our TKinter instance

# Set the signal parameters
Fs = spf.getframerate()  # Sampling Frequency
T = 1.0 / Fs  # Sampling Rate (every T seconds)
L = spf.getnframes()  # Number of samples
Lwav = L / Fs  # Total length of the song (in seconds)

# Prompt user for window
print "There are", L, "samples in the chosen audio file at a sample rate of", Fs, "Hz"
print "The song is", Lwav, "seconds long."
WindowStartTime = float((raw_input("Starting time (0): ") or 0))
WindowEndTime = float(input("End time: "))
WindowLengthTime = WindowEndTime - WindowStartTime

# Assertion
if WindowEndTime < WindowStartTime or WindowEndTime > Lwav:
    print "I'm sorry, that is not a valid end time"
    sys.exit(0)

# Determine our sample numbers
WindowStart = int(math.floor(WindowStartTime * Fs))
WindowEnd = int(math.floor(WindowEndTime * Fs))
L = WindowEnd - WindowStart

# Generate the time vector
t = np.linspace(0, L - 1, L) * T
tOffset = t + WindowStartTime  # Vector from 0 to number of Samples and multiply by our sample rate

# Get the actual audio data
y = spf.readframes(WindowEnd)  # Read the samples up to the end of the window
y = np.fromstring(y, 'Int16')
y = y[WindowStart:]  # Chop the beginning of the signal up to the start of the window

# Assert not stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)

# First subplot - the waveform
plt.subplot(211)
plt.title('Waveform')
plt.xlabel("Time(milliseconds)")
plt.ylabel("Amplitude")
plt.plot(tOffset[0:L], y[0:L])  # Plot the time vs amplitude



# Let's set up the FFT
#NFFT = nextpow2(L)  # Next power of 2 from length of y
NFFT = 1024  # Next power of 2 from length of y
Y = np.fft.fft(y, NFFT) / L
spf = Fs / 2 * np.linspace(0, 1, NFFT / 2 + 1)
Yadj = 2 * abs(Y[0:NFFT / 2 + 1])


# Second subplot - the FFT
plt.subplot(212)
plt.title('Frequencies')
plt.xlabel("Frequency (Hz)")
plt.ylabel("|Y(f)|")
plt.plot(spf, Yadj)  # Plot the frequencies against the Y(f)


# Show the plot
plt.tight_layout()
plt.show()

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(playjawn.getsampwidth()),
                channels=playjawn.getnchannels(),
                rate=playjawn.getframerate(),
                output=True)

# read data
playjawn.setpos(WindowStart)
data = playjawn.readframes(L)
stream.write(data)

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
