"""

    Uh oh..

    This car is headed straight for a brick wall...

    The driver is watching Netflix on his phone and will not see it in time...

    SAVE HIM!! (or not - he seriously shouldn't Netflix and drive I mean cmon)


    ... Oh, and once you're done saving him, try to do it while maintaining
        a speed of 100 mph!

"""

def control(actual_position, actual_velocity, dt):
    """ ALL OF YOUR CONTROL MAGICKS GO HERE """

    wheel_command    = 1  # +1 == turn left, full deflection
    throttle_command = 1  # +1 == speed up

    return {'steer':wheel_command, 'throttle':throttle_command}


# importing all the things
import matplotlib.pyplot as plt
from time import time
import numpy as np

from numpy.linalg import norm  # norm is the same thing as sqrt(x**2 + y**2)


# First, enable interactive plotting
plt.ion() # this fancy function makes a matplotlib window ALIIVEEEEE!

# Let's set some start variables!
pos_initial = np.array([0., 0.])
vel_initial = np.array([30., 0.])

"""
 Why NUMPY arrays?
    If you try [1,2,3] - [4,5,6], you get a Python error (how to minus lists?)
    But! array([1,2,3]) - array([4,5,6]) = array([-3, -3, -3])

    Pretty cool, eh?
"""

trail_points    = 500  # how long do the car's tracks last?

# Using a dictionary, we will store the entire trail of all points!
car_trail = { 'x': [pos_initial[0]], 'y': [pos_initial[1]] }

_ = plt.plot(1000, 0)  # set the screen limits
__ = plt.plot(1000, +100)  # set the screen limits
___ = plt.plot(1000, -100)  # set the screen limits

car = plt.plot(np.array([0,0]))[0]  # create the car!

wall = plt.plot([500,500],[+100,-25])[0]  # create the wall!

accel_vect = plt.plot([0,0])[0]

def car_physics(control, position, velocity):
    ''' These car physics are greatly exaggerated and simplified '''

    # Control processing
    control['steer']    *= -np.pi/2  # 1 == turn 90 degrees (or try...)
    control['throttle'] *= 500  # exaggerated throttle


    direction = velocity / norm(velocity)  # direction of travel, unit vector

    # F = m*a, which means a = F/m... F is throttle in our case
    car_mass = 100 # kg, average car mass
    motor_acceleration = control['throttle'] / car_mass

    # Not possible to steer more than about 45 degrees == pi/4 radians
    if control['steer'] > np.pi/2:
        control['steer'] = np.pi/2
    elif control['steer'] < -np.pi/2:
        control['steer'] = -np.pi/2


    # now, which direction are we accelerating into?
    # here, we are ROTATING the direction vector

    turn_direction = np.array([
        + np.cos(control['steer']) * direction[0]
        - np.sin(control['steer']) * direction[1],  # x rotated

        + np.sin(control['steer']) * direction[0]
        + np.cos(control['steer']) * direction[1],  # y rotated
        ])


    print('turn_direction', turn_direction, direction)



    ''' Friction on tires is more at higher speed '''
    friction_coefficient = 0.1  # how much friction / mph?
    friction = velocity * friction_coefficient

    acceleration = motor_acceleration * turn_direction

    accel_vect.set_xdata([position[0], position[0] + 5*acceleration[0]])
    accel_vect.set_ydata([position[1], position[1] + 5*acceleration[1]])

    return acceleration - friction


pos = pos_initial
vel = vel_initial
acc = car_physics({'steer':0, 'throttle':0}, pos, vel)

while True:

    dt = .1 # how much time has passed ? delta-t / dt

    ctrl = control(pos, vel, dt)
    acc = car_physics(ctrl, pos, vel)
    vel += (acc) * dt
    pos += (vel) * dt


    car_trail['x'].append(pos[0])
    car_trail['y'].append(pos[1])

    car.set_xdata(car_trail['x'])  # get all the saved x data
    car.set_ydata(car_trail['y'])  # get all the saved y data

    print('Trail N : ', len(car_trail['x']), end =' | ')
    print('Distance: ', round(norm(pos),2), end =' | ')
    print('Velocity: ', round(norm(vel),2), end =' | ')
    print('Steering: ', round(ctrl['steer'],2), end =' | ')
    print('Throttle: ', round(ctrl['throttle'],2))

    if len(car_trail['x']) > trail_points:
        car_trail['x'].pop(0)
        car_trail['y'].pop(0)

    plt.pause(.01)
