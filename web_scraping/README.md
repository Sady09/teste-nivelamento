# Web Scraping e Download de PDFs do Site da ANS

## Descrição

Este projeto realiza o web scraping de uma página da ANS (Agência Nacional de Saúde Suplementar) para encontrar links específicos para documentos em PDF. Ele baixa esses documentos e os compacta em um arquivo ZIP. O projeto utiliza as bibliotecas `requests`, `zipfile`, `os` e `BeautifulSoup` do Python.

## Pré-requisitos

- Python 3.6 ou superior
- As seguintes bibliotecas Python: `requests`, `beautifulsoup4`

## Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

3. Instale as dependências necessárias:

```bash
pip install requests beautifulsoup4
```

## Execução

1. Execute o script principal:

```bash
python main.py
```

## Funcionamento do Script

O script `main.py` realiza as seguintes etapas:

1. Cria o diretório `downloads` se ele não existir.
2. Acessa a página da ANS especificada e faz o scraping do conteúdo HTML.
3. Busca os links para os anexos I e II na página.
4. Baixa os arquivos PDF dos anexos I e II.
5. Salva os arquivos PDF no diretório `downloads`.
6. Compacta os arquivos PDF em um arquivo ZIP.
7. Exibe uma mensagem de conclusão indicando o sucesso das operações.

## Observações

- Caso os links para os anexos não sejam encontrados, o script exibirá uma mensagem de erro correspondente.
- Certifique-se de que o site da ANS está acessível e que os links para os anexos não foram alterados.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
