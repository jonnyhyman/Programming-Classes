import numpy as np  # the first thing any starfleet officer does...!
'''
Part 1: Romulans.........................!
'''
x = 1000  # km
y = 500   # km

# since we can may treat the x and y as sides of a triangle,
# we can use the pythagorean theorem to get the hypotenuse (range)!

# range**2 = x**2 + y**2
# range = + sqrt(x**2 + y**2)  ORR!! - sqrt(x**2 + y**2)
# although, the ship probably isn't behind us so ignore the negative sqrt...

range = np.sqrt( np.power(x,2) + np.power(y,2) )  # power == ** ... KAPOW!

print('Captain, the Romulan ship is', range,'kilometers and closing...')

input('ENTER to continue')

'''
Part 2: THE BORG AAAAHHHH!
'''

mark0 = 65  # degrees
mark1 = 55  # degrees
diameter = 3 # kilometers

# step 0: assume the borg ship is coming at you face-on
#        (no angling from your viewpoint)... Makes two triangle angles the same

# step 1: split the (not-90-degree) triangle into two halves, so that
#         in the middle are two 90 degree triangles

# step 2: figure out (mark0 - mark1)/2, the triangle's inner angle

inner = (mark0 - mark1) / 2

# step 3: sin = opp / hyp, in our case sin(inner) = (3km/2) / range
# step 4: solve for range --> range = (diameter/2) / np.sin(np.deg2rad(inner))
# ......... you could use sympy in step 4 but I cheated and used paper ........

range = (diameter/2) / np.sin(np.deg2rad(inner))

print('Captain, the Borg ship is', range, 'kilometers and closing...')

import webbrowser # shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
webbrowser.open('https://media.giphy.com/media/tK3THRanG0d0c/giphy.gif')
