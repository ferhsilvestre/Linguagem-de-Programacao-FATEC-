# 6. Uma empresa prestadora de serviços armazena informações sobre os serviços prestados. Sabe-se que a empresa pode realizar no máximo três serviços diariamente. É de interesse de sua direção manter um histórico mensal (30 dias) sobre os serviços prestados.
# A empresa realiza quatro tipos de serviços:

# 1) pintura;

# 2) jardinagem;

# 3) faxina e

# 4) reforma em geral.

# Cada serviço realizado deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente, numa matriz 30x3 referente a estrutura Servico_prestado.

# Cadastre/digite os quatro tipos de serviços (código e descrição) que a empresa poderá realizar. Para isso, utilize um vetor de quatro posições referente a estrutura Tipo_servico. O programa deverá mostrar o seguinte menu de opções:

# Cadastrar os tipos de serviços
# Mostrar todos os tipos de serviço
# Cadastrar os serviços prestados
# Mostrar todos os serviços prestados
# Mostrar os serviços prestados em determinado dia
# Mostrar os serviços prestados dentro de um intervalo de valor
# Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
# Sair
# Para a opção 1: deve-se cadastrar os tipos de serviços oferecidos pela empresa, com código e descrição.

# Para a opção 3: deve-se considerar que deverão ser cadastrados os serviços prestados ao logo do mês. Em cada dia podem ser cadastrados, no máximo, três serviços prestados.

# Utilize uma matriz capaz de armazenar em cada posição todas as informações referentes a um serviço prestado (número, valor, código do serviço, código do cliente). Cada linha representa um dia do mês. Dessa maneira, considere a matriz com dimensão 30 × 3.

# Solicite o dia em que o serviço foi prestado e as demais informações. Lembre-se de que a empresa só pode prestar os serviços que já tenham sido cadastrados no vetor de tipo de serviços.

# Caso o usuário digite um código de tipo de serviço inválido, o programa deverá mostrar uma mensagem de erro.

# Quando o usuário tentar cadastrar mais de três serviços prestados em um mesmo dia, também deverá mostrar uma mensagem de erro.

# Para a opção 5: o programa deverá receber o dia que se deseja consultar e mostrar os respectivos serviços prestados.

# Para a opção 6: o programa deverá receber o valor mínimo e o valor máximo e mostrar os serviços prestados que estiverem nesse intervalo.

# Para a opção 7: o programa deverá mostrar todos os serviços prestados, conforme o exemplo a seguir.

#               DIA 01
# No do serviço	Valor do serviço R$	Código do serviço	Descrição	Código do cliente
# 100	200,00	1	Pintura	1
# 150	100,00	3	Faxina	5
# 201	640,00	4	Reforma em geral	2
#               DIA 02
# No do serviço	Valor do serviço R$	Código do serviço	Descrição	Código do cliente
# 301	600,00	4	Reforma em geral	3
# 280	352,00	1	Pintura	2
# 306	200,00	2	Jardinagem	1

class Servico_Prestado:
    numero = 0
    valor =  0
    codigo_servico = 0
    codigo_cliente = 0

class Tipo_Servico:
    codigo = 0
    descricao = ''

def cadastrar_tipo_servico():
    tipos_servicos = []
    for i in range (4):
        tipo = Tipo_Servico()
        tipo.codigo = int(input("Cadastre o número do tipo de serviço: "))
        tipo.descricao = input("Cadastre a descrição do tipo de serviço: ")
        tipos_servicos.append(tipo)
    return tipos_servicos

def mostrar_tipo_servico(v_ts):
    header = "\nCódigo | Descrição"
    print(header)
    for i in v_ts:
        line = f"{i.codigo}      | {i.descricao}"
        print(line)

def cadastrar_servicos_prestados(v_ts, v_servicos):
    if v_ts == []:
        print("\nNão existe nenhum serviço cadastrado")
    
    else:
        dia = int(input("Entre com o dia para cadastro dos servicos: "))
        if len(v_servicos[dia-1]) <3:
            servico = Servico_Prestado()
            servico.numero = int(input("Entre com o número do serviço: "))
            servico.valor = float(input("Entre com o valor do serviço: "))

            servico.codigo_servico = int(input("Entre com o codigo do serviço: "))
            if servico.codigo_servico not in [i.codigo for i in v_ts]:
                print("\nEntre com um código de servico cadastrado")
                return None

            servico.codigo_cliente = int(input("Entre com o codigo do cliente: "))
            v_servicos[dia-1].append(servico)

        else:
            print("\nJa foram cadastrado 3 servicos para este dia")

    return v_servicos

