import scipy.integrate as spi

def func(x):
    return x ** 2 + 1

integral, error = spi.quad(func, 0, 2)
print(integral)