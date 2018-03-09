

' "pip install sympy" before you do this '
import sympy

x = sympy.Symbol('x')

eq = 2*x - 2
sol=sympy.solve(eq)  # solve for x
print('congratulations:',sol)

y = sympy.Symbol('y')

# this is equig
eq = x**2 + y**2 - 1
sol=sympy.solve(eq)  # solve for x
print('congratulations:',sol)
