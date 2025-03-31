import pdfplumber
import pandas as pd
import zipfile
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

caminho_pdf = './web_scraping/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

def processar_pdf(caminho_pdf):
    dados = []
    
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables()  
            for tabela in tabelas:
                for linha in tabela:  
                    dados.append(linha)
    
    colunas = dados[0]  
    df = pd.DataFrame(dados[1:], columns=colunas)

    df.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)
    df["Seg. Odontológica"] = df["Seg. Odontológica"].replace({"OD": "Seg. Odontológica"})
    df["Seg. Ambulatorial"] = df["Seg. Ambulatorial"].replace({"AMB": "Seg. Ambulatorial"})
   
    df.to_csv("teste.csv", index=False, encoding='utf-8')
 
    
    print(f"Foi")

processar_pdf(caminho_pdf)

