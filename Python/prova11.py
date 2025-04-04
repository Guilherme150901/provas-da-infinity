class Animal: 
    def falar(self):
        print("Este animal faz um som!")
            
class Cachorro(Animal):
    def falar(self):
        print("O cachorro late!")
        
class Gato(Animal):
    def falar(self):
        print("O gato mia!")

def escolherAnimal():
    escolha = input("Digite gato ou cachorro:").lower()
    if escolha == "cachorro":
        animal = Cachorro()
    elif escolha == "gato":
        animal = Gato()
    else:
        print("Digite o nome correto!")
        return    
    animal.falar()
    
escolherAnimal()