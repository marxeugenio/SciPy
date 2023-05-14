import numpy as np
from scipy.optimize import minimize

def func(x):
    return np.sin(x[0]) * np.cos(x[1]) * (1/(np.abs(x[2]) + 1))

res = minimize(func, [0.5, 0.5, 0.5], method="Nelder-Mead")
print(res.x)