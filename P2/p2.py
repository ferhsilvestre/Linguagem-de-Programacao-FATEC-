# 1. [6,0 pontos] Em Python crie um programa que atenda o menu a seguir. Desenvolva uma função para cada opção do menu. Utilize a criação de estruturas. Cadastrar 5 (vetor) vendas ( Tipo_Venda: cod_venda (int), dia(int), total(float), cliente (Tipo_Cliente: cod_cliente (int), nome(str) )
# Menu de opções:

# 1 Cadastrar clientes

# 2 Mostrar todos os clientes

# 3 Cadastrar vendas

# 4 Mostrar todas as vendas

# 5 Mostrar o total de vendas de um determinado dia

# 6 Armazenar todos os campos da venda em um arquivo

# 7 Apresentar o conteúdo do arquivo

# 8 Sair

# Observaçôes:

# Na opção 5, o usuário do sistema informará/digitará o dia que quer e o sistema/programa fará uma pesquisa e calculará o total de vendas de dias iguais, somar o total dos dois lançamentos do dia 25, três no dia 10, lembrando que, as vendas podem ter o registro como demonstra este exemplo, uma venda dia 10, outra dia 24, duas no dia 25, uma dia 20, uma dia 10, mais uma outra no dia 10 e assim por diante.

# Na opção 6 e 7 o nome do arquivo deverá ser vendas.txt

class Tipo_Venda:
    cod_venda = 0
    dia = 0
    total = 0.0
    cliente = 0

class Tipo_Cliente:
    cod_cliente = 0
    nome = ''

def cadastrar_clientes(vetor):
    cadastrar = 'S'
    while cadastrar == 'S':
        cliente = Tipo_Cliente()
        cliente.cod_cliente = int(input('Cadastre o código do cliente: '))
        cliente.nome = input('Informe o nome do cliente: ')
        vetor.append(cliente)

        cadastrar = input('Deseja cadastrar outro cliente? (S/N) ').upper().strip()
        
def mostrar_clientes(clientes):
    header = "\nCódigo | Nome\n"
    print(header)
    for cliente in clientes: 
        print(f"{cliente.cod_cliente}      | {cliente.nome}")

def cadastrar_vendas(vetor):
    cadastrar = 'S'
    while cadastrar == 'S':
        if len(vetor) != 5:
            vendas = Tipo_Venda()
            vendas.cod_venda = int(input('Cadastre o código da venda: '))
            vendas.dia = int(input('Informe o dia: '))
            if vendas.dia < 1 or vendas.dia > 31:
                print("Entre com um dia válido!")
                break
            vendas.total = float(input('Informe o valor da venda: '))
            vendas.cliente = int(input('Informe o código do cliente: '))
            vetor.append(vendas)

            cadastrar = input('Deseja cadastrar outra venda? (S/N) ').upper().strip()

        else:
            print('O total de vendas cadastradas já foi atingido!')
            cadastrar = 'N'

def mostrar_vendas(vendas):
    header = "\nCódigo | Cliente | Dia  | Total\n"
    print(header)
    for i in vendas:
        print(f'{i.cod_venda}      | {i.cliente}       | {i.dia}   | {i.total:.2f}')

def mostrar_total_dia(vendas):
    total = 0
    dia = int(input("Digite o dia: "))
    if dia < 1 or dia > 31:
        print('Entre com um dia válido!')
    else:
        for i in vendas:
            if i.dia == dia:
                total += i.total
        print(f'O total de vendas do dia {dia} é de R$ {total:.2f}')

def armazenar(vendas):
    arq_vendas = open('vendas.txt', 'w')
    for i in vendas:
        arq_vendas.write(f'{i.cod_venda},{i.dia},{i.total:.2f},{i.cliente}\n')
    arq_vendas.close()

def apresentar():
    arq_vendas = open('vendas.txt','r')
    print('\nCódigo \t\t Cliente \t Dia \t\t Total\n')
    for i in arq_vendas.readlines():
        c, d, t, x = i.strip().split(',')
        print(c,'\t\t',x,'\t\t',d,'\t\t',t)
    arq_vendas.close()

def menu():
    print('\n*** MENU ***')
    print('1. Cadastrar clientes ')
    print('2. Mostrar todos os clientes')
    print('3. Cadastrar vendas')
    print('4. Mostrar todas as vendas')
    print('5. Mostrar o total de vendas de um determinado dia')
    print('6. Armazenar todos os campos da venda em um arquivo')
    print('7. Apresentar o conteúdo do arquivo')
    print('8. Sair')
    opcao = int( input('\nQual opção deseja? '))
    return opcao

def main():
    vetor_clientes, vetor_vendas = [], []

    opt = 0
    while opt != 8:
        opt = menu()
        if opt == 1:
           cadastrar_clientes(vetor_clientes)

        elif opt == 2:
            mostrar_clientes(vetor_clientes)

        elif opt == 3:
            cadastrar_vendas(vetor_vendas)

        elif opt == 4:
            mostrar_vendas(vetor_vendas)

        elif opt == 5:
            mostrar_total_dia(vetor_vendas)
        
        elif opt == 6:
            armazenar(vetor_vendas)

        elif opt == 7:
            apresentar()

        elif opt == 8:
            print('\nSaindo')

        else:
            print('\nEssa opção é inválida, por favor selecione uma opção válida!')

main()
