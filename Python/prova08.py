#[PYIA-A08] Importe o módulo 'os' e use a função 'listdir' para listar todos os arquivos
# e pastas presentes no diretório onde o script Python está sendo executado. A função 'listdir'
# retornará uma lista contendo os nomes dos arquivos e pastas. Após obter essa lista, exiba cada
# item da lista individualmente na saída do console.

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
