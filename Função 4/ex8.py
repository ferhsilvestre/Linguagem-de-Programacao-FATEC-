# 8. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
# a) Função para construir um menu de opções para uma calculadora:

# *** Minha Calculadora ***
# Digite um número.....: 
# Digite outro número..: 
    # + Soma dois números
#     - Subtrai dois números
#     * Multiplica dois números
#     / Divide dois números
# Qual opção deseja? 
# b) Desenvolva uma função para cada opção de cálculo.

# Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

# A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.

def menu():
    print('\n*** Minha Calculadora ***')
    print('+ Soma dois números ')
    print('- Subtrai dois números')
    print('* Multiplica dois números')
    print('/ Divide dois números')
    opcao = input('\nQual opção deseja? ')
    return opcao
def somar(num1, num2):
    return f'A soma entre os dois números é {num1 + num2}'
def subtrair(num1, num2):
    return f'A subtração entre os dois números é {num1 - num2}'
def multiplicar(num1, num2):
    return f'A multiplicação entre os dois números é {num1 * num2}'
def dividir(num1, num2):
    if num2 > 0:
        return f'A divisão entre os dois números é {num1 / num2:.2f}'
    else:
        return 'Não pode ocorrer divisão por zero'
def main():
    op = menu()
    while op == '+' or op == '-' or op == '*' or op == '/':
        n1 = int(input('\nDigite um número.....: '))
        n2 = int(input('Digite outro número..: '))
        if op == '+':
            print(somar(n1, n2))            
        if op == '-':
            print(subtrair(n1, n2))
        if op == '*':
            print(multiplicar(n1,n2))
        if op == '/':
            print(dividir(n1, n2))
        op = menu()
    print('\nTermino do programa...............')
main()