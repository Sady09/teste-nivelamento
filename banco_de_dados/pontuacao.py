import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')

csv_files = [
    os.path.join(data_dir, '1T2023.csv'),
    os.path.join(data_dir, '2T2023.csv'),
    os.path.join(data_dir, '3T2023.csv'),
    os.path.join(data_dir, '4T2023.csv'),
    os.path.join(data_dir, '1T2024.csv'),
    os.path.join(data_dir, '2T2024.csv'),
    os.path.join(data_dir, '3T2024.csv'),
    os.path.join(data_dir, '4T2024.csv'),
]

for file in csv_files:
    df = pd.read_csv(file, delimiter=';', encoding='utf-8')
    df = df.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
    df.to_csv(file, index=False, sep=';', encoding='utf-8')

print("Substituição concluída!")