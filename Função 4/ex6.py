# 6. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
# a) Função para construir um menu de opções para uma calculadora:

# Menu de cálculos
# 1.   Número ao quadrado
# 2.   Número ao cubo
# 3.   Raiz do número
# 4.   Raiz cúbica do número
# Qual é a opção desejada?
# b) Desenvolva uma função para cada opção de cálculo.

# Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos números do menu.

# A função de desenho/construção do menu, esta chamará todas as outras passando a elas o valor digitado.

def menu():
    print('\n*** Calculadora ***')
    print('1 Número ao quadrado')
    print('2 Número ao cubo')
    print('3 Raiz do número')
    print('4 Raiz cúbica do número')
    opcao = input('\nQual é a opção desejada? ')
    return opcao

def quadrado(numero):
    return numero ** 2

def cubo(numero):
    return numero ** 3

def raiz_q(numero):
    from math import sqrt
    return sqrt(numero)

def raiz_c(numero):
    import numpy as np
    return np.cbrt(numero)

def main():
    op = menu()
    while op == '1' or op == '2' or op == '3' or op == '4':
        num = float(input('\nDigite um número: '))
        if op == '1':
            print(f'O número {num} elevado ao quadrado é {quadrado(num)}')
        if op == '2':
            print(f'O número {num} elevado ao cubo é {cubo(num)}')
        if op == '3':
            print(f'A raiz quadrada de {num} é {raiz_q(num)}')
        if op == '4':
            print(f'A raiz cúbica de {num} é {raiz_c(num)}')
        op = menu()
    print('\nFim do programa')

main()