numeroFixo = 7
adivinhe = 0
tentativa = 3

while tentativa > 0:   
    adivinhe = int(input("Adivinhe um número de 1 à 10: "))
    tentativa -= 1

    if adivinhe < numeroFixo:
        print("Tente novamente! O número é maior")
    elif adivinhe > numeroFixo:
        print("Tente novamente! O número é menor")
    else:
        print(f"Parabéns! O número escolhido foi {numeroFixo}")
        break 

    if tentativa > 0:
        print(f"Você tem mais {tentativa} tentativa(s)")
    else:
        print("Você perdeu! Acabaram as tentativas") 

                  
