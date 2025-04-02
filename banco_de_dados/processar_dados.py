import pandas as pd

file_path = r'D:\teste_nivelamento_programacao\banco_de_dados\data\4T2024.csv'

df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

filtro = df['DESCRICAO'].str.contains('EVENTOS/SINISTROS', case=False, na=False)

print("Valores da coluna 'DESCRICAO' que contêm 'EVENTOS/SINISTROS':")
print(df.loc[filtro, 'DESCRICAO'])