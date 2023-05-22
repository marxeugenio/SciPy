import numpy as np
from scipy.interpolate import interp1d

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 4, 6, 8, 10])

f = interp1d(x, y, kind="linear")

x_new = 2.5
y_new = f(x_new)
print("Valor interpolado em", x_new, ":", y_new)
