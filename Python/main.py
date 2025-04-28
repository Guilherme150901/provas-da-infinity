import flet as ft
from datetime import date
from classes import Pessoa, Cliente, Quarto, Reserva, HotelController

def main(page: ft.Page):
    page.title = "🏨 Sistema de Gerenciamento de Hotel"
    page.scroll = "auto"
    page.bgcolor = "#f7f7f7"
    page.padding = 30
    hotel = HotelController()

    # Listagens
    cliente_list = ft.Column()
    quarto_list = ft.Column()
    reserva_list = ft.Column()

    # Funções
    def cadastrar_cliente(nome, telefone, email):
        cliente = hotel.cadastrar_cliente(nome, telefone, email)
        cliente_list.controls.append(ft.Text(f"👤 {cliente.exibir_info()}", color="blue", size=14))
        page.update()

    def cadastrar_quarto(numero, tipo):
        numero = int(numero)
        if any(q._numero == numero for q in hotel.quartos):
            quarto_list.controls.append(ft.Text("⚠️ Número de quarto já cadastrado!", color="red", size=12))
            page.update()
            return

        preco = 220 if tipo == "Duplo" else 150
        quarto = hotel.adicionar_quarto(numero, tipo, preco)
        quarto_list.controls.append(ft.Text(f"🛏️ {quarto.exibir_info()}", color="green", size=14))
        page.update()

    def fazer_reserva(cliente_id, quarto_numero, data_inicio, data_fim):
        try:
            cliente = next((c for c in hotel.clientes if c.get_id() == int(cliente_id)), None)
            quarto = next((q for q in hotel.quartos if q._numero == int(quarto_numero)), None)
            if cliente and quarto:
                reserva = hotel.fazer_reserva(cliente, quarto, data_inicio, data_fim)
                if reserva:
                    reserva_list.controls.append(ft.Text(f"📅 {reserva.exibir_info()}", color="orange", size=14))
                else:
                    reserva_list.controls.append(ft.Text("❌ Quarto não disponível para reserva", color="red", size=12))
            else:
                reserva_list.controls.append(ft.Text("⚠️ Cliente ou quarto não encontrado", color="red", size=12))
            page.update()
        except Exception as e:
            reserva_list.controls.append(ft.Text(f"Erro: {str(e)}", color="red"))
            page.update()

    def editar_reserva(reserva_id, nova_data_inicio, nova_data_fim):
        reserva = next((r for r in hotel.reservas if r._id == int(reserva_id)), None)
        if reserva:
            mensagem = hotel.modificar_reserva(reserva, nova_data_inicio, nova_data_fim)
            reserva_list.controls.append(ft.Text(f"✏️ {mensagem}", color="blue", size=14))
        else:
            reserva_list.controls.append(ft.Text("⚠️ Reserva não encontrada", color="red", size=12))
        page.update()

    # Componentes de entrada
    section_title = lambda text: ft.Text(text, size=20, weight="bold", color="#333", style="italic")

    # Cadastro Cliente
    nome_input = ft.TextField(label="Nome", width=250)
    telefone_input = ft.TextField(label="Telefone", width=250)
    email_input = ft.TextField(label="Email", width=250)
    cadastrar_cliente_btn = ft.ElevatedButton("Cadastrar Cliente", bgcolor="#4CAF50", color="white",
        on_click=lambda e: cadastrar_cliente(nome_input.value, telefone_input.value, email_input.value)
    )

    cliente_section = ft.Column([
        section_title("👤 Cadastro de Cliente"),
        nome_input, telefone_input, email_input,
        cadastrar_cliente_btn, cliente_list
    ], spacing=10)

    # Cadastro Quarto
    numero_quarto_input = ft.TextField(label="Número do Quarto", width=200)
    preco_quarto_output = ft.TextField(label="Preço da Diária", read_only=True, value="R$ 150.00", width=200)

    def atualizar_preco(e):
        preco_quarto_output.value = "R$ 150.00" if tipo_quarto_input.value == "Simples" else "R$ 220.00"
        page.update()

    tipo_quarto_input = ft.Dropdown(
        label="Tipo do Quarto",
        width=200,
        options=[ft.dropdown.Option("Simples"), ft.dropdown.Option("Duplo")],
        on_change=atualizar_preco
    )

    cadastrar_quarto_btn = ft.ElevatedButton("Cadastrar Quarto", bgcolor="#2196F3", color="white",
        on_click=lambda e: cadastrar_quarto(numero_quarto_input.value, tipo_quarto_input.value)
    )

    quarto_section = ft.Column([
        section_title("🛏️ Cadastro de Quarto"),
        ft.Row([numero_quarto_input, tipo_quarto_input, preco_quarto_output], spacing=10),
        cadastrar_quarto_btn,
        quarto_list
    ], spacing=10)

    # Reserva
    cliente_reserva_input = ft.TextField(label="ID do Cliente", width=200)
    numero_quarto_reserva_input = ft.TextField(label="Número do Quarto", width=200)
    data_inicio_reserva_input = ft.TextField(label="Data Início (YYYY-MM-DD)", width=200)
    data_fim_reserva_input = ft.TextField(label="Data Fim (YYYY-MM-DD)", width=200)
    realizar_reserva_btn = ft.ElevatedButton("Realizar Reserva", bgcolor="#FF9800", color="white",
        on_click=lambda e: fazer_reserva(
            cliente_reserva_input.value,
            numero_quarto_reserva_input.value,
            data_inicio_reserva_input.value,
            data_fim_reserva_input.value
        )
    )

    reserva_section = ft.Column([
        section_title("📅 Realizar Reserva"),
        ft.Row([
            cliente_reserva_input,
            numero_quarto_reserva_input,
            data_inicio_reserva_input,
            data_fim_reserva_input
        ], wrap=True, spacing=10),
        realizar_reserva_btn,
        reserva_list
    ], spacing=10)

    # Editar Reserva
    reserva_id_input = ft.TextField(label="ID da Reserva para Edição", width=200)
    nova_data_inicio_input = ft.TextField(label="Nova Data Início (YYYY-MM-DD)", width=200)
    nova_data_fim_input = ft.TextField(label="Nova Data Fim (YYYY-MM-DD)", width=200)
    editar_reserva_btn = ft.ElevatedButton("Editar Reserva", bgcolor="#3F51B5", color="white",
        on_click=lambda e: editar_reserva(
            reserva_id_input.value,
            nova_data_inicio_input.value,
            nova_data_fim_input.value
        )
    )

    editar_reserva_section = ft.Column([
        section_title("✏️ Editar Reserva"),
        ft.Row([reserva_id_input, nova_data_inicio_input, nova_data_fim_input], spacing=10),
        editar_reserva_btn,
        reserva_list
    ], spacing=10)

    # Adicionando tudo à página
    page.add(
        ft.Text("🏨 Bem-vindo ao Hotel Manager!", size=26, weight="bold", color="#444"),
        ft.Divider(),
        cliente_section,
        ft.Divider(),
        quarto_section,
        ft.Divider(),
        reserva_section,
        ft.Divider(),
        editar_reserva_section
    )

ft.app(target=main)
