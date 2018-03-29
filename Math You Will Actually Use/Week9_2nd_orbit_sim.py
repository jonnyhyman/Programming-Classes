'''

    A SPACESHIP ORBITAL SIMULATION - WITH REAL PHYSICS

    CHALLENGES (ordered by difficulty)

    Straightforward : mess around with the velocity. Try to get the spaceship to slingshot around earth's core
    Simple          : print out the angle of the ship around earth as it orbits (hint arccos/arcsin/arctan)
    Simple          : change the strength of gravity & try making it POSTIIVE :P

    SPICY           : only track number of trail points based on how much time has passed
    SPICY           : make the entire simulation REAL TIME
    SCARY           : simulate the moon's gravitational pull on earth & the spaceship too
    OR SCARY        : make the whole simulator 3D

'''

import matplotlib.pyplot as plt
from time import time
import numpy as np

# First, enable interactive plotting
plt.ion()

circle_angles = np.linspace(0, (2*np.pi), 100)


# ----------------------------- Getting earth set up
R0 = 6371 * 1e3  # kilometers

earth_r = np.linspace(R0,         R0, 100)
earth_X = earth_r*np.cos(circle_angles)
earth_Y = earth_r*np.sin(circle_angles)
earth = plt.plot(earth_X,earth_Y)[0]

# ----------------------------- Getting spaceship all set up

''' NOTE: numpy.arrays are used throughout. why?
        If you try [1,0,0] * 3 with Python lists, you'll get an error.
        If you try [1,0,0] * 3 with Numpy arrays, you'll get [3,0,0]... Useful!
'''


alt_initial = 408_773  # ISS altitude, meters

# let's start y = initial altitude + radius of earth
pos_initial = np.array([0., alt_initial + R0])
vel_initial = np.array([7666.736, 0.]) # ISS horizontal velocity, meters

trail_points    = 500
spaceship_trail = { 'x': [pos_initial[0]], 'y': [pos_initial[1]] }
spaceship = plt.plot(*pos_initial)[0]

# ----------------------------- Getting physics set up

gravity_acceleration = -9.81  # m/s

def gravity(pos):

    G =  6.674 * 1e-11  # universal gravitational constant
    M =  5.972 * 1e24   # mass of earth

    # g = GM / r**2
    gravity_acceleration = G*M / (np.sqrt(pos[0]**2 + pos[1]**2))**2

    # which direction?
    # what vector tells us the direction of gravity?
    # the "down" vector of course!

    # also known as the negative of the position vector (normalized)!
    #     pos / the magnitude of pos         * gravity_acceleration at this alt
    g = (-pos/np.sqrt(pos[0]**2 + pos[1]**2)) * gravity_acceleration

    return g


pos = pos_initial
vel = vel_initial
acc = gravity(pos)

dt = 10

while True:

    acc = gravity(pos)
    vel += (acc) * dt
    pos += (vel) * dt

    spaceship_trail['x'].append(pos[0])
    spaceship_trail['y'].append(pos[1])

    spaceship.set_xdata(spaceship_trail['x'])  # get all the saved x data
    spaceship.set_ydata(spaceship_trail['y'])  # get all the saved y data

    print('Trail N : ', len(spaceship_trail['x']), end =' | ')
    print('Altitude: ', round(np.linalg.norm(pos),2), end =' | ')
    print('Velocity: ', round(np.linalg.norm(vel),2), end =' | ')
    print('Gravity : ', round(np.linalg.norm(acc),2))

    if len(spaceship_trail['x']) > trail_points:
        spaceship_trail['x'].pop(0)
        spaceship_trail['y'].pop(0)

    plt.pause(.01)
