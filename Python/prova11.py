#[PYIA-A11] Crie uma classe base chamada Animal que tenha um método chamado falar,
# o qual imprime uma mensagem genérica, como "Este animal faz um som." Em seguida, 
# crie duas subclasses chamadas Cachorro e Gato que herdem de Animal. Dentro de cada
# uma dessas subclasses, sobrescreva o método falar para que ele imprima uma mensagem 
# específica para cada animal. Por exemplo, na classe Cachorro, o método falar pode imprimir
# "O cachorro late." e, na classe Gato, pode imprimir "O gato mia."

class Animal: 
    def falar(self):
        return "Este animal faz um som!"
            
class Cachorro(Animal):
    def falar(self):
        return "O cachorro late!"
        
class Gato(Animal):
    def falar(self):
        return "O gato mia!"

def escolherAnimal():
    escolha = input("Digite gato ou cachorro:").lower()
    if escolha == "cachorro":
        animal = Cachorro()
    elif escolha == "gato":
        animal = Gato()
    else:
        print("Digite o nome correto!")
        return    
    print(animal.falar())
    
escolherAnimal()
