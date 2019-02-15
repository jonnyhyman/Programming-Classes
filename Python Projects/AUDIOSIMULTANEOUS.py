"""PyAudio Example: Play a wave file."""

from multiprocessing import Process

import pyaudio
import wave
import sys

from time import time
import numpy as np

CHUNK = 32

#wf0 = wave.open('Cs5.wav', 'rb')
# #wf1 = wave.open('Cs5.wav', 'rb')
#

#
# # read data
# data0 = wf0.readframes(CHUNK)
# #data1 = wf1.readframes(CHUNK)
#
# # play stream (3)
# while True:
#
#     mix = np.frombuffer(data0, np.float)# + np.from_bytes(data1)
#     print(mix)
#
#     stream.write(mix)
#
#     data0 = wf0.readframes(CHUNK)
#     #data1 = wf1.readframes(CHUNK)
# ------------------------------
from scipy.io.wavfile import read
a = read("Cs5.wav")
mix = np.array(a[1], dtype=np.float32)

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=pyaudio.paFloat32, #p.get_format_from_width(4),
                channels=mix.shape[1],
                rate=a[0],
                output=True)

start = time()
while time() - start < 10:

    print(mix)

    stream.write(mix)

    #data0 = wf0.readframes(CHUNK)
    #data1 = wf1.readframes(CHUNK)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()
