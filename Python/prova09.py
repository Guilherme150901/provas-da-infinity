import flet as ft

def main(page: ft.Page):
    page.title = "Gerenciador de Tarefas"

    tarefas = []

    def adicionar_tarefa(e):
        tarefa = campo_texto.value.strip()  
        if tarefa:  
            tarefas.append(tarefa) 
            campo_texto.value = ""  
            atualizar_tarefas() 

    def atualizar_tarefas():
        lista_tarefas.controls.clear() 
        for tarefa in tarefas:
            lista_tarefas.controls.append(ft.Text(tarefa)) 
        page.update()  

    campo_texto = ft.TextField(label="Digite a tarefa", autofocus=True)

    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)

    lista_tarefas = ft.Column()

    page.add(campo_texto, botao_adicionar, lista_tarefas)

ft.app(target=main)
