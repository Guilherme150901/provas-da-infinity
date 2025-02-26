import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    return dado1, dado2, soma

dado1, dado2, soma = lancar_dados()
print(f"O primeiro dado caiu no número {dado1} e o segundo caiu no número {dado2}!\n {dado1} + {dado2} = {soma}")