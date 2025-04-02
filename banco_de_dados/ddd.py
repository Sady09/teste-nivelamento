import pandas as pd

file_path = r'D:\teste_nivelamento_programacao\banco_de_dados\data\Relatorio_cadop.csv'

df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

df['Numero'] = df['Numero'].fillna('')
df['Numero'] = df['Numero'].astype(str).str.replace(';', '')

df.to_csv(file_path, index=False, sep=';', encoding='utf-8', quoting=1)
print("Arquivo corrigido e salvo.")