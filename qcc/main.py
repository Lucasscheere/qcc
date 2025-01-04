import pandas as pd
import x_bar
import R_bar
import capability

df = pd.read_csv('./dados_simulados.csv')
df.drop('Média', axis=1, inplace=True)

capability.plot_capability(df, 95, 105)