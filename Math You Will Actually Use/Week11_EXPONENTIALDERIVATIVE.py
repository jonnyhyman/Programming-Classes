import sympy

x = sympy.Symbol('x')

expression = sympy.exp(x)

print()
print()
print(expression)

derivative = sympy.diff(expression, x)

print('derivative:', derivative)
