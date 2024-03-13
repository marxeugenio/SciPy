import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Criando pontos de dados aleatórios
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Adicionando algum ruído aos pontos de dados
noise = np.random.normal(0, 0.1, y.shape)
y_noisy = y + noise

# Interpolação dos pontos de dados
f = interp1d(x, y_noisy, kind='cubic')

# Criando um conjunto de pontos de dados intermediários para plotagem suave
x_new = np.linspace(0, 10, 100)
y_new = f(x_new)

# Plotagem dos pontos de dados originais, dos pontos de dados ruidosos e da interpolação
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Dados Originais')
plt.plot(x, y_noisy, 'x', label='Dados com Ruído')
plt.plot(x_new, y_new, '-', label='Interpolação Cúbica')
plt.title('Interpolação de Dados Utilizando scipy')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
