CREATE DATABASE IF NOT EXISTS PROVASQL;
USE PROVASQL;

CREATE TABLE IF NOT EXISTS produtos (
    produtoID INT PRIMARY KEY,
    nomeProduto VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS fornecedores (
    fornecedorID INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS estoque (
    estoqueID INT PRIMARY KEY AUTO_INCREMENT,
    produtoID INT NOT NULL,
    fornecedorID INT NOT NULL,
    quantidade INT NOT NULL,
    dataEntrada DATE NOT NULL,
    FOREIGN KEY (produtoID) REFERENCES produtos (produtoID),
    FOREIGN KEY (fornecedorID) REFERENCES fornecedores (fornecedorID)
);

INSERT INTO produtos VALUES (1, 'Notebook'), (2, 'Mouse');
INSERT INTO fornecedores VALUES (1), (2);
INSERT INTO estoque (produtoID, fornecedorID, quantidade, dataEntrada)
VALUES
  (1, 1, 10, '2025-05-01'),
  (2, 2, 50, '2025-05-02'),
  (1, 1, 5,  '2025-05-10');

SELECT e.EstoqueID, e.ProdutoID, p.NomeProduto, e.Quantidade, e.DataEntrada
FROM Estoque e
LEFT JOIN Produtos p ON e.ProdutoID = p.ProdutoID
UNION
SELECT e.EstoqueID, e.ProdutoID, p.NomeProduto, e.Quantidade, e.DataEntrada
FROM Estoque e
RIGHT JOIN Produtos p ON e.ProdutoID = p.ProdutoID;

SELECT 
    p.nomeProduto,
    SUM(e.quantidade) AS totalRecebido
FROM estoque e
JOIN produtos p ON e.produtoID = p.produtoID
GROUP BY e.produtoID;

ALTER TABLE estoque ADD observacao VARCHAR(255);