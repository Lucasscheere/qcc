import pandas as pd
import numpy as np

# Simular 30 amostras de tamanho 5, com média 100 e desvio padrão 5
np.random.seed(42)
data = np.random.normal(loc=100, scale=5, size=(30, 5))

# Criar um DataFrame
df = pd.DataFrame(data)
df.columns = ['Amostra_' + str(i+1) for i in range(5)]

# Calcular a média de cada amostra
df['Média'] = df.mean(axis=1)

# Salvar em um arquivo CSV
df.to_csv('dados_simulados.csv', index=False)