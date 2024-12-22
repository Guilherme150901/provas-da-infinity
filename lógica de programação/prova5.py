numeroAlunos = int(input("Digite a quantidade de alunos: "))
somaMedias = 0

for num in range(numeroAlunos):
    nome = input(f"Digite o Nome do aluno {num + 1}: ")
    somaNotas = 0
    
    for i in range(3):
        nota = float(input(f"Digite a nota {i + 1} do aluno {nome}: "))
        somaNotas += nota
        
    media = somaNotas / 3
    somaMedias += media
    
    if media > 7:
        situacao = "Aprovado"
    else: 
        situacao = "Reprovado"
        
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    
mediaGeral = somaMedias / numeroAlunos
print(f" A média geral da turma é {mediaGeral:.2f}")            


