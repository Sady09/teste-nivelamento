📊 Projetos de Análise e Processamento de Dados

📌 Descrição

Este documento descreve uma série de projetos focados em análise e processamento de dados. Cada projeto aborda uma área específica, como web scraping, transformação de dados, criação de APIs e integração de banco de dados.

🚀 Projetos

1️⃣ Web-Scraping com PDFPlumber e Beautiful Soup

📌 Objetivo:
Realizar web scraping de documentos PDF utilizando a biblioteca PDFPlumber e de páginas web utilizando Beautiful Soup. A intenção era extrair informações específicas de PDFs e páginas HTML para posterior análise e processamento.

🔧 Dependências

pdfplumber

beautifulsoup4

requests

📥 Como Baixar as Dependências

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências:

pip install pdfplumber beautifulsoup4 requests

2️⃣ Transformação de Dados com Pandas

📌 Objetivo:
Transformar dados de arquivos CSV utilizando a biblioteca Pandas em Python. Foram realizadas diversas operações de limpeza e transformação nos dados para prepará-los para análise.

🔧 Dependências

pandas

📥 Como Baixar as Dependências

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências:

pip install pandas

3️⃣ API com FastAPI e Front-end com Vue.js

📌 Objetivo:
Este projeto é uma aplicação fullstack, utilizando FastAPI no back-end e Vue.js no front-end. O objetivo é fornecer um sistema de busca de operadoras de saúde a partir de um arquivo CSV. A ideia é disponibilizar uma interface de programação para realizar consultas e obter dados de forma estruturada.

🔧 Dependências

fastapi

uvicorn

Vue.js (frontend)

Node.js e npm/yarn para gerenciar pacotes do Vue

📥 Como Baixar as Dependências e Executar o Projeto

Crie um ambiente virtual (opcional, mas recomendado) e instale as dependências do backend:

python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências do backend:

pip install fastapi uvicorn

Execute a aplicação backend:

uvicorn main:app --reload

Instale as dependências do frontend e execute o servidor Vue:

cd frontend
npm install  # Ou `yarn install` se estiver usando Yarn
npm run dev  # Ou `yarn dev`

✅ O front-end estará disponível em http://localhost:5173 (ou outra porta especificada pelo Vue).

4️⃣ Banco de Dados Incompleto

📌 Objetivo:
Criar um banco de dados estruturado para armazenar e consultar os dados das operadoras de saúde. A ideia era desenvolver queries para estruturar as tabelas necessárias e importar o conteúdo dos arquivos CSV preparados.

⚠️ Desafios Encontrados

🚨 O projeto do banco de dados ficou incompleto, pois não consegui integrar corretamente os diversos arquivos CSV e criar uma estrutura de dados coesa. Além disso, houve dificuldades na padronização dos dados e na elaboração de queries analíticas para responder às perguntas propostas.

📂 Como Baixar os Arquivos do Projeto

Clone o repositório para o seu ambiente local:

git clone https://github.com/Sady09/teste-nivelamento.git
cd teste-nivelamento

📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

🛠️ Desenvolvido com dedicação! 🚀
