import db
from classes import Produto

def menu():
    print("\n1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Quantidade")
    print("4. Remover Produto")
    print("5. Registrar Venda")
    print("6. Ver Vendas")
    print("7. Sair")
    return input("Escolha uma opção: ")

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    descricao = input("Descrição: ").strip()
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

def remover_produto_usuario():
    try:
        id_produto = int(input("ID do produto a remover: "))
        produto = db.buscar_produto_por_id(id_produto)
        if produto:
            confirmacao = input(f"Tem certeza que deseja remover '{produto.nome}'? (s/n): ").strip().lower()
            if confirmacao == 's':
                db.remover_produto_db(id_produto)
                print(f"Produto '{produto.nome}' removido com sucesso.")
            else:
                print("Remoção cancelada.")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("ID inválido.")

def registrar_venda_usuario():
    try:
        id_produto = int(input("ID do produto vendido: "))
        quantidade = int(input("Quantidade vendida: "))
        sucesso, mensagem = db.registrar_venda(id_produto, quantidade)
        print(mensagem)
    except ValueError:
        print("Dados inválidos. Certifique-se de inserir números.")

def ver_vendas():
    vendas = db.listar_vendas()
    if vendas:
        for venda in vendas:
            print(venda)
    else:
        print("Nenhuma venda registrada.")

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
            remover_produto_usuario()
        elif opcao == "5":
            registrar_venda_usuario()
        elif opcao == "6":
            ver_vendas()
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

