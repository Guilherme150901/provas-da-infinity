from datetime import date

class Pessoa:
    """
    Classe que representa uma pessoa com informações básicas como nome, telefone e email.
    """
    def __init__(self, nome, telefone, email):
        """
        Inicializa a instância com nome, telefone e email.
        Args:
            nome: Nome da pessoa.
            telefone: Número de telefone da pessoa.
            email: Email da pessoa.
        """
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def exibir_info(self):
        """
        Exibe as informações da pessoa, como nome, telefone e email.
        Retorna uma string com as informações detalhadas da pessoa.
        """
        return f"Nome: {self._nome}, Telefone: {self._telefone}, Email: {self._email}"

class Cliente(Pessoa):
    """
    Classe que representa um cliente do hotel. Herda de 'Pessoa' e adiciona um identificador único para cada cliente.
    """
    _id_geral = 0  # ID geral que será incrementado para cada cliente criado

    def __init__(self, nome, telefone, email):
        """
        Inicializa a instância de Cliente e atribui um identificador único.
        Args:
            nome: Nome do cliente.
            telefone: Número de telefone do cliente.
            email: Email do cliente.
        """
        super().__init__(nome, telefone, email)  # Chama o construtor da classe base 'Pessoa'
        Cliente._id_geral += 1
        self._id = Cliente._id_geral  # Atribui um ID único para o cliente

    def get_id(self):
        """
        Retorna o identificador único do cliente.
        Retorna o ID único do cliente.
        """
        return self._id

    def exibir_info(self):
        """
        Exibe as informações do cliente, incluindo seu ID único.
        Retorna uma string com as informações detalhadas do cliente.
        """
        return f"Cliente{self._id} - " + super().exibir_info()

class Quarto:
    """
    Classe que representa um quarto do hotel, incluindo o número, tipo, preço da diária e o status de disponibilidade.
    """
    def __init__(self, numero, tipo, preco_diaria):
        """
        Inicializa a instância de Quarto.
        Args:
            numero: Número do quarto.
            tipo: Tipo do quarto ('Simples', 'Duplo').
            preco_diaria: Preço da diária para o quarto.
        """
        self._numero = numero
        self._tipo = tipo
        self._preco = preco_diaria
        self._disponivel = True  # Quarto disponível inicialmente

    def reservar(self):
        """
        Marca o quarto como ocupado (não disponível).
        """
        self._disponivel = False

    def liberar(self):
        """
        Marca o quarto como disponível.
        """
        self._disponivel = True

    def esta_disponivel(self):
        """
        Verifica se o quarto está disponível.
        Retorna um valor booleano indicando se o quarto está disponível.
        """
        return self._disponivel

    def exibir_info(self):
        """
        Exibe as informações do quarto, incluindo seu status de disponibilidade.
        Retorna uma string com o número, tipo, preço e status do quarto (se está disponível ou ocupado).
        """
        status = "Disponível" if self._disponivel else "Ocupado"
        return f"Quarto {self._numero} ({self._tipo}) - R${self._preco:.2f} - {status}"

class Reserva:
    """
    Classe que representa uma reserva de um cliente em um quarto do hotel, incluindo as datas de início e fim da reserva.
    """
    def __init__(self, cliente, quarto, data_inicio: date, data_fim: date):
        """
        Inicializa a instância de Reserva.
        Args:
            cliente: O cliente que está fazendo a reserva.
            quarto: O quarto que está sendo reservado.
            data_inicio: A data de início da reserva.
            data_fim: A data de término da reserva.
        """
        self._cliente = cliente
        self._quarto = quarto
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._status = "Ativa"  # Status da reserva (ativa inicialmente)

        self._quarto.reservar()  # Marca o quarto como ocupado

    def cancelar(self):
        """
        Cancela a reserva e libera o quarto.
        """
        self._status = "Cancelada"
        self._quarto.liberar()

    def modificar(self, nova_data_inicio, nova_data_fim):
        """
        Modifica as datas de início e fim da reserva.
        Args:
            nova_data_inicio: A nova data de início da reserva.
            nova_data_fim: A nova data de fim da reserva.
        """
        self._data_inicio = nova_data_inicio
        self._data_fim = nova_data_fim

    def get_data_inicio(self):
        """
        Retorna a data de início da reserva.
        """
        return self._data_inicio

    def get_data_fim(self):
        """
        Retorna a data de fim da reserva.
        """
        return self._data_fim

    def exibir_info(self):
        """
        Exibe as informações da reserva, incluindo o cliente, o quarto e o status da reserva.
        Retorna uma string com as informações detalhadas da reserva.
        """
        return (
            f"Reserva de {self._cliente.exibir_info()} "
            f"no {self._quarto.exibir_info()} "
            f"de {self._data_inicio} até {self._data_fim} - Status: {self._status}"
        )


