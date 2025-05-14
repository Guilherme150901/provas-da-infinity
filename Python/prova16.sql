USE meubanco;

CREATE TABLE IF NOT EXISTS produtos (
	produtoID INT PRIMARY KEY AUTO_INCREMENT,
    nomeProduto VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL (9,2) NOT NULL,
    CHECK (preco > 0)
);

INSERT INTO produtos(nomeProduto, quantidade, preco) VALUES ("Processador Ryzen 7", 1, 1115.90);
INSERT INTO produtos(nomeProduto, quantidade, preco) VALUES ("Memória Ram 8 GB", 2, 230.00);
INSERT INTO produtos(nomeProduto, quantidade, preco) VALUES ("Placa mãe B450M", 1, 529.99);

SELECT * FROM meubanco.produtos;