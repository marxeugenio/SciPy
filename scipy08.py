import numpy as np
from scipy.integrate import quad

def func(x):
    return x ** 2

result, error = quad(func, 0, 1)
print("Resultado da integral: ", result)