class HotelController:
    """
    Classe que gerencia o hotel, incluindo clientes, quartos e reservas. Possui métodos para cadastrar clientes, 
    adicionar quartos, fazer reservas e listar informações.
    """
    def __init__(self):
        """
        Inicializa a instância de HotelController, com listas para clientes, quartos e reservas.
        """
        self.clientes = []  # Lista de clientes do hotel
        self.quartos = []  # Lista de quartos do hotel
        self.reservas = []  # Lista de reservas feitas

    def cadastrar_cliente(self, nome, telefone, email):
        """
        Cadastra um novo cliente no sistema.
        Args:
            nome: Nome do cliente.
            telefone: Número de telefone do cliente.
            email: Email do cliente.
        Retorna o objeto Cliente criado e adicionado à lista de clientes.
        """
        cliente = Cliente(nome, telefone, email)
        self.clientes.append(cliente)
        return cliente

    def adicionar_quarto(self, numero, tipo, preco):
        """
        Adiciona um novo quarto ao hotel.
        Args:
            numero: Número do quarto.
            tipo: Tipo do quarto (ex: 'Simples', 'Duplo').
            preco: Preço da diária para o quarto.
        Retorna o objeto Quarto criado e adicionado à lista de quartos.
        """
        quarto = Quarto(numero, tipo, preco)
        self.quartos.append(quarto)
        return quarto

    def fazer_reserva(self, cliente, quarto, data_ini, data_fim):
        """
        Faz uma nova reserva de um quarto para um cliente.
        Args:
            cliente: O cliente que fará a reserva.
            quarto: O quarto que será reservado.
            data_ini: Data de início da reserva.
            data_fim: Data de fim da reserva.
        Retorna o objeto Reserva criado, caso o quarto esteja disponível. Caso contrário, retorna None.
        """
        if quarto.esta_disponivel():
            reserva = Reserva(cliente, quarto, data_ini, data_fim)
            self.reservas.append(reserva)
            return reserva
        else:
            return None

    def cancelar_reserva(self, reserva):
        """
        Cancela uma reserva existente.
        Retorna uma mensagem informando que a reserva foi cancelada com sucesso.
        """
        reserva.cancelar()
        return "Reserva cancelada com sucesso."

    def modificar_reserva(self, reserva, nova_data_inicio, nova_data_fim):
        """
        Modifica a data de uma reserva existente.
        Args:
            reserva: A reserva a ser modificada.
            nova_data_inicio: Nova data de início da reserva.
            nova_data_fim: Nova data de fim da reserva.
        Retorna uma mensagem informando que a reserva foi modificada.
        """
        reserva.modificar(nova_data_inicio, nova_data_fim)
        return f"Reserva modificada de {reserva._data_inicio} para {nova_data_inicio}."

    def listar_reservas(self):
        """
        Lista todas as reservas no sistema.
        Retorna uma lista de informações detalhadas de todas as reservas.
        """
        return [reserva.exibir_info() for reserva in self.reservas]

    def listar_clientes(self):
        """
        Lista todos os clientes cadastrados no sistema.
        Retorna uma lista de informações detalhadas de todos os clientes.
        """
        return [cliente.exibir_info() for cliente in self.clientes]

    def listar_quartos(self):
        """
        Lista todos os quartos cadastrados no sistema.
        Retorna uma lista de informações detalhadas de todos os quartos.
        """
        return [quarto.exibir_info() for quarto in self.quartos]

    def verificar_disponibilidade(self, numero_quarto):
        """
        Verifica a disponibilidade de um quarto específico.
        Args:
            numero_quarto: Número do quarto a ser verificado.
        Retorna uma mensagem indicando se o quarto está disponível ou ocupado.
        """
        quarto = next((q for q in self.quartos if q._numero == numero_quarto), None)
        if quarto:
            return "Disponível" if quarto.esta_disponivel() else "Ocupado"
        else:
            return "Quarto não encontrado"