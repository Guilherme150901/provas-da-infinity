-- [PYIA-A15] Crie uma tabela chamada Clientes com as colunas ID, Nome,Idade
-- e Cidade. Defina a coluna ID como a chave primária e autoincrementável.

CREATE DATABASE IF NOT EXISTS MEUBANCO;
USE meubanco;

CREATE TABLE IF NOT EXISTS clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    idade INT NOT NULL,
    cidade VARCHAR(50) NOT NULL
);
