from classes import GerenciadorPacientes

sistema = GerenciadorPacientes()

while True:
    #menu de interação
    print("\n=== Sistema de Cadastro de Pacientes ===")
    print("1- Cadastrar Paciente")
    print("2- Listar Pacientes")
    print("3- Chamar Próxima Senha")
    print("4- Sair")
    opcao = input("Escolha uma opção: ")
    #cadastro do paciente
    if opcao == '1':
        #obtendo informações do paciente 
        nome = input("Nome do paciente: ").capitalize().strip()
        try:
            idade = int(input("Idade do paciente: "))
        except ValueError:
            print("Erro: idade inválida.")
            continue

        print("Especialidades disponíveis:")
        especialidade = list(sistema.lista_especialidade.keys())
        for i,esp in enumerate(especialidade): # listando as especialidade disponíveis
            print(f"{i} - {esp}")
            
        esp = int(input("Escolha a especialidade: "))
        #verificação de especialidade 
        if especialidade[esp] not in sistema.lista_especialidade:
            print("Especialidade inválida.")
            continue
        #adicionando paciente 
        resultado = sistema.adicionar_paciente(nome, especialidade[esp], idade)
        print(resultado)
        
    #listagem por especialidade
    elif opcao == '2':
        especialidade = list(sistema.lista_especialidade.keys())
        
        print("Especialidades disponíveis para listagem:")
        for i,esp in enumerate(especialidade): # listando as especialidade
            print(f"{i} - {esp}")
        #tratamento de erro da opção escolhida 
        try:  
            opcao_listagem = int(input('Escolha uma opção: '))
            if 0 <= opcao_listagem <= len(especialidade):
                pass
            else:
                print('Especialidade inválida')
        except ValueError:
            print('ERRO! digita um número')
        #pegando a lista de pacientes
        pacientes = sistema.listar_pacientes()
        
        # adicionando paciente da listagem escolhida na lista 
        pacientes_filtrados = [p for p in pacientes if p['especialidade'] == especialidade[opcao_listagem]]
        if not pacientes_filtrados:
            print(f'Nenhum paciente cadastrado para {especialidade[opcao_listagem]}')
        else:
            print(f'Paciente de {especialidade[opcao_listagem]}')
            for p in pacientes_filtrados:
                print(f"Nome: {p['nome']} | Tipo: {p['tipo']} | Triagem: {p['triagem']} | Senha: {p['senha']}")

    #Chamar o próximo paciente da fila por especialidade           
    elif opcao == '3':
        especialidade = list(sistema.lista_especialidade.keys())

        print("Especialidades disponíveis para chamada:")
        for i, esp in enumerate(especialidade):
            print(f"{i} - {esp}")
        try:
            escolha = int(input("Escolha a especialidade: "))
            if 0 <= escolha < len(especialidade):
                esp_escolhida = especialidade[escolha]
                resultado = sistema.chamar_paciente(esp_escolhida)
                print(resultado)
            else:
                print("Especialidade inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")    
    #sair do sistema 
    elif opcao == '4':
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")

