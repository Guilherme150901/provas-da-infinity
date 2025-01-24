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

