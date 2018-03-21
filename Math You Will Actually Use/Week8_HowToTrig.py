# THIS...
# IS.....
# TRIGGGGGGGGG!
print('''

CONSIDER THE FOLLOWING...

Imagine coordinates, x, and y

            |y
            |
            |
-----------------------------x
            |
            |
            |

What is the most glorious shape in the world?
Why, a circle of course!

I can't draw a circle with my keyboard (O, is that right??)
So let's plot it


OH, btw, we're making a circle with radius = 1

There's an EXTREMELY FANCY WAY to explain to your fellow mathematicians
that your circle has radius 1. You ready? The term is "UNIT".

It is a UNIT circle if it has radius 1.

''')

import matplotlib.pyplot as plt
import numpy as np

# Create the x axis, from -1 to 1, including 1 (linspace does this auto)

xs = np.linspace(-1,1,100)  # from -1 to 1, make 100 equally spaced points

ys = {'top':[], 'bot':[]}  # create a python dictionary holding the circle's ys

# top half

for x in xs:

    y_top = + np.sqrt( 1**2 - x**2)
    y_bot = - np.sqrt( 1**2 - x**2)

    ys['top'].append( y_top )
    ys['bot'].append( y_bot )

plt.plot(xs, ys['top'])
plt.plot(xs, ys['bot'])
plt.show()

print(
'''
Now, all that was a bit tedious wasn't it?

What if...

What if we could just say "I WANT A UNIT CIRCLE THAT GOES AROUND ONCE",
and it would just... WORK?

Hmmm...

In 'polar' coordinates, instead of using x and y as our "coordinates",
we can just use "r" and "theta", or a "radius" and an "angle"........

So maybe we can just "sweep" over angles, and plot the radii?

Something like...
'''


''' What is the circumference of a circle?

    ... I hope you remember...

    It's 2 * pi * radius.... Since our radius is 1, what's the circumference?

    2*pi. SO!

AHA!

 What if we just define our angles as fractions of the circumference?
 (instead of using degrees)

    So 0 degrees = 0 * 2*pi

    So 45 degrees = (2*pi / 8) =     (pi / 4) <--> 45 deg

    So 90 degrees = (2*pi / 4) =     (pi / 2) <--> 90 deg

    So 180 deg = (2*pi / 2)    =      (pi)    <--> 180 deg

    So 360 deg = (2*pi / 1)    =    (2*pi)    <--> 360 deg


    ... FYI these new fancy fractional angles are called 'radians'
'''
)

from numpy import pi

angles = np.linspace(0, 2*pi, 100)

print('''

Okay, now how do to translate our new polar coordinates into xs and ys?
(We need to do this so we can plot...)

''')

# Here's how........

xs = np.cos(angles)  # cosine maps an angle to an X value on the unit circle
ys = np.sin(angles)  # sine maps an angle to a Y value on the unit circle

plt.plot(xs, ys)
plt.show()

print(
''' Well... That was easy. But what the heck is cos and sine?

    The answer is best seen by drawing triangles inside of circles.

    I shall explain on the white board...!

    -----------------------------------------

    SOH : sin = opposite/hypotenuse
    CAH : cos = adjacent/hypotenuse
    TOA : tan = opposite/adjacent

    -----------------------------------------

    Basically,

    x = cos(angle) works because cosine = adjacent / hypotenuse = x / 1
    y = sin(angle) works because cosine = opposite / hypotenuse = y / 1

    if we draw the triangle like this:

          /|
    hyp  / |
        /  | opposite side
        ----
        adj

    where (angle) is measured between the adj and hypotenuse sides

    Notice also that:

        x**2 + y**2 = 1

                which means that

        cos(angle)**2 + sin(angle)**2 = 1    (for any angle)

'''
)

print(
'''

Congratulations!
That's basically all of the really important stuff about trigonometry!


If you ever want to get the ANGLE, and you know the LENGTH,

use angle = arccos(length), or
    angle = arcsin(length), or
    angle = arctan(length),

    which will all work for a certain range of lengths (not all lengths...)

Some extra tidbits:

    - There are these things called "trig identities"...
    - They are used like crazy in calculus and physics...
    - Basically, they boil down to equivalent ways to say exactly the same thing
    - If you want to see most of them, go here:
        https://en.wikipedia.org/wiki/List_of_trigonometric_identities

'''
)
