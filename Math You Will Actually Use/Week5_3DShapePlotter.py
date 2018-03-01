

'''

        Your mission.
        If you choose to accept it...

        PLOT
        THE
        PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE

        Challenge 1:
            Try to figure out how to make the PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE
            niiiiiicee and smoooooth, not some rectange piece of TRASH

        Challenge 2:
            Try to figure out how to change the color of it

        Challenge 3:
            Try to figure out how to make it CIRCULAR (from above)
            instead of some kind of rectangular piece of TRASH
                (these aren't pita chips, after all...)

'''

# PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE equation is:
# Z = X**2 - Y**2   !! OR !! Z = Y**2 - X**2 (spot the difference...)

from mpl_toolkits.mplot3d import Axes3D  # import the 3D thingy from matplotlib
import matplotlib.pyplot as plt          # import the plotter from matplotlib
from matplotlib import cm                # import matplotlib itself :O
from matplotlib.ticker import LinearLocator, FormatStrFormatter
# I have no clue what the above line does...

import numpy as np  # import numpy, a really useful math / matrix package


fig = plt.figure()  # create a plot "figure" (window holding our PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE)
ax = fig.gca(projection='3d')  # tell the plot to be 3 dimensional

# Make data.
X = np.arange(-1, 1, 0.25)  # from -5 to 5, at every .25 along the way
Y = np.arange(-1, 1, 0.25)  # from -5 to 5, at every .25 along the way
X, Y = np.meshgrid(X, Y)    # for every x, make a line of ys and vice-a-versa
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
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

# FYI, showing the PRINGLLLLLLEEEEEEEEEEEEEEEEEEEEE takes upwards of 30 sec
plt.show()
