import requests
import zipfile
import os
from bs4 import BeautifulSoup

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

current_dir = os.path.dirname(os.path.abspath(__file__))
downloads_dir = os.path.join(current_dir, 'downloads')
os.makedirs(downloads_dir, exist_ok=True)

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

anexo_1 = soup.find('a', href=True, string='Anexo I.')
anexo_2 = soup.find('a', href=True, string='Anexo II.')

if anexo_1 and anexo_2:
    anexo1_url = anexo_1['href']
    anexo2_url = anexo_2['href']

    anexo1_response = requests.get(anexo1_url)
    anexo2_response = requests.get(anexo2_url)

    anexo1_filename = os.path.join(downloads_dir, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')
    anexo2_filename = os.path.join(downloads_dir, 'Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf')

    with open(anexo1_filename, 'wb') as f1:
        f1.write(anexo1_response.content)
    print('Anexo I baixado com sucesso!')

    with open(anexo2_filename, 'wb') as f2:
        f2.write(anexo2_response.content)
    print('Anexo II baixado com sucesso!')

    with zipfile.ZipFile(os.path.join(downloads_dir, 'anexos.zip'), 'w') as zipf:
        zipf.write(anexo1_filename, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')
        zipf.write(anexo2_filename, 'Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf')
    print('Arquivos compactados com sucesso em anexos.zip!')
else:
    if not anexo_1:
        print('Anexo I não encontrado!')
    if not anexo_2:
        print('Anexo II não encontrado!')