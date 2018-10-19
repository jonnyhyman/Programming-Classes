"""
    YOUR CHALLENGES...
    ...IF YOU ACCEPT THEM:

    (in order of SPICYNESS)

    1. TABASCO: Change the points to be different
    2. SRIRACHA: Add more points - see if it can always fit all of them
    3. HABANERO: Change the fit to a different fit algorithm


"""


import numpy as np
import matplotlib.pyplot as plt

# Create a couple of points
points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])

# Get the x and y lists ('vectors'):
# x = [1,2,3,9]
# y = [1,4,1,3]

x = points[:,0]
y = points[:,1]

# calculate "polynomial" (curvy) fit
z = np.polyfit(x, y, 3)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()
