import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Sistema de equações diferenciais não lineares (exemplo: sistema de Lotka-Volterra)
def lotka_volterra(t, y, alpha, beta, delta, gamma):
    x, y = y
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Parâmetros do sistema Lotka-Volterra
alpha = 0.1
beta = 0.02
delta = 0.01
gamma = 0.1

# Condições iniciais
initial_conditions = [40, 9]

# Tempo de integração
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Resolver o sistema de equações diferenciais usando solve_ivp
solution = solve_ivp(
    lotka_volterra,
    t_span,
    initial_conditions,
    args=(alpha, beta, delta, gamma),
    t_eval=t_eval,
)

# Extrair resultados da solução
t = solution.t
x, y = solution.y

# Plotar os resultados
plt.plot(t, x, label='Presas (x)')
plt.plot(t, y, label='Predadores (y)')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Modelo Lotka-Volterra')
plt.legend()
plt.show()
