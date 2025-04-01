from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

df = pd.read_csv("Relatorio_cadop.csv", delimiter=";", encoding="utf-8")
df.columns = df.columns.str.strip()

@app.get("/buscar/")
def buscar_operadora(query: str = Query("", min_length=2)):
    query = query.strip()
    if not query:
        return {"message": "Nenhum termo de busca fornecido."}
    
    colunas_validas = {"Razao_Social", "Nome_Fantasia", "Modalidade"}
    colunas_presentes = colunas_validas.intersection(df.columns)
    
    if not colunas_presentes:
        return {"error": "Colunas necessárias não encontradas no arquivo CSV."}
    
    resultados = df[
        df["Razao_Social"].astype(str).str.contains(query, case=False, na=False) |
        df["Nome_Fantasia"].astype(str).str.contains(query, case=False, na=False) |
        df["Modalidade"].astype(str).str.contains(query, case=False, na=False)
    ]
    
    return resultados.fillna("").to_dict(orient="records")