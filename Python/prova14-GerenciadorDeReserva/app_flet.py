import flet as ft
from datetime import datetime
from sistemaPOO import GerenciadorDeReservas, Reserva

gerenciador = GerenciadorDeReservas()
reserva_em_edicao = {"reserva": None}
cliente_em_edicao = {"cliente": None}

def main(page: ft.Page):
    page.title = "Gerenciador de Reserva"
    page.scroll = "auto"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#e0f7fa"

    def input_style(label):
        return ft.TextField(label=label, filled=True, border_radius=10, bgcolor="#ffffff", border_color="#90caf9")

    def styled_container(content):
        return ft.Container(content=content, padding=15, bgcolor="white", border_radius=12,
                            border=ft.border.all(1, ft.colors.BLUE_GREY_200), margin=10,
                            shadow=ft.BoxShadow(blur_radius=8, color=ft.colors.BLUE_GREY_100))

    nome_input = input_style("Nome")
    telefone_input = input_style("Telefone")
    email_input = input_style("E-mail")
    
    clientes_listagem = ft.Column()

    def atualizar_clientes_listagem():
        clientes_listagem.controls.clear()
        for c in gerenciador.clientes:
            clientes_listagem.controls.append(
                ft.Row([
                    ft.Text(c.exibir_info(), expand=True),
                    ft.IconButton(icon=ft.icons.EDIT, tooltip="Editar", on_click=lambda e, c=c: editar_cliente(c))
                ])
            )
        page.update()

    def cadastrar_cliente(e):
        if not nome_input.value or not telefone_input.value or not email_input.value:
            clientes_listagem.controls.append(ft.Text("Todos os campos são obrigatórios!", color="red"))
        else:
            if cliente_em_edicao["cliente"]:
                cliente = cliente_em_edicao["cliente"]
                cliente.nome = nome_input.value
                cliente.telefone = telefone_input.value
                cliente.email = email_input.value
                cliente_em_edicao["cliente"] = None
            else:
                gerenciador.cadastrar_cliente(nome_input.value, telefone_input.value, email_input.value)

            nome_input.value = telefone_input.value = email_input.value = ""
            atualizar_clientes_listagem()
        page.update()

    def editar_cliente(cliente):
        cliente_em_edicao["cliente"] = cliente
        nome_input.value = cliente.nome
        telefone_input.value = cliente.telefone
        email_input.value = cliente.email
        page.update()

    id_cliente_input = input_style("ID do Cliente")
    id_cliente_input.width = 180

    tipo_quarto_dropdown = ft.Dropdown(
        label="Tipo de Quarto",
        options=[ft.dropdown.Option(tipo) for tipo in gerenciador.tipos_quarto_disponiveis()],
        on_change=lambda e: atualizar_quartos(e.control.value),
        width=180
    )

    numero_quarto_dropdown = ft.Dropdown(label="Número do Quarto", width=180)
    preco_input = ft.TextField(label="Preço (R$)", read_only=True, width=180, filled=True, bgcolor="#f1f8e9")

    def atualizar_quartos(tipo):
        numero_quarto_dropdown.options.clear()
        quartos = gerenciador.get_quartos_por_tipo(tipo)
        if quartos:
            numero_quarto_dropdown.options.extend([ft.dropdown.Option(str(q.numero)) for q in quartos])
            preco_input.value = str(quartos[0].preco)
        else:
            preco_input.value = "Indisponível"
        page.update()

    data_checkin = input_style("Data Check-in (YYYY-MM-DD)")
    data_checkout = input_style("Data Check-out (YYYY-MM-DD)")

    reservas_info = ft.Column()

    def mostrar_reserva(reserva):
        info = gerenciador.exibir_reserva(reserva)
        texto = ft.Text(info, selectable=True, size=16)

        editar_btn = ft.ElevatedButton("Editar", icon="EDIT", on_click=lambda _: editar_reserva(reserva))
        excluir_btn = ft.OutlinedButton("Excluir", icon="DELETE", on_click=lambda _: excluir_reserva(reserva))

        return styled_container(ft.Column([
            texto,
            ft.Row([editar_btn, excluir_btn], alignment=ft.MainAxisAlignment.END)
        ]))

    def fazer_reserva(e):
        try:
            cliente = gerenciador.get_cliente_por_id(int(id_cliente_input.value))
            if not cliente:
                reservas_info.controls.append(ft.Text("Cliente não encontrado!", color="red"))
                return

            quarto = gerenciador.get_quarto_por_numero(int(numero_quarto_dropdown.value))
            checkin = datetime.strptime(data_checkin.value, "%Y-%m-%d").date()
            checkout = datetime.strptime(data_checkout.value, "%Y-%m-%d").date()

            if reserva_em_edicao["reserva"]:
                resultado = gerenciador.modificar_reserva(reserva_em_edicao["reserva"], checkin, checkout)
                reservas_info.controls.clear()
                reservas_info.controls.extend([mostrar_reserva(r) for r in gerenciador.reservas])
                reserva_em_edicao["reserva"] = None
            else:
                resultado = gerenciador.fazer_reserva(cliente, quarto, checkin, checkout)
                if isinstance(resultado, Reserva):
                    reservas_info.controls.append(mostrar_reserva(resultado))
                else:
                    reservas_info.controls.append(ft.Text(resultado, color="red"))

            id_cliente_input.value = ""
            tipo_quarto_dropdown.value = ""
            numero_quarto_dropdown.value = ""
            preco_input.value = ""
            data_checkin.value = ""
            data_checkout.value = ""
            page.update()

        except Exception as ex:
            reservas_info.controls.append(ft.Text(f"Erro: {str(ex)}", color="red"))
            page.update()

    def editar_reserva(reserva):
        reserva_em_edicao["reserva"] = reserva
        id_cliente_input.value = str(reserva.cliente.id)
        tipo_quarto_dropdown.value = reserva.quarto.tipo
        atualizar_quartos(reserva.quarto.tipo)
        numero_quarto_dropdown.value = str(reserva.quarto.numero)
        preco_input.value = str(reserva.quarto.preco)
        data_checkin.value = str(reserva.data_inicio)
        data_checkout.value = str(reserva.data_fim)
        page.update()

    def excluir_reserva(reserva):
        gerenciador.cancelar_reserva(reserva)
        reservas_info.controls.clear()
        reservas_info.controls.extend([mostrar_reserva(r) for r in gerenciador.reservas])
        page.update()

    page.add(
        ft.Column([
            ft.Text("Hotel Boutique", size=32, weight=ft.FontWeight.BOLD, text_align="center"),
            styled_container(ft.Column([
                ft.Text("Cadastro de Cliente", size=20, weight=ft.FontWeight.W_600),
                nome_input, telefone_input, email_input,
                ft.ElevatedButton("Cadastrar Cliente", on_click=cadastrar_cliente),
                ft.Text("Clientes Cadastrados:", size=16, weight=ft.FontWeight.BOLD),
                clientes_listagem
            ])),
            styled_container(ft.Column([
                ft.Text("Fazer Reserva", size=20, weight=ft.FontWeight.W_600),
                ft.Row([id_cliente_input, tipo_quarto_dropdown]),
                ft.Row([numero_quarto_dropdown, preco_input]),
                ft.Row([data_checkin, data_checkout]),
                ft.ElevatedButton("Fazer Reserva", on_click=fazer_reserva),
            ])),
            ft.Text("Reservas Atuais", size=24, weight=ft.FontWeight.BOLD),
            reservas_info
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=700
        )
    )

    atualizar_clientes_listagem()

ft.app(target=main)
