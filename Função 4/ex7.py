# 7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
# a) Função para construir um menu de opções para uma calculadora:

# *** Minha Calculadora ***
# Digite um número.....: 
# Digite outro número..: 
#     + Soma dois números
#     - Subtrai dois números
#     * Multiplica dois números
#     / Divide dois números
# Qual opção deseja? 
# b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

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
    print('O resultado da soma é', num1 + num2)
def subtrair(num1, num2):
    print('O resultado da subtraçao é', num1 - num2)
def multiplicar(num1, num2):
    print('O resultado da multiplição é', num1 * num2)
def dividir(num1, num2):
    if num2 > 0:
        print(f'O resultado da divisão é {num1 / num2:.2f}')
    else:
        print('Não pode ocorrer divisão por zero')
def main():
    op = menu()
    while op == '+' or op == '-' or op == '*' or op == '/':
        n1 = int(input('\nDigite um número.....: '))
        n2 = int(input('Digite outro número..: '))
        if op == '+':
            somar(n1, n2)
        if op == '-':
            subtrair(n1, n2)
        if op == '*':
            multiplicar(n1,n2)
        if op == '/':
            dividir(n1, n2)
        op = menu()
    print('\nTermino do programa...............')
main()