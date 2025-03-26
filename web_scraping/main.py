import requests
import zipfile
from bs4 import BeautifulSoup

r = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
soup = BeautifulSoup(r.text, 'html.parser')

anexo_1 = soup.find('a', href=True, string='Anexo I.')
anexo_2 = soup.find('a', href=True, string='Anexo II.')

if anexo_1 and anexo_2:
    anexo1_url = anexo_1['href']
    anexo2_url = anexo_2['href']

    anexo1_response = requests.get(anexo1_url)
    anexo2_response = requests.get(anexo2_url)

    anexo1_filename = 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    anexo2_filename = 'Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'

    with open(anexo1_filename, 'wb') as f1:
        f1.write(anexo1_response.content)
    print('Anexo I baixado com sucesso!')

    with open(anexo2_filename, 'wb') as f2:
        f2.write(anexo2_response.content)
    print('Anexo II baixado com sucesso!')

    with zipfile.ZipFile('anexos.zip', 'w') as zipf:
        zipf.write(anexo1_filename)
        zipf.write(anexo2_filename)
    print('Arquivos compactados com sucesso em anexos.zip!')
else:
    if not anexo_1:
        print('Anexo I não encontrado!')
    if not anexo_2:
        print('Anexo II não encontrado!')