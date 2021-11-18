# 3. Elabore uma estrutura para representar e armazenar 10 alunos (matricula, nome, telefone). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.
# Menu de opções:

# Cadastrar alunos
# Visualizar todos os dados
# Sair

class Tipo_Aluno:
    matricula = 0
    nome = ''
    telefone = 0

def cadastrar_alunos():
    arq_aluno = open('aluno.txt','w')
    for i in range(10):
        a = Tipo_Aluno()
        a.matricula = int(input('Informe o número da matrícula: '))
        a.nome = input('Informe o nome do aluno: ')
        a.telefone = int(input('Informe o número do telefone: '))
        arq_aluno.write(f'{a.matricula},{a.nome},{a.telefone}\n')
    arq_aluno.close()

def visualizar_dados():
    arq_aluno = open('aluno.txt','r')
    for x in arq_aluno.readlines():
        c,n,p = x.strip().split(',')
        print(c,'\t\t',n,'\t\t',p)
    arq_aluno.close()

def menu():
    print()
    print('1. Cadastrar alunos')
    print('2. Visualizar todos os dados')
    print('3. Sair')
    opcao = int( input('\nQual opção deseja? '))
    return opcao

def main():
    opt = 0
    while opt != 3:
        opt = menu()
        if opt == 1:
            cadastrar_alunos()
        elif opt == 2:
            visualizar_dados()
        elif opt == 3:
            print('\nSaindo')
        else:
            print('\nEssa opção é inválida, por favor selecione uma opção válida!')

main()
