import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Definindo a função a ser minimizada
def funcao_objetivo(x):
    return x**2 + 10*np.sin(x)

# Escolhendo um ponto inicial para otimização
ponto_inicial = 0

# Realizando a otimização
resultado = minimize(funcao_objetivo, ponto_inicial, method='BFGS')

# Extraindo o resultado
minimo_global = resultado.x
valor_minimo = resultado.fun

# Imprimindo o resultado
print(f'Mínimo Global encontrado em x = {minimo_global[0]}, com valor mínimo = {valor_minimo}')

# Criando um gráfico da função
x_vals = np.linspace(-10, 10, 100)
y_vals = funcao_objetivo(x_vals)

plt.plot(x_vals, y_vals, label='Função Objetivo')
plt.scatter(minimo_global, valor_minimo, color='red', marker='o', label='Mínimo Global')
plt.title('Otimização usando SciPy')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
