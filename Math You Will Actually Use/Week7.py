import sympy  # import the calculator with variable buttons :)
from sympy import Symbol, symbols

# -------------------------- first, solve the simple equation 2*x=2
x, y = symbols('x y')  # plural

# -------------------------- next, lets do the equation of a circle


equation = 2**x + x*y**2 - 1 # x**2 + y**2 = r**2 where r =1

solution = sympy.solve(equation, y)  # solve for y

print(solution)

# notice how one is the TOP half of the circle
# and the other in the list is the BOTTOM half
phi
e**z
exp(z)