def mostrar_servicos_prestados(v_servicos):
    print()
    print_line2("No do serviço", "Valor do serviço", "Código do serviço", "Código do cliente")
    for lin in range(len(v_servicos)):
        for col in range(len(v_servicos[lin])):
            if v_servicos[lin][col].numero != 0:
                print_line2(v_servicos[lin][col].numero, f'{v_servicos[lin][col].valor:.2f}', v_servicos[lin][col].codigo_servico, v_servicos[lin][col].codigo_cliente)

def mostrar_dia(v_servicos):
    dia = int(input("Digite o dia para buscar: "))
    print()
    print_line2("No do serviço", "Valor do serviço", "Código do serviço", "Código do cliente")
    for col in range(len(v_servicos[dia-1])):       
        print_line2(v_servicos[dia-1][col].numero, f'{v_servicos[dia-1][col].valor:.2f}', v_servicos[dia-1][col].codigo_servico, v_servicos[dia-1][col].codigo_cliente)

def mostrar_intervalo(v_servicos):
    valor_minimo = float(input("Digite o valor minimo para buscar: "))
    valor_maximo = float(input("Digite o valor maximo para buscar: "))
    print()
    print_line2("No do serviço", "Valor do serviço", "Código do serviço", "Código do cliente")
    for lin in range(len(v_servicos)):
        for col in range(len(v_servicos[lin])):
            if v_servicos[lin][col].valor >= valor_minimo and v_servicos[lin][col].valor <= valor_maximo:
                 print_line2(v_servicos[lin][col].numero, f'{v_servicos[lin][col].valor:.2f}', v_servicos[lin][col].codigo_servico, v_servicos[lin][col].codigo_cliente)

def relatorio_geral(v_ts, v_servicos):
    for lin in range(len(v_servicos)):
        print('\nDia',lin+1)
        print_line("No do serviço", "Valor do serviço", "Código do serviço", "Código do cliente", "Descricao Servico")
        for col in range(len(v_servicos[lin])):
            if v_servicos[lin][col].numero != 0:
                for i in range(len(v_ts)):
                    if v_ts[i].codigo == v_servicos[lin][col].codigo_servico:
                        descricao = v_ts[i].descricao
                print_line(v_servicos[lin][col].numero, f'{v_servicos[lin][col].valor:.2f}', v_servicos[lin][col].codigo_servico, v_servicos[lin][col].codigo_cliente, descricao)

# Funções para formatar as tabelas
def print_line(servico,valor,codigo,cliente, descricao, spaces=[14, 18, 19, 18, 20]):
    txt_base = "{servico: <{spaces[0]}}| {valor: <{spaces[1]}}| {codigo: <{spaces[2]}}| {descricao: <{spaces[4]}}| {cliente: <{spaces[3]}}"
    print(txt_base.format(servico=servico, valor=valor, codigo=codigo, descricao=descricao, cliente=cliente, spaces=spaces))

def print_line2(servico,valor,codigo,cliente, spaces=[14, 18, 19, 18]):
    txt_base = "{servico: <{spaces[0]}}| {valor: <{spaces[1]}}| {codigo: <{spaces[2]}}| {cliente: <{spaces[3]}}"
    print(txt_base.format(servico=servico, valor=valor, codigo=codigo, cliente=cliente, spaces=spaces))

def menu():
    print('\n*** EMPRESA DE PRESTAÇÃO DE SERVIÇOS ***')
    print('1. Cadastrar os tipos de serviços ')
    print('2. Mostrar todos os tipos de serviço')
    print('3. Cadastrar os serviços prestados')
    print('4. Mostrar todos os serviços prestados')
    print('5. Mostrar os serviços prestados em determinado dia')
    print('6. Mostrar os serviços prestados dentro de um intervalo de valor')
    print('7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço')
    print('8. Sair')
    opcao = int( input('\nQual opção deseja? '))
    return opcao

def main():

    tipos_servicos = []
    servicos_prestados = []
    for i in range(0, 31):
        servicos_prestados.insert(i, [])

    opt = 0
    while opt != 8:
        opt = menu()
        if opt == 1:
            tipos_servicos = cadastrar_tipo_servico()

        elif opt == 2:
            mostrar_tipo_servico(tipos_servicos)

        elif opt == 3:
            cadastrar_servicos_prestados(tipos_servicos, servicos_prestados)

        elif opt == 4:
            mostrar_servicos_prestados(servicos_prestados)

        elif opt == 5:
            mostrar_dia(servicos_prestados)
        
        elif opt == 6:
            mostrar_intervalo(servicos_prestados)

        elif opt == 7:
            relatorio_geral(tipos_servicos, servicos_prestados)

        elif opt == 8:
            print('\nSaindo')

        else:
            print('\nEssa opção é inválida, por favor selecione uma opção válida!')

main()