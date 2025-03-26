import requests
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

    with open('Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf', 'wb') as f1:
        f1.write(anexo1_response.content)
    print('Anexo I baixado com sucesso!')

    with open('Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf', 'wb') as f2:
        f2.write(anexo2_response.content)
    print('Anexo II baixado com sucesso!')
else:
    if not anexo_1:
        print('Anexo I não encontrado!')
    if not anexo_2:
        print('Anexo II não encontrado!')