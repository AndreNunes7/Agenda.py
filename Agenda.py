#Agenda.py

import csv

agenda = {}




def tracos():
    print("-" * 35)



def mostrar_contatos():
    tracos()
    for contato, dados in agenda.items():
        print(f"nome:     |  {contato:<12}")
        for chave, valor in dados.items():
            print(f"{chave + ':' :<10}| {valor}")
        tracos()




def buscar_contatos():
    tracos()
    while True:
        
        pgt2 = input("Digite o nome do contato que deseja buscar (ou '0' para sair): ")
        tracos()
        if pgt2 == '0':
            break
        if pgt2 in agenda:
            print("Nome:", pgt2)
            for chave, valor in agenda[pgt2].items():
                print(chave + ":", valor)
            tracos()
        else:
            print("Nome não consta na agenda.")
            tracos()




def validar_campo(valor, campo):
    """
     Valida os campos do contato (nome, telefone, email e endereço).
    Lança exceções (ValueError) se algum campo não atender aos critérios especificados.

    Args:
        valor (str): Valor do campo a ser validado.
        campo (str): Campo a ser validado (contato, telefone, email, endereco).

    Raises:
        ValueError: Se algum campo não estiver de acordo com as regras definidas.
    
    """
    
    if campo == "contato":
        if valor == "":
            raise ValueError("Você não pode deixar o campo vazio!")
    elif campo == "telefone":
        if not valor.isdigit():
            raise ValueError("Você precisa digitar somente números!")
    elif campo == "email":
        if not valor:
            raise ValueError("O email não pode estar vazio!")
    elif campo == "endereco":
        if not valor:
            raise ValueError("O endereço não pode estar vazio!")



def solicitar_valor(mensagem, campo):
    """
    Solicita um valor específico do campo ao usuário e realiza a validação do valor fornecido.

    Args:
        mensagem (str): Mensagem de solicitação do valor ao usuário.
        campo (str): Campo a ser validado (contato, telefone, email, endereco).

    Returns:
        str: Valor fornecido pelo usuário, se for válido.

    """

    while True:
        valor = input(mensagem)
        try:

            validar_campo(valor, campo)
            return valor
        except ValueError as e:
            tracos()
            print("Erro ao adicionar", campo + ":", str(e))
            tracos()





