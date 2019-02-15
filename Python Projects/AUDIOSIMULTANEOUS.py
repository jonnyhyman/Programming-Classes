import PyAudioMixer as pam
from time import time
import wave

#import pdb; pdb.set_trace()

mixer = pam.Mixer()
mixer.start()
snd = pam.Sound(mixer, filename="Cs5.wav")
snd1 = pam.Sound(mixer, filename="Gs5.wav")


snd.play()

notstarted = True
start = time()
while True:

    if time()-start > 1 and notstarted:
        print('STARTED1')
        snd1.play()
        print('STARTED2')
        notstarted = False
