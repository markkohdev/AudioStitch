import matplotlib.pyplot as plt

import numpy as np
import scipy.signal as signal


def nextpow2(i):
    n = 1
    while n < i: n *= 2
    return n



# Set the signal parameters
Fs = 44100  # Sampling Frequency
Fs2 = 22500 # Half sampling frequency
T = 1.0 / Fs  # Sampling Rate (every T seconds)
T2 = 1.0 / Fs2
L = 1000  # Number of samples we want (length)
L2 = L/2

# Generate the signal
t = np.linspace(0, L - 1, L)*T  # Vector from 0 to number of Samples and multiply by our sample rate
t2 = np.linspace(0, L2 - 1, L)*T2  # Vector from 0 to number of Samples and multiply by our sample rate
y = 0.4*np.sin(2*np.pi* 400*t) + np.sin(2 * np.pi * 14000 * t)  # Fill our signal vector based on time
yf = y[::2]

# Let's set up the FFT
NFFT = nextpow2(L) # Next power of 2 from length of y
print 'NFFT:',NFFT
Y = np.fft.fft(y, NFFT)/L
Yadj = 2*abs(Y[0:NFFT/2+1])
f = Fs/2*np.linspace(0,1,NFFT/2+1)


# Let's set up the FFT2
NFFT2 = nextpow2(L2)
print 'NFFT2:',NFFT2
Yf = np.fft.fft(yf, NFFT2)/L2
Yfadj = 2*abs(Yf[0:NFFT2/2+1])
f2 = Fs2/2*np.linspace(0,1,NFFT2/2+1)


# First subplot - the waveform
plt.subplot(411)
plt.title('Waveform')
plt.xlabel("Time(milliseconds)")
plt.ylabel("Amplitude")
plt.plot(Fs*t[0:L], y[0:L])  # Plot the time vs amplitude

# Second subplot - the waveform
plt.subplot(412)
plt.title('Waveform')
plt.xlabel("Time(milliseconds)")
plt.ylabel("Amplitude")
plt.plot(Fs2*t2[0:L2], yf[0:L2])  # Plot the time vs amplitude


# Second subplot - the FFT
plt.subplot(413)
plt.title('Frequencies')
plt.xlabel("Frequency (Hz)")
plt.ylabel("|Y(f)|")
plt.plot(f, Yadj)  # Plot the frequencies against the Y(f)

# Second subplot - the FFT
plt.subplot(414)
plt.title('Frequencies')
plt.xlabel("Frequency (Hz)")
plt.ylabel("|Y(f)|")
plt.plot(f2, Yfadj)  # Plot the frequencies against the Y(f)


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
