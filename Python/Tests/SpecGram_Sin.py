__author__ = 'Mark'
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import wave
import sys
import math

pi = np.pi
fft = np.fft.fft

# create a wave with 1Mhz and 0.5Mhz frequencies
dt = 2e-9
t = np.arange(0, 10e-6, dt)
y = np.cos(2 * pi * 1e6 * t) + (np.cos(2 * pi * 2e6 *t) * np.cos(2 * pi * 2e6 * t))
y *= np.hanning(len(y))
yy = np.concatenate((y, ([0] * 10 * len(y))))

# FFT of this
Fs = 1 / dt  # sampling rate, Fs = 500MHz = 1/2ns
n = len(yy)  # length of the signal
k = np.arange(n)
T = n / Fs
frq = k / T  # two sides frequency range
frq = frq[range(n / 2)]  # one side frequency range
Y = fft(yy) / n  # fft computing and normalization
Y = Y[range(n / 2)] / max(Y[range(n / 2)])

# plotting the data
plt.subplot(311)
plt.plot(t * 1e3, y, 'r')
plt.xlabel('Time (micro seconds)')
plt.ylabel('Amplitude')
plt.grid()

# plotting the spectrum
plt.subplot(312)
plt.plot(frq[0:600], abs(Y[0:600]), 'k')
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.grid()

# plotting the specgram
plt.subplot(313)
Pxx, freqs, bins, im = specgram(y, NFFT=512, Fs=Fs, noverlap=10)
plt.show()