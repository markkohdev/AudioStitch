import matplotlib.pyplot as plt

import numpy as np
import wave
import sys
import math
# import pyaudio
from Tkinter import Tk
from tkFileDialog import askopenfilename


def nextpow2(i):
    n = 1
    while n < i: n *= 2
    return n

# Set the signal parameters
Freq = input("What frequency would you like (in Hz): ")  # Frequency of our sine wav
Fs = 44100  # Sampling Frequency
T = 1.0 / Fs  # Sampling Rate (every T seconds)
L = 10000  # Number of samples we want (length)

# Generate the signal
t = np.linspace(0, L - 1, L)*T  # Vector from 0 to number of Samples and multiply by our sample rate
y = np.sin(2 * np.pi * Freq * t)  # Fill our signal vector based on time
# y = 0.4*np.sin(2*np.pi* 400*t) + np.sin(2 * np.pi * Freq * t)  # Fill our signal vector based on time


# First subplot - the waveform
plt.subplot(211)
plt.title('Waveform')
plt.xlabel("Time(milliseconds)")
plt.ylabel("Amplitude")
plt.plot(Fs*t[0:L], y[0:L])  # Plot the time vs amplitude



# Let's set up the FFT
NFFT = nextpow2(L) # Next power of 2 from length of y
Y = np.fft.fft(y, NFFT)/L
f = Fs/2*np.linspace(0,1,NFFT/2+1)
Yadj = 2*abs(Y[0:NFFT/2+1])


# Second subplot - the FFT
plt.subplot(212)
plt.title('Frequencies')
plt.xlabel("Frequency (Hz)")
plt.ylabel("|Y(f)|")
plt.plot(f, Yadj)  # Plot the frequencies against the Y(f)


# Show the plot
plt.tight_layout()
plt.show()

plt.close()

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
