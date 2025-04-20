#1[PYIA-A13] Crie uma classe chamada ContaBancaria que tenha dois atributos privados,
# _saldo e _titular. O atributo _saldo deve armazenar o saldo da conta, enquanto o 
# atributo _titular deve armazenar o nome do titular da conta. Para interagir com esses
# atributos, implemente métodos públicos que permitam realizar operações bancárias. Crie
# um método depositar que permita adicionar um valor ao saldo, um método sacar que permita
# retirar um valor do saldo (caso haja saldo suficiente), e um método exibir_saldo que exiba
# o saldo atual da conta. Utilize métodos para encapsular o acesso ao saldo, garantindo que ele
# só possa ser alterado de maneira controlada pelos métodos de depósito e saque.

class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.__titular = titular 
        self.__saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo!")
    
    def sacar (self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")
    
    def exibirSaldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")

nome = input("Digite o nome do titular da conta: ")
conta = ContaBancaria(nome)

while True:
    print(f"\nBem-vindo ao banco {nome}!")
    operacao = int(input("Escolha uma operação:\n1- Depositar\n2- Sacar\n3- Exibir saldo\n4- Sair\n"))

    if operacao == 1:
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)
    elif operacao == 2:
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
    elif operacao == 3:
        conta.exibirSaldo()
    elif operacao == 4:
        print("Obrigado por utilizar nosso banco. Até mais!")
        break
    else:
        print("Operação inválida. Tente novamente.")
