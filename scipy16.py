import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Função para gerar coordenadas da espiral
def generate_spiral(t, a, b, c):
    x = a * np.sin(b * t)
    y = a * np.cos(b * t)
    z = c * t
    return x, y, z

# Configurações iniciais
a, b, c = 1, 0.1, 0.5
t_max = 50
num_points = 500

# Inicializar o gráfico
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Função de inicialização para criar a linha inicial
def init():
    line, = ax.plot([], [], [], lw=2)
    return line,

# Função de animação
def update(frame):
    t = np.linspace(0, frame, num_points)
    x, y, z = generate_spiral(t, a, b, c)
    line.set_data(x, y)
    line.set_3d_properties(z)
    return line,

# Criar a animação
ani = FuncAnimation(fig, update, frames=np.linspace(0, t_max, num_points), init_func=init, blit=True)

# Mostrar o gráfico
plt.title('Animação de uma Espiral 3D')
plt.show()
