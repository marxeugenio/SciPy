from scipy.integrate import quad

def func(x):
    return x ** 2

resul, error = quad(func, -1, 1)