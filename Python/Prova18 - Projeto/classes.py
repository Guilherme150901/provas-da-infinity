from datetime import datetime

class Produto:
    def __init__(self, id_produto, nome, descricao, quantidade, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"ID{self.id_produto} - {self.nome}: {self.quantidade} em estoque, R$ {self.preco:.2f}"

    def atualizar_quantidade(self, quantidade):
        self.quantidade += quantidade
        if self.quantidade < 0:
            self.quantidade = 0
            return f"Estoque insuficiente para {self.nome}. Quantidade ajustada para 0."

class Venda:
    def __init__(self, id_venda, id_produto, quantidade_vendida, data_venda):
        self.id_venda = id_venda
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda

    def __str__(self):
        return f"Venda {self.id_venda} | Produto ID {self.id_produto} | Quantidade: {self.quantidade_vendida} | Data: {self.data_venda}"
