inicio = int(input("Digite um número inicial: "))
fim = int(input("Digite um número final: "))
soma = 0
pares = 0

for num in range(inicio, fim + 1):
    if num % 2 == 0:
       soma += num
       pares += 1

if pares > 0:
    print(f"A soma dos números pares é {soma}")
else:
    print("Não há números pares no intervalo!")    





