# Projetos de Análise e Processamento de Dados

## Descrição

Este documento descreve uma série de projetos focados em análise e processamento de dados. Cada projeto aborda uma área específica, como web scraping, transformação de dados, criação de APIs e integração de banco de dados.

## Projetos

### 1. Web-Scraping com PDFPlumber e Beautiful Soup

Este projeto tinha como objetivo realizar web scraping de documentos PDF utilizando a biblioteca PDFPlumber e de páginas web utilizando Beautiful Soup. A intenção era extrair informações específicas de PDFs e páginas HTML para posterior análise e processamento.

#### Desafios Encontrados
Apesar das tentativas de extrair dados de PDFs e páginas web, não consegui obter os resultados esperados. As dificuldades incluíam a formatação inconsistente dos dados nos PDFs e a complexidade das estruturas HTML das páginas web.

#### Dependências
- pdfplumber
- beautifulsoup4
- requests

#### Como Baixar as Dependências

1. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

2. Instale as dependências:

```bash
pip install pdfplumber beautifulsoup4 requests
```

### 2. Transformação de Dados com Pandas

Neste projeto, o objetivo foi transformar dados de arquivos CSV utilizando a biblioteca Pandas em Python. Foram realizadas diversas operações de limpeza e transformação nos dados para prepará-los para análise.

#### Desafios Encontrados
Embora várias abordagens tenham sido tentadas, não consegui integrar corretamente os diversos arquivos CSV que vieram separados e formatá-los de forma adequada. As dificuldades envolveram a padronização dos dados, tratamento de valores faltantes e a unificação dos diversos arquivos em uma única estrutura de dados coesa.

#### Dependências
- pandas

#### Como Baixar as Dependências

1. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

2. Instale as dependências:

```bash
pip install pandas
```

### 3. API com FastAPI

O projeto de API utilizou FastAPI para criar um backend que fornecesse um sistema de busca de operadoras de saúde a partir de um arquivo CSV. A ideia era disponibilizar uma interface de programação para realizar consultas e obter dados de forma estruturada.

#### Desafios Encontrados
Não foi possível concluir a implementação da API devido a dificuldades na integração dos dados e na configuração correta do backend.

#### Dependências
- fastapi
- uvicorn

#### Como Baixar as Dependências

1. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

2. Instale as dependências:

```bash
pip install fastapi uvicorn
```

3. Execute a aplicação backend:

```bash
uvicorn main:app --reload
```

### 4. Banco de Dados Incompleto

Este projeto visava a criação de um banco de dados estruturado para armazenar e consultar os dados das operadoras de saúde. A ideia era desenvolver queries para estruturar as tabelas necessárias e importar o conteúdo dos arquivos CSV preparados.

#### Desafios Encontrados
O projeto do banco de dados ficou incompleto, pois não consegui integrar corretamente os diversos arquivos CSV e criar uma estrutura de dados coesa. Além disso, houve dificuldades na padronização dos dados e na elaboração de queries analíticas para responder às perguntas propostas.

## Como Baixar os Arquivos do Projeto

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/Sady09/teste-nivelamento.git
cd teste-nivelamento
```

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
