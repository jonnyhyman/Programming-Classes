' "pip install sympy" before you do any of this '

import sympy  # import the calculator with variable buttons :)

# -------------------------- first, solve the simple equation 2*x=2
x = sympy.Symbol('x')  # create a "symoblic variable" x

equation = 2*x - 2  # define the equation 2*x = 2

solution = sympy.solve(equation, x)  # solve for x

print(solution)  # print the list of all solutions

# -------------------------- next, lets do the equation of a circle
y = sympy.Symbol('y')

equation = x**2 + y**2 - 1**2 # x**2 + y**2 = r**2 where r =1

solution = sympy.solve(equation, y)  # solve for y

print(solution)

# notice how one is the TOP half of the circle
# and the other in the list is the BOTTOM half
