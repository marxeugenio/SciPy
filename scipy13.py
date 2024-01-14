import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definir uma equação diferencial simples (por exemplo, um oscilador harmônico amortecido)
def harmonic_oscillator(t, y, omega, damping):
    dydt = [y[1], -omega**2 * y[0] - 2 * damping * omega * y[1]]
    return dydt

# Parâmetros do oscilador harmônico amortecido
omega = 1.0  # Frequência angular
damping = 0.1  # Coeficiente de amortecimento

# Condições iniciais
initial_conditions = [1.0, 0.0]

# Tempo de integração
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Resolver a equação diferencial usando solve_ivp
solution = solve_ivp(
    harmonic_oscillator,
    t_span,
    initial_conditions,
    args=(omega, damping),
    t_eval=t_eval,
)

# Extrair resultados da solução
t = solution.t
y = solution.y

# Plotar os resultados
plt.plot(t, y[0], label='Posição')
plt.plot(t, y[1], label='Velocidade')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.title('Oscilador Harmônico Amortecido')
plt.legend()
plt.show()
