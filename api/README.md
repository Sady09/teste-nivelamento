# Projeto Full-Stack com FastAPI (Backend) e Vue.js (Frontend)

## Descrição

Este é um projeto full-stack que utiliza FastAPI para o backend e Vue.js para o frontend. O objetivo do projeto é fornecer um sistema de busca de operadoras de saúde a partir de um arquivo CSV.

## Tecnologias Utilizadas

- **Backend**: Python, FastAPI, Pandas
- **Frontend**: Vue.js

## Configuração e Execução

### Backend

1. Navegue até o diretório `backend`:

```bash
cd backend
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação backend:

```bash
uvicorn main:app --reload
```

### Frontend

1. Navegue até o diretório `frontend`:

```bash
cd frontend
```

2. Instale as dependências:

```bash
npm install
```

3. Execute a aplicação frontend:

```bash
npm run serve
```

## Observações

- Certifique-se de que o arquivo CSV `Relatorio_cadop.csv` está localizado no diretório `backend`.
- Caso as colunas necessárias não sejam encontradas no arquivo CSV, o backend retornará um erro.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
