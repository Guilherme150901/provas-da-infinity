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
