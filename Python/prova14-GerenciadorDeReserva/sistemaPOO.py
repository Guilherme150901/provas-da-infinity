from datetime import date

class Pessoa:
    _contador_id = 0

    def __init__(self, nome, telefone, email):
        Pessoa._contador_id += 1
        self._id = Pessoa._contador_id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    @property
    def id(self):
        return self._id

    def exibir_info(self):
        return f"ID: {self.id} | Nome: {self.nome} - Telefone: {self.telefone} - Email: {self.email}"

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)

class Quarto:
    precos = {
        "single": 230.0,
        "double": 260.0,
        "suite": 290.0
    }

    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.preco = self.precos.get(tipo, 0.0)
        self.disponivel = True

    def reservar(self):
        self.disponivel = False

    def liberar(self):
        self.disponivel = True

class Reserva:
    def __init__(self, cliente, quarto, data_inicio: date, data_fim: date):
        if data_fim <= data_inicio:
            raise ValueError("A data de check-out precisa ser depois da data de check-in.")
        if data_inicio < date.today():
            raise ValueError("A data de check-in não pode ser anterior à data atual.")

        self.cliente = cliente
        self.quarto = quarto
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = "Ativa"
        self.quarto.reservar()

    def cancelar(self):
        self.status = "Cancelada"
        self.quarto.liberar()

    def modificar(self, nova_data_inicio, nova_data_fim):
        if nova_data_fim <= nova_data_inicio:
            raise ValueError("A data de check-out precisa ser depois da data de check-in.")
        if nova_data_inicio < date.today():
            raise ValueError("A data de check-in não pode ser anterior à data atual.")
        self.data_inicio = nova_data_inicio
        self.data_fim = nova_data_fim

class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []
        self._criar_quartos_padrao()

    def _criar_quartos_padrao(self):
        tipos = ["single"] * 5 + ["double"] * 5 + ["suite"] * 5
        for numero, tipo in enumerate(tipos, start=1):
            self.quartos.append(Quarto(numero, tipo))

    def cadastrar_cliente(self, nome, telefone, email):
        cliente = Cliente(nome, telefone, email)
        self.clientes.append(cliente)
        return cliente

    def fazer_reserva(self, cliente, quarto, data_ini, data_fim):
        if quarto.disponivel:
            try:
                reserva = Reserva(cliente, quarto, data_ini, data_fim)
                self.reservas.append(reserva)
                return reserva
            except ValueError as e:
                return str(e)
        else:
            return "Quarto indisponível para reserva."

    def cancelar_reserva(self, reserva):
        reserva.cancelar()
        self.reservas.remove(reserva)

    def modificar_reserva(self, reserva, nova_data_inicio, nova_data_fim):
        try:
            reserva.modificar(nova_data_inicio, nova_data_fim)
            return "Reserva modificada com sucesso."
        except ValueError as e:
            return str(e)

    def get_quarto_por_numero(self, numero):
        return next((q for q in self.quartos if q.numero == numero), None)

    def get_cliente_por_id(self, id_cliente):
        return next((c for c in self.clientes if c.id == id_cliente), None)

    def get_quartos_por_tipo(self, tipo):
        return [q for q in self.quartos if q.tipo == tipo and q.disponivel]

    def tipos_quarto_disponiveis(self):
        return list(Quarto.precos.keys())

    def exibir_reserva(self, reserva):
        return (f"{reserva.cliente.nome} (ID: {reserva.cliente.id})\n"
                f"Quarto {reserva.quarto.numero} ({reserva.quarto.tipo}) - R${reserva.quarto.preco:.2f}\n"
                f"{reserva.data_inicio} até {reserva.data_fim} - Status: {reserva.status}")
