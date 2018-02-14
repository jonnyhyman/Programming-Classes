import matplotlib.pyplot as jonnysradplots
# "jonnysradplots" is an "alias" / temporary rename of "matplotlib.pyplot"

xs = range(-50,50 +1) # [-50, -49, -48, ..., 48, 49, 50]
# range() includes the start point, and NOT the end point, so do (start, end+1)

def circle(x, whichhalf):  # this thing is a function

    # equation is x**2 + y**2 = r**2
    # we solved for y, so that we have y = + (r**2 - x**2)**(1/2) for top half
    #                              and y = - (r**2 - x**2)**(1/2) for bot half

    radius = 42

    if whichhalf == 'top':
        return +( (radius)**2 - x**2) ** (1/2)  # 1/2 exponent = square root
    else:
        return -( (radius)**2 - x**2) ** (1/2)

tops = []
for x in xs:
    # add the circle point to the end of the top list
    point = circle(x, 'top')  # assign to point what circle returns
    tops.append(point)

bots = []
for x in xs:
    # add the circle point to the end of the bot list
    point = circle(x, 'bottom')  # assign to point what circle returns
    bots.append(point)

# These two lines are a more "Pythonic" way to do the exact same thing as above
tops = [ circle(x, 'top') for x in xs]     # "for each x, add circle(x) to tops"
bots = [ circle(x, 'bottom') for x in xs]  # "for each x, add circle(x) to bots"

# Now, ladies and gentlemen, we plot!
jonnysradplots.plot(xs,tops)  # plot the tops
jonnysradplots.plot(xs,bots)  # plot the bots (in the same graph)
jonnysradplots.show()  # show the darn thing!
