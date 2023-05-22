from scipy.optimize import minimize

def func(x):
    return (x - 2) ** 2

result = minimize (func, 0)
