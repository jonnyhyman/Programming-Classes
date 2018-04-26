'''

    A SPACESHIP ORBITAL SIMULATION - WITH REAL PHYSICS

    CHALLENGES (ordered by difficulty)

    Question: If ISS was orbiting around Mars, would it stay in orbit?

            Mars Gravity : -3.71 m/s^2
            Mars Mass    :  6.39 * 1e23 kg
            Mars Radius  :  3389 km

    Question: If a spaceship orbits at an altitude of 500km around Mars,
              what velocity does it need to stay in a mostly CIRCULAR orbit?

    Question: How much does Phobos, the innermost, largest moon of Mars,
                mess with the orbit of a spaceship in orbit at 1000km?

            Phobos Distance from Center of Mars: ~ 9300 km
            Phobos Radius : 11 km
            Phobos Mass : 1.0659 * 1e16 kg

    Question: How much change in velocity (delta-v) does that same spaceship
              need for its orbit to actually "intersect" the planet (barely)

              In otherwords, what is the difference in orbital velocity and
              maximum velocity required to impact the surface tangentially?

'''

import matplotlib.pyplot as plt
from time import time
import numpy as np

# First, enable interactive plotting
plt.ion() # this fancy function makes a matplotlib window ALIIVEEEEE!

# We want to draw the planet.... So let's do it in POLAR COORDINATES!
# First we need some angles...
# This gets 100 evenly spaced angles between 0 and 2pi
circle_angles = np.linspace(0, (2*np.pi), 100)

# ----------------------------- Getting planet set up
R0 = 6371 * 1e3  # km * 1e3 => meters, radius of the planet

planet_r = np.linspace(R0,   R0,    100)  # get 100 evenly spaced R0s
planet_X = planet_r*np.cos(circle_angles)  # X = take the cos(all_angles) * R0
planet_Y = planet_r*np.sin(circle_angles)  # Y = take the cos(all_angles) * R0
planet = plt.plot(planet_X,planet_Y)[0]     # make a plot with x and y

# ----------------------------- Getting spaceship all set up

''' NOTE: numpy.arrays are used throughout. why?
        If you try [1,0,0] * 3 with Python lists, you'll get an error.
        If you try [1,0,0] * 3 with Numpy arrays, you'll get [3,0,0]... Useful!
'''


alt_initial = 408_773  # ISS altitude, meters

# let's start y = initial altitude + radius of planet
pos_initial = np.array([
                            0.,
                            alt_initial + R0
                        ])

vel_initial = np.array([
                            7666.736,
                            0.
                        ]) # ISS horizontal velocity, meters per second


trail_points    = 500  # how many points should the trail keep?
spaceship_trail = { 'x': [pos_initial[0]], 'y': [pos_initial[1]] }
spaceship = plt.plot(*pos_initial)[0]  # give plot the position intially

# ----------------------------- Getting physics set up

def gravity(pos):

    G =  6.674 * 1e-11  # universal gravitational constant
    M =  5.972 * 1e24   # mass of planet, kg

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
