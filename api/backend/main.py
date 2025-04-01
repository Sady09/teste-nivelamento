from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Permitir somente o frontend do Vue.js
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# Carregar dados do CSV
file_path = "Relatorio_cadop.csv"
df = pd.read_csv(file_path, delimiter=";", encoding="utf-8")

# Remover espaços nos nomes das colunas
df.columns = df.columns.str.strip()

@app.get("/buscar/")
def buscar_operadora(query: str = Query("", min_length=2)):
    """
    Busca operadoras pelo nome fantasia, razão social ou modalidade.
    """
    query = query.strip()
    if not query:
        return {"message": "Nenhum termo de busca fornecido."}
    
    # Garantir que as colunas existem antes de acessar
    colunas_validas = {"Razao_Social", "Nome_Fantasia", "Modalidade"}
    colunas_presentes = colunas_validas.intersection(df.columns)
    
    if not colunas_presentes:
        return {"error": "Colunas necessárias não encontradas no arquivo CSV."}
    
    # Filtrar resultados
    resultados = df[
        df["Razao_Social"].astype(str).str.contains(query, case=False, na=False) |
        df["Nome_Fantasia"].astype(str).str.contains(query, case=False, na=False) |
        df["Modalidade"].astype(str).str.contains(query, case=False, na=False)
    ]
    
    # Substituir NaN por string vazia antes de converter para JSON
    return resultados.fillna("").to_dict(orient="records")