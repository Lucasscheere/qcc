import pandas as pd
import x_bar
import R_bar
import capability

df = pd.read_csv('dados_simulados.csv')
df.drop('Média', axis=1, inplace=True)

x_bar.plot_xbar(df)

R_bar.plot_r_chart(df)

capability.plot_capability(df, 85, 115)

print(capability.calculate_capability(df, 85, 115))