from scipy.optimize import bisect

def f(x):
    return x ** 3 - 3 * x + 1

x = bisect(f, 0, 2)
print(x)