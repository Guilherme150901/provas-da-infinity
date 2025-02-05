numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

def calcular (num1, num2, num3):
    media_aritmetica = (num1 + num2 + num3) / 3
    return media_aritmetica

print(f"O Resultado da média aritmética é: {calcular(numero1, numero2, numero3):.2f}")
