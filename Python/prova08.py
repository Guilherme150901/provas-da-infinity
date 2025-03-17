import os

def listar_itens(diretorio):
    itens = os.listdir(diretorio)

    for item in itens:
        caminho_item = os.path.join(diretorio, item)
        
        if os.path.isdir(caminho_item):
            print(f"Diretório: {item}")
            listar_itens(caminho_item)  
        elif os.path.isfile(caminho_item):
            print(f"Arquivo: {item}")

diretorio_atual = os.getcwd()
listar_itens(diretorio_atual)
