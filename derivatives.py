import sympy as sp
from scipy.misc import derivative
x=sp.Symbol('x')
print(sp.diff(3*x**2 +1,x))
def f(x):
    return 3*x**2 +1
print(derivative(f,2))
#in derivatives we have to give a function not equation
#derivatives for numerical derivations
#for equation derivations use sympy run the code for better understanding.
