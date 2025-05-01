from datetime import date

class Pessoa:
    def __init__(self, nome, telefone, email):
        self._nome = nome
        self._telefone = telefone
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email

    def exibir_info(self):
        return f"Nome: {self._nome}, Telefone: {self._telefone}, Email: {self._email}"

class Cliente(Pessoa):
    _id_geral = 0

    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)
        Cliente._id_geral += 1
        self._id = Cliente._id_geral

    @property
    def id(self):
        return self._id

    def exibir_info(self):
        return f"Cliente {self._id} - {super().exibir_info()}"

class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self._numero = numero
        self._tipo = tipo
        self._preco = preco_diaria
        self._disponivel = True

    @property
    def numero(self):
        return self._numero

    @property
    def tipo(self):
        return self._tipo

    @property
    def preco(self):
        return self._preco

    def reservar(self):
        self._disponivel = False

    def liberar(self):
        self._disponivel = True

    def esta_disponivel(self):
        return self._disponivel

    def exibir_info(self):
        status = "Disponível" if self._disponivel else "Ocupado"
        return f"Quarto {self._numero} ({self._tipo}) - R${self._preco:.2f} - {status}"

class Reserva:
    def __init__(self, cliente, quarto, data_inicio: date, data_fim: date):
        if data_fim < data_inicio or data_inicio < date.today():
            raise ValueError("Datas inválidas para a reserva.")
        self._cliente = cliente
        self._quarto = quarto
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._status = "Ativa"
        self._quarto.reservar()

    @property
    def data_inicio(self):
        return self._data_inicio

    @property
    def data_fim(self):
        return self._data_fim

    @property
    def status(self):
        return self._status

    def cancelar(self):
        self._status = "Cancelada"
        self._quarto.liberar()

    def modificar(self, nova_data_inicio, nova_data_fim):
        if nova_data_fim < nova_data_inicio or nova_data_inicio < date.today():
            raise ValueError("Datas inválidas para a modificação.")
        self._data_inicio = nova_data_inicio
        self._data_fim = nova_data_fim

    def exibir_info(self):
        return (
            f"Reserva de {self._cliente.exibir_info()} "
            f"no {self._quarto.exibir_info()} "
            f"de {self._data_inicio} até {self._data_fim} - Status: {self._status}"
        )

class HotelController:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def cadastrar_cliente(self, nome, telefone, email):
        cliente = Cliente(nome, telefone, email)
        self.clientes.append(cliente)
        return cliente

    def adicionar_quarto(self, numero, tipo, preco):
        quarto = Quarto(numero, tipo, preco)
        self.quartos.append(quarto)
        return quarto

    def fazer_reserva(self, cliente, quarto, data_ini, data_fim):
        if quarto.esta_disponivel():
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
        return "Reserva cancelada com sucesso."

    def modificar_reserva(self, reserva, nova_data_inicio, nova_data_fim):
        try:
            reserva.modificar(nova_data_inicio, nova_data_fim)
            return "Reserva modificada com sucesso."
        except ValueError as e:
            return str(e)

    def listar_reservas(self):
        return [reserva.exibir_info() for reserva in self.reservas]

    def listar_clientes(self):
        return [cliente.exibir_info() for cliente in self.clientes]

    def listar_quartos(self):
        return [quarto.exibir_info() for quarto in self.quartos]

    def verificar_disponibilidade(self, numero_quarto):
        quarto = self.get_quarto_por_numero(numero_quarto)
        if quarto:
            return "Disponível" if quarto.esta_disponivel() else "Ocupado"
        else:
            return "Quarto não encontrado"

    def get_quarto_por_numero(self, numero):
        return next((q for q in self.quartos if q.numero == numero), None)
