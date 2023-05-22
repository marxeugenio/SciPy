import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x,a,b,c):
    return a * np.exp(-b * x) + c

x = np.linspace(0, 4, 50)
y = func(x, 2.5, 1.3, 0.5)

np.random.seed(0)
y_noise = y + 0.2 * np.random.normal(size=len(x))

params, params_covariance = curve_fit(func, x, y_noise)

plt.scatter(x, y_noise, label="Dados com Ruído")
plt.plot(x, func(x, *params), "r", label="Curva Ajustada")
plt.legend()
plt.show()