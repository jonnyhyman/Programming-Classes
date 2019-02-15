import PyAudioMixer as pam
import time

import wave

#import pdb; pdb.set_trace()

mixer = pam.Mixer()

snd = pam.Sound(mixer, filename="Cs5.wav")
snd1 = pam.Sound(mixer, filename="Cs5.wav")

mixer.start()
snd.play()
#time.sleep(0.5)
snd1.play()
