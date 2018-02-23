
import matplotlib.pyplot as plt

x0 = input("What x should we start at? >> " )
xf = input("What x should we end at? >> ")
eq = input("Type your equation with x! >> " )

# assuming we get something like:
# eq = '2*x'

xs = range(int(x0), int(xf)+1)
ys = []

for x in xs:

    y = eval(eq.replace('x', str(x)))
    ys.append(y)

plt.plot(xs, ys)
plt.show()
