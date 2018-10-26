

'''

        Your mission.
        If you choose to accept it...

        PLOT
        THE
        PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE

        Challenge 1 TABASCO SPICY:
            Try to figure out how to make the PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE
            niiiiiicee and smoooooth, not some rectangle piece of TRASH

        Challenge 2 HABANERO SPICY:
            Try to figure out how to change the color of it

        Challenge 3 GHOST PEPPER SPICYNESS:
            Give it a completely different shape, such as a chipotle bowl?!?!

'''

# PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE equation is:
# Z = X**2 - Y**2   !! OR !! Z = Y**2 - X**2 (spot the difference...)

from mpl_toolkits.mplot3d import Axes3D  # import the 3D thingy from matplotlib
import matplotlib.pyplot as plt          # import the plotter from matplotlib
from matplotlib import cm                # import matplotlib itself :O

import numpy as np  # import numpy, a really useful math / matrix package


fig = plt.figure()  # create a plot "figure" (window holding our PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE)
ax = fig.gca(projection='3d')  # tell the plot to be 3 dimensional

# Make data.
X = np.arange(-1, 1, 0.25)  # from -1 to 1, at every .25 along the way
Y = np.arange(-1, 1, 0.25)  # from -1 to 1, at every .25 along the way
X, Y = np.meshgrid(X, Y)    # for every x, make a line of ys and vice-a-versa

# Now, for every single X, Y pair, create a 3rd list, Z, which has the value
# for Z of that X,Y pair. If (X,Y) = (2,3), then Z = (2**2 + 3**2) there!

Z = X**2 - Y**2

# Plot the PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE
surf = ax.plot_surface( X, Y, Z,

                        # give it some color !
                        # https://matplotlib.org/users/colormaps.html
                        cmap=cm.coolwarm,
                        linewidth=0,  # how fat should the boundary lines be?
                        antialiased=False,  # make it niiiiiicee and smoooooth?
                        )

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

# FYI, showing the PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE takes upwards of 30 sec
plt.show()
