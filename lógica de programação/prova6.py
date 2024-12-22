usuario = "guilherme1509"
senha = "Gui03071501!"
tentativas = 3

for i in range(tentativas, 0, -1):
    loginUsuario = input("Digite o seu usuário: ")
    loginSenha = input("Digite a sua senha: ")
    
    if loginUsuario == usuario and loginSenha == senha:
        print("Bem vindo ao sistema !")
        break
    else:
        print(f"Usuário ou senha inválido, tente novamente ! Restam {i - 1} tentativas. ")
           
    if i == 1:
        print("Acesso bloqueado")    