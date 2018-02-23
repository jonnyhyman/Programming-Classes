import matplotlib.pyplot as plt

# Let the user input an equation
userTyped = input('Type your equation here! : ')

xs = range(0, 100)  # take a range of xs from 0 to 99

ys = [] # get ready to fill ys
for x in xs:
    # figure out the y value for this x
    y_value = userTyped.replace('x', str(x))
    y_value = eval(y_value)  # do the math
    ys.append(y_value)  # add the y value to end of list

plt.plot(xs, ys)
plt.show()
