tarefas_diarias = []

def adicionar_tarefas():
    while True:
        nome = input("Nome da tarefa: ")
        descricao = input("Descrição da tarefa: ")
        prioridade = input("Prioridade da tarefa: Baixa, média ou alta: ").strip().capitalize()
        while prioridade not in ["Alta", "Média", "Baixa"]:
            print("Prioridade inválida! Por favor, digite 'Alta', 'Média' ou 'Baixa'.")
            prioridade = input("Prioridade da tarefa: ").strip().capitalize()
        categoria = input("Categoria da tarefa: ")

        tarefa = {
            "Nome": nome,
            "Descrição": descricao,
            "Prioridade": prioridade,
            "Categoria": categoria,
            "Concluída": False  
        }

        tarefas_diarias.append(tarefa)
        print("Tarefa adicionada com sucesso!")
        
        adicionar_outra = input("Deseja adicionar outra tarefa? (Sim/Não): ").strip().lower()
        if adicionar_outra == "não" or adicionar_outra == "n":
            break

def listar_tarefas():
    if tarefas_diarias:
        print("\nTarefas diárias:")    
        for i, tarefa in enumerate(tarefas_diarias):
            status = "Concluída" if tarefa["Concluída"] else "Pendente"
            print(f"{i + 1}. Nome: {tarefa['Nome']} - Status: {status}")
            print(f"Descrição: {tarefa['Descrição']}")
            print(f"Prioridade: {tarefa['Prioridade']}")
            print(f"Categoria: {tarefa['Categoria']}")
            print("-" * 30)
    else:
        print("Nenhuma tarefa foi adicionada!")

def marcar_como_concluida():
    while True:
        try:
            posicao = int(input("Informe o número da tarefa que deseja marcar como concluída: ")) - 1
            
            if 0 <= posicao < len(tarefas_diarias):
                tarefas_diarias[posicao]["Concluída"] = True
                print("Tarefa marcada como concluída!")
                opcao = input("Deseja adicionar outra tarefa? (Sim/Não): ").strip().lower()
                if opcao == "sim" or opcao == "s":
                    adicionar_tarefas()  
                    break
                elif opcao == "não" or opcao == "n":
                    break
                else:
                    print("Opção inválida! Voltando para o menu.")
                    break
            else:
                print("Posição inválida!")
        except ValueError:
            print("Por favor, insira um número válido.")

def tarefa_prioridade():
    prioridades = {"Alta": 1, "Média": 2, "Baixa": 3}
    tarefas_ordenadas = sorted(tarefas_diarias, key=lambda x: prioridades.get(x["Prioridade"], 4))

    if tarefas_ordenadas:
        print("\nTarefas ordenadas por prioridade:")
        for i, tarefa in enumerate(tarefas_ordenadas):
            status = "Concluída" if tarefa["Concluída"] else "Pendente"
            print(f"{i + 1}. Nome: {tarefa['Nome']} - Status: {status}")
            print(f"Descrição: {tarefa['Descrição']}")
            print(f"Prioridade: {tarefa['Prioridade']}")
            print(f"Categoria: {tarefa['Categoria']}")
            print("-" * 30)
    else:
        print("Nenhuma tarefa para exibir.")

adicionar_tarefas()
listar_tarefas()
marcar_como_concluida()
tarefa_prioridade()