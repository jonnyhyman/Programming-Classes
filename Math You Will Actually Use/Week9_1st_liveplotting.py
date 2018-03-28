'''

This is a quick demo for INTERACTIVE PLOTTING with Python / Matplotlib.

We're going to plot a smiley face in real time. :)

IMPORTANT:

        - I wrote this excessively lazily (way more code than needed)
        - I highlighted the important things that make it work with ********'s


CHALLENGES (ordered by difficulty):

        Straightforward : change the amount of time it takes to plot
        Simple          : change the color of the eyes to match
        SPICY           : add a monacle, hat, or something else on the head
        SCARY           : make the smiley face FROWN :(

'''
import matplotlib.pyplot as plt

import numpy as np
from time import time

# using polar coordinates because we are COOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL

seconds_to_draw = 5.0

''' ******** enable INTERACTIVE plotting '''
plt.ion()

# get the axes set up with proper scaling!
X, Y = np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)

''' ******** add a line to the plot graphic'''
head = plt.plot(X,Y)[0]
smile = plt.plot(X,Y)[0]
eyeL = plt.plot(X,Y)[0]
eyeR = plt.plot(X,Y)[0]

start = time()
while True:

    amount = (time()-start)/seconds_to_draw

    if amount > 1:
        amount = 1

    # ---------- Head

    head_angle = np.linspace(0, (2*np.pi) * amount   , 100)
    head_radii = np.linspace(1, 1, 100)

    X, Y = head_radii*np.cos(head_angle), head_radii*np.sin(head_angle)

    head.set_xdata(X)
    head.set_ydata(Y)

    # ---------- Smile

    smile_angle = np.linspace(- np.pi/4,
                              -(np.pi/4)*(1-amount) - (3*np.pi/4) * amount, 100)
    smile_radii = np.linspace(.5, .5, 100)

    smileX = smile_radii*np.cos(smile_angle)
    smileY = smile_radii*np.sin(smile_angle)

    smile.set_xdata(smileX)
    smile.set_ydata(smileY)

    # ---------- Left eye

    eye_angle = np.linspace(0, 2*np.pi*amount, 100)
    eye_radii = np.linspace(.03, .03, 100)

    #  offset so it's the correct side eyeball, not Mike Wazowski
    eye_X = eye_radii*np.cos(eye_angle) - .5
    eye_Y = eye_radii*np.sin(eye_angle) + .5

    eyeL.set_xdata(eye_X)
    eyeL.set_ydata(eye_Y)

    # ---------- Right eye

    eye_angle = np.linspace(0, 2*np.pi*amount, 100)
    eye_radii = np.linspace(.03, .03, 100)

    #  offset so it's the correct side eyeball, not Mike Wazowski
    eye_X = eye_radii*np.cos(eye_angle) + .5
    eye_Y = eye_radii*np.sin(eye_angle) + .5

    eyeR.set_xdata(eye_X)
    eyeR.set_ydata(eye_Y)

    ''' ******** update the plots every .01 seconds '''
    plt.pause(.01)
