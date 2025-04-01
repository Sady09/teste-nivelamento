import pdfplumber
import pandas as pd
import zipfile
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

caminho_pdf = './web_scraping/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
nome_csv = os.path.join(data_dir, "Teste_Joao_Sady.csv")
nome_zip = os.path.join(data_dir, "Teste_Joao_Sady.zip")

def processar_pdf(caminho_pdf, nome_csv, nome_zip):
    dados = []

    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                tabelas = pagina.extract_tables()  
                for tabela in tabelas:
                    for linha in tabela:  
                        dados.append(linha)
    except:
        print("Execute o web scraping primeiro")
        return
    
    colunas = dados[0]  
    df = pd.DataFrame(dados[1:], columns=colunas)

    df.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)
    df["Seg. Odontológica"] = df["Seg. Odontológica"].replace({"OD": "Seg. Odontológica"})
    df["Seg. Ambulatorial"] = df["Seg. Ambulatorial"].replace({"AMB": "Seg. Ambulatorial"})
   
    df.to_csv(nome_csv, index=False, encoding='utf-8')
    
    with zipfile.ZipFile(os.path.join(data_dir, 'Teste_Joao_Sady.zip'), 'w') as zipf:
        zipf.write(nome_csv, "Teste_Joao_Sady.csv")
    
    print(f"Processamento concluído. CSV salvo em {nome_csv} e compactado como {nome_zip}.")

processar_pdf(caminho_pdf, nome_csv, nome_zip)

