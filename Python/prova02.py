#[PYIA-A02] Crie um dicionário que irá armazenar informações de um contato, incluindo o nome,
# o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira
# o nome do contato, o número de telefone e o endereço de email. Após coletar todas as informações
#necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido
# pelo usuário.

contato = {
    "Nome do contado": "",
    "Número de telefone": "",
    "Email": ""}

nome_do_contato = input("Digite o nome do contato: ")
numero_de_telefone = int(input("Digite o número de telefone: "))
email = input("Digite o Email do contato: ")

contato["Nome do contado"] = nome_do_contato
contato["Número de telefone"] = numero_de_telefone
contato["Email"] = email

print(contato)