def incluir_contato():

    """
        Solicita e adiciona um novo contato à agenda.
    """
    
    contato = solicitar_valor("Digite o nome do contato: ", "contato")
    telefone = solicitar_valor("Digite o número de telefone do contato: ", "telefone")
    email = solicitar_valor("Digite o e-mail do contato: ", "email")
    endereco = solicitar_valor("Digite o endereço do contato: ", "endereco")

    agenda[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    

    salvar()
    tracos()
    print(f"Contato {contato} adicionado com sucesso!")
    tracos()
    

        




def editar_contatos():
    while True:
        
        print("Escolha o contato que deseja editar (ou '0' para sair):")
        for i, contato in enumerate(agenda.keys()):
            print(f"[{i + 1}] -", contato)
        print()
        tracos()
        escolha = input("Digite o número do contato: ")
        
        tracos()
        

        if escolha == '0':
            break
        
        elif not escolha.isdigit():
            print("Você deve digitar somente números!")
            continue

        
        
        escolha_int = int(escolha) -1
        
        chaves = list(agenda.keys())
        
        print(f"Contato {chaves[escolha_int]} selecionado com sucesso!")
        tracos()
        if escolha_int in range(len(chaves)):
            contato_editar = chaves[escolha_int]
            telefone = solicitar_valor("Novo número de telefone do contato: ", "telefone")
            email = solicitar_valor("Novo e-mail do contato: ", "email")
            endereco = solicitar_valor("Novo endereço do contato: ", "endereco")

            agenda[contato_editar] = {
                "telefone": telefone,
                "email": email,
                "endereco": endereco
            }
            
            salvar()
            tracos()
            print(f"Contato {contato_editar} editado com sucesso!")
            tracos()
        else:
            print("Número de contato inválido ou inexistente!")

            	
            




def excluir_contato():
    while True:
        try:
            if not agenda:  # Verifica se o dicionário está vazio
                print("A agenda está vazia. Não há contatos para excluir.")
                tracos()
                return
            
            print("Qual contato deseja remover? (ou '0' para sair): ")
            print()
            for i, contato in enumerate(agenda.keys()):
                print(f"[{i + 1}] -", contato)
            
            tracos()
            contato_input = input("Digite o número do contato: ")
            tracos()
            if contato_input == "0":
                break
            if not contato_input.strip():  # Verifica se o valor está vazio ou contém apenas espaços em branco
                raise ValueError("Você não pode deixar o campo vazio!")
            
            if not contato_input.isdigit(): # Verifica se o valor é numerico
                raise ValueError("Você só deve digitar números!")
            
            
            contato = int(contato_input) - 1
            
            chaves = list(agenda.keys())  # Convertendo as chaves em uma lista
            if contato in range(len(chaves)):
                contato_remover = chaves[contato]
                del agenda[contato_remover]
                

                print(f"Contato {contato_remover} excluído com sucesso!")
                salvar()
                
                tracos()
                
            else:
                tracos()
                print("Opção inválida.")
                tracos()
        
        except ValueError as e:
            print(e)
            tracos()







def exportar_contatos(filename):
    try:
        with open(filename, "w") as file:
            #file.write("Nome, telefone, email, endereco\n")
            
            for contato in agenda:
                telefone = agenda[contato]["telefone"]
                email = agenda[contato]["email"]
                endereco = agenda[contato]["endereco"]
                
                file.write(f"{contato}, {telefone}, {email}, {endereco}\n")
            
            file.close()

        tracos()
        print("Arquivo exportado com sucesso.")
        

    except:
        print(">>>>> Erro ao exportar contatos!")





def importar_contatos(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Pula a primeira linha que contém os cabeçalhos
            
            for row in reader:
                contato = row[0]
                telefone = row[1]
                email = row[2]
                endereco = row[3]
                
                agenda[contato] = {
                    "telefone": telefone,
                    "email": email,
                    "endereco": endereco
                }
            
        tracos()
        print("Contatos importados com sucesso.")
        tracos()

    except FileNotFoundError:
        print("Arquivo não encontrado.")

    except Exception as error:
        print("Erro ao importar contatos:", str(error))





def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open("database.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                agenda[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print(">>>>> Database carregado com sucesso!")
        qtd_contatos = len(agenda)
        print(f">>>> {qtd_contatos} contato(s) carregado(s)")
        tracos()
    except FileNotFoundError:
        print(">>>>> Arquivo não encontrado!")
    except Exception as error:
        print(">>>> Algum erro inesperado ocorreu")
        print(error)








def imprimir_menu():
    
    print("[1] - Mostrar todos os contatos da agenda")
    print("[2] - Buscar contatos da agenda")
    print("[3] - Incluir contato")
    print("[4] - Editar contatos")
    print("[5] - Excluir contato")
    print("[6] - Exportar contatos para CSV")
    print("[7] - Importar contatos CSV")
    print("[0] - Fechar agenda")
    tracos()




# PROGRAMA PRINCIPAL


carregar()
while True:

    imprimir_menu()
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        mostrar_contatos()
    elif opcao == "2":
        buscar_contatos()
    elif opcao == "3":
        
        incluir_contato()
    elif opcao == "4":
        
        editar_contatos()
    elif opcao == "5":
        excluir_contato()
    elif opcao == "6":
        name_file = input("Digite o nome do arquivo para exportar: ")
        exportar_contatos(name_file)
    elif opcao == "7":
        tracos()
        name_file = input("Digite o nome do arquivo para importar: ")
        importar_contatos(name_file)
    elif opcao == "0":
        tracos()
        print("Agenda fechada. Até mais!")
        tracos()
        break
    else:
        tracos()
        print("Opção inválida. Digite uma opção válida.")
        tracos()
    




