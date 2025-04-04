#[PYIA-A09] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a
# uma lista de tarefas. A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar
# o nome da tarefa e um botão para adicionar a tarefa à lista. Quando o usuário clicar no botão, o item deve ser
# adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. A lista de
# tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.

import flet as ft

def main(page: ft.Page):
    page.title = "Gerenciador de Tarefas"

    tarefas = []
        tarefa = campo_texto.value.strip()  
        if tarefa:  
            tarefas.append(tarefa) 
            campo_texto.value = ""  
            atualizar_tarefas() 

    def atualizar_tarefas():
        lista_tarefas.controls.clear() 

    def adicionar_tarefa(e):
        for tarefa in tarefas:
            lista_tarefas.controls.append(ft.Text(tarefa)) 
        page.update()  

    campo_texto = ft.TextField(label="Digite a tarefa", autofocus=True)

    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)

    lista_tarefas = ft.Column()

    page.add(campo_texto, botao_adicionar, lista_tarefas)

ft.app(target=main)
