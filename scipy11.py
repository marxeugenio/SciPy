import numpy as np
from scipy import stats

# Dados de exemplo (pode substituir pelos seus próprios dados)
dados = [10, 12, 15, 13, 14, 12, 11, 9, 15, 13]

# Cálculo da média
media = np.mean(dados)
print("Média:", media)

# Cálculo do desvio padrão
desvio_padrao = np.std(dados)
print("Desvio padrão:", desvio_padrao)

# Cálculo da variância
variancia = np.var(dados)
print("Variância:", variancia)

# Teste de normalidade usando o teste de Shapiro-Wilk
stat, p = stats.shapiro(dados)
print("Estatística do teste de Shapiro-Wilk:", stat)
print("Valor-p:", p)
