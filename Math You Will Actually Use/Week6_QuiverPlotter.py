'''
==============
3D quiver plot
==============

Demonstrates plotting directional arrows at points on a 3d meshgrid.

YOUR MISSION, if you choose to accept it:

1. Make a tornado shape

2. Make a tornado shape with higher velocity at higher altitude

'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')  # tell matplotlib we're doing a 3d plot

# Make the grid of x y and z points
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
					  np.arange(-0.8, 1, 0.2),
					  np.arange(0, .1, 0.01))

# Make the direction data for each arrows at each x, y, z point
# These are crazy equations. Try messing them up and see what happens!! :)

# U is the x amount for EVERY vector at each X, Y, Z
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)

# V is the y component of EVERY vector at each X, Y, Z
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)

# W is the z component of EVERY vector at each X, Y, Z
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
	 np.sin(np.pi * z))


# TORNADO TIME
u = z*u
v = z*v
w = z*w
# As z gets to zero, u, v and w will be getting closer to zero too
## THE KEY TO MAKING THIS WORK IS normalize = FALSE below!!

# Do the "quiver" plot in 3d, given all of the data
ax.quiver(x, y, z, u, v, w,

            length=0.1,  # set the max length of vector
            normalize=False, # make all vectors same length?

        )

plt.show()
