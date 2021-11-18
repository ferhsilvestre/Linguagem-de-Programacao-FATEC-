# 2. Elabore uma estrutura para representar e armazenar 10 produtos (código, nome, preço). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura.Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.
# Menu de opções:

# Cadastrar produtos
# Visualizar todos os dados
# Sair

class Tipo_Produto:
    codigo = 0
    nome = ''
    preco = 0.0

def cadastrar_produtos():
    arq_produto = open('produto.txt','w')
    for i in range(10):
        tp = Tipo_Produto()
        tp.codigo = int(input('Informe o código do produto: '))
        tp.nome = input('Informe o nome do produto: ')
        tp.preco = float(input('Informe o preço do produto: '))
        arq_produto.write(f'{tp.codigo},{tp.nome},{tp.preco:.2f}\n')
    arq_produto.close()

def visualizar_dados():
    arq_produto = open('produto.txt','r')
    for x in arq_produto.readlines():
        c,n,p = x.strip().split(',')
        print(c,'\t\t',n,'\t\t',p)
    arq_produto.close()

def menu():
    print()
    print('1. Cadastrar produtos ')
    print('2. Visualizar todos os dados')
    print('3. Sair')
    opcao = int( input('\nQual opção deseja? '))
    return opcao

def main():
    opt = 0
    while opt != 3:
        opt = menu()
        if opt == 1:
            cadastrar_produtos()
        elif opt == 2:
            visualizar_dados()
        elif opt == 3:
            print('\nSaindo')
        else:
            print('\nEssa opção é inválida, por favor selecione uma opção válida!')

main()
