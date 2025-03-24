import flet as ft

def enviarContato(e):
    nome = nome_input.value
    email = email_input.value
    mensagem = mensagem_input.value

    mensagem_salva = f"Formulário enviado com sucesso!\nNome: {nome}\n Email: {email}\n Mensagem: {mensagem}"

    pagina.controls.append(ft.Text(value = mensagem_salva))

    nome_input.value = ""
    email_input.value = ""
    mensagem_input.value = ""

    pagina.update()


def main(page: ft.Page):
    global nome_input, email_input, mensagem_input, pagina 

    pagina = page
    page.title = "Formulário de Contato"

    nome_input = ft.TextField(
        hint_text="Digite o nome do contato",
        bgcolor=ft.Colors.GREY,
        prefix_icon=ft.Icons.ABC_ROUNDED,
        suffix_icon=ft.Icons.EDIT_NOTE_ROUNDED,
        border_radius=ft.border_radius.all(30),
    )

    email_input = ft.TextField(
        hint_text="Digite o e-mail",
        bgcolor=ft.Colors.GREY,
        prefix_icon=ft.Icons.EMAIL,
        suffix_icon=ft.Icons.EDIT_NOTE_ROUNDED,
        border_radius=ft.border_radius.all(30),
    )

    mensagem_input = ft.TextField(
        hint_text="Digite a mensagem",
        bgcolor=ft.Colors.GREY,
        prefix_icon=ft.Icons.MESSAGE,
        suffix_icon=ft.Icons.EDIT_NOTE_ROUNDED,
        border_radius=ft.border_radius.all(30),
        multiline=True
    )

    botao_salvar = ft.ElevatedButton("Salvar", on_click=enviarContato)

    page.add(
        ft.Text(value="Nome:"),
        nome_input,
        ft.Text(value="Email:"),
        email_input,
        ft.Text(value="Mensagem:"),
        mensagem_input,
        botao_salvar
    )

ft.app(target=main)