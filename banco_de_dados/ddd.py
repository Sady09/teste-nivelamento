import pandas as pd

# Caminho para o arquivo CSV
file_path = r'D:\teste_nivelamento_programacao\banco_de_dados\data\Relatorio_cadop.csv'

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

# Verificar e corrigir valores problemáticos
df['Numero'] = df['Numero'].fillna('')  # Substituir valores nulos por vazio
df['Numero'] = df['Numero'].astype(str).str.replace(';', '')  # Remover delimitadores extras

# Salvar o arquivo corrigido
df.to_csv(file_path, index=False, sep=';', encoding='utf-8', quoting=1)
print("Arquivo corrigido e salvo.")