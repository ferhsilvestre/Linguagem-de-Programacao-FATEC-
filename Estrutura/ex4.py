# 4. Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de gerenciamento para a escola? Implemente utilizando estrutura. Também use a criação de funções para cada operação. Use o menu a seguir:
# Menu de opções:

# 1.Cadastrar alunos
# 2.Consulta por nome
# 3.Visualizar todos os dados
# 4.Sair

class Cadastro:
    nome_completo = ''
    data_nascimento = 0
    telefone = 0
    endereco = ''
    serie_atual = 0

alunos = []

def cadastrar_alunos():
    if len(alunos) == 500:
        print('\nVocê atingiu o limite de cadastros!')
    
    else:
        cadastro = Cadastro()
        print('\nCADASTRAR\n')
        cadastro.nome_completo = input('Nome completo: ')
        cadastro.data_nascimento = input('Data de nascimento [DD/MM/AAAA]: ')
        cadastro.telefone = input('Telefone: ')
        cadastro.endereco = input('Endereço: ')
        cadastro.serie_atual = input('Série atual: ')
        alunos.append(cadastro)

def consulta_nome():
    nome = input('\nDigite o nome do aluno para buscar: ').upper()
    busca = False

    for cadastro in alunos:
        if busca == False:
            if cadastro.nome_completo.upper() == nome:
                print('-' * 50)
                print('Nome Completo:', cadastro.nome_completo)
                print('Data de Nascimento:', cadastro.data_nascimento)
                print('Telefone:', cadastro.telefone)
                print('Endereço:', cadastro.endereco)
                print('Série:', cadastro.serie_atual)
                print('-' * 50)
                busca = True
    
    if busca == False:
        print('\nAluno não cadastrado')            

def visualizar_dados():
    for cadastro in alunos:
        print('-' * 50)
        print('Nome Completo:', cadastro.nome_completo)
        print('Data de Nascimento:', cadastro.data_nascimento)
        print('Telefone:', cadastro.telefone)
        print('Endereço:', cadastro.endereco)
        print('Série:', cadastro.serie_atual)
        print('-' * 50)

def menu():
    print()
    print('-' * 30)
    print('1. Cadastrar alunos')
    print('2. Consulta por nome')
    print('3. Visualizar todos os dados')
    print('4. Sair')
    print('-' * 30)
    opcao = int(input('Escolha uma das opções: '))
    return opcao

def main():
    opcao = 0
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            cadastrar_alunos()

        elif opcao == 2:
            consulta_nome()

        elif opcao == 3:
            visualizar_dados()

        elif opcao == 4:
            print('\nSaindo')

        else:
            print('\nEssa opção é inválida, por favor selecione uma opção válida!')
       
main()