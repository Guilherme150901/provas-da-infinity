#[PYIA-A12]  Crie uma classe base chamada Veiculo que tenha um método chamado movimentar.
#  Este método deve imprimir a mensagem "Veículo está em movimento." para indicar que qualquer
#  veículo está em movimento. Em seguida, crie duas subclasses chamadas Carro e Moto que herdem
#  de Veiculo. Dentro de cada uma dessas subclasses, sobrescreva o método movimentar para imprimir
#  mensagens específicas para cada tipo de veículo. Na classe Carro, o método movimentar deve imprimir
#  "Carro está dirigindo.", enquanto na classe Moto, o método deve imprimir "Moto está acelerando."

class Veiculo:
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor 

    def movimentar(self):
        return "O veículo está em movimento"

class Carro(Veiculo):
    def movimentar(self):
        return f"O {self.nome} {self.cor} está sendo dirigido!"

class Moto(Veiculo):
    def movimentar(self):
        return f"A {self.nome} {self.cor} está acelerando!"            

nome = input("Digite o nome do veículo: ")
marca = input("Digite a marca do veículo: ")
cor = input("Digite a cor do veículo: ").lower()
veiculo = input("Digite o tipo de veículo (carro ou moto): ").lower()

carro = Carro(nome, marca, cor)
moto = Moto(nome, marca, cor)

if veiculo == "carro":
    print(carro.movimentar())
elif veiculo == "moto":
    print(moto.movimentar())
else:
    print("Tipo de veículo não encontrado")