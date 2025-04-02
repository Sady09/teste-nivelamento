-- Importação dos dados cadastrais das operadoras
COPY operadoras (
    Registro_ANS, 
    CNPJ, 
    Razao_Social, 
    Nome_Fantasia, 
    Modalidade, 
    Logradouro, 
    Numero, 
    Complemento, 
    Bairro, 
    Cidade, 
    UF, 
    CEP, 
    DDD, 
    Telefone, 
    Fax, 
    Endereco_eletronico, 
    Representante, 
    Cargo_Representante, 
    Regiao_de_Comercializacao, 
    Data_Registro_ANS
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER
QUOTE '"'
ENCODING 'UTF8';

-- Importação dos dados das demonstrações contábeis
COPY demonstracoes_contabeis (
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\1T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis (
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\2t2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis (
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\3T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis (
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\4T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis (
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\1T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis (
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\2T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis (
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\3T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis (
    data, 
    reg_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM 'D:\teste_nivelamento_programacao\banco_de_dados\data\4T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';