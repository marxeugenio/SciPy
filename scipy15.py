import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def create_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = np.array([mandelbrot(complex(x, y), max_iter) for x, y in np.nditer([X, Y])])
    return Z.reshape((width, height))

def plot_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    mandelbrot_set = create_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)
    plt.imshow(mandelbrot_set, extent=(xmin, xmax, ymin, ymax), cmap='viridis', origin='lower')
    plt.colorbar()
    plt.title('Conjunto de Mandelbrot')
    plt.show()

# Parâmetros para o conjunto de Mandelbrot
width, height = 800, 800
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
max_iter = 100

# Plotar o conjunto de Mandelbrot
plot_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)
