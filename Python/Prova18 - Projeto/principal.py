import db
from classes import Produto

def menu():
    print("\n1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Quantidade")
    print("4. Remover Produto")
    print("5. Sair")
    return input("Escolha uma opção: ")

def cadastrar_produto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))
    produto = Produto(None, nome, descricao, quantidade, preco)
    db.inserir_produto(produto)
    print(f"Produto '{nome}' cadastrado com sucesso.")

def listar_produtos():
    produtos = db.listar_produtos()
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print("Nenhum produto cadastrado.")

def atualizar_quantidade():
    id_produto = int(input("ID do produto: "))
    quantidade = int(input("Quantidade a adicionar (use número negativo para subtrair): "))
    db.atualizar_quantidade(id_produto, quantidade)
    print(f"Quantidade do produto {id_produto} atualizada.")

def remover_produto():
    id_produto = int(input("ID do produto a remover: "))
    db.remover_produto(id_produto)
    print(f"Produto {id_produto} removido.")

def main():
    db.criar_tabelas()
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_quantidade()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()


