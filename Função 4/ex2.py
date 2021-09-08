# 2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.

def soma(x,y):
    s = x + y
    return s

def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'A soma entre {n1} e {n2} é {soma(n1,n2)}')

main()