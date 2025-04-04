#[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos.
# Esta função deve comparar os três números e identificar qual deles é o maior. Para isso,
# utilize uma estrutura de controle que verifique qual número é maior que os outros dois. 
# A função deve então retornar o maior número encontrado.

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))

def maior_numero (num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return f"O maior numéro é o primeiro com o valor {num1}"
    elif num2 > num1 and num2 > num3:
        return f"O maior numéro é o segundo com o valor {num2}"
    else:
        return f"O maior numéro é o terceiro com o valor {num3}"
    
print(maior_numero(numero1, numero2, numero3))  
