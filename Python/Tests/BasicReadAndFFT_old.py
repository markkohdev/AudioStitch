import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
from Tkinter import Tk
from tkFileDialog import askopenfilename

# Prompt the user for the filename
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()
spf = wave.open(filename, 'r')

# Extract Raw Audio from Wav File
numframes = spf.getnframes()
samplerate = spf.getframerate()
audiolength = numframes / samplerate

# Prompt user for window
print 'There are', numframes, 'frames in the chosen audio file at a sample rate of', samplerate
print "The song is", audiolength, "seconds long."
starttime = float((raw_input("Starting time (0): ") or 0))
endtime = input("End time: ")
elapsed = endtime - starttime

# Assertion
if endtime < starttime or endtime > audiolength:
    print "I'm sorry, that is not a valid end time"
    sys.exit(0)

# Determine our sample numbers
startsample = int(math.floor(starttime * samplerate))
endsample = int(math.floor(endtime * samplerate))
numsamples = endsample - startsample

# Get the actual audio data
signal = spf.readframes(endsample)
signal = np.fromstring(signal, 'Int16')
signal = signal[startsample:]

# If Stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)

# Get the x axis labels for the plot using linear spacing
xaxis = np.linspace(starttime, endtime, num=numsamples)

# Create a plot object
# plt.figure(1)

# First subplot - the waveform
plt.subplot(211)
plt.title('Waveform')
plt.xlabel("Seconds")
plt.ylabel("Amplitude")
plt.plot(xaxis, signal)


# Second subplot - the FFT
plt.subplot(212)
plt.title('Frequencies')
plt.xlabel("Frequency")
plt.ylabel("Decibels")
fft = np.fft.fft(signal)
fft = fft[len(fft)/2:]
scaledfft = [20 * math.log(abs(x),10) for x in fft]
plt.plot(scaledfft)


# Show the plot
plt.tight_layout()
plt.show()
spf.close()

#plt.figure(1)
#plt.close()
#sys.exit(0)

# # If we wanna play the audio
# player = pyaudio.PyAudio()
# stream = player.open(format = player.get_format_from_width(spf.getsampwidth()),
# channels = spf.getnchannels(),
#                      rate = spf.getframerate(),
#                      output = True)
# playstream = signal
# stream.write(playstream)
#
# stream.stop_stream()
# stream.close()
#
# player.terminate()
