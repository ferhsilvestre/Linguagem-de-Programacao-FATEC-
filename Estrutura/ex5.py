# 5. Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. Crie uma função para cada opção do menu a seguir. Utilize a estrutura na passagem de parâmetro:
# Menu de opções:

# Cadastrar contas
# Visualizar todas as contas
# Consultar por nome
# Alterar nome e saldo de um número de conta
# Excluir a conta com menor saldo
# Sair

# Observação:

# No item de menu 4. Alterar nome e/ou saldo de um número de conta, entenda que apenas pode ser alterado o nome e o saldo depois que você pesquisar pelo número da conta.
# No item 5 do menu, encontre o menor saldo dentre todos cadastrados, depois exclua esta ÚNICA conta.. O assunto de excluir algo de um vetor foi dado na disciplina de Algoritmo.

class Conta_Bancaria:
    numero_conta = 0
    nome_titular = ''
    saldo = 0

contas = []

def cadastrar_contas():
    if len(contas) == 15:
        print('\nVocê atingiu o limite de cadastros!')
        main()
    
    else:
        cadastro = Conta_Bancaria()
        print('\nCADASTRAR\n')
        numero = int(input('Número da conta: '))
        if len(contas) > 0 and any(x for x in contas if x.numero_conta == numero):
            print('Esse número de conta já existe!')
        else:
            cadastro.numero_conta = numero
            cadastro.nome_titular = input('Nome do titular: ')
            cadastro.saldo = float(input('Informe o saldo: '))
            contas.append(cadastro)
        main()

def visualizar_contas():
    for cadastro in contas:
        print('-' * 50)
        print('Número da conta:', cadastro.numero_conta)
        print('Nome do titular:', cadastro.nome_titular)
        print(f'Saldo: {cadastro.saldo:.2f}')
        print('-' * 50)
    main()

def consulta_nome():
    nome = input('\nInforme o nome do titular da conta para buscar: ').upper()
    busca = False

    for cadastro in contas:
        if busca == False:
            if cadastro.nome_titular.upper() == nome:
                print('-' * 50)
                print('Número da conta:', cadastro.numero_conta)
                print('Nome do titular:', cadastro.nome_titular)
                print(f'Saldo: {cadastro.saldo:.2f}')
                print('-' * 50)
                busca = True
    
    if busca == False:
        print('\nTitular não cadastrado')            
    main()

def alterar_nome_saldo():
    pesquisa = int(input('\nDigite o número da conta que quer alterar: '))
    for cadastro in contas:
        if pesquisa == cadastro.numero_conta:
            cadastro.nome_titular = input('Insira um novo nome do titular: ')
            cadastro.saldo = float(input('Informe o novo valor de saldo: '))
    main()

def excluir_conta_menor():
    menor = None
    posicao = 0
    for i in range(len(contas)):
        cadastro = contas[i].saldo
        if menor == None:
            menor = cadastro
        elif cadastro < menor:
            menor = cadastro
            posicao = i
    contas.pop(posicao)
    print(f'\nConta com saldo de R$ {menor:.2f} excluída!')
    main()                    

def menu():
    print()
    print('-' * 50)
    print('1. Cadastrar contas')
    print('2. Visualizar todas as contas')
    print('3. Consultar por nome')
    print('4. Alterar nome e saldo de um número de conta')
    print('5. Excluir a conta com menor saldo')
    print('6. Sair')
    print('-' * 50)
    opcao = int(input('Escolha uma das opções: '))
    return opcao

def main():
    opcao = menu()
    if opcao == 1:
        cadastrar_contas()

    elif opcao == 2:
        visualizar_contas()

    elif opcao == 3:
        consulta_nome()

    elif opcao == 4:
        alterar_nome_saldo()

    elif opcao == 5:
        excluir_conta_menor()

    elif opcao == 6:
        print('\nSaindo')

    else:
        print('\nEssa opção é inválida, por favor selecione uma opção válida!')
        main()

main()